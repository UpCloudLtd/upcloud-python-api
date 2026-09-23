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

# Build in an isolated venv to avoid relying on runner Python packages
BUILD_VENV=".venv-release-build"
rm -rf "$BUILD_VENV"
python3 -m venv "$BUILD_VENV"
# shellcheck disable=SC1090
source "$BUILD_VENV/bin/activate"

python -m pip install --upgrade pip setuptools wheel build twine tomlkit poetry-core

# Set poetry version in pyproject.toml
python generator/scripts/set_version.py \
  "$SDK_DIR/pyproject.toml" \
  "$PY_VERSION"

echo "== Building sdist + wheel =="
rm -rf "$SDK_DIR/dist"
mkdir -p "$SDK_DIR/dist"
python -m build --outdir "$SDK_DIR/dist" "$SDK_DIR"

echo "== Validating distributions (twine check) =="
python -m twine check "$SDK_DIR/dist"/*

deactivate

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
