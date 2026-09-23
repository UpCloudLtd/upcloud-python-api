#!/usr/bin/env bash
set -euo pipefail

echo "== Generate Python SDK docs (pydoc-markdown) =="

# Always run from repo root (important)
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT_DIR"

SDK_DIR="sdk"
OUT_DIR="docs-src"
OUT_FILE="$OUT_DIR/reference.md"
CONFIG="generator/config/pydoc-markdown.yml"

if [ ! -d "$SDK_DIR" ]; then
  echo "ERROR: $SDK_DIR/ not found. Merge a regen PR first."
  exit 1
fi

if [ ! -f "$SDK_DIR/pyproject.toml" ]; then
  echo "ERROR: $SDK_DIR/pyproject.toml not found."
  exit 1
fi

mkdir -p "$OUT_DIR"

echo "== Install SDK and generate docs =="
uvx --with "./$SDK_DIR" pydoc-markdown "$CONFIG"

if [ ! -f "$OUT_FILE" ]; then
  echo "ERROR: Expected output not found: $OUT_FILE"
  exit 1
fi

echo "Generated: $OUT_FILE ($(wc -l < "$OUT_FILE") lines)"
