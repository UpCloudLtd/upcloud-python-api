from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.server_ip_addresses_ip_address_item import ServerIpAddressesIpAddressItem


T = TypeVar("T", bound="ServerIpAddresses")


@_attrs_define
class ServerIpAddresses:
    """IP addresses assigned to the Cloud Server

    Example:
        {'ip_address': [{'access': 'utility', 'address': '10.0.0.10', 'family': 'IPv4'}]}

    Attributes:
        ip_address (list[ServerIpAddressesIpAddressItem]):
    """

    ip_address: list[ServerIpAddressesIpAddressItem]

    def to_dict(self) -> dict[str, Any]:
        ip_address = []
        for ip_address_item_data in self.ip_address:
            ip_address_item = ip_address_item_data.to_dict()
            ip_address.append(ip_address_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "ip_address": ip_address,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_ip_addresses_ip_address_item import ServerIpAddressesIpAddressItem  # noqa: PLC0415

        d = dict(src_dict)
        ip_address = []
        _ip_address = d.pop("ip_address")
        for ip_address_item_data in _ip_address:
            ip_address_item = ServerIpAddressesIpAddressItem.from_dict(ip_address_item_data)

            ip_address.append(ip_address_item)

        server_ip_addresses = cls(
            ip_address=ip_address,
        )

        return server_ip_addresses
