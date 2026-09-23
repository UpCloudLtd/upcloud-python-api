#!/usr/bin/env bash
set -euo pipefail

# Test Object Storage 2.0 API
# Tests: list_services, create_service, list_services again

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SDK_DIR="${UPCLOUD_SDK_PATH:-$(cd "$SCRIPT_DIR/../.." && pwd)}"

echo "======================================"
echo "Testing Object Storage 2.0 API"
echo "======================================"

# Check for required environment variables
if [[ -z "${UPCLOUD_TOKEN:-}" ]]; then
    echo "ERROR: UPCLOUD_TOKEN environment variable is required"
    exit 1
fi

echo ""
echo "== Test Object Storage 2.0 API with local SDK =="
uv run --no-project --with "$SDK_DIR" python "$SCRIPT_DIR/test_object_storage.py"
