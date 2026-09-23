#!/usr/bin/env bash
set -euo pipefail

echo "== Generate Python SDK docs (pydoc-markdown) =="

# Always run from repo root (important)
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT_DIR"

OUT_DIR="docs-src"
OUT_FILE="$OUT_DIR/reference.md"
CONFIG="generator/config/pydoc-markdown.yml"

if [ ! -d "upcloud_api" ]; then
  echo "ERROR: upcloud_api/ not found. Merge a regen PR first."
  exit 1
fi

if [ ! -f "pyproject.toml" ]; then
  echo "ERROR: pyproject.toml not found."
  exit 1
fi

mkdir -p "$OUT_DIR"

echo "== Install SDK and generate docs =="
uvx --with "." pydoc-markdown "$CONFIG"

if [ ! -f "$OUT_FILE" ]; then
  echo "ERROR: Expected output not found: $OUT_FILE"
  exit 1
fi

echo "Generated: $OUT_FILE ($(wc -l < "$OUT_FILE") lines)"
