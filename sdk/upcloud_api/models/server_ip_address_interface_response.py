from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.server_interface_ip_address import ServerInterfaceIpAddress


T = TypeVar("T", bound="ServerIpAddressInterfaceResponse")


@_attrs_define
class ServerIpAddressInterfaceResponse:
    """IP address response for a network interface

    Example:
        {'ip_address': {'address': '10.0.0.30', 'dhcp_provided': 'no', 'family': 'IPv4'}}

    Attributes:
        ip_address (ServerInterfaceIpAddress): Network interface IP address Example: {'address': '10.0.0.20',
            'dhcp_provided': 'yes', 'family': 'IPv4', 'floating': 'no', 'release_policy': 'release'}.
    """

    ip_address: ServerInterfaceIpAddress
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ip_address = self.ip_address.to_dict()

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
        ip_address = ServerInterfaceIpAddress.from_dict(d.pop("ip_address"))

        server_ip_address_interface_response = cls(
            ip_address=ip_address,
        )

        server_ip_address_interface_response.additional_properties = d
        return server_ip_address_interface_response

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
