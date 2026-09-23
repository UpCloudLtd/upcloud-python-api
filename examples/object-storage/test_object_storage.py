#!/usr/bin/env python3
"""Test script for Object Storage 2.0 API (Managed Object Storage).

This test validates the SDK against the UpCloud API. When the SDK has bugs,
this test will fail with detailed diagnostic information for maintainers.

Tests:
- Authenticate client
- List existing services
- Create a new service
- List services again to verify creation
- Delete the test service
"""

import sys
import os
import time
import traceback
from upcloud_api import AuthenticatedClient
from upcloud_api.api.object_storage_2 import (
    list_services,
    create_service,
    delete_service,
)
from upcloud_api.models import ServiceCreate
from upcloud_api.models.property_configured_status import PropertyConfiguredStatus


def main():
    token = os.environ.get("UPCLOUD_TOKEN")
    
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
    
    print("\n2. Listing existing Managed Object Storage services (BEFORE)...")
    print("   Testing SDK function: list_services.sync_detailed()")
    try:
        print(f"\n   Attempting SDK call...")
        response = list_services.sync_detailed(client=client)
        
        if response.status_code == 200 and response.parsed is not None:
            services_before = response.parsed or []
            
            print(f"   Found {len(services_before)} service(s)")
            for service in services_before:
                service_name = getattr(service, 'name', 'unknown')
                service_region = getattr(service, 'region', 'unknown')
                print(f"     - {service_name} (region: {service_region})")
        else:
            print(f"   Failed with status: {response.status_code}")
            sys.exit(1)
    except Exception as e:
        print(f"\n   SDK ERROR: {type(e).__name__}: {e}")
        traceback.print_exc()
        sys.exit(1)
    
    print("\n3. Creating a new Managed Object Storage service...")
    test_service_name = f"test-sdk-{int(time.time())}"
    created_service_uuid = None
    
    try:
        # Create service using SDK models
        service_payload = ServiceCreate(
            name=test_service_name,
            region="europe-1",
            configured_status=PropertyConfiguredStatus.STARTED
        )
        
        response = create_service.sync_detailed(
            client=client,
            body=service_payload
        )
        
        if response.status_code in (200, 201, 202) and response.parsed:
            print(f"     Service '{test_service_name}' created successfully")
            print(f"     Name: {getattr(response.parsed, 'name', 'N/A')}")
            print(f"     Region: {getattr(response.parsed, 'region', 'N/A')}")
            print(f"     State: {getattr(response.parsed, 'operational_state', 'N/A')}")
            created_service_uuid = getattr(response.parsed, "uuid", None)
            if not created_service_uuid:
                created_service_uuid = response.parsed.additional_properties.get("uuid")
        else:
            print(f"     Failed with status: {response.status_code}")
            sys.exit(1)
    except Exception as e:
        print(f"     Error: {e}")
        traceback.print_exc()
        sys.exit(1)
    
    print("\n4. Listing Managed Object Storage services (AFTER)...")
    try:
        response = list_services.sync_detailed(client=client)
        
        if response.status_code == 200 and response.parsed is not None:
            services_after = response.parsed or []
            
            print(f"     Found {len(services_after)} service(s)")
            for service in services_after:
                service_name = getattr(service, 'name', 'unknown')
                service_region = getattr(service, 'region', 'unknown')
                is_new = " [NEW]" if service_name == test_service_name else ""
                print(f"     - {service_name} (region: {service_region}){is_new}")
            
            # Verify the new service appears
            if len(services_after) == len(services_before) + 1:
                print(f"\n     Verification passed: Service count increased by 1")
            else:
                print(f"\n     Warning: Expected {len(services_before) + 1} services, found {len(services_after)}")
        else:
            print(f"     Failed with status: {response.status_code}")
            sys.exit(1)
    except Exception as e:
        print(f"   ✗ Error: {e}")
        traceback.print_exc()
        sys.exit(1)
    
    print("\n5. Cleaning up - deleting test service...")
    try:
        # Wait a bit for the service to fully provision
        print(f"   Waiting 5 seconds for service to fully provision...")
        time.sleep(5)
        
        if not created_service_uuid:
            print("     No service UUID found from create response; skipping delete")
        else:
            response = delete_service.sync_detailed(
                client=client,
                service_uuid=created_service_uuid
            )
        
            if response.status_code in (200, 204):
                print(f"     Service '{test_service_name}' deleted successfully")
            elif response.status_code == 404:
                print(f"     Service not found for deletion (may have been auto-deleted)")
            else:
                print(f"     Failed to delete (status: {response.status_code})")
                print(f"     Note: Manual cleanup may be required for service '{test_service_name}'")
    except Exception as e:
        print(f"     Error during cleanup: {e}")
        traceback.print_exc()
        print(f"     Note: Manual cleanup may be required for service '{test_service_name}'")
        sys.exit(1)
    
    print("\n" + "="*50)
    print("  Object Storage 2.0 API validation completed")
    print("="*50)


if __name__ == "__main__":
    main()
