#!/usr/bin/env bash
set -euo pipefail

VERSION="${1:-}"
if [ -z "$VERSION" ]; then
  echo "Usage: $0 vX.Y.Z"
  exit 1
fi

# Strip leading "v" for Python packaging versions
PY_VERSION="${VERSION#v}"

SDK_DIR="sdk"
ARTIFACT_DIR="generator/release-artifacts"

if [ ! -d "$SDK_DIR" ]; then
  echo "ERROR: $SDK_DIR/ not found. Did you merge a regen PR?"
  exit 1
fi

if [ ! -f "$SDK_DIR/pyproject.toml" ]; then
  echo "ERROR: $SDK_DIR/pyproject.toml not found. SDK not packaged?"
  exit 1
fi

echo "== Prepare Release: Python SDK (${VERSION}) =="

# Set the package version before building; the spec version stays unchanged.
uv run --locked python generator/scripts/set_version.py \
  "$SDK_DIR/pyproject.toml" \
  "$PY_VERSION"

echo "== Building sdist + wheel =="
uv build --out-dir "$SDK_DIR/dist" "$SDK_DIR"

echo "== Validating distributions (twine check) =="
uvx --from twine twine check "$SDK_DIR/dist"/*

echo "== Creating release artifacts directory =="
rm -rf "$ARTIFACT_DIR"
mkdir -p "$ARTIFACT_DIR"

# 1) Template-parity tarball of the generated SDK folder
TARBALL="python-sdk.tar.gz"
tar -czf "$ARTIFACT_DIR/$TARBALL" "$SDK_DIR"

# 2) Copy wheel + sdist into release artifacts
cp -v "$SDK_DIR/dist"/* "$ARTIFACT_DIR/"

# 3) Traceability file (helps with debugging later)
cat > "$ARTIFACT_DIR/build-info.txt" <<EOF
tag=${VERSION}
python_version=${PY_VERSION}
sdk_dir=${SDK_DIR}
built_at_utc=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
EOF

echo "== Release artifacts created =="
ls -la "$ARTIFACT_DIR"
echo "Created artifact bundle in: $ARTIFACT_DIR/"
