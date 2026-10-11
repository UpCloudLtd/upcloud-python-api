"""Tests for the jq filter that removes collision-prone schema titles."""

import json
import shutil
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FILTER = ROOT / "generator" / "scripts" / "strip_schema_titles.jq"


class StripSchemaTitlesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.jq = shutil.which("jq")
        if cls.jq is None:
            raise AssertionError("jq not found on PATH; run `mise install`")

    def strip(self, spec):
        return subprocess.run(  # noqa: S603 - jq from PATH and repository-local filter
            [self.jq, "-f", str(FILTER)],
            input=json.dumps(spec),
            capture_output=True,
            text=True,
            check=False,
        )

    def test_removes_only_top_level_and_inline_branch_titles(self):
        spec = {
            "info": {"title": "Keep"},
            "components": {
                "schemas": {
                    "example": {
                        "title": "Remove top-level",
                        "oneOf": [
                            {"title": "Remove branch", "type": "string"},
                            {"$ref": "#/components/schemas/other", "title": "Keep ref title"},
                        ],
                        "properties": {
                            "value": {
                                "title": "Keep property title",
                                "anyOf": [{"title": "Remove nested branch", "type": "integer"}],
                            }
                        },
                        "items": {"allOf": [{"title": "Remove item branch", "type": "boolean"}]},
                        "prefixItems": [
                            {"oneOf": [{"title": "Remove prefix branch", "type": "null"}]}
                        ],
                    },
                    "booleanSchema": True,
                }
            },
        }
        expected = {
            "info": {"title": "Keep"},
            "components": {
                "schemas": {
                    "example": {
                        "oneOf": [
                            {"type": "string"},
                            {"$ref": "#/components/schemas/other", "title": "Keep ref title"},
                        ],
                        "properties": {
                            "value": {
                                "title": "Keep property title",
                                "anyOf": [{"type": "integer"}],
                            }
                        },
                        "items": {"allOf": [{"type": "boolean"}]},
                        "prefixItems": [{"oneOf": [{"type": "null"}]}],
                    },
                    "booleanSchema": True,
                }
            },
        }
        result = self.strip(spec)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout), expected)

    def test_filter_is_idempotent(self):
        spec = {
            "components": {
                "schemas": {
                    "example": {
                        "title": "Remove",
                        "oneOf": [{"title": "Remove branch", "type": "string"}],
                    }
                }
            }
        }
        first = self.strip(spec)
        self.assertEqual(first.returncode, 0, first.stderr)
        second = subprocess.run(  # noqa: S603 - jq from PATH and repository-local filter
            [self.jq, "-f", str(FILTER)],
            input=first.stdout,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(second.returncode, 0, second.stderr)
        self.assertEqual(first.stdout, second.stdout)


if __name__ == "__main__":
    unittest.main()
