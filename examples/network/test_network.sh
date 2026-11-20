#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SDK_DIR="${UPCLOUD_SDK_PATH:-$(cd "$SCRIPT_DIR/../.." && pwd)}"

echo "======================================"
echo "Testing Network and Router APIs"
echo "======================================"

if [[ -z "${UPCLOUD_TOKEN:-}" ]]; then
    echo "ERROR: UPCLOUD_TOKEN environment variable is required"
    exit 1
fi

echo "== Test Network and Router APIs with local SDK =="
uv run --no-cache --no-project --with "$SDK_DIR" python "$SCRIPT_DIR/test_network.py"
