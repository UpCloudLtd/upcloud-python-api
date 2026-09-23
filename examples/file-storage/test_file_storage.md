# Testing the File Storage API

This example demonstrates how to use the UpCloud Python SDK to interact with the File Storage API. We'll create a test script that:

- Authenticates a client using a bearer token
- Lists existing File Storage services
- Creates a new File Storage service
- Verifies the service was created
- Cleans up by deleting the test service

## The Python Test Script

Let's build the test script step by step.

### Imports and Module Docstring

First, we define the script's purpose and import the necessary modules. We need the UpCloud SDK client, the file storage API functions, and the models for creating services.

```py filename=test_file_storage_test.py
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
from uuid import UUID

from upcloud_api.api.file_storage import (
    list_services,
    create_service,
    delete_service,
)
from upcloud_api.models import FileStorageServiceCreate
from upcloud_api.models.file_storage_configured_status import FileStorageConfiguredStatus

from upcloud_api import AuthenticatedClient

```

### Main Function Setup

The `main()` function starts by reading configuration from environment variables. The `UPCLOUD_TOKEN` is required for authentication, while the zone and size have sensible defaults.

```py filename=test_file_storage_test.py

def main():
    """Run the File Storage API test."""
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
```

### Step 2: List Existing Services (Before)

Before creating a new service, we list all existing File Storage services. This establishes a baseline count that we'll use later to verify our new service was created.

```py filename=test_file_storage_test.py

    print("\n2. Listing existing File Storage services (BEFORE)...")
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
        print(f"   Error: {e}")
        sys.exit(1)
```

### Step 3: Create a New File Storage Service

Now we create a new File Storage service using the `FileStorageServiceCreate` model. We generate a unique name using a timestamp to avoid conflicts.

```py filename=test_file_storage_test.py

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
            sys.exit(1)
    except Exception as e:
        print(f"     Error: {e}")
        sys.exit(1)
```

### Step 4: List Services Again (After)

After creating the service, we list all services again to verify the new service appears in the list. We compare the count with the baseline from step 2.

```py filename=test_file_storage_test.py

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
        sys.exit(1)
```

### Step 5: Cleanup - Delete the Test Service

Finally, we clean up by deleting the test service we created. We wait a few seconds for the service to fully provision before attempting deletion.

```py filename=test_file_storage_test.py

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
        print(f"     Note: Manual cleanup may be required for service '{test_service_name}'")
        sys.exit(1)

    print("\n" + "=" * 50)
    print("  File Storage API validation completed")
    print("=" * 50)
```

### Entry Point

The script's entry point calls the `main()` function when executed directly.

```py filename=test_file_storage_test.py


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

# Test File Storage API
# Tests: list_services, create_service, list_services again, delete_service
```

### Configuration Variables

mdtest runs the shell script in a temporary directory. Point it at the checked-out SDK with `UPCLOUD_SDK_PATH`.

```sh filename=test.sh

SDK_DIR="${UPCLOUD_SDK_PATH:?Set UPCLOUD_SDK_PATH to the local sdk directory}"
```

### Test Header Output

Display a header to indicate the start of the File Storage API test.

```sh filename=test.sh

echo "======================================"
echo "Testing File Storage API"
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
echo "== Test File Storage API with local SDK =="
uv run --no-project --with "$SDK_DIR" python test_file_storage_test.py
```

## Execute the Test

Finally, we run the shell script to execute the complete test.

```sh
bash test.sh
```
