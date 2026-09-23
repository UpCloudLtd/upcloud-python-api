#!/usr/bin/env python3
"""
Test script for Tag API.

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
import traceback

from upcloud_api.api.tag import (
    create_tag,
    delete_tag,
    list_tags,
)
from upcloud_api.models import Tag
from upcloud_api.models.tag_servers import TagServers
from upcloud_api.models.tag_tag import TagTag
from upcloud_api.types import UNSET

from upcloud_api import AuthenticatedClient


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

    print("\n2. Listing existing tags (BEFORE)...")
    print("   Testing SDK function: list_tags.sync_detailed()")
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
            print(f"   Parsed: {response.parsed}")
            sys.exit(1)
    except Exception as e:
        print(f"\n   SDK ERROR: {type(e).__name__}: {e}")
        traceback.print_exc()
        sys.exit(1)

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
            print(f"     Parsed: {response.parsed}")
            sys.exit(1)
    except Exception as e:
        print(f"     Error: {e}")
        traceback.print_exc()
        sys.exit(1)

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
            print(f"     Parsed: {response.parsed}")
            sys.exit(1)
    except Exception as e:
        print(f"     Error: {e}")
        traceback.print_exc()
        sys.exit(1)

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
        traceback.print_exc()
        print(f"     Note: Manual cleanup may be required for tag '{test_tag_name}'")
        sys.exit(1)

    print("\n" + "=" * 50)
    print("  Tag API validation completed")
    print("=" * 50)


if __name__ == "__main__":
    main()
