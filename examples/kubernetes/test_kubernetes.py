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
import traceback
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

    print("\n2. Listing existing Kubernetes clusters (BEFORE)...")
    print("   Testing SDK function: get_clusters.sync_detailed()")
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
            print(f"   Parsed: {response.parsed}")
            sys.exit(1)
    except Exception as e:
        print(f"\n   SDK ERROR: {type(e).__name__}: {e}")
        traceback.print_exc()
        sys.exit(1)

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
            print(f"     Parsed: {response.parsed}")
            sys.exit(1)
    except Exception as e:
        print(f"     Error: {e}")
        traceback.print_exc()
        sys.exit(1)

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
            print(f"     Parsed: {response.parsed}")
            sys.exit(1)
    except Exception as e:
        print(f"     Error: {e}")
        traceback.print_exc()
        sys.exit(1)

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
        traceback.print_exc()
        print(f"     Note: Manual cleanup may be required for cluster '{test_cluster_name}'")
        sys.exit(1)

    print("\n" + "=" * 50)
    print("  Kubernetes API validation completed")
    print("=" * 50)


if __name__ == "__main__":
    main()
