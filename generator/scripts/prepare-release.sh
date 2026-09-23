#!/usr/bin/env bash
set -euo pipefail

VERSION="${1:-}"
if [ -z "$VERSION" ]; then
  echo "Usage: $0 vX.Y.Z"
  exit 1
fi

# Strip leading "v" for Python packaging versions
PY_VERSION="${VERSION#v}"

ARTIFACT_DIR="generator/release-artifacts"
BUILD_DIR="$ARTIFACT_DIR/dist"

if [ ! -d "upcloud_api" ]; then
  echo "ERROR: upcloud_api/ not found. Did you merge a regen PR?"
  exit 1
fi

if [ ! -f "pyproject.toml" ]; then
  echo "ERROR: pyproject.toml not found. SDK not packaged?"
  exit 1
fi

echo "== Prepare Release: Python SDK (${VERSION}) =="

rm -rf "$ARTIFACT_DIR"
mkdir -p "$BUILD_DIR"

# Set the package version before building; the spec version stays unchanged.
uv run --locked python generator/scripts/set_version.py pyproject.toml "$PY_VERSION"

echo "== Building sdist + wheel =="
uv build --out-dir "$BUILD_DIR"

echo "== Validating distributions (twine check) =="
uvx --from twine twine check "$BUILD_DIR"/*

# 1) Source tarball of the SDK project
TARBALL="python-sdk.tar.gz"
tar --exclude='__pycache__' --exclude='*.pyc' -czf "$ARTIFACT_DIR/$TARBALL" \
  pyproject.toml README.md LICENSE.txt upcloud_api

# 2) Copy wheel + sdist into release artifacts
cp -v "$BUILD_DIR"/* "$ARTIFACT_DIR/"

# 3) Traceability file (helps with debugging later)
cat > "$ARTIFACT_DIR/build-info.txt" <<EOF
tag=${VERSION}
python_version=${PY_VERSION}
sdk_dir=.
built_at_utc=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
EOF

echo "== Release artifacts created =="
ls -la "$ARTIFACT_DIR"
echo "Created artifact bundle in: $ARTIFACT_DIR/"
