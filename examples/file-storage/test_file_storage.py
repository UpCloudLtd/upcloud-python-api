#!/usr/bin/env python3
"""Test script for File Storage API.

Tests:
- Authenticate client
- List existing services
- Create a new service
- List services again to verify creation
- Delete the test service
"""

import os
import sys
import time
import traceback
from uuid import UUID

from upcloud_api import AuthenticatedClient
from upcloud_api.api.file_storage import (
    list_services,
    create_service,
    delete_service,
)
from upcloud_api.models import FileStorageServiceCreate
from upcloud_api.models.file_storage_configured_status import FileStorageConfiguredStatus


def main():
    token = os.environ.get("UPCLOUD_TOKEN")
    zone = os.environ.get("FILE_STORAGE_ZONE", "fi-hel2")
    size_gib = int(os.environ.get("FILE_STORAGE_SIZE_GIB", "250"))

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

    print("\n2. Listing existing File Storage services (BEFORE)...")
    print("   Testing SDK function: list_services.sync_detailed()")
    try:
        response = list_services.sync_detailed(client=client)

        if response.status_code == 200 and response.parsed is not None:
            services_before = response.parsed or []

            print(f"   Found {len(services_before)} service(s)")
            for service in services_before:
                service_name = getattr(service, "name", "unknown")
                service_zone = getattr(service, "zone", "unknown")
                service_size = getattr(service, "size_gib", "unknown")
                print(f"     - {service_name} (zone: {service_zone}, size_gib: {service_size})")
        else:
            print(f"   Failed with status: {response.status_code}")
            sys.exit(1)
    except Exception as e:
        print(f"\n   SDK ERROR: {type(e).__name__}: {e}")
        traceback.print_exc()
        sys.exit(1)

    print("\n3. Creating a new File Storage service...")
    test_service_name = f"test-fs-{int(time.time())}"
    created_service_uuid = None

    try:
        service_payload = FileStorageServiceCreate(
            name=test_service_name,
            zone=zone,
            configured_status=FileStorageConfiguredStatus.STARTED,
            size_gib=size_gib,
        )

        response = create_service.sync_detailed(
            client=client,
            body=service_payload,
        )

        if response.status_code in (200, 201, 202) and response.parsed:
            print(f"     Service '{test_service_name}' created successfully")
            print(f"     Name: {getattr(response.parsed, 'name', 'N/A')}")
            print(f"     Zone: {getattr(response.parsed, 'zone', 'N/A')}")
            print(f"     Size GiB: {getattr(response.parsed, 'size_gib', 'N/A')}")
            created_service_uuid = getattr(response.parsed, "uuid", None)
            if not created_service_uuid:
                created_service_uuid = response.parsed.additional_properties.get("uuid")
        else:
            print(f"     Failed with status: {response.status_code}")
            try:
                body_text = response.content.decode("utf-8", errors="replace")
            except Exception:
                body_text = str(response.content)
            print(f"     Response body: {body_text}")
            print(f"     Parsed: {response.parsed}")
            sys.exit(1)
    except Exception as e:
        print(f"     Error: {e}")
        traceback.print_exc()
        sys.exit(1)

    print("\n4. Listing File Storage services (AFTER)...")
    try:
        response = list_services.sync_detailed(client=client)

        if response.status_code == 200 and response.parsed is not None:
            services_after = response.parsed or []

            print(f"     Found {len(services_after)} service(s)")
            for service in services_after:
                service_name = getattr(service, "name", "unknown")
                service_zone = getattr(service, "zone", "unknown")
                is_new = " [NEW]" if service_name == test_service_name else ""
                print(f"     - {service_name} (zone: {service_zone}){is_new}")

            if len(services_after) == len(services_before) + 1:
                print("\n     Verification passed: Service count increased by 1")
            else:
                print(
                    f"\n     Warning: Expected {len(services_before) + 1} services, found {len(services_after)}"
                )
        else:
            print(f"     Failed with status: {response.status_code}")
            sys.exit(1)
    except Exception as e:
        print(f"     Error: {e}")
        traceback.print_exc()
        sys.exit(1)

    print("\n5. Cleaning up - deleting test service...")
    try:
        print("   Waiting 5 seconds for service to fully provision...")
        time.sleep(5)

        if not created_service_uuid:
            print("     No service UUID found from create response; skipping delete")
        else:
            response = delete_service.sync_detailed(
                client=client,
                service_uuid=UUID(str(created_service_uuid)),
            )

            if response.status_code in (200, 204):
                print(f"     Service '{test_service_name}' deleted successfully")
            elif response.status_code == 404:
                print("     Service not found for deletion (may have been auto-deleted)")
            else:
                print(f"     Failed to delete (status: {response.status_code})")
                print(f"     Note: Manual cleanup may be required for service '{test_service_name}'")
    except Exception as e:
        print(f"     Error during cleanup: {e}")
        traceback.print_exc()
        print(f"     Note: Manual cleanup may be required for service '{test_service_name}'")
        sys.exit(1)

    print("\n" + "=" * 50)
    print("  File Storage API validation completed")
    print("=" * 50)


if __name__ == "__main__":
    main()
