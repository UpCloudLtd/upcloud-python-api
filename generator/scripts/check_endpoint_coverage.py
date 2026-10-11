"""
Compare OpenAPI operations with generated Python endpoint contracts.

Python-specific: it parses the modules that openapi-python-client generates.
"""

import ast
import json
import re
import sys
from collections import Counter
from pathlib import Path

HTTP_METHODS = {"get", "put", "post", "delete", "patch", "head", "options", "trace"}
SURFACES = {"sync_detailed", "asyncio_detailed"}


def normalize_path(path: str) -> str:
    """Replace every path parameter name with `{}`."""
    return re.sub(r"\{[^}]+\}", "{}", path)


def operations(spec: dict) -> dict[tuple[str, str], dict]:
    """Map each (method, normalized path) in the spec to its operation."""
    result = {}
    for path, item in spec["paths"].items():
        for method, operation in item.items():
            if method in HTTP_METHODS:
                contract = (method, normalize_path(path))
                if contract in result:
                    raise ValueError(f"Duplicate OpenAPI contract: {method} {path}")
                result[contract] = {
                    **operation,
                    "path": path,
                    "method": method,
                    "parameters": item.get("parameters", []) + operation.get("parameters", []),
                }
    return result


def endpoint_contract(path: Path) -> tuple[str, str]:
    """Return the (method, normalized path) that a generated endpoint module requests."""
    tree = ast.parse(path.read_text(encoding="utf-8"))
    functions = {
        node.name: node
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }
    missing = SURFACES - functions.keys()
    if missing:
        raise ValueError(f"{path}: missing call surfaces {sorted(missing)}")
    if not isinstance(functions["asyncio_detailed"], ast.AsyncFunctionDef):
        raise ValueError(f"{path}: asyncio_detailed is not async")
    if ("sync" in functions) != ("asyncio" in functions):
        raise ValueError(f"{path}: inconsistent parsed sync/async surfaces")
    builder = functions.get("_get_kwargs")
    if builder is None:
        raise ValueError(f"{path}: missing _get_kwargs")
    contracts = []
    for node in ast.walk(builder):
        if not isinstance(node, ast.Dict):
            continue
        values = {
            key.value: value
            for key, value in zip(node.keys, node.values, strict=True)
            if isinstance(key, ast.Constant)
        }
        if not {"method", "url"} <= values.keys():
            continue
        url = values["url"]
        if (
            isinstance(url, ast.Call)
            and isinstance(url.func, ast.Attribute)
            and url.func.attr == "format"
        ):
            url = url.func.value
        if not isinstance(url, ast.Constant) or not isinstance(values["method"], ast.Constant):
            raise ValueError(f"{path}: unsupported method/URL expression")
        contracts.append((values["method"].value, normalize_path(url.value)))
    if len(contracts) != 1:
        raise ValueError(f"{path}: expected one request contract, found {len(contracts)}")
    return contracts[0]


def generated_operations(directory: Path) -> tuple[dict[tuple[str, str], Path], list[str]]:
    """Map each generated endpoint contract to its module, plus parse errors."""
    result = {}
    errors = []
    for path in sorted(directory.glob("*/*.py")):
        if path.name == "__init__.py":
            continue
        try:
            contract = endpoint_contract(path)
        except ValueError as error:
            errors.append(str(error))
            continue
        if contract in result:
            errors.append(
                f"Duplicate generated contract: {contract}: {result[contract]} and {path}"
            )
        result[contract] = path
    if not result:
        errors.append(f"No generated endpoints found in {directory}")
    return result, errors


def check_coverage(spec: dict, directory: Path, patched: dict | None = None) -> list[str]:
    """Return every missing, unexpected, or duplicate operation as an error."""
    expected = operations(spec)
    generated, errors = generated_operations(directory)
    for contract in sorted(expected.keys() - generated.keys()):
        errors.append(f"Missing {expected[contract]['operationId']}: {contract}")
    for contract in sorted(generated.keys() - expected.keys()):
        errors.append(f"Unexpected {generated[contract]}: {contract}")
    ids = Counter(operation["operationId"] for operation in expected.values())
    errors.extend(f"Duplicate operationId: {name}" for name, count in ids.items() if count > 1)
    if patched is not None and expected.keys() != operations(patched).keys():
        errors.append("Preprocessing changed the method/path inventory")
    return errors


def main() -> int:
    """Check coverage for the command-line arguments; exit 1 on any error."""
    if len(sys.argv) != 4:
        print(
            "Usage: check_endpoint_coverage.py <spec.json> <spec.patched.json> <api-dir>",
            file=sys.stderr,
        )
        return 2
    spec, patched = (json.loads(Path(p).read_text()) for p in sys.argv[1:3])
    errors = check_coverage(spec, Path(sys.argv[3]), patched)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Endpoint coverage passed: {len(operations(spec))} operations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
