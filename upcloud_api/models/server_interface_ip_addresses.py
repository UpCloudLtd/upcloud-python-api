from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.server_interface_ip_address import ServerInterfaceIpAddress


T = TypeVar("T", bound="ServerInterfaceIpAddresses")


@_attrs_define
class ServerInterfaceIpAddresses:
    """IP addresses attached to the interface

    Attributes:
        ip_address (list[ServerInterfaceIpAddress]):
    """

    ip_address: list[ServerInterfaceIpAddress]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ip_address = []
        for ip_address_item_data in self.ip_address:
            ip_address_item = ip_address_item_data.to_dict()
            ip_address.append(ip_address_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ip_address": ip_address,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_interface_ip_address import ServerInterfaceIpAddress  # noqa: PLC0415

        d = dict(src_dict)
        ip_address = []
        _ip_address = d.pop("ip_address")
        for ip_address_item_data in _ip_address:
            ip_address_item = ServerInterfaceIpAddress.from_dict(ip_address_item_data)

            ip_address.append(ip_address_item)

        server_interface_ip_addresses = cls(
            ip_address=ip_address,
        )

        server_interface_ip_addresses.additional_properties = d
        return server_interface_ip_addresses

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
