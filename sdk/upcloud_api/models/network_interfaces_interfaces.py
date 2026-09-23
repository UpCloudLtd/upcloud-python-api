from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.network_interface import NetworkInterface


T = TypeVar("T", bound="NetworkInterfacesInterfaces")


@_attrs_define
class NetworkInterfacesInterfaces:
    """
    Example:
        {'interface': {'uuid': '8f6d1ec2-8f5e-4b67-8fcb-6fa9c1a8a003', 'type': 'private', 'network':
            '8f6d1ec2-8f5e-4b67-8fcb-6fa9c1a8a001', 'mac': '00:16:3e:12:34:56', 'source_ip_filtering': 'yes', 'bootable':
            'no', 'ip_addresses': [{'ip_address': {'address': '10.0.0.10', 'family': 'IPv4', 'floating': 'no',
            'release_policy': 'keep', 'dhcp_provided': 'yes'}}]}}

    Attributes:
        interface (NetworkInterface): Response schema for listing network interfaces Example: {'uuid':
            '8f6d1ec2-8f5e-4b67-8fcb-6fa9c1a8a003', 'type': 'private', 'network': '8f6d1ec2-8f5e-4b67-8fcb-6fa9c1a8a001',
            'mac': '00:16:3e:12:34:56', 'source_ip_filtering': 'yes', 'bootable': 'no', 'ip_addresses': [{'ip_address':
            {'address': '10.0.0.10', 'family': 'IPv4', 'floating': 'no', 'release_policy': 'keep', 'dhcp_provided':
            'yes'}}]}.
    """

    interface: NetworkInterface
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interface = self.interface.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "interface": interface,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.network_interface import NetworkInterface  # noqa: PLC0415

        d = dict(src_dict)
        interface = NetworkInterface.from_dict(d.pop("interface"))

        network_interfaces_interfaces = cls(
            interface=interface,
        )

        network_interfaces_interfaces.additional_properties = d
        return network_interfaces_interfaces

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
