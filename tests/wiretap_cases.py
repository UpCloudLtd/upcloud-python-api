"""Derive SDK calls from OpenAPI examples, without endpoint-specific fixtures."""

import datetime
import importlib
import inspect
import json
import re
import types
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Any, Literal, Union, get_args, get_origin, get_type_hints
from uuid import UUID

from generator.scripts.check_endpoint_coverage import generated_operations, operations

ROOT = Path(__file__).resolve().parents[1]


class UnsupportedExample(ValueError):
    """An input cannot be derived without inventing a complex fixture."""


class InvalidExample(ValueError):
    """An available example cannot be converted to the generated input type."""


def resolve(spec: dict, value: dict) -> dict:
    seen = set()
    while "$ref" in value:
        ref = value["$ref"]
        if not ref.startswith("#/") or ref in seen:
            raise UnsupportedExample(f"Unsupported reference: {ref}")
        seen.add(ref)
        target = spec
        for part in ref[2:].split("/"):
            target = target[part.replace("~1", "/").replace("~0", "~")]
        value = {**target, **{key: item for key, item in value.items() if key != "$ref"}}
    return value


def example(spec: dict, schema: dict, depth: int = 0):
    """Prefer explicit examples; synthesize only simple required object properties."""
    if depth > 10:
        raise UnsupportedExample("Recursive/complex schema exceeds example depth")
    schema = resolve(spec, schema)
    if "example" in schema:
        return schema["example"]
    examples = schema.get("examples")
    if isinstance(examples, list) and examples:
        return examples[0]
    if isinstance(examples, dict) and examples:
        selected = resolve(spec, next(iter(examples.values())))
        if "value" in selected:
            return selected["value"]
        raise UnsupportedExample("Example requires external data")
    for key in ("const", "default"):
        if key in schema:
            return schema[key]
    if schema.get("enum"):
        return schema["enum"][0]
    if schema.get("format") == "uuid":
        return "00000000-0000-4000-8000-000000000001"
    if "schema" in schema:
        return example(spec, schema["schema"], depth + 1)
    for key in ("oneOf", "anyOf"):
        if schema.get(key):
            return example(spec, schema[key][0], depth + 1)
    if schema.get("type") == "object" or "properties" in schema:
        return {
            name: example(spec, schema["properties"][name], depth + 1)
            for name in schema.get("required", [])
        }
    raise UnsupportedExample("No example/default/enum for required input")


def python_name(name: str) -> str:
    name = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", name)
    return re.sub(r"[^a-zA-Z0-9_]", "_", name).lower()


def convert(value, annotation):
    """Convert wire examples to the types accepted by generated SDK signatures."""
    origin = get_origin(annotation)
    if origin in (types.UnionType, Union):
        errors = []
        for branch in get_args(annotation):
            try:
                return convert(value, branch)
            except (ValueError, TypeError, KeyError) as error:
                errors.append(str(error))
        raise InvalidExample(f"Example matches no generated union branch: {errors}")
    if origin is Literal:
        if value not in get_args(annotation):
            raise ValueError(f"Expected one of {get_args(annotation)}")
        return value
    if annotation is type(None):
        if value is None:
            return None
        raise TypeError("Expected null")
    if inspect.isclass(annotation) and issubclass(annotation, Enum):
        return annotation(value)
    if annotation is UUID:
        return UUID(value)
    if annotation in (datetime.datetime, datetime.date):
        return annotation.fromisoformat(value)
    if hasattr(annotation, "from_dict"):
        if not isinstance(value, dict):
            raise TypeError("Expected model object")
        return annotation.from_dict(value)
    if origin is list:
        return [convert(item, get_args(annotation)[0]) for item in value]
    if annotation is Any or origin is dict:
        return value
    if annotation in (str, int, float, bool):
        if not isinstance(value, annotation):
            raise TypeError(f"Expected {annotation.__name__}, got {type(value).__name__}")
        return value
    raise TypeError(f"Unsupported generated input type: {annotation}")


@dataclass
class Case:
    operation_id: str
    module: str
    kwargs: dict
    status: int
    has_body: bool
    query: dict


def derive_cases(
    spec: dict, api_directory: Path
) -> tuple[list[Case], list[dict], list[str], list[str]]:
    """Return cases, unsupported operations, operations without generated code, and errors."""
    generated, errors = generated_operations(api_directory)
    cases = []
    unsupported = []
    # check:endpoints owns missing-operation failures; they are inventoried here only.
    missing = []
    for contract, operation in operations(spec).items():
        if contract not in generated:
            missing.append(operation["operationId"])
            continue
        path = generated[contract]
        module_name = ".".join(path.relative_to(ROOT).with_suffix("").parts)
        module = importlib.import_module(module_name)
        signature = inspect.signature(module.sync_detailed)
        hints = get_type_hints(module.sync_detailed)
        kwargs = {}
        query = {}
        try:
            for reference in operation["parameters"]:
                parameter = resolve(spec, reference)
                if parameter["in"] not in ("path", "query"):
                    if parameter.get("required"):
                        raise UnsupportedExample(f"Required {parameter['in']} parameter")
                    continue
                name = python_name(parameter["name"])
                if name not in signature.parameters and name + "_" in signature.parameters:
                    name += "_"
                try:
                    value = example(spec, parameter)
                except UnsupportedExample:
                    if parameter.get("required") or parameter["in"] == "path":
                        raise
                    continue
                if name not in signature.parameters:
                    raise UnsupportedExample(f"No generated argument for {parameter['name']}")
                kwargs[name] = convert(value, hints[name])
                converted = kwargs[name]
                if isinstance(converted, (datetime.datetime, datetime.date)):
                    value = converted.isoformat()
                if parameter["in"] == "query" and isinstance(value, (str, int, float, bool)):
                    query[parameter["name"]] = (
                        str(value).lower() if isinstance(value, bool) else str(value)
                    )
            request = resolve(spec, operation.get("requestBody", {}))
            if request:
                content = request.get("content", {})
                if "application/json" not in content:
                    raise UnsupportedExample(f"Non-JSON request body: {list(content)}")
                kwargs["body"] = convert(example(spec, content["application/json"]), hints["body"])
            missing_arguments = [
                name
                for name, param in signature.parameters.items()
                if name != "client"
                and param.default is inspect.Parameter.empty
                and name not in kwargs
            ]
            if missing_arguments:
                raise UnsupportedExample(f"Missing required SDK arguments: {missing_arguments}")
            statuses = sorted(
                int(code)
                for code in operation["responses"]
                if code.isdigit() and 200 <= int(code) < 300
            )
            if not statuses:
                raise UnsupportedExample("No explicit successful response status")
            status = statuses[0]
            response = resolve(spec, operation["responses"][str(status)])
            cases.append(
                Case(
                    operation["operationId"],
                    module_name,
                    kwargs,
                    status,
                    bool(response.get("content")) and status != 204,
                    query,
                )
            )
        except UnsupportedExample as error:
            unsupported.append({"operation": operation["operationId"], "reason": str(error)})
        except (ValueError, TypeError, KeyError) as error:
            errors.append(f"{operation['operationId']}: invalid example/generated input: {error}")
    return cases, unsupported, missing, errors


def load_cases():
    spec = json.loads((ROOT / "generator/openapi/spec.patched.json").read_text())
    return derive_cases(spec, ROOT / "upcloud_api/api")
