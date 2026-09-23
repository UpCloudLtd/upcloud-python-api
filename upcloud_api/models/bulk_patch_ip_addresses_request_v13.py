from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.bulk_patch_ip_addresses_request_v13_ip_addresses_item import (
        BulkPatchIpAddressesRequestV13IpAddressesItem,
    )


T = TypeVar("T", bound="BulkPatchIpAddressesRequestV13")


@_attrs_define
class BulkPatchIpAddressesRequestV13:
    """Request schema for bulk patching IP addresses

    Attributes:
        ip_addresses (list[BulkPatchIpAddressesRequestV13IpAddressesItem]):
    """

    ip_addresses: list[BulkPatchIpAddressesRequestV13IpAddressesItem]

    def to_dict(self) -> dict[str, Any]:
        ip_addresses = []
        for ip_addresses_item_data in self.ip_addresses:
            ip_addresses_item = ip_addresses_item_data.to_dict()
            ip_addresses.append(ip_addresses_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "ip_addresses": ip_addresses,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bulk_patch_ip_addresses_request_v13_ip_addresses_item import (
            BulkPatchIpAddressesRequestV13IpAddressesItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        ip_addresses = []
        _ip_addresses = d.pop("ip_addresses")
        for ip_addresses_item_data in _ip_addresses:
            ip_addresses_item = BulkPatchIpAddressesRequestV13IpAddressesItem.from_dict(ip_addresses_item_data)

            ip_addresses.append(ip_addresses_item)

        bulk_patch_ip_addresses_request_v13 = cls(
            ip_addresses=ip_addresses,
        )

        return bulk_patch_ip_addresses_request_v13
