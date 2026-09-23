# Testing the Tag API

This example demonstrates how to use the UpCloud Python SDK to interact with the Tag API. We'll create a test script that:

- Authenticates a client using a bearer token
- Lists existing tags
- Creates a new tag
- Verifies the tag was created
- Cleans up by deleting the test tag

## The Python Test Script

Let's build the test script step by step.

### Imports and Module Docstring

First, we define the script's purpose and import the necessary modules. We need the UpCloud SDK client, the tag API functions, and the models for creating tags.

```py filename=test_tag_test.py
#!/usr/bin/env python3
"""Test script for Tag API.

Tests:
- Authenticate client
- List existing tags
- Create a new tag
- List tags again to verify creation
- Delete the test tag
"""

import os
import sys
import time

from upcloud_api.api.tag import (
    list_tags,
    create_tag,
    delete_tag,
)
from upcloud_api.models import Tag
from upcloud_api.models.tag_servers import TagServers
from upcloud_api.models.tag_tag import TagTag
from upcloud_api.types import UNSET

from upcloud_api import AuthenticatedClient

```

### Main Function Setup

The `main()` function starts by reading the authentication token from environment variables. The `UPCLOUD_TOKEN` is required for authentication.

```py filename=test_tag_test.py

def main():
    """Run the Tag API test."""
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

### Step 2: List Existing Tags (Before)

Before creating a new tag, we list all existing tags. This establishes a baseline count that we'll use later to verify our new tag was created.

```py filename=test_tag_test.py

    print("\n2. Listing existing tags (BEFORE)...")
    try:
        response = list_tags.sync_detailed(client=client)

        if response.status_code == 200 and response.parsed is not None:
            tags_response = response.parsed
            tags_before = getattr(tags_response, "tags", None)
            if tags_before:
                tag_list = getattr(tags_before, "tag", []) or []
                print(f"   Found {len(tag_list)} tag(s)")
                for tag_item in tag_list:
                    tag_name = getattr(tag_item, "name", "unknown")
                    tag_desc = getattr(tag_item, "description", UNSET)
                    desc_str = f" - {tag_desc}" if tag_desc is not UNSET else ""
                    print(f"     - {tag_name}{desc_str}")
            else:
                tag_list = []
                print("   Found 0 tag(s)")
        else:
            print(f"   Failed with status: {response.status_code}")
            sys.exit(1)
    except Exception as e:
        print(f"   Error: {e}")
        sys.exit(1)
```

### Step 3: Create a New Tag

Now we create a new tag using the `Tag`, `TagTag`, and `TagServers` models. We generate a unique name using a timestamp to avoid conflicts.

```py filename=test_tag_test.py

    print("\n3. Creating a new tag...")
    test_tag_name = f"test-tag-{int(time.time())}"

    try:
        tag_servers = TagServers(server=UNSET)
        tag_data = TagTag(
            name=test_tag_name,
            description="Test tag created by SDK example",
            servers=tag_servers,
        )
        tag_payload = Tag(tag=tag_data)

        response = create_tag.sync_detailed(
            client=client,
            body=tag_payload,
        )

        if response.status_code == 200 and response.parsed is not None:
            created_tag = response.parsed
            tag_obj = getattr(created_tag, "tag", None)
            if tag_obj:
                created_name = getattr(tag_obj, "name", "N/A")
                print(f"     Tag '{created_name}' created successfully")
            else:
                print(f"     Tag '{test_tag_name}' created successfully")
        else:
            print(f"     Failed with status: {response.status_code}")
            sys.exit(1)
    except Exception as e:
        print(f"     Error: {e}")
        sys.exit(1)
```

### Step 4: List Tags Again (After)

After creating the tag, we list all tags again to verify the new tag appears in the list. We compare the count with the baseline from step 2.

```py filename=test_tag_test.py

    print("\n4. Listing tags (AFTER)...")
    try:
        response = list_tags.sync_detailed(client=client)

        if response.status_code == 200 and response.parsed is not None:
            tags_response = response.parsed
            tags_after = getattr(tags_response, "tags", None)
            if tags_after:
                tag_list_after = getattr(tags_after, "tag", []) or []
                print(f"     Found {len(tag_list_after)} tag(s)")
                for tag_item in tag_list_after:
                    tag_name = getattr(tag_item, "name", "unknown")
                    tag_desc = getattr(tag_item, "description", UNSET)
                    desc_str = f" - {tag_desc}" if tag_desc is not UNSET else ""
                    is_new = " [NEW]" if tag_name == test_tag_name else ""
                    print(f"     - {tag_name}{desc_str}{is_new}")

                if len(tag_list_after) == len(tag_list) + 1:
                    print("\n     Verification passed: Tag count increased by 1")
                else:
                    print(
                        f"\n     Warning: Expected {len(tag_list) + 1} tags, found {len(tag_list_after)}"
                    )
            else:
                print("     Found 0 tag(s)")
        else:
            print(f"     Failed with status: {response.status_code}")
            sys.exit(1)
    except Exception as e:
        print(f"     Error: {e}")
        sys.exit(1)
```

### Step 5: Cleanup - Delete the Test Tag

Finally, we clean up by deleting the test tag we created.

```py filename=test_tag_test.py

    print("\n5. Cleaning up - deleting test tag...")
    try:
        response = delete_tag.sync_detailed(
            client=client,
            name=test_tag_name,
        )

        if response.status_code == 204:
            print(f"     Tag '{test_tag_name}' deleted successfully")
        elif response.status_code == 404:
            print("     Tag not found for deletion (may have been auto-deleted)")
        else:
            print(f"     Failed to delete (status: {response.status_code})")
            print(f"     Note: Manual cleanup may be required for tag '{test_tag_name}'")
    except Exception as e:
        print(f"     Error during cleanup: {e}")
        print(f"     Note: Manual cleanup may be required for tag '{test_tag_name}'")
        sys.exit(1)

    print("\n" + "=" * 50)
    print("  Tag API validation completed")
    print("=" * 50)
```

### Entry Point

The script's entry point calls the `main()` function when executed directly.

```py filename=test_tag_test.py


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

# Test Tag API
# Tests: list_tags, create_tag, list_tags again, delete_tag
```

### Configuration Variables

mdtest runs the shell script in a temporary directory. Point it at the repository root with `UPCLOUD_SDK_PATH`.

```sh filename=test.sh

SDK_DIR="${UPCLOUD_SDK_PATH:?Set UPCLOUD_SDK_PATH to the repository root}"
```

### Test Header Output

Display a header to indicate the start of the Tag API test.

```sh filename=test.sh

echo "======================================"
echo "Testing Tag API"
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
echo "== Test Tag API with local SDK =="
uv run --no-project --with "$SDK_DIR" python test_tag_test.py
```

## Execute the Test

Finally, we run the shell script to execute the complete test.

```sh
bash test.sh
```
