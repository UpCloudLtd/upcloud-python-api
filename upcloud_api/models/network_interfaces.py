from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.network_interfaces_interfaces import NetworkInterfacesInterfaces


T = TypeVar("T", bound="NetworkInterfaces")


@_attrs_define
class NetworkInterfaces:
    """Response schema for listing network interfaces

    Example:
        {'interfaces': {'interface': {'uuid': '8f6d1ec2-8f5e-4b67-8fcb-6fa9c1a8a003', 'type': 'private', 'network':
            '8f6d1ec2-8f5e-4b67-8fcb-6fa9c1a8a001', 'mac': '00:16:3e:12:34:56', 'source_ip_filtering': 'yes', 'bootable':
            'no', 'ip_addresses': [{'ip_address': {'address': '10.0.0.10', 'family': 'IPv4', 'floating': 'no',
            'release_policy': 'keep', 'dhcp_provided': 'yes'}}]}}}

    Attributes:
        interfaces (NetworkInterfacesInterfaces):  Example: {'interface': {'uuid':
            '8f6d1ec2-8f5e-4b67-8fcb-6fa9c1a8a003', 'type': 'private', 'network': '8f6d1ec2-8f5e-4b67-8fcb-6fa9c1a8a001',
            'mac': '00:16:3e:12:34:56', 'source_ip_filtering': 'yes', 'bootable': 'no', 'ip_addresses': [{'ip_address':
            {'address': '10.0.0.10', 'family': 'IPv4', 'floating': 'no', 'release_policy': 'keep', 'dhcp_provided':
            'yes'}}]}}.
    """

    interfaces: NetworkInterfacesInterfaces
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interfaces = self.interfaces.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "interfaces": interfaces,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.network_interfaces_interfaces import NetworkInterfacesInterfaces  # noqa: PLC0415

        d = dict(src_dict)
        interfaces = NetworkInterfacesInterfaces.from_dict(d.pop("interfaces"))

        network_interfaces = cls(
            interfaces=interfaces,
        )

        network_interfaces.additional_properties = d
        return network_interfaces

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
