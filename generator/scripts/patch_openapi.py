#!/usr/bin/env python3
import json
import sys
from typing import Any, Dict, List, Tuple

# Exact operations to remove (path, method)
REMOVE: List[Tuple[str, str]] = []

def log(msg: str) -> None:
    print(f"[patch_openapi] {msg}")

def fix_kubernetes_default_storage_encryption(spec: Dict[str, Any]) -> None:
    """
    Fix kubernetesDefaultStorageEncryption schema that has invalid allOf.
    
    The original schema has allOf with:
    1. $ref to kubernetesStorageEncryption (valid)
    2. Just a description field (invalid - not a complete schema)
    3. Just x-go-type extension (invalid - not a complete schema)
    
    The generator fails because items 2 and 3 are not valid schemas in allOf.
    
    Since this spec is OpenAPI 3.1 (JSON Schema 2020-12), we can use sibling 
    properties alongside $ref. We flatten the allOf and keep all properties:
    - $ref: inherit the enum from kubernetesStorageEncryption
    - description: custom description for this usage
    - x-go-type: Go code generation hint
    """
    schemas = spec.get("components", {}).get("schemas", {})
    if "kubernetesDefaultStorageEncryption" not in schemas:
        log("WARNING: kubernetesDefaultStorageEncryption schema not found, skipping fix")
        return
    
    original = schemas["kubernetesDefaultStorageEncryption"]
    if "allOf" not in original:
        log("INFO: kubernetesDefaultStorageEncryption doesn't have allOf, already fixed?")
        return
    
    log("Fixing kubernetesDefaultStorageEncryption schema (flattening invalid allOf)")
    
    # In OpenAPI 3.1, we can have sibling properties with $ref
    # This preserves all original intent: inherits enum, overrides description, keeps Go hint
    schemas["kubernetesDefaultStorageEncryption"] = {
        "description": "The default storage encryption strategy for all node groups.",
        "x-go-type": "StorageEncryption",
        "$ref": "#/components/schemas/kubernetesStorageEncryption"
    }
    log("Fixed: Flattened to $ref with sibling properties (preserves description + x-go-type)")

def strip_titles_from_top_level_schemas(spec: Dict[str, Any]) -> None:
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
    for schema_key, schema in schemas.items():
        if isinstance(schema, dict) and "title" in schema:
            del schema["title"]
            removed_count += 1
    log(f"Stripped 'title' from {removed_count} top-level schemas (class names now derived from schema keys)")

def strip_titles_from_inline_schemas(spec: Dict[str, Any]) -> None:
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

    for schema_key, schema in schemas.items():
        if isinstance(schema, dict):
            strip_recursive(schema)

    log(f"Stripped 'title' from {removed_count} inline schemas (branch class names now derived from position)")

def fix_kubernetes_post_cluster_response_code(spec: Dict[str, Any]) -> None:
    """
    Fix postCluster response code from 201 to 200.
    
    The OpenAPI spec defines a 201 Created response, but the actual API returns
    200 OK when creating a cluster. This mismatch causes the SDK to fail parsing
    the response because it falls into the error handling path.
    
    We change the response code from 201 to 200 to match actual API behavior.
    """
    paths = spec.get("paths", {})
    kubernetes_path = paths.get("/1.3/kubernetes")
    
    if not kubernetes_path or not isinstance(kubernetes_path, dict):
        log("WARNING: /1.3/kubernetes path not found, skipping postCluster fix")
        return
    
    post_op = kubernetes_path.get("post")
    if not post_op or not isinstance(post_op, dict):
        log("WARNING: POST /1.3/kubernetes operation not found, skipping postCluster fix")
        return
    
    responses = post_op.get("responses")
    if not responses or not isinstance(responses, dict):
        log("WARNING: POST /1.3/kubernetes responses not found, skipping postCluster fix")
        return
    
    if "201" not in responses:
        log("INFO: POST /1.3/kubernetes doesn't have 201 response, already fixed?")
        return
    
    log("Fixing postCluster response code: 201 → 200 (matches actual API behavior)")
    
    # Move the 201 response to 200
    response_201 = responses.pop("201")
    responses["200"] = response_201
    
    log("Fixed: postCluster now expects 200 OK response")

def fix_firewall_ruleset_error_response(spec: Dict[str, Any]) -> None:
    """
    Fix firewallRulesetErrorResponse invalid_params field.
    
    The field is defined as an array but has 'required' and 'properties' at the
    array level instead of inside 'items'. This is invalid - arrays should define
    their element structure in 'items'.
    
    We move the required/properties into a proper items object schema.
    """
    schemas = spec.get("components", {}).get("schemas", {})
    if "firewallRulesetErrorResponse" not in schemas:
        log("WARNING: firewallRulesetErrorResponse schema not found, skipping fix")
        return
    
    schema = schemas["firewallRulesetErrorResponse"]
    if not isinstance(schema, dict):
        return
    
    props = schema.get("properties", {})
    if "invalid_params" not in props:
        return
    
    invalid_params = props["invalid_params"]
    if not isinstance(invalid_params, dict):
        return
    
    # Check if it has the bug (array with properties/required at wrong level)
    if invalid_params.get("type") == "array" and "properties" in invalid_params:
        log("Fixing firewallRulesetErrorResponse.invalid_params (moving properties into items)")
        
        # Extract the incorrectly placed fields
        properties = invalid_params.pop("properties")
        required = invalid_params.pop("required", None)
        
        # Create proper items schema
        items_schema = {
            "type": "object",
            "properties": properties
        }
        if required:
            items_schema["required"] = required
        
        # Set the items field
        invalid_params["items"] = items_schema
        log("Fixed: Restructured array schema to have proper items definition")

def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: patch_openapi.py <input_spec.json> <output_spec.json>", file=sys.stderr)
        return 2

    in_path, out_path = sys.argv[1], sys.argv[2]
    log(f"Input:  {in_path}")
    log(f"Output: {out_path}")

    try:
        with open(in_path, "r", encoding="utf-8") as f:
            spec: Dict[str, Any] = json.load(f)
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

    removed_ops: List[str] = []
    missing_targets: List[str] = []
    cleaned_empty_paths: List[str] = []

    for path, method in REMOVE:
        target = f"{method.upper()} {path}"
        p = paths.get(path)

        if p is None:
            missing_targets.append(f"{target} (path missing)")
            continue
        if not isinstance(p, dict):
            missing_targets.append(f"{target} (path value not an object)")
            continue

        if method not in p:
            missing_targets.append(f"{target} (method missing)")
            continue

        op = p.get(method)
        # Log useful debug details about what we are deleting
        opid = None
        if isinstance(op, dict):
            opid = op.get("operationId")

        log(f"Removing operation: {target}" + (f" (operationId={opid})" if opid else ""))

        del p[method]
        removed_ops.append(target)

        # If no operations left under this path, remove the path too.
        # (Keep parameters/servers/etc if you want; your pasted paths look operation-only.)
        remaining_keys = list(p.keys())
        # Typical OpenAPI keys in a path item are http methods + optional "parameters"
        http_methods = {"get","put","post","delete","options","head","patch","trace"}
        remaining_http = [k for k in remaining_keys if k in http_methods]
        if len(remaining_http) == 0:
            # If there are other keys like 'parameters', you can decide to keep or delete.
            # We'll delete only if empty or only non-http keys are absent.
            non_http_keys = [k for k in remaining_keys if k not in http_methods]
            if len(non_http_keys) == 0:
                del paths[path]
                cleaned_empty_paths.append(path)
                log(f"Removed empty path item: {path}")
            else:
                log(f"Path {path} has no http methods left, but kept non-http keys: {non_http_keys}")

    spec["paths"] = paths

    # Fix schema issues
    fix_kubernetes_default_storage_encryption(spec)
    strip_titles_from_top_level_schemas(spec)
    strip_titles_from_inline_schemas(spec)
    fix_firewall_ruleset_error_response(spec)
    fix_kubernetes_post_cluster_response_code(spec)

    # Summary logs
    log("---- Summary ----")
    log(f"Removed operations: {len(removed_ops)}")
    for r in removed_ops:
        log(f"  - removed: {r}")

    if missing_targets:
        log(f"Targets not removed (not found): {len(missing_targets)}")
        for m in missing_targets:
            log(f"  - not found: {m}")

    if cleaned_empty_paths:
        log(f"Removed empty paths: {len(cleaned_empty_paths)}")
        for p in cleaned_empty_paths:
            log(f"  - removed path: {p}")

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
