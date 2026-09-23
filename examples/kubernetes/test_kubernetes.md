# Testing the Kubernetes API

This example demonstrates how to use the UpCloud Python SDK to interact with the Kubernetes (UKS) API. We'll create a test script that:

- Authenticates a client using a bearer token
- Lists existing Kubernetes clusters
- Creates a new Kubernetes cluster with a node group
- Verifies the cluster was created
- Cleans up by deleting the test cluster

## Prerequisites

> **Note:** This test currently requires an existing UpCloud network. You must provide
> the network UUID via the `UKS_NETWORK` environment variable.
>
> In a future version, once the Python SDK supports network creation, this example
> will be updated to create its own network programmatically, eliminating the need
> for the `UKS_NETWORK` environment variable.

## The Python Test Script

Let's build the test script step by step.

### Imports and Module Docstring

First, we define the script's purpose and import the necessary modules. We need the UpCloud SDK client, the Kubernetes API functions, and the models for creating clusters.

```py filename=test_kubernetes_test.py
#!/usr/bin/env python3
"""Test script for Kubernetes API.

Tests:
- Authenticate client
- List existing clusters
- Create a new cluster
- List clusters again to verify creation
- Delete the test cluster
"""

import os
import sys
import time
from uuid import UUID

from upcloud_api import AuthenticatedClient
from upcloud_api.api.kubernetes import (
    get_clusters,
    post_cluster,
    delete_cluster,
)
from upcloud_api.models import KubernetesCluster
from upcloud_api.models.kubernetes_node_group import KubernetesNodeGroup
from upcloud_api.types import UNSET

```

### Main Function Setup

The `main()` function starts by reading configuration from environment variables. The `UPCLOUD_TOKEN` and `UKS_NETWORK` are required, while other parameters have sensible defaults.

```py filename=test_kubernetes_test.py

def main():
    token = os.environ.get("UPCLOUD_TOKEN")
    network = os.environ.get("UKS_NETWORK")  # Network UUID
    zone = os.environ.get("UKS_ZONE", "fi-hel1")
    network_cidr = os.environ.get("UKS_NETWORK_CIDR", "10.0.0.0/24")
    version = os.environ.get("UKS_VERSION", "1.34")
    node_group_plan = os.environ.get("UKS_NODE_GROUP_PLAN", "DEV-1xCPU-2GB")
    node_group_count = int(os.environ.get("UKS_NODE_GROUP_COUNT", "1"))
    ssh_keys_raw = os.environ.get("UKS_SSH_KEYS", "").strip()

    if not token:
        print("ERROR: UPCLOUD_TOKEN environment variable is required")
        sys.exit(1)

    missing = [
        name
        for name, value in (
            ("UKS_NETWORK", network),
        )
        if not value
    ]
    if missing:
        print("ERROR: Missing required environment variables: " + ", ".join(missing))
        sys.exit(1)

    ssh_keys = [key.strip() for key in ssh_keys_raw.split(",") if key.strip()] if ssh_keys_raw else None

    print("1. Authenticating client...")
    try:
        client = AuthenticatedClient(token=token)
        print("   Client authenticated successfully")
    except Exception as e:
        print(f"   Error: {e}")
        sys.exit(1)
```

### Step 2: List Existing Clusters (Before)

Before creating a new cluster, we list all existing Kubernetes clusters. This establishes a baseline count that we'll use later to verify our new cluster was created.

```py filename=test_kubernetes_test.py

    print("\n2. Listing existing Kubernetes clusters (BEFORE)...")
    try:
        response = get_clusters.sync_detailed(client=client)

        if response.status_code == 200 and response.parsed is not None:
            clusters_before = response.parsed or []

            print(f"   Found {len(clusters_before)} cluster(s)")
            for cluster in clusters_before:
                cluster_name = getattr(cluster, "name", "unknown")
                cluster_zone = getattr(cluster, "zone", "unknown")
                print(f"     - {cluster_name} (zone: {cluster_zone})")
        else:
            print(f"   Failed with status: {response.status_code}")
            sys.exit(1)
    except Exception as e:
        print(f"   Error: {e}")
        sys.exit(1)
```

### Step 3: Create a New Kubernetes Cluster

Now we create a new Kubernetes cluster using the `KubernetesCluster` and `KubernetesNodeGroup` models. We generate a unique name using a timestamp to avoid conflicts.

```py filename=test_kubernetes_test.py

    print("\n3. Creating a new Kubernetes cluster...")
    test_cluster_name = f"test-k8s-{int(time.time())}"
    created_cluster_uuid = None

    try:
        node_group = KubernetesNodeGroup(
            name="default",
            count=node_group_count,
            plan=node_group_plan,
            ssh_keys=ssh_keys if ssh_keys is not None else UNSET,
        )

        cluster_payload = KubernetesCluster(
            name=test_cluster_name,
            network=network,
            zone=zone,
            version=version,
            labels=[],
            network_cidr=network_cidr,
            node_groups=[node_group],
        )

        response = post_cluster.sync_detailed(
            client=client,
            body=cluster_payload,
        )

        if response.status_code == 200 and response.parsed is not None:
            created_cluster = response.parsed
            created_cluster_uuid = getattr(created_cluster, "uuid", None)
            print(f"     Cluster '{test_cluster_name}' created successfully")
        else:
            print(f"     Failed with status: {response.status_code}")
            sys.exit(1)
    except Exception as e:
        print(f"     Error: {e}")
        sys.exit(1)
```

### Step 4: List Clusters Again (After)

After creating the cluster, we list all clusters again to verify the new cluster appears in the list. We compare the count with the baseline from step 2.

```py filename=test_kubernetes_test.py

    print("\n4. Listing Kubernetes clusters (AFTER)...")
    try:
        response = get_clusters.sync_detailed(client=client)

        if response.status_code == 200 and response.parsed is not None:
            clusters_after = response.parsed or []

            print(f"     Found {len(clusters_after)} cluster(s)")
            for cluster in clusters_after:
                cluster_name = getattr(cluster, "name", "unknown")
                cluster_zone = getattr(cluster, "zone", "unknown")
                is_new = " [NEW]" if cluster_name == test_cluster_name else ""
                print(f"     - {cluster_name} (zone: {cluster_zone}){is_new}")

            if len(clusters_after) == len(clusters_before) + 1:
                print("\n     Verification passed: Cluster count increased by 1")
            else:
                print(
                    f"\n     Warning: Expected {len(clusters_before) + 1} clusters, found {len(clusters_after)}"
                )
        else:
            print(f"     Failed with status: {response.status_code}")
            sys.exit(1)
    except Exception as e:
        print(f"     Error: {e}")
        sys.exit(1)
```

### Step 5: Cleanup - Delete the Test Cluster

Finally, we clean up by deleting the test cluster we created. We wait a few seconds for the cluster to start provisioning before attempting deletion.

```py filename=test_kubernetes_test.py

    print("\n5. Cleaning up - deleting test cluster...")
    try:
        print("   Waiting 10 seconds for cluster to start provisioning...")
        time.sleep(10)

        if not created_cluster_uuid:
            print("     No cluster UUID found from create response; skipping delete")
        else:
            response = delete_cluster.sync_detailed(
                client=client,
                uuid=UUID(str(created_cluster_uuid)),
            )

            if response.status_code in (200, 202, 204):
                print(f"     Cluster '{test_cluster_name}' delete requested successfully")
            elif response.status_code == 404:
                print("     Cluster not found for deletion (may have been auto-deleted)")
            else:
                print(f"     Failed to delete (status: {response.status_code})")
                print(f"     Note: Manual cleanup may be required for cluster '{test_cluster_name}'")
    except Exception as e:
        print(f"     Error during cleanup: {e}")
        print(f"     Note: Manual cleanup may be required for cluster '{test_cluster_name}'")
        sys.exit(1)

    print("\n" + "=" * 50)
    print("  Kubernetes API validation completed")
    print("=" * 50)
```

### Entry Point

The script's entry point calls the `main()` function when executed directly.

```py filename=test_kubernetes_test.py


if __name__ == "__main__":
    main()
```

## Running the Test

Now that we have the Python script, let's build the shell script that will set up the environment and run the test.

### Shell Script Header

The script uses strict mode (`set -euo pipefail`) to exit on any error, undefined variable, or pipeline failure.

```sh filename=test.sh
#!/usr/bin/env bash
set -euo pipefail

# Test Kubernetes API
# Tests: list_clusters, create_cluster, list_clusters again, delete_cluster
```

### Configuration Variables

We define the package name (as published on TestPyPI), the virtual environment directory, and the Python binary to use.

```sh filename=test.sh

# TestPyPI project name is "upcloud-api" (installs the "upcloud_api" module)
PKG_NAME="upcloud-api"
VENV_DIR=".venv-test-kubernetes"
PYTHON_BIN="${PYTHON_BIN:-python3}"
```

### Test Header Output

Display a header to indicate the start of the Kubernetes API test.

```sh filename=test.sh

echo "======================================"
echo "Testing Kubernetes API"
echo "======================================"
```

### Environment Variable Check

The test requires the `UPCLOUD_TOKEN` and `UKS_NETWORK` environment variables to be set.

```sh filename=test.sh

# Check for required environment variables
if [[ -z "${UPCLOUD_TOKEN:-}" ]]; then
    echo "ERROR: UPCLOUD_TOKEN environment variable is required"
    exit 1
fi
if [[ -z "${UKS_NETWORK:-}" ]]; then
    echo "ERROR: UKS_NETWORK environment variable is required"
    exit 1
fi
```

### Create Virtual Environment

We create a fresh virtual environment to ensure a clean test environment without any cached packages.

```sh filename=test.sh

echo "== Create clean virtualenv =="
rm -rf "${VENV_DIR}"
"${PYTHON_BIN}" -m venv "${VENV_DIR}"
# shellcheck disable=SC1091
source "${VENV_DIR}/bin/activate"

python -m pip install --upgrade pip > /dev/null
```

### Install SDK from TestPyPI

We install the `upcloud-api` package from TestPyPI, along with the `httpx` dependency from the main PyPI repository.

```sh filename=test.sh

echo "== Install ${PKG_NAME} + test deps from TestPyPI =="
pip install \
    --no-cache-dir \
    --index-url https://test.pypi.org/simple/ \
    --extra-index-url https://pypi.org/simple \
    "${PKG_NAME}" \
    httpx > /dev/null
```

### Run the Python Test

Now we execute the Python test script we created earlier.

```sh filename=test.sh

echo ""
echo "== Test Kubernetes API =="
python test_kubernetes_test.py
```

### Cleanup

After the test completes, we deactivate and remove the virtual environment.

```sh filename=test.sh

echo ""
echo "== Cleanup =="
deactivate
rm -rf "${VENV_DIR}"
echo "✓ Done"
```

## Execute the Test

Finally, we run the shell script to execute the complete test.

```sh
bash test.sh
```
