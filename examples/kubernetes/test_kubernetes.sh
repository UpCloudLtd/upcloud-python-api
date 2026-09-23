#!/usr/bin/env bash
set -euo pipefail

# Test Kubernetes API
# Tests: create_network, list_clusters, create_cluster, list_clusters again,
# delete_cluster, delete_network

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SDK_DIR="${UPCLOUD_SDK_PATH:-$(cd "$SCRIPT_DIR/../.." && pwd)}"

echo "======================================"
echo "Testing Kubernetes API"
echo "======================================"

# Check for required environment variables
if [[ -z "${UPCLOUD_TOKEN:-}" ]]; then
    echo "ERROR: UPCLOUD_TOKEN environment variable is required"
    exit 1
fi

echo ""
echo "== Test Kubernetes API with local SDK =="
uv run --no-project --with "$SDK_DIR" python "$SCRIPT_DIR/test_kubernetes.py"
