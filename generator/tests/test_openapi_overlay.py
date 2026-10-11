"""Tests for generator/openapi/overlay.yaml applied with the mise-provided Speakeasy CLI."""

import copy
import functools
import itertools
import json
import operator
import shutil
import subprocess
import unittest
import uuid
from pathlib import Path

from upcloud_api.models.gateway_service_log_session_create_response import (
    GatewayServiceLogSessionCreateResponse,
)
from upcloud_api.models.kubernetes_cluster_available_upgrades import (
    KubernetesClusterAvailableUpgrades,
)

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
GATEWAY_ROUTER = {"uuid": "fedcba98-7654-3210-fedc-ba9876543210"}
EMPTY_STRING_BRANCH = {"type": "string", "maxLength": 0}
DATABASE_EXAMPLES = {
    "databaseServiceCreateOpenAPI": ("8", "8.4"),
    "databaseServiceModifyOpenAPI": ("8", "8.4"),
    "databaseServiceCloneOpenAPI": ("13", "15"),
}
CLUSTER_VERSION = "1.26"
CLUSTER_LABELS = [{"key": "env", "value": "prod"}, {"key": "app", "value": "cats-dating-app"}]
CLUSTER_RESPONSES = (
    "kubernetesGetClusters",
    "kubernetesGetCluster",
    "kubernetesPatchCluster",
    "kubernetesPostCluster",
)
TUNNEL_REQUESTS = ("gatewayTunnelCreateRequest", "gatewayTunnelModifyRequest")
OLD_TUNNEL_AUTH = {"type": "psk", "psk": "MySecretPsk123"}
NEW_TUNNEL_AUTH = {"authentication": "psk", "psk": "MySecretPsk123"}
DATABASE_TYPE_PROPERTIES = {
    "automatic_utility_network_ip_filter": False,
    "ip_filter": ["0.0.0.0/0"],
    "public_access": True,
    "version": "13",
}


def json_example(example):
    """Return an application/json content map holding the given example."""
    return {"application/json": {"example": example}}


def cluster_examples(components):
    """Yield every Kubernetes cluster object in the cluster response examples."""
    for name in CLUSTER_RESPONSES:
        example = components["responses"][name]["content"]["application/json"]["example"]
        yield from example if isinstance(example, list) else [example]


def database_example(version):
    """Return a database request schema whose example carries the given engine version."""
    return {
        "examples": [
            {
                "title": "db",
                "properties": {"automatic_utility_network_ip_filter": True, "version": version},
            }
        ]
    }


def defective_spec():
    """Return a minimal spec with the defects the overlay fixes, plus unrelated data."""
    spec = {
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
                "accounts": {
                    "example": {
                        "accounts": {
                            "account": [
                                {"type": "mymain", "username": "test"},
                                {"type": "sub", "username": "other"},
                            ]
                        }
                    }
                },
                "databasePlanComponentsResponse": {
                    "properties": {
                        "backups": {
                            "properties": {
                                "name": {
                                    "type": "string",
                                    "enum": ["mini", "regular", "extended"],
                                    "example": "standard",
                                }
                            }
                        }
                    }
                },
                "gatewayServiceCreateRequest": {
                    "examples": [{"name": "gw", "features": [], "routers": [], "addresses": []}]
                },
                "gatewayServiceModifyRequest": {
                    "examples": [{"name": "gw", "features": [], "labels": []}],
                    "properties": {"features": {"examples": [[]], "minItems": 1}},
                },
                **{name: database_example(old) for name, (old, _) in DATABASE_EXAMPLES.items()},
                "serverVncPort": {
                    "oneOf": [{"type": "integer"}, {"type": "string", "const": ""}],
                    "example": 5901,
                },
                "storageImport": {
                    "properties": {
                        "completed": {
                            "oneOf": [{"const": ""}, {"type": "string", "format": "date-time"}]
                        }
                    }
                },
                "auditLogsFilterOptionsResponse": {
                    "properties": {
                        "resource_types": {
                            "type": "array",
                            "items": {"type": "string", "enum": ["account", "server"]},
                        }
                    }
                },
                "auditLogsResourceTypesParameter": {
                    "type": "array",
                    "items": {"type": "string", "enum": ["account", "server"]},
                },
                "objectStorage2EndpointResponse": {
                    "properties": {"type": {"type": "string", "enum": ["public", "private"]}}
                },
                "databaseAvailableServiceTypesResponse": {
                    "examples": [
                        {"postgres": {"name": "postgresql", "properties": {"version": "13"}}}
                    ]
                },
                "databaseServiceTypeResponse": {
                    "examples": [{"name": "postgresql", "properties": {"version": "13"}}]
                },
                "loadBalancerProblemResponse": {
                    "properties": {
                        "correlation_id": {"type": "string", "format": "uuid", "example": "req-1"}
                    }
                },
                **{
                    name: {
                        "examples": [
                            {"name": "tunnel", "ipsec": {"authentication": dict(OLD_TUNNEL_AUTH)}}
                        ]
                    }
                    for name in TUNNEL_REQUESTS
                },
                "gatewayServiceLogSessionCreateResponse": {"examples": [{"sessions": ["vpn"]}]},
                "databaseNetworkCreate": {
                    "examples": [
                        {"name": "my-network", "type": "public", "family": "IPv4"},
                        {
                            "uuid": "123e4567-e89b-12d3-a456-426614174000",
                            "name": "my-network",
                            "type": "public",
                            "family": "IPv4",
                        },
                    ]
                },
                "firewallRulesetFirewallMultipleRuleCreate": {
                    "examples": [
                        [
                            {
                                "direction": "in",
                                "action": "accept",
                                "family": "IPv4",
                                "protocol": "tcp",
                                "enabled": False,
                            },
                            {"direction": "out", "action": "drop", "family": "IPv6"},
                        ]
                    ]
                },
            },
            "responses": {
                "kubernetesPostCluster": {
                    "description": "Created cluster",
                    "content": json_example({"name": "created"}),
                },
                "kubernetesGetClusters": {
                    "content": json_example([{"name": "first"}, {"name": "second"}])
                },
                "kubernetesGetCluster": {"content": json_example({"name": "one"})},
                "kubernetesPatchCluster": {"content": json_example({"name": "patched"})},
                "kubernetesGetAvailableUpgrades": {
                    "content": json_example([{"versions": ["1.31.8", "1.32.0"]}])
                },
            },
            "requestBodies": {
                "kubernetesPostCluster": {
                    "content": json_example(
                        {"name": "new", "labels": copy.deepcopy(CLUSTER_LABELS)}
                    )
                }
            },
        },
    }
    spec["components"]["schemas"]["databaseServiceCloneOpenAPI"].update(
        type="object",
        oneOf=[{"$ref": "#/components/schemas/databaseServiceClonePg"}],
        additionalProperties=False,
    )
    return spec


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
        schemas["accounts"]["example"]["accounts"]["account"][0]["type"] = "main"
        schemas["databasePlanComponentsResponse"]["properties"]["backups"]["properties"]["name"][
            "example"
        ] = "regular"
        create_example = schemas["gatewayServiceCreateRequest"]["examples"][0]
        create_example["features"] = ["nat"]
        create_example["routers"] = [GATEWAY_ROUTER]
        schemas["gatewayServiceModifyRequest"]["examples"][0].pop("features")
        for name, (_, new) in DATABASE_EXAMPLES.items():
            schemas[name]["examples"][0]["properties"]["version"] = new
        schemas["serverVncPort"]["oneOf"][1] = EMPTY_STRING_BRANCH
        schemas["storageImport"]["properties"]["completed"]["oneOf"][0] = EMPTY_STRING_BRANCH
        schemas["auditLogsFilterOptionsResponse"]["properties"]["resource_types"]["items"][
            "enum"
        ].append("network")
        schemas["auditLogsResourceTypesParameter"]["items"]["enum"].append("network")
        schemas["objectStorage2EndpointResponse"]["properties"]["type"]["enum"].append("static")
        for example in cluster_examples(expected["components"]):
            example.update(version=CLUSTER_VERSION, labels=CLUSTER_LABELS)
        request_bodies = expected["components"]["requestBodies"]
        request_bodies["kubernetesPostCluster"]["content"]["application/json"]["example"][
            "version"
        ] = CLUSTER_VERSION
        schemas["databaseAvailableServiceTypesResponse"]["examples"][0]["postgres"][
            "properties"
        ] = {}
        schemas["databaseServiceTypeResponse"]["examples"][0]["properties"] = {}
        schemas["loadBalancerProblemResponse"]["properties"]["correlation_id"].pop("format")
        for name in TUNNEL_REQUESTS:
            schemas[name]["examples"][0]["ipsec"]["authentication"] = NEW_TUNNEL_AUTH
        schemas["databaseServiceCloneOpenAPI"].pop("additionalProperties")
        schemas["databaseServiceCloneOpenAPI"]["unevaluatedProperties"] = False
        schemas["gatewayServiceLogSessionCreateResponse"]["examples"][0]["sessions"] = [
            {
                "session_id": "01234567-89ab-cdef-0123-456789abcdef",
                "token": "01234567-89ab-cdef-0123-456789abcdef",
            }
        ]
        schemas["databaseNetworkCreate"]["examples"] = [
            {**example, "type": "private"}
            for example in schemas["databaseNetworkCreate"]["examples"]
        ]
        schemas["firewallRulesetFirewallMultipleRuleCreate"]["examples"] = [
            {"rules": schemas["firewallRulesetFirewallMultipleRuleCreate"]["examples"][0]}
        ]
        expected["components"]["responses"]["kubernetesGetAvailableUpgrades"]["content"][
            "application/json"
        ]["example"] = {"versions": ["1.31.8", "1.32.0"]}

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

    def test_example_fixes_match_the_source_spec(self):
        """Each example fix replaces the upstream value it expects with an in-schema value."""
        source = json.loads(SPEC.read_text(encoding="utf-8"))["components"]["schemas"]
        output = self.overlay_document(json.loads(SPEC.read_text(encoding="utf-8")))
        output = output["components"]["schemas"]

        account_enum = source["accounts"]["properties"]["accounts"]["properties"]["account"][
            "items"
        ]["properties"]["type"]["enum"]
        source_account = source["accounts"]["example"]["accounts"]["account"][0]
        output_account = output["accounts"]["example"]["accounts"]["account"][0]
        self.assertEqual(source_account["type"], "mymain")
        self.assertEqual(output_account["type"], "main")
        self.assertIn(output_account["type"], account_enum)

        source_plan = source["databasePlanComponentsResponse"]
        source_name = source_plan["properties"]["backups"]["properties"]["name"]
        output_name = output["databasePlanComponentsResponse"]["properties"]["backups"][
            "properties"
        ]["name"]
        self.assertEqual(source_name["example"], "standard")
        self.assertEqual(output_name["example"], source_plan["examples"][0]["backups"]["name"])
        self.assertIn(output_name["example"], source_name["enum"])

        source_create = source["gatewayServiceCreateRequest"]
        output_create = output["gatewayServiceCreateRequest"]["examples"][0]
        for name in ("features", "routers"):
            self.assertEqual(source_create["examples"][0][name], [])
            self.assertIn(name, source_create["required"])
            self.assertEqual(output_create[name], source_create["properties"][name]["examples"][0])
            self.assertGreaterEqual(
                len(output_create[name]), source_create["properties"][name]["minItems"]
            )

        source_modify = source["gatewayServiceModifyRequest"]
        self.assertEqual(source_modify["examples"][0]["features"], [])
        self.assertEqual(source_modify["properties"]["features"]["minItems"], 1)
        self.assertNotIn("features", source_modify.get("required", []))
        output_modify = output["gatewayServiceModifyRequest"]
        self.assertNotIn("features", output_modify["examples"][0])
        self.assertEqual(output_modify["properties"], source_modify["properties"])

        engine_enums = {
            "8.4": source["databaseServicePropertiesMysql"]["properties"]["version"]["enum"],
            "15": source["databaseServicePropertiesPg"]["properties"]["version"]["enum"],
        }
        for name, (old, new) in DATABASE_EXAMPLES.items():
            with self.subTest(schema=name):
                source_properties = source[name]["examples"][0]["properties"]
                output_properties = output[name]["examples"][0]["properties"]
                self.assertEqual(source_properties["version"], old)
                self.assertEqual(output_properties, {**source_properties, "version": new})
                self.assertIn(new, engine_enums[new])

        self.assertEqual(source["serverVncPort"]["oneOf"][1], {"type": "string", "const": ""})
        self.assertEqual(output["serverVncPort"]["oneOf"][1], EMPTY_STRING_BRANCH)
        self.assertEqual(output["serverVncPort"]["oneOf"][0], source["serverVncPort"]["oneOf"][0])
        source_completed = source["storageImport"]["properties"]["completed"]["oneOf"]
        output_completed = output["storageImport"]["properties"]["completed"]["oneOf"]
        self.assertEqual(source_completed[0], {"const": ""})
        self.assertEqual(output_completed, [EMPTY_STRING_BRANCH, source_completed[1]])

    def test_contract_fixes_match_the_source_spec(self):
        """Each enum, format, example and wrapper fix starts from the upstream value it expects."""
        source = json.loads(SPEC.read_text(encoding="utf-8"))
        output = self.overlay_document(json.loads(SPEC.read_text(encoding="utf-8")))
        source_schemas = source["components"]["schemas"]
        output_schemas = output["components"]["schemas"]

        enum_paths = {
            ("auditLogsFilterOptionsResponse", "properties", "resource_types", "items"): "network",
            ("auditLogsResourceTypesParameter", "items"): "network",
            ("objectStorage2EndpointResponse", "properties", "type"): "static",
        }
        for path, value in enum_paths.items():
            with self.subTest(enum=path[0]):
                source_enum = functools.reduce(operator.getitem, path, source_schemas)["enum"]
                output_enum = functools.reduce(operator.getitem, path, output_schemas)["enum"]
                self.assertNotIn(value, source_enum)
                self.assertEqual(output_enum, [*source_enum, value])

        self.assertEqual(source_schemas["kubernetesClusterVersion"]["default"], CLUSTER_VERSION)
        required = source_schemas["kubernetesCluster"]["required"]
        request_path = ("requestBodies", "kubernetesPostCluster", "content", "application/json")
        source_request = functools.reduce(operator.getitem, request_path, source["components"])
        output_request = functools.reduce(operator.getitem, request_path, output["components"])
        self.assertNotIn("version", source_request["example"])
        self.assertEqual(source_request["example"]["labels"], CLUSTER_LABELS)
        self.assertEqual(
            output_request["example"], {**source_request["example"], "version": CLUSTER_VERSION}
        )
        source_clusters = list(cluster_examples(source["components"]))
        output_clusters = list(cluster_examples(output["components"]))
        self.assertEqual(len(output_clusters), 5)
        for source_cluster, output_cluster in zip(source_clusters, output_clusters, strict=True):
            self.assertNotIn("version", source_cluster)
            self.assertNotIn("labels", source_cluster)
            self.assertEqual(
                output_cluster,
                {**source_cluster, "version": CLUSTER_VERSION, "labels": CLUSTER_LABELS},
            )
            self.assertLessEqual(set(required), set(output_cluster))

        database_types = (
            ("databaseAvailableServiceTypesResponse", "examples", 0, "postgres"),
            ("databaseServiceTypeResponse", "examples", 0),
        )
        for path in database_types:
            with self.subTest(example=path[0]):
                source_example = functools.reduce(operator.getitem, path, source_schemas)
                output_example = functools.reduce(operator.getitem, path, output_schemas)
                self.assertEqual(source_example["properties"], DATABASE_TYPE_PROPERTIES)
                self.assertEqual(output_example, {**source_example, "properties": {}})

        source_id = source_schemas["loadBalancerProblemResponse"]["properties"]["correlation_id"]
        output_id = output_schemas["loadBalancerProblemResponse"]["properties"]["correlation_id"]
        self.assertEqual(source_id["format"], "uuid")
        self.assertEqual(output_id, {k: v for k, v in source_id.items() if k != "format"})

        auth_types = source_schemas["gatewayIpsecAuthenticationType"]["enum"]
        for name in TUNNEL_REQUESTS:
            with self.subTest(schema=name):
                source_ipsec = source_schemas[name]["examples"][0]["ipsec"]
                output_ipsec = output_schemas[name]["examples"][0]["ipsec"]
                self.assertEqual(source_ipsec["authentication"], OLD_TUNNEL_AUTH)
                self.assertEqual(output_ipsec, {**source_ipsec, "authentication": NEW_TUNNEL_AUTH})
                auth = source_schemas[name]["properties"]["ipsec"]["properties"]["authentication"]
                self.assertIs(auth["additionalProperties"], False)
                self.assertLessEqual(set(auth["required"]), set(NEW_TUNNEL_AUTH))
                self.assertLessEqual(set(NEW_TUNNEL_AUTH), set(auth["properties"]))
                self.assertIn(NEW_TUNNEL_AUTH["authentication"], auth_types)
                self.assertRegex(NEW_TUNNEL_AUTH["psk"], auth["properties"]["psk"]["pattern"])

        source_clone = source_schemas["databaseServiceCloneOpenAPI"]
        output_clone = output_schemas["databaseServiceCloneOpenAPI"]
        self.assertIs(source_clone["additionalProperties"], False)
        self.assertNotIn("unevaluatedProperties", source_clone)
        self.assertNotIn("additionalProperties", output_clone)
        self.assertIs(output_clone["unevaluatedProperties"], False)
        self.assertEqual(len(source_clone["oneOf"]), 5)
        self.assertEqual(output_clone["oneOf"], source_clone["oneOf"])
        self.assertEqual(output_clone["properties"], source_clone["properties"])

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

    def test_corrected_examples_preserve_contract_shapes(self):
        source = json.loads(SPEC.read_text(encoding="utf-8"))
        output = self.overlay_document(source)
        source_components = source["components"]
        output_components = output["components"]

        source_upgrade = source_components["responses"]["kubernetesGetAvailableUpgrades"][
            "content"
        ]["application/json"]["example"]
        output_upgrade = output_components["responses"]["kubernetesGetAvailableUpgrades"][
            "content"
        ]["application/json"]["example"]
        self.assertEqual(len(source_upgrade), 1)
        self.assertEqual(output_upgrade, source_upgrade[0])
        self.assertEqual(
            KubernetesClusterAvailableUpgrades.from_dict(output_upgrade).to_dict(), output_upgrade
        )

        source_schemas = source_components["schemas"]
        output_schemas = output_components["schemas"]
        source_sessions = source_schemas["gatewayServiceLogSessionCreateResponse"]["examples"][0][
            "sessions"
        ]
        details_sessions = source_schemas["gatewayServiceLogSessionDetailsResponse"]["examples"][
            0
        ]["sessions"]
        output_sessions_schema = output_schemas["gatewayServiceLogSessionCreateResponse"]
        output_sessions = output_sessions_schema["examples"][0]["sessions"]
        self.assertEqual(source_sessions, ["vpn"])
        self.assertEqual(details_sessions[0].keys(), {"session_id", "token"})
        self.assertEqual(output_sessions, details_sessions)
        self.assertEqual(
            GatewayServiceLogSessionCreateResponse.from_dict(
                output_sessions_schema["examples"][0]
            ).to_dict(),
            output_sessions_schema["examples"][0],
        )

        source_network = source_schemas["databaseNetworkCreate"]
        output_network = output_schemas["databaseNetworkCreate"]
        allowed_types = source_schemas["databaseNetworkType"]["enum"]
        self.assertEqual(
            [example["type"] for example in source_network["examples"]], ["public"] * 2
        )
        self.assertEqual(allowed_types, ["private"])
        self.assertEqual(
            output_network["examples"],
            [{**example, "type": "private"} for example in source_network["examples"]],
        )
        self.assertTrue(
            all(example["type"] in allowed_types for example in output_network["examples"])
        )

        source_firewall = source_schemas["firewallRulesetFirewallMultipleRuleCreate"]["examples"][
            0
        ]
        output_firewall = output_schemas["firewallRulesetFirewallMultipleRuleCreate"]["examples"][
            0
        ]
        self.assertIsInstance(source_firewall, list)
        self.assertEqual(output_firewall, {"rules": source_firewall})

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
