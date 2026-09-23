#!/usr/bin/env python3
"""
Test script for Kubernetes API.

Tests:
- Authenticate client
- Create a network for the cluster
- List existing clusters
- Create a new cluster
- List clusters again to verify creation
- Delete the test cluster
- Delete the test network
"""

import os
import sys
import time
import traceback
from uuid import UUID

from upcloud_api.api.kubernetes import (
    create_kubernetes_cluster,
    delete_kubernetes_cluster,
    list_kubernetes_clusters,
)
from upcloud_api.api.network import create_network, delete_network
from upcloud_api.models import (
    CreateNetworkRequest,
    CreateNetworkRequestNetwork,
    CreateNetworkRequestNetworkIpNetworks,
    CreateNetworkRequestNetworkIpNetworksIpNetworkItem,
    KubernetesCluster,
    NetworkBooleanYesno,
    NetworkIpFamily,
    NetworkType,
)
from upcloud_api.models.kubernetes_node_group import KubernetesNodeGroup
from upcloud_api.types import UNSET

from upcloud_api import AuthenticatedClient


def main():
    """Run the Kubernetes API test."""
    token = os.environ.get("UPCLOUD_TOKEN")
    zone = os.environ.get("UKS_ZONE", "fi-hel1")
    network_cidr = os.environ.get("UKS_NETWORK_CIDR", "10.0.0.0/24")
    version = os.environ.get("UKS_VERSION", "1.34")
    node_group_plan = os.environ.get("UKS_NODE_GROUP_PLAN", "DEV-1xCPU-2GB")
    node_group_count = int(os.environ.get("UKS_NODE_GROUP_COUNT", "1"))
    ssh_keys_raw = os.environ.get("UKS_SSH_KEYS", "").strip()

    if not token:
        print("ERROR: UPCLOUD_TOKEN environment variable is required")
        sys.exit(1)

    ssh_keys = (
        [key.strip() for key in ssh_keys_raw.split(",") if key.strip()] if ssh_keys_raw else None
    )

    print("1. Authenticating client...")
    try:
        client = AuthenticatedClient(token=token)
        print("   Client authenticated successfully")
    except Exception as e:
        print(f"   Error: {e}")
        sys.exit(1)

    print("\n2. Creating a network for the cluster...")
    print("   Testing SDK function: create_network.sync_detailed()")
    test_network_name = f"test-k8s-net-{int(time.time())}"
    created_network_uuid = None

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

    print("\n3. Listing existing Kubernetes clusters (BEFORE)...")
    print("   Testing SDK function: list_kubernetes_clusters.sync_detailed()")
    try:
        response = list_kubernetes_clusters.sync_detailed(client=client)

        if response.status_code == 200 and response.parsed is not None:
            clusters_before = response.parsed or []

            print(f"   Found {len(clusters_before)} cluster(s)")
            for cluster in clusters_before:
                cluster_name = getattr(cluster, "name", "unknown")
                cluster_zone = getattr(cluster, "zone", "unknown")
                print(f"     - {cluster_name} (zone: {cluster_zone})")
        else:
            print(f"   Failed with status: {response.status_code}")
            print(f"   Parsed: {response.parsed}")
            sys.exit(1)
    except Exception as e:
        print(f"\n   SDK ERROR: {type(e).__name__}: {e}")
        traceback.print_exc()
        sys.exit(1)

    print("\n4. Creating a new Kubernetes cluster...")
    print("   Testing SDK function: create_kubernetes_cluster.sync_detailed()")
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
            network=str(created_network_uuid),
            zone=zone,
            version=version,
            labels=[],
            network_cidr=network_cidr,
            node_groups=[node_group],
        )

        response = create_kubernetes_cluster.sync_detailed(
            client=client,
            body=cluster_payload,
        )

        if response.status_code == 200 and response.parsed is not None:
            created_cluster = response.parsed
            created_cluster_uuid = getattr(created_cluster, "uuid", None)
            print(f"     Cluster '{test_cluster_name}' created successfully")
        else:
            print(f"     Failed with status: {response.status_code}")
            print(f"     Parsed: {response.parsed}")
            sys.exit(1)
    except Exception as e:
        print(f"     Error: {e}")
        traceback.print_exc()
        sys.exit(1)

    print("\n5. Listing Kubernetes clusters (AFTER)...")
    try:
        response = list_kubernetes_clusters.sync_detailed(client=client)

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
            print(f"     Parsed: {response.parsed}")
            sys.exit(1)
    except Exception as e:
        print(f"     Error: {e}")
        traceback.print_exc()
        sys.exit(1)

    print("\n6. Cleaning up - deleting test cluster...")
    print("   Testing SDK function: delete_kubernetes_cluster.sync_detailed()")
    try:
        print("   Waiting 10 seconds for cluster to start provisioning...")
        time.sleep(10)

        if not created_cluster_uuid:
            print("     No cluster UUID found from create response; skipping delete")
        else:
            response = delete_kubernetes_cluster.sync_detailed(
                client=client,
                uuid=UUID(str(created_cluster_uuid)),
            )

            if response.status_code in (200, 202, 204):
                print(f"     Cluster '{test_cluster_name}' delete requested successfully")
            elif response.status_code == 404:
                print("     Cluster not found for deletion (may have been auto-deleted)")
            else:
                print(f"     Failed to delete (status: {response.status_code})")
                print(
                    f"     Note: Manual cleanup may be required for cluster '{test_cluster_name}'"
                )
    except Exception as e:
        print(f"     Error during cleanup: {e}")
        traceback.print_exc()
        print(f"     Note: Manual cleanup may be required for cluster '{test_cluster_name}'")

    print("\n7. Cleaning up - deleting test network...")
    print("   Testing SDK function: delete_network.sync_detailed()")
    print("   Waiting 30 seconds for the cluster's node group to detach from the network...")
    time.sleep(30)
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

    print("\n" + "=" * 50)
    print("  Kubernetes API validation completed")
    print("=" * 50)


if __name__ == "__main__":
    main()
