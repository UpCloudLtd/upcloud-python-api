#!/usr/bin/env bash
set -euo pipefail

# Test File Storage API
# Tests: list_services, create_service, list_services again, delete_service

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SDK_DIR="${UPCLOUD_SDK_PATH:-$(cd "$SCRIPT_DIR/../.." && pwd)/sdk}"

echo "======================================"
echo "Testing File Storage API"
echo "======================================"

# Check for required environment variables
if [[ -z "${UPCLOUD_TOKEN:-}" ]]; then
    echo "ERROR: UPCLOUD_TOKEN environment variable is required"
    exit 1
fi

echo ""
echo "== Test File Storage API with local SDK =="
uv run --no-project --with "$SDK_DIR" python "$SCRIPT_DIR/test_file_storage.py"
