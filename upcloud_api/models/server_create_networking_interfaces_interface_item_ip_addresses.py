from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.server_create_networking_interfaces_interface_item_ip_addresses_ip_address_item import (
        ServerCreateNetworkingInterfacesInterfaceItemIpAddressesIpAddressItem,
    )


T = TypeVar("T", bound="ServerCreateNetworkingInterfacesInterfaceItemIpAddresses")


@_attrs_define
class ServerCreateNetworkingInterfacesInterfaceItemIpAddresses:
    """
    Attributes:
        ip_address (list[ServerCreateNetworkingInterfacesInterfaceItemIpAddressesIpAddressItem]):
    """

    ip_address: list[ServerCreateNetworkingInterfacesInterfaceItemIpAddressesIpAddressItem]

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
        from ..models.server_create_networking_interfaces_interface_item_ip_addresses_ip_address_item import (
            ServerCreateNetworkingInterfacesInterfaceItemIpAddressesIpAddressItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        ip_address = []
        _ip_address = d.pop("ip_address")
        for ip_address_item_data in _ip_address:
            ip_address_item = ServerCreateNetworkingInterfacesInterfaceItemIpAddressesIpAddressItem.from_dict(
                ip_address_item_data
            )

            ip_address.append(ip_address_item)

        server_create_networking_interfaces_interface_item_ip_addresses = cls(
            ip_address=ip_address,
        )

        return server_create_networking_interfaces_interface_item_ip_addresses
