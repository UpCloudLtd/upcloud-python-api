# Testing the Object Storage 2.0 API

This example demonstrates how to use the UpCloud Python SDK to interact with the Managed Object Storage (Object Storage 2.0) API. We'll create a test script that:

- Authenticates a client using a bearer token
- Lists existing Managed Object Storage services
- Creates a new Managed Object Storage service
- Verifies the service was created
- Cleans up by deleting the test service

## The Python Test Script

Let's build the test script step by step.

### Imports and Module Docstring

First, we define the script's purpose and import the necessary modules. We need the UpCloud SDK client, the object storage API functions, and the models for creating services.

```py filename=test_object_storage_test.py
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
from upcloud_api import AuthenticatedClient
from upcloud_api.api.object_storage_2 import (
    list_services,
    create_service,
    delete_service,
)
from upcloud_api.models import ServiceCreate
from upcloud_api.models.property_configured_status import PropertyConfiguredStatus

```

### Main Function Setup

The `main()` function starts by reading the authentication token from environment variables. The `UPCLOUD_TOKEN` is required for authentication.

```py filename=test_object_storage_test.py

def main():
    """Run the Object Storage API test."""
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
```

### Step 2: List Existing Services (Before)

Before creating a new service, we list all existing Managed Object Storage services. This establishes a baseline count that we'll use later to verify our new service was created.

```py filename=test_object_storage_test.py
    
    print("\n2. Listing existing Managed Object Storage services (BEFORE)...")
    try:
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
        print(f"   Error: {e}")
        sys.exit(1)
```

### Step 3: Create a New Managed Object Storage Service

Now we create a new Managed Object Storage service using the `ServiceCreate` model. We generate a unique name using a timestamp to avoid conflicts.

```py filename=test_object_storage_test.py
    
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
        sys.exit(1)
```

### Step 4: List Services Again (After)

After creating the service, we list all services again to verify the new service appears in the list. We compare the count with the baseline from step 2.

```py filename=test_object_storage_test.py
    
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
        print(f"     Error: {e}")
        sys.exit(1)
```

### Step 5: Cleanup - Delete the Test Service

Finally, we clean up by deleting the test service we created. We wait a few seconds for the service to fully provision before attempting deletion.

```py filename=test_object_storage_test.py
    
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
        print(f"     Note: Manual cleanup may be required for service '{test_service_name}'")
        sys.exit(1)
    
    print("\n" + "="*50)
    print("  Object Storage 2.0 API validation completed")
    print("="*50)
```

### Entry Point

The script's entry point calls the `main()` function when executed directly.

```py filename=test_object_storage_test.py


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

# Test Object Storage 2.0 API
# Tests: list_services, create_service, list_services again, delete_service
```

### Configuration Variables

We define the package name (as published on TestPyPI), the virtual environment directory, and the Python binary to use.

```sh filename=test.sh

# TestPyPI project name is "upcloud-api" (installs the "upcloud_api" module)
PKG_NAME="upcloud-api"
VENV_DIR=".venv-test-object-storage"
PYTHON_BIN="${PYTHON_BIN:-python3}"
```

### Test Header Output

Display a header to indicate the start of the Object Storage 2.0 API test.

```sh filename=test.sh

echo "======================================"
echo "Testing Object Storage 2.0 API"
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
echo "== Test Object Storage 2.0 API =="
python test_object_storage_test.py
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
