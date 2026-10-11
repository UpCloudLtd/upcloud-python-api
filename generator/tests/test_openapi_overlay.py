"""Tests for generator/openapi/overlay.yaml applied with the mise-provided Speakeasy CLI."""

import copy
import json
import shutil
import subprocess
import sys
import unittest
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OVERLAY = ROOT / "generator" / "openapi" / "overlay.yaml"
SPEC = ROOT / "generator" / "openapi" / "spec.json"
PATCHED_SPEC = ROOT / "generator" / "openapi" / "spec.patched.json"
PATCH_SCRIPT = ROOT / "generator" / "scripts" / "patch_openapi.py"

STORAGE = "kubernetesDefaultStorageEncryption"
FIREWALL = "firewallRulesetErrorResponse"
CLUSTER_PATH = "/1.3/kubernetes"
CLUSTER_RESPONSE = {"$ref": "#/components/responses/kubernetesPostCluster"}
INVALID_PARAM_PROPERTIES = {
    "name": {
        "type": "string",
        "examples": ["zone", "networks.0.ip_address"],
        "description": "Path to the field with invalid parameter.",
    },
    "reason": {
        "type": "string",
        "examples": ["Zone is not valid."],
        "description": "Human-readable error message.",
    },
}


def defective_spec():
    """Return a minimal spec with the three defects the overlay fixes, plus unrelated data."""
    return {
        "openapi": "3.1.1",
        "info": {"title": "Fixture", "version": "test"},
        "paths": {
            CLUSTER_PATH: {
                "get": {"responses": {"201": copy.deepcopy(CLUSTER_RESPONSE)}},
                "post": {
                    "responses": {
                        "201": copy.deepcopy(CLUSTER_RESPONSE),
                        "400": {"description": "Invalid"},
                    }
                },
            },
            "/other": {"post": {"responses": {"201": copy.deepcopy(CLUSTER_RESPONSE)}}},
        },
        "components": {
            "schemas": {
                STORAGE: {
                    "allOf": [
                        {"$ref": "#/components/schemas/kubernetesStorageEncryption"},
                        {"description": "The default storage encryption strategy for all node groups."},
                        {},
                    ]
                },
                FIREWALL: {
                    "type": "object",
                    "properties": {
                        "invalid_params": {
                            "type": "array",
                            "properties": copy.deepcopy(INVALID_PARAM_PROPERTIES),
                            "title": "InvalidParameters",
                            "required": ["name", "reason"],
                            "description": "List of invalid parameters in the request.",
                        },
                        "message": {"type": "string"},
                    },
                },
                "unrelated": {"title": "Keep", "type": "string"},
            },
            "responses": {"kubernetesPostCluster": {"description": "Created cluster"}},
        },
    }


class OpenAPIOverlayTests(unittest.TestCase):
    """Run `speakeasy overlay apply --strict` on repository-local fixtures."""

    @classmethod
    def setUpClass(cls):
        """Require the mise-pinned binary; a missing tool is a failure, not a skip."""
        cls.speakeasy = shutil.which("speakeasy")
        if cls.speakeasy is None:
            raise AssertionError("speakeasy not found on PATH; run `mise install`")

    def setUp(self):
        """Create an isolated scratch directory inside the project, never in /tmp."""
        self.directory = Path(__file__).resolve().parent / f".overlay-test-{uuid.uuid4().hex}"
        self.directory.mkdir()
        self.addCleanup(shutil.rmtree, self.directory)

    def apply_overlay(self, schema_path, out_path):
        """Apply the overlay in strict mode and return the completed process."""
        return subprocess.run(  # noqa: S603 - pinned tool and local test fixtures only
            [
                self.speakeasy,
                "overlay",
                "apply",
                "--strict",
                "--overlay",
                str(OVERLAY),
                "--schema",
                str(schema_path),
                "--out",
                str(out_path),
            ],
            capture_output=True,
            text=True,
            check=False,
            stdin=subprocess.DEVNULL,
        )

    def overlay_document(self, document):
        """Write a fixture, apply the overlay, and return the parsed output."""
        schema_path = self.directory / "input.json"
        out_path = self.directory / "output.json"
        schema_path.write_text(json.dumps(document, indent=2), encoding="utf-8")
        result = self.apply_overlay(schema_path, out_path)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        return json.loads(out_path.read_text(encoding="utf-8"))

    def test_fixes_only_the_defects(self):
        """Fix each defect shape and leave other operations and schemas untouched."""
        spec = defective_spec()
        expected = copy.deepcopy(spec)
        schemas = expected["components"]["schemas"]
        schemas[STORAGE] = {
            "description": "The default storage encryption strategy for all node groups.",
            "x-go-type": "StorageEncryption",
            "$ref": "#/components/schemas/kubernetesStorageEncryption",
        }
        invalid_params = schemas[FIREWALL]["properties"]["invalid_params"]
        invalid_params["items"] = {
            "type": "object",
            "properties": invalid_params.pop("properties"),
            "required": invalid_params.pop("required"),
        }
        responses = expected["paths"][CLUSTER_PATH]["post"]["responses"]
        responses["200"] = responses.pop("201")

        output = self.overlay_document(spec)
        self.assertEqual(output, expected)
        # Key order decides the bytes of spec.patched.json.
        self.assertEqual(list(output["components"]["schemas"][STORAGE]), list(schemas[STORAGE]))
        self.assertEqual(list(output["paths"][CLUSTER_PATH]["post"]["responses"]), ["400", "200"])

    def test_strict_fails_when_defects_are_already_fixed(self):
        """Fail loudly once upstream fixes a defect, so the stale action gets deleted."""
        fixed_path = self.directory / "fixed.json"
        fixed_path.write_text(json.dumps(self.overlay_document(defective_spec())), encoding="utf-8")
        result = self.apply_overlay(fixed_path, self.directory / "again.json")
        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_static_copies_match_the_source_spec(self):
        """Detect drift between the values the overlay duplicates and spec.json."""
        source = json.loads(SPEC.read_text(encoding="utf-8"))
        output = self.overlay_document(source)

        source_responses = source["paths"][CLUSTER_PATH]["post"]["responses"]
        output_responses = output["paths"][CLUSTER_PATH]["post"]["responses"]
        self.assertEqual(output_responses["200"], source_responses["201"])

        source_params = source["components"]["schemas"][FIREWALL]["properties"]["invalid_params"]
        output_items = output["components"]["schemas"][FIREWALL]["properties"]["invalid_params"]["items"]
        self.assertEqual(output_items["properties"], source_params["properties"])
        self.assertEqual(output_items["required"], source_params["required"])

        source_storage = source["components"]["schemas"][STORAGE]["allOf"]
        output_storage = output["components"]["schemas"][STORAGE]
        self.assertEqual(output_storage["$ref"], source_storage[0]["$ref"])
        self.assertEqual(output_storage["description"], source_storage[1]["description"])

    def test_overlay_then_title_pass_matches_committed_patched_spec(self):
        """Overlay followed by the title pass reproduces spec.patched.json."""
        overlaid_path = self.directory / "overlaid.json"
        patched_path = self.directory / "patched.json"
        result = self.apply_overlay(SPEC, overlaid_path)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        result = subprocess.run(  # noqa: S603 - fixed interpreter/script and local test fixtures only
            [sys.executable, str(PATCH_SCRIPT), str(overlaid_path), str(patched_path)],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(
            json.loads(patched_path.read_text(encoding="utf-8")),
            json.loads(PATCHED_SPEC.read_text(encoding="utf-8")),
        )


if __name__ == "__main__":
    unittest.main()
