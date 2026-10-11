#!/usr/bin/env python3
"""
Strip schema titles from the UpCloud OpenAPI spec so openapi-python-client can generate it.

Python-specific; runs after generator/openapi/overlay.yaml is applied. Only title
removal lives here because Overlay 1.0.0 cannot delete primitive-valued keys; every
other spec fix belongs in the overlay.
"""

import json
import sys
from typing import Any


def log(msg: str) -> None:
    """Print a message with the script prefix."""
    print(f"[patch_openapi] {msg}")


def strip_titles_from_top_level_schemas(spec: dict[str, Any]) -> None:
    """
    Remove 'title' from every entry in components/schemas.

    Problem:
        openapi-python-client derives Python class names from the 'title' field
        when present, falling back to the schema key name only when title is
        absent. All generated classes land in a single flat models/ namespace.

        The UpCloud spec uses short, generic titles like 'NetworkCreate',
        'LabelCreate', 'ErrorResponse', 'NetworkType', etc. across multiple
        API domains (objectStorage2, fileStorage, database, loadBalancer,
        firewallRuleset). These identical titles cause the generator to attempt
        creating duplicate Python classes, which it rejects — silently dropping
        entire schema trees and all endpoints that depend on them.

    Fix:
        Strip 'title' from all top-level components/schemas entries.
        The generator then falls back to the schema key name, which is always
        unique by OpenAPI contract (e.g. 'objectStorage2NetworkCreate' becomes
        class ObjectStorage2NetworkCreate, 'fileStorageNetworkCreate' becomes
        FileStorageNetworkCreate). This is consistent, collision-free, and
        requires no future maintenance regardless of how many new API domains
        are added to the spec.
    """
    schemas = spec.get("components", {}).get("schemas", {})
    removed_count = 0
    for schema in schemas.values():
        if isinstance(schema, dict) and "title" in schema:
            del schema["title"]
            removed_count += 1
    log(
        f"Stripped 'title' from {removed_count} top-level schemas (class names now derived from schema keys)"
    )


def strip_titles_from_inline_schemas(spec: dict[str, Any]) -> None:
    """
    Remove 'title' from all inline schemas within oneOf/anyOf/allOf branches
    (and recursively within properties, items, etc.) throughout the spec.

    Problem:
        Same as the top-level title collision problem, but at the branch level.
        Multiple schemas can have oneOf/anyOf branches with identical 'title' values
        across different schemas. The generator uses the branch 'title' directly as
        the Python class name for the anonymous union branch model, causing class name
        collisions when the second schema tries to register the same class.

        The generator's union.py picks up the branch title as the subscript:
            subscript = sub_prop_data.title  (if set)
        And model_property.py uses it for the class name:
            title = data.title or name        # data.title takes priority over name!

        Known collisions in this spec:
        - "Static member":           loadBalancerMemberCreate[0] + loadBalancerMemberModify[0]
        - "Dynamic member":          loadBalancerMemberCreate[1] + loadBalancerMemberModify[1]
        - "Range matcher":           loadBalancerMatcherIntCreate[0] + loadBalancerMatcherBackendCreate[0]
        - "Equality/comparison matcher": loadBalancerMatcherIntCreate[1] + loadBalancerMatcherBackendCreate[1]

        The second schema in each pair fails with:
            "Unable to parse schema /components/schemas/..."
            "Invalid property in union ..."

    Fix:
        Strip 'title' from all inline branch schemas. Without a title, the generator
        falls back to positional subscripts (type_0, type_1, ...) combined with the
        parent schema name, creating unique class names such as:
        - LoadBalancerMemberCreateType0  /  LoadBalancerMemberModifyType0
        - LoadBalancerMatcherIntCreateType0  /  LoadBalancerMatcherBackendCreateType0

        This future-proofs against any new branch-level title collisions as more API
        domains are added to the spec. Top-level schema key names are unique by OpenAPI
        contract; inline branch titles carry no such guarantee.

    Source fix needed (uplb):
        Files that define these schemas with duplicate branch titles should add unique
        titles or remove them:
        - internal/controller/schema/files/member_create.json
        - internal/controller/schema/files/member_modify.json
        - internal/controller/schema/files/matcher_int_create.json
        - internal/controller/schema/files/matcher_backend_create.json
    """
    schemas = spec.get("components", {}).get("schemas", {})
    removed_count = 0

    def strip_recursive(schema: dict, depth: int = 0) -> None:
        nonlocal removed_count
        if depth > 20:  # prevent infinite recursion on pathological specs
            return
        for key in ("oneOf", "anyOf", "allOf"):
            for branch in schema.get(key, []):
                if isinstance(branch, dict) and "$ref" not in branch:
                    if "title" in branch:
                        del branch["title"]
                        removed_count += 1
                    strip_recursive(branch, depth + 1)
        for prop_schema in schema.get("properties", {}).values():
            if isinstance(prop_schema, dict) and "$ref" not in prop_schema:
                strip_recursive(prop_schema, depth + 1)
        items = schema.get("items")
        if isinstance(items, dict) and "$ref" not in items:
            strip_recursive(items, depth + 1)
        for prefix_item in schema.get("prefixItems", []):
            if isinstance(prefix_item, dict) and "$ref" not in prefix_item:
                strip_recursive(prefix_item, depth + 1)

    for schema in schemas.values():
        if isinstance(schema, dict):
            strip_recursive(schema)

    log(
        f"Stripped 'title' from {removed_count} inline schemas (branch class names now derived from position)"
    )


def main() -> int:
    """Patch the input spec into the output path; return the exit status."""
    if len(sys.argv) != 3:
        print("Usage: patch_openapi.py <input_spec.json> <output_spec.json>", file=sys.stderr)
        return 2

    in_path, out_path = sys.argv[1], sys.argv[2]
    log(f"Input:  {in_path}")
    log(f"Output: {out_path}")

    try:
        with open(in_path, encoding="utf-8") as f:
            spec: dict[str, Any] = json.load(f)
    except FileNotFoundError:
        log(f"ERROR: input spec not found: {in_path}")
        return 2
    except json.JSONDecodeError as e:
        log(f"ERROR: input spec is not valid JSON: {e}")
        return 2

    paths = spec.get("paths")
    if not isinstance(paths, dict):
        log("ERROR: spec['paths'] missing or not an object")
        return 2

    log(f"Paths in spec: {len(paths)}")

    strip_titles_from_top_level_schemas(spec)
    strip_titles_from_inline_schemas(spec)

    try:
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(spec, f, indent=2, sort_keys=False)
            f.write("\n")
    except Exception as e:
        log(f"ERROR: failed writing output spec: {e}")
        return 2

    log("Patch completed successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
