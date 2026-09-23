#!/usr/bin/env python3
import sys
from tomlkit import parse, dumps

def main():
    if len(sys.argv) != 3:
        print("Usage: set_version.py <pyproject.toml> <version>", file=sys.stderr)
        sys.exit(1)

    path = sys.argv[1]
    version = sys.argv[2]

    with open(path, "r", encoding="utf-8") as f:
        doc = parse(f.read())

    changed = False

    # Poetry-style version
    if "tool" in doc and "poetry" in doc["tool"] and "version" in doc["tool"]["poetry"]:
        doc["tool"]["poetry"]["version"] = version
        changed = True

    # PEP 621 fallback
    if "project" in doc and "version" in doc["project"]:
        doc["project"]["version"] = version
        changed = True

    if not changed:
        print(
            "ERROR: Could not find a version field in pyproject.toml "
            "([tool.poetry].version or [project].version)",
            file=sys.stderr,
        )
        sys.exit(1)

    with open(path, "w", encoding="utf-8") as f:
        f.write(dumps(doc))

    print(f"Updated {path} version -> {version}")

if __name__ == "__main__":
    main()
