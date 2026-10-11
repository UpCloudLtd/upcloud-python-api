"""Focused regression tests for the OpenAPI preprocessing patches."""

import copy
import importlib.util
import io
import json
import shutil
import subprocess
import sys
import unittest
import uuid
from contextlib import redirect_stdout
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "patch_openapi.py"
MODULE_SPEC = importlib.util.spec_from_file_location("patch_openapi", SCRIPT)
patch_openapi = importlib.util.module_from_spec(MODULE_SPEC)
MODULE_SPEC.loader.exec_module(patch_openapi)


class OpenAPIPatchTests(unittest.TestCase):
    """Exercise each patch without needing the full upstream specification."""

    def apply(self, patch, spec):
        """Apply a patch while keeping its diagnostic output out of test results."""
        with redirect_stdout(io.StringIO()):
            patch(spec)

    def test_top_level_titles_only(self):
        """Remove schema titles without altering nested or document metadata."""
        spec = {
            "info": {"title": "API"},
            "components": {
                "schemas": {
                    "example": {
                        "title": "Collision",
                        "type": "object",
                        "properties": {"value": {"title": "Nested", "type": "string"}},
                    },
                    "booleanSchema": True,
                }
            },
        }
        expected = copy.deepcopy(spec)
        del expected["components"]["schemas"]["example"]["title"]
        self.apply(patch_openapi.strip_titles_from_top_level_schemas, spec)
        self.assertEqual(spec, expected)
        self.apply(patch_openapi.strip_titles_from_top_level_schemas, spec)
        self.assertEqual(spec, expected)

    def test_inline_titles_cover_recursive_schema_locations(self):
        """Strip union branch titles recursively, retaining references and other titles."""
        branch = {"title": "Collision", "type": "string", "description": "Keep me"}
        expected_branch = {"type": "string", "description": "Keep me"}
        reference = {"$ref": "#/components/schemas/other", "title": "Reference title"}
        schema = {
            "title": "Top-level title",
            "oneOf": [copy.deepcopy(branch), reference],
            "anyOf": [copy.deepcopy(branch)],
            "allOf": [copy.deepcopy(branch)],
            "properties": {
                "value": {
                    "title": "Property title",
                    "oneOf": [
                        copy.deepcopy(branch),
                    ],
                }
            },
            "items": {"anyOf": [copy.deepcopy(branch)]},
            "prefixItems": [{"allOf": [copy.deepcopy(branch)]}],
        }
        spec = {"components": {"schemas": {"example": schema, "booleanSchema": False}}}
        expected = copy.deepcopy(spec)
        expected_schema = expected["components"]["schemas"]["example"]
        for keyword in ("oneOf", "anyOf", "allOf"):
            expected_schema[keyword][0] = copy.deepcopy(expected_branch)
        expected_schema["properties"]["value"]["oneOf"][0] = copy.deepcopy(expected_branch)
        expected_schema["items"]["anyOf"][0] = copy.deepcopy(expected_branch)
        expected_schema["prefixItems"][0]["allOf"][0] = copy.deepcopy(expected_branch)
        self.apply(patch_openapi.strip_titles_from_inline_schemas, spec)
        self.assertEqual(spec, expected)
        self.apply(patch_openapi.strip_titles_from_inline_schemas, spec)
        self.assertEqual(spec, expected)

    def test_absent_patch_targets_are_noops(self):
        """Allow minimal specifications and absent target operations."""
        for spec in (
            {},
            {"paths": {}, "components": {"schemas": {}}},
            {"paths": {"/1.3/kubernetes": {"get": {}}}},
        ):
            for patch in (
                patch_openapi.strip_titles_from_top_level_schemas,
                patch_openapi.strip_titles_from_inline_schemas,
            ):
                with self.subTest(spec=spec, patch=patch.__name__):
                    expected = copy.deepcopy(spec)
                    self.apply(patch, spec)
                    self.assertEqual(spec, expected)


class PatchCLITests(unittest.TestCase):
    """Validate the actual script entry point using repository-local fixtures."""

    def setUp(self):
        """Create an isolated scratch directory inside the project, never in /tmp."""
        self.directory = Path(__file__).resolve().parent / f".patch-test-{uuid.uuid4().hex}"
        self.directory.mkdir()
        self.addCleanup(shutil.rmtree, self.directory)

    def run_cli(self, *arguments):
        """Run the script with the same interpreter as the test runner."""
        return subprocess.run(  # noqa: S603 - fixed interpreter/script and local test fixtures only
            [sys.executable, str(SCRIPT), *(str(argument) for argument in arguments)],
            capture_output=True,
            text=True,
            check=False,
        )

    def test_invalid_inputs_fail_without_writing_output(self):
        """Reject absent arguments, nonexistent input, invalid JSON, and invalid paths."""
        input_path = self.directory / "input.json"
        output_path = self.directory / "output.json"
        result = self.run_cli()
        self.assertEqual(result.returncode, 2)
        self.assertIn("Usage:", result.stderr)
        result = self.run_cli(input_path, output_path)
        self.assertEqual(result.returncode, 2)
        self.assertIn("not found", result.stdout)
        for content, message in (
            ("{", "not valid JSON"),
            ('{"info": {}}', "missing or not an object"),
            ('{"paths": []}', "missing or not an object"),
        ):
            with self.subTest(content=content):
                input_path.write_text(content, encoding="utf-8")
                result = self.run_cli(input_path, output_path)
                self.assertEqual(result.returncode, 2)
                self.assertIn(message, result.stdout)
                self.assertFalse(output_path.exists())

    def test_pipeline_preserves_unrelated_data_and_is_idempotent(self):
        """Strip titles through the CLI and preserve unrelated document content."""
        spec = {
            "openapi": "3.1.0",
            "info": {"title": "Keep title", "version": "test"},
            "paths": {
                "/1.3/kubernetes": {
                    "post": {
                        "responses": {
                            "201": {"description": "Created"},
                        }
                    }
                },
                "/unrelated": {"get": {"operationId": "keep", "responses": {}}},
            },
            "components": {
                "schemas": {
                    "example": {
                        "title": "Remove",
                        "oneOf": [
                            {"title": "Remove branch", "type": "string"},
                        ],
                        "description": "Keep description",
                    },
                    "plain": {"type": "string", "description": "Keep me"},
                }
            },
            "x-unrelated": {"title": "Keep extension title", "value": [1, 2]},
        }
        expected = copy.deepcopy(spec)
        schemas = expected["components"]["schemas"]
        del schemas["example"]["title"]
        del schemas["example"]["oneOf"][0]["title"]
        input_path = self.directory / "input.json"
        output_path = self.directory / "output.json"
        second_path = self.directory / "second.json"
        input_path.write_text(json.dumps(spec), encoding="utf-8")
        first = self.run_cli(input_path, output_path)
        self.assertEqual(first.returncode, 0, first.stdout + first.stderr)
        self.assertEqual(json.loads(output_path.read_text(encoding="utf-8")), expected)
        second = self.run_cli(output_path, second_path)
        self.assertEqual(second.returncode, 0, second.stdout + second.stderr)
        self.assertEqual(output_path.read_bytes(), second_path.read_bytes())


if __name__ == "__main__":
    unittest.main()
