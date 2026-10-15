# Testing the Network and Router APIs

This example demonstrates how to use the UpCloud Python SDK to create a private network with labels, attach it to a router, and clean everything up again. We'll create a test script that:

- Authenticates a client using a bearer token
- Creates a router
- Creates a private network with labels, attached to the router
- Verifies the network's labels
- Verifies the network is attached to the router
- Cleans up by deleting the test network and the test router

## Prerequisites

This test creates and destroys its own router and network, so only `UPCLOUD_TOKEN` is required.

## The Python Test Script

Let's build the test script step by step.

### Imports and Module Docstring

First, we define the script's purpose and import the necessary modules. We need the UpCloud SDK client, the network and router API functions, and the models for creating networks, labels, and routers.

```py filename=test_network_test.py
#!/usr/bin/env python3
"""
Test script for Network and Router APIs.

Tests:
- Authenticate client
- Create a router
- Create a private network with labels, attached to the router
- Get the network and verify its labels
- Get the router and verify the network is attached
- Delete the test network
- Delete the test router
"""

import os
import sys
import time
import traceback
from uuid import UUID

from upcloud_api import AuthenticatedClient
from upcloud_api.api.network import create_network, delete_network, get_network_details
from upcloud_api.api.router import create_router, delete_router, get_router
from upcloud_api.models import (
    CreateNetworkRequest,
    CreateNetworkRequestNetwork,
    CreateNetworkRequestNetworkIpNetworks,
    CreateNetworkRequestNetworkIpNetworksIpNetworkItem,
    NetworkBooleanYesno,
    NetworkIpFamily,
    NetworkLabel,
    NetworkType,
    RouterCreate,
    RouterCreateRouter,
)
```

### Main Function Setup

The `main()` function starts by reading configuration from environment variables. The `UPCLOUD_TOKEN` is required for authentication, while the zone and network CIDR have sensible defaults.

```py filename=test_network_test.py

def main():
    """Run the Network and Router API test."""
    token = os.environ.get("UPCLOUD_TOKEN")
    zone = os.environ.get("NETWORK_ZONE", "fi-hel1")
    network_cidr = os.environ.get("NETWORK_CIDR", "10.0.0.0/24")

    if not token:
        print("ERROR: UPCLOUD_TOKEN environment variable is required")
        sys.exit(1)

    print("1. Authenticating client...")
    try:
        client = AuthenticatedClient(token=token)
        print("   Client authenticated successfully")
    except Exception as e:
        print(f"   Error: {e}")
        sys.exit(1)
```

### Step 2: Create a Router

The network will be attached to a router, so we create the router first. We keep its UUID for the network payload, for verification, and for cleanup.

```py filename=test_network_test.py

    print("\n2. Creating a router...")
    print("   Testing SDK function: create_router.sync_detailed()")
    test_router_name = f"test-router-{int(time.time())}"
    created_router_uuid = None

    try:
        router_payload = RouterCreate(router=RouterCreateRouter(name=test_router_name))

        response = create_router.sync_detailed(client=client, body=router_payload)

        if response.status_code == 201 and response.parsed is not None:
            created_router_uuid = response.parsed.router.uuid
            print(f"     Router '{test_router_name}' created successfully ({created_router_uuid})")
        else:
            print(f"     Failed with status: {response.status_code}")
            print(f"     Parsed: {response.parsed}")
            sys.exit(1)
    except Exception as e:
        print(f"     Error: {e}")
        traceback.print_exc()
        sys.exit(1)
```

### Step 3: Create a Private Network with Labels

Now we create a private network with one IPv4 subnet and DHCP enabled. We add labels through the `labels` field of the network and attach the network to the router through the `router` field. We generate a unique name using a timestamp to avoid conflicts.

```py filename=test_network_test.py

    print("\n3. Creating a private network with labels, attached to the router...")
    print("   Testing SDK function: create_network.sync_detailed()")
    test_network_name = f"test-net-{int(time.time())}"
    created_network_uuid = None
    network_labels = [
        NetworkLabel(key="env", value="test"),
        NetworkLabel(key="purpose", value="sdk-example"),
    ]

    try:
        network_payload = CreateNetworkRequest(
            network=CreateNetworkRequestNetwork(
                type_=NetworkType.PRIVATE,
                name=test_network_name,
                zone=zone,
                ip_networks=CreateNetworkRequestNetworkIpNetworks(
                    ip_network=[
                        CreateNetworkRequestNetworkIpNetworksIpNetworkItem(
                            family=NetworkIpFamily.IPV4,
                            address=network_cidr,
                            dhcp=NetworkBooleanYesno.YES,
                        )
                    ]
                ),
                router=created_router_uuid,
                labels=network_labels,
            )
        )

        response = create_network.sync_detailed(client=client, body=network_payload)

        if response.status_code == 201 and response.parsed is not None:
            created_network_uuid = response.parsed.network.uuid
            print(
                f"     Network '{test_network_name}' created successfully ({created_network_uuid})"
            )
        else:
            print(f"     Failed with status: {response.status_code}")
            print(f"     Parsed: {response.parsed}")
            sys.exit(1)
    except Exception as e:
        print(f"     Error: {e}")
        traceback.print_exc()
        sys.exit(1)
```

### Step 4: Get the Network and Verify Its Labels

We fetch the network by UUID and check that it is in the expected zone, is attached to our router, and carries the labels we sent. The network details response returns `labels` as a list of `key`/`value` pairs, which the SDK exposes as `network.labels`. If the API does not return them, the script reports that instead of failing.

```py filename=test_network_test.py

    print("\n4. Getting network details and verifying labels...")
    print("   Testing SDK function: get_network_details.sync_detailed()")

    try:
        response = get_network_details.sync_detailed(
            client=client,
            uuid=UUID(str(created_network_uuid)),
        )

        if response.status_code == 200 and response.parsed is not None:
            network = response.parsed.network
            print(f"     Network '{network.name}' found in zone '{network.zone}'")

            if str(network.router) == str(created_router_uuid):
                print("     Network is attached to the test router")
            else:
                print(
                    f"     Warning: Network router is {network.router}, expected {created_router_uuid}"
                )

            returned_labels = network.labels or []
            if returned_labels:
                for label in returned_labels:
                    print(f"     - {label.key}={label.value}")
                returned_pairs = {(label.key, label.value) for label in returned_labels}
                expected_pairs = {(label.key, label.value) for label in network_labels}
                if returned_pairs == expected_pairs:
                    print("     Verification passed: all labels are present")
                else:
                    print(
                        f"     Warning: Expected labels {expected_pairs}, found {returned_pairs}"
                    )
            else:
                print("     Note: Labels were not returned in the network details response")
        else:
            print(f"     Failed with status: {response.status_code}")
            print(f"     Parsed: {response.parsed}")
            sys.exit(1)
    except Exception as e:
        print(f"     Error: {e}")
        traceback.print_exc()
        sys.exit(1)
```

### Step 5: Get the Router and Verify the Attachment

Next, we fetch the router and check that the network appears in its list of attached networks.

```py filename=test_network_test.py

    print("\n5. Getting router details and verifying network attachment...")
    print("   Testing SDK function: get_router.sync_detailed()")

    try:
        response = get_router.sync_detailed(
            router=UUID(str(created_router_uuid)),
            client=client,
        )

        if response.status_code == 200 and response.parsed is not None:
            router_details = response.parsed.router
            attached_uuids = [
                str(attached.uuid) for attached in router_details.attached_networks.network
            ]
            print(
                f"     Router '{router_details.name}' has {len(attached_uuids)} attached network(s)"
            )

            if str(created_network_uuid) in attached_uuids:
                print("     Verification passed: test network is attached to the router")
            else:
                print("     Warning: test network is not listed as attached to the router")
        else:
            print(f"     Failed with status: {response.status_code}")
            print(f"     Parsed: {response.parsed}")
            sys.exit(1)
    except Exception as e:
        print(f"     Error: {e}")
        traceback.print_exc()
        sys.exit(1)
```

### Step 6: Cleanup - Delete the Network and the Router

Finally, we clean up. A router with attached networks cannot be deleted, so we delete the network first and then the router.

```py filename=test_network_test.py

    print("\n6. Cleaning up - deleting test network...")
    print("   Testing SDK function: delete_network.sync_detailed()")
    try:
        if not created_network_uuid:
            print("     No network UUID found from create response; skipping delete")
        else:
            response = delete_network.sync_detailed(
                client=client,
                uuid=UUID(str(created_network_uuid)),
            )

            if response.status_code == 204:
                print(f"     Network '{test_network_name}' deleted successfully")
            elif response.status_code == 404:
                print("     Network not found for deletion (may have been auto-deleted)")
            else:
                print(f"     Failed to delete (status: {response.status_code})")
                print(
                    f"     Note: Manual cleanup may be required for network '{test_network_name}'"
                )
    except Exception as e:
        print(f"     Error during cleanup: {e}")
        traceback.print_exc()
        print(f"     Note: Manual cleanup may be required for network '{test_network_name}'")
        sys.exit(1)

    print("\n6. Cleaning up - deleting test router...")
    print("   Testing SDK function: delete_router.sync_detailed()")
    try:
        if not created_router_uuid:
            print("     No router UUID found from create response; skipping delete")
        else:
            response = delete_router.sync_detailed(
                router=UUID(str(created_router_uuid)),
                client=client,
            )

            if response.status_code == 204:
                print(f"     Router '{test_router_name}' deleted successfully")
            elif response.status_code == 404:
                print("     Router not found for deletion (may have been auto-deleted)")
            else:
                print(f"     Failed to delete (status: {response.status_code})")
                print(f"     Note: Manual cleanup may be required for router '{test_router_name}'")
    except Exception as e:
        print(f"     Error during cleanup: {e}")
        traceback.print_exc()
        print(f"     Note: Manual cleanup may be required for router '{test_router_name}'")
        sys.exit(1)

    print("\n" + "=" * 50)
    print("  Network and Router API validation completed")
    print("=" * 50)
```

### Entry Point

The script's entry point calls the `main()` function when executed directly.

```py filename=test_network_test.py


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

# Test Network and Router APIs
# Tests: create_router, create_network (with labels), get_network_details,
# get_router, delete_network, delete_router
```

### Configuration Variables

mdtest runs the shell script in a temporary directory. Point it at the repository root with `UPCLOUD_SDK_PATH`.

```sh filename=test.sh

SDK_DIR="${UPCLOUD_SDK_PATH:?Set UPCLOUD_SDK_PATH to the repository root}"
```

### Test Header Output

Display a header to indicate the start of the Network and Router API test.

```sh filename=test.sh

echo "======================================"
echo "Testing Network and Router APIs"
echo "======================================"
```

### Environment Variable Check

The test requires the `UPCLOUD_TOKEN` environment variable to be set with a valid UpCloud API bearer token.

```sh filename=test.sh

# Check for required environment variables
if [[ -z "${UPCLOUD_TOKEN:-}" ]]; then
    echo "ERROR: UPCLOUD_TOKEN environment variable is required"
    exit 1
fi
```

### Run the Python Test

Run the test against the checked-out SDK in a uv-managed, isolated environment.

```sh filename=test.sh

echo ""
echo "== Test Network and Router APIs with local SDK =="
uv run --no-cache --no-project --with "$SDK_DIR" python test_network_test.py
```

## Execute the Test

Finally, we run the shell script to execute the complete test.

```sh
bash test.sh
```
