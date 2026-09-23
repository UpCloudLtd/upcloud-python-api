from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.ip_address_ip_release_policy import IpAddressIpReleasePolicy

T = TypeVar("T", bound="BulkPatchIpAddressesRequestV13IpAddressesItem")


@_attrs_define
class BulkPatchIpAddressesRequestV13IpAddressesItem:
    """
    Attributes:
        address (str): IP address Example: 10.0.0.20.
        main_account_id (int): Unique numeric identifier of an account.
        delegated_to_account_id (int): Unique numeric identifier of an account.
        release_policy (IpAddressIpReleasePolicy): Action taken when the resource using the address is deleted: release
            deletes the address, while keep preserves it as a detached floating IP address Example: release.
    """

    address: str
    main_account_id: int
    delegated_to_account_id: int
    release_policy: IpAddressIpReleasePolicy

    def to_dict(self) -> dict[str, Any]:
        address: str
        address = self.address

        main_account_id = self.main_account_id

        delegated_to_account_id = self.delegated_to_account_id

        release_policy = self.release_policy.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "address": address,
                "main_account_id": main_account_id,
                "delegated_to_account_id": delegated_to_account_id,
                "release_policy": release_policy,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_address(data: object) -> str:
            return cast(str, data)

        address = _parse_address(d.pop("address"))

        main_account_id = d.pop("main_account_id")

        delegated_to_account_id = d.pop("delegated_to_account_id")

        release_policy = IpAddressIpReleasePolicy(d.pop("release_policy"))

        bulk_patch_ip_addresses_request_v13_ip_addresses_item = cls(
            address=address,
            main_account_id=main_account_id,
            delegated_to_account_id=delegated_to_account_id,
            release_policy=release_policy,
        )

        return bulk_patch_ip_addresses_request_v13_ip_addresses_item
