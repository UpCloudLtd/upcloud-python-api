from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.server_networking_interfaces import ServerNetworkingInterfaces


T = TypeVar("T", bound="ServerNetworking")


@_attrs_define
class ServerNetworking:
    """Network interfaces configured for the Cloud Server

    Example:
        {'interfaces': {'interface': [{'bootable': 'no', 'index': 4, 'ip_addresses': {'ip_address': [{'address':
            '10.0.0.20', 'dhcp_provided': 'yes', 'family': 'IPv4', 'floating': 'no', 'release_policy': 'release'}]}, 'mac':
            'de:ff:ff:ff:cc:20', 'network': '0374ce47-4303-4490-987d-32dc96cfd79b', 'source_ip_filtering': 'yes', 'type':
            'private'}]}}

    Attributes:
        interfaces (ServerNetworkingInterfaces | Unset): Network interfaces attached to the Cloud Server
    """

    interfaces: ServerNetworkingInterfaces | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interfaces: dict[str, Any] | Unset = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = self.interfaces.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_networking_interfaces import ServerNetworkingInterfaces  # noqa: PLC0415

        d = dict(src_dict)
        _interfaces = d.pop("interfaces", UNSET)
        interfaces: ServerNetworkingInterfaces | Unset
        if isinstance(_interfaces, Unset):
            interfaces = UNSET
        else:
            interfaces = ServerNetworkingInterfaces.from_dict(_interfaces)

        server_networking = cls(
            interfaces=interfaces,
        )

        server_networking.additional_properties = d
        return server_networking

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
