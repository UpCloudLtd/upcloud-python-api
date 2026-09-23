#!/usr/bin/env bash
set -euo pipefail

# Test File Storage API
# Tests: list_services, create_service, list_services again, delete_service

# TestPyPI project name is "upcloud-api" (installs the "upcloud_api" module)
PKG_NAME="upcloud-api"
VENV_DIR=".venv-test-file-storage"
PYTHON_BIN="${PYTHON_BIN:-python3}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "======================================"
echo "Testing File Storage API"
echo "======================================"

# Check for required environment variables
if [[ -z "${UPCLOUD_TOKEN:-}" ]]; then
    echo "ERROR: UPCLOUD_TOKEN environment variable is required"
    exit 1
fi

echo "== Create clean virtualenv =="
rm -rf "${VENV_DIR}"
"${PYTHON_BIN}" -m venv "${VENV_DIR}"
# shellcheck disable=SC1091
source "${VENV_DIR}/bin/activate"

python -m pip install --upgrade pip > /dev/null

echo "== Install ${PKG_NAME} + test deps from TestPyPI =="
pip install \
    --no-cache-dir \
    --index-url https://test.pypi.org/simple/ \
    --extra-index-url https://pypi.org/simple \
    "${PKG_NAME}" \
    httpx > /dev/null

echo ""
echo "== Test File Storage API =="
python "${SCRIPT_DIR}/test_file_storage.py"

echo ""
echo "== Cleanup =="
deactivate
rm -rf "${VENV_DIR}"
echo "✓ Done"
