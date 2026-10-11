"""Tests for generator/openapi/overlay.yaml applied with the mise-provided Speakeasy CLI."""

import copy
import itertools
import json
import shutil
import subprocess
import unittest
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OVERLAY = ROOT / "generator" / "openapi" / "overlay.yaml"
SPEC = ROOT / "generator" / "openapi" / "spec.json"
PATCHED_SPEC = ROOT / "generator" / "openapi" / "spec.patched.json"
TITLE_FILTER = ROOT / "generator" / "scripts" / "strip_schema_titles.jq"

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
OLD_LABEL_FILTER_PATTERN = r"^(?!_)[\x20-\x3C\x3E-\x7E]{2,32}(?:=.*)?$"
NEW_LABEL_FILTER_PATTERN = r"^[\x20-\x3C\x3E-\x5E\x60-\x7E][\x20-\x3C\x3E-\x7E]{1,31}(?:=.*)?$"
IP_BLOCK_PATTERN = r"^([0-9]{1,3}\.){3}[0-9]{1,3}(/([0-9]|[12][0-9]|3[0-2]))?$"


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
                        {
                            "description": "The default storage encryption strategy for all node groups."
                        },
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
                "storageLabelFilter": {"type": "string", "pattern": OLD_LABEL_FILTER_PATTERN},
                "kubernetesPrefixedClaimOrExpression": {
                    "type": "object",
                    "properties": {
                        "prefix": {
                            "type": "string",
                            "description": "Prefix prepended to the claim's value. Must be set (may be empty) when claim is set. Mutually exclusive with expression.\n",
                            "nullable": True,
                            "example": "oidc:",
                        }
                    },
                },
                "gatewayLabelValue": {
                    "type": "string",
                    "examples": ["production", "backend", "web-app", "backup", "engineering"],
                    "title": "Label value",
                    "maxLength": 255,
                    "pattern": r"\A[\p{L}\p{N}\p{P}\p{S}\p{M}\p{Z}]*\z",
                    "description": "The value of a label.",
                    "nullable": True,
                },
                "firewallRulesetLabelValue": {
                    "type": "string",
                    "examples": ["production", "backend", "web-app", "backup", "engineering"],
                    "title": "Label Value",
                    "maxLength": 255,
                    "pattern": r"\A[\p{L}\p{N}\p{P}\p{S}\p{M}\p{Z}]*\z",
                    "description": "Schema for a label value property, allowing a string or null with specific character constraints.",
                    "nullable": True,
                },
                "kubernetesIPBlock": {
                    "type": "string",
                    "pattern": r"^([0-9]{1,3}\.){3}[0-9]{1,3}($|/(0-32))$",
                },
                "createStorageRequest": {
                    "properties": {
                        "storage": {
                            "properties": {
                                "backup_rule": {
                                    "oneOf": [
                                        {"$ref": "#/components/schemas/storageBackupRule"},
                                        {"type": "object"},
                                    ]
                                }
                            }
                        }
                    }
                },
                "modifyStorageBody": {
                    "properties": {
                        "storage": {
                            "properties": {
                                "backup_rule": {
                                    "oneOf": [
                                        {"$ref": "#/components/schemas/storageBackupRule"},
                                        {"type": "object"},
                                    ]
                                }
                            }
                        }
                    }
                },
                "storageDetails": {
                    "properties": {
                        "backup_rule": {
                            "oneOf": [
                                {"$ref": "#/components/schemas/storageBackupRule"},
                                {"type": "object"},
                            ]
                        }
                    }
                },
                "accountResourceLimits": {
                    "properties": {
                        "type": {},
                        "required": {},
                        "additionalProperties": {},
                        "cores": {"type": "integer"},
                    }
                },
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
        cls.jq = shutil.which("jq")
        if cls.jq is None:
            raise AssertionError("jq not found on PATH; run `mise install`")

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
        schemas["storageLabelFilter"]["pattern"] = NEW_LABEL_FILTER_PATTERN
        prefix = schemas["kubernetesPrefixedClaimOrExpression"]["properties"]["prefix"]
        prefix.pop("nullable")
        prefix["type"] = ["string", "null"]
        for name in ("gatewayLabelValue", "firewallRulesetLabelValue"):
            schemas[name].pop("nullable")
            schemas[name]["type"] = ["string", "null"]
        schemas["kubernetesIPBlock"]["pattern"] = IP_BLOCK_PATTERN
        for name in ("createStorageRequest", "modifyStorageBody"):
            schemas[name]["properties"]["storage"]["properties"]["backup_rule"]["oneOf"][1][
                "maxProperties"
            ] = 0
        schemas["storageDetails"]["properties"]["backup_rule"]["oneOf"][1]["maxProperties"] = 0
        for name in ("type", "required", "additionalProperties"):
            schemas["accountResourceLimits"]["properties"].pop(name)

        output = self.overlay_document(spec)
        self.assertEqual(output, expected)
        # Key order decides the bytes of spec.patched.json.
        self.assertEqual(list(output["components"]["schemas"][STORAGE]), list(schemas[STORAGE]))
        self.assertEqual(list(output["paths"][CLUSTER_PATH]["post"]["responses"]), ["400", "200"])
        schemas = output["components"]["schemas"]
        self.assertEqual(schemas["storageLabelFilter"]["pattern"], NEW_LABEL_FILTER_PATTERN)
        self.assertEqual(schemas["kubernetesIPBlock"]["pattern"], IP_BLOCK_PATTERN)
        self.assertNotIn("nullable", schemas["gatewayLabelValue"])
        self.assertEqual(schemas["gatewayLabelValue"]["type"], ["string", "null"])
        self.assertNotIn("type", schemas["accountResourceLimits"]["properties"])

    def test_strict_fails_when_defects_are_already_fixed(self):
        """Fail loudly once upstream fixes a defect, so the stale action gets deleted."""
        fixed_path = self.directory / "fixed.json"
        fixed_path.write_text(
            json.dumps(self.overlay_document(defective_spec())), encoding="utf-8"
        )
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
        output_items = output["components"]["schemas"][FIREWALL]["properties"]["invalid_params"][
            "items"
        ]
        self.assertEqual(output_items["properties"], source_params["properties"])
        self.assertEqual(output_items["required"], source_params["required"])

        source_storage = source["components"]["schemas"][STORAGE]["allOf"]
        output_storage = output["components"]["schemas"][STORAGE]
        self.assertEqual(output_storage["$ref"], source_storage[0]["$ref"])
        self.assertEqual(output_storage["description"], source_storage[1]["description"])

        source_filter = source["components"]["schemas"]["storageLabelFilter"]
        self.assertEqual(source_filter["pattern"], OLD_LABEL_FILTER_PATTERN)
        self.assertEqual(
            output["components"]["schemas"]["storageLabelFilter"]["pattern"],
            NEW_LABEL_FILTER_PATTERN,
        )

        nullable_schemas = {
            "kubernetesPrefixedClaimOrExpression": "prefix",
            "gatewayLabelValue": None,
            "firewallRulesetLabelValue": None,
        }
        for name, property_name in nullable_schemas.items():
            source_schema = source["components"]["schemas"][name]
            if property_name:
                source_schema = source_schema["properties"][property_name]
                output_schema = output["components"]["schemas"][name]["properties"][property_name]
            else:
                output_schema = output["components"]["schemas"][name]
            self.assertIs(source_schema["nullable"], True)
            self.assertEqual(output_schema["type"], ["string", "null"])
            self.assertNotIn("nullable", output_schema)

        source_ip = source["components"]["schemas"]["kubernetesIPBlock"]
        self.assertEqual(source_ip["pattern"], r"^([0-9]{1,3}\.){3}[0-9]{1,3}($|/(0-32))$")
        self.assertEqual(
            output["components"]["schemas"]["kubernetesIPBlock"]["pattern"], IP_BLOCK_PATTERN
        )

        for name in ("createStorageRequest", "modifyStorageBody"):
            source_branch = source["components"]["schemas"][name]["properties"]["storage"][
                "properties"
            ]["backup_rule"]["oneOf"][1]
            self.assertEqual(source_branch, {"type": "object"})
            branch = output["components"]["schemas"][name]["properties"]["storage"]["properties"][
                "backup_rule"
            ]["oneOf"][1]
            self.assertEqual(branch, {"type": "object", "maxProperties": 0})
        self.assertEqual(
            source["components"]["schemas"]["storageDetails"]["properties"]["backup_rule"][
                "oneOf"
            ][1],
            {"type": "object"},
        )
        self.assertEqual(
            output["components"]["schemas"]["storageDetails"]["properties"]["backup_rule"][
                "oneOf"
            ][1],
            {"type": "object", "maxProperties": 0},
        )

        source_limits = source["components"]["schemas"]["accountResourceLimits"]
        output_limits = output["components"]["schemas"]["accountResourceLimits"]
        for name in ("type", "required", "additionalProperties"):
            self.assertEqual(source_limits["properties"][name], {})
            self.assertNotIn(name, output_limits["properties"])

    def test_rewritten_patterns_preserve_intended_matching(self):
        import re

        old = re.compile(OLD_LABEL_FILTER_PATTERN)
        new = re.compile(NEW_LABEL_FILTER_PATTERN)
        alphabet = ["_", "a", "=", " ", "=", "~", "\x7f"]
        candidates = {
            "".join(characters)
            for length in range(1, 4)
            for characters in itertools.product(alphabet, repeat=length)
        }
        for length in (1, 2, 32, 33):
            candidates.update({"a" * length, "_" + "a" * (length - 1), "a" * length + "=value"})
        candidates.update({"a=b", "ab=", "ab=value", "_a=value"})
        for candidate in candidates:
            self.assertEqual(
                bool(old.fullmatch(candidate)), bool(new.fullmatch(candidate)), candidate
            )

        ip_block = re.compile(IP_BLOCK_PATTERN)
        for candidate in ("1.2.3.0/24", "1.1.1.1", "0.0.0.0/0"):
            self.assertIsNotNone(ip_block.fullmatch(candidate))
        for candidate in ("1.2.3.4/33", "1.2.3.4/0-32"):
            self.assertIsNone(ip_block.fullmatch(candidate))

    def test_overlay_then_title_filter_matches_committed_patched_spec(self):
        """Overlay followed by the jq title filter reproduces spec.patched.json."""
        overlaid_path = self.directory / "overlaid.json"
        patched_path = self.directory / "patched.json"
        result = self.apply_overlay(SPEC, overlaid_path)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        result = subprocess.run(  # noqa: S603 - fixed tool and repository-local input paths
            [self.jq, "-f", str(TITLE_FILTER), str(overlaid_path)],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        patched_path.write_text(result.stdout, encoding="utf-8")
        self.assertEqual(
            json.loads(patched_path.read_text(encoding="utf-8")),
            json.loads(PATCHED_SPEC.read_text(encoding="utf-8")),
        )


if __name__ == "__main__":
    unittest.main()
