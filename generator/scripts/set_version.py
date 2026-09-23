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

    if "project" not in doc or "version" not in doc["project"]:
        print(
            "ERROR: Could not find [project].version in pyproject.toml",
            file=sys.stderr,
        )
        sys.exit(1)

    doc["project"]["version"] = version
    with open(path, "w", encoding="utf-8") as f:
        f.write(dumps(doc))

    print(f"Updated {path} version -> {version}")

if __name__ == "__main__":
    main()
