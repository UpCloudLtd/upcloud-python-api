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


if __name__ == "__main__":
    main()
