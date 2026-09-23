from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.network_boolean_yesno import NetworkBooleanYesno
from ..models.network_type import NetworkType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.network_interface_ip_addresses_item import NetworkInterfaceIpAddressesItem


T = TypeVar("T", bound="NetworkInterface")


@_attrs_define
class NetworkInterface:
    """Response schema for listing network interfaces

    Example:
        {'uuid': '8f6d1ec2-8f5e-4b67-8fcb-6fa9c1a8a003', 'type': 'private', 'network':
            '8f6d1ec2-8f5e-4b67-8fcb-6fa9c1a8a001', 'mac': '00:16:3e:12:34:56', 'source_ip_filtering': 'yes', 'bootable':
            'no', 'ip_addresses': [{'ip_address': {'address': '10.0.0.10', 'family': 'IPv4', 'floating': 'no',
            'release_policy': 'keep', 'dhcp_provided': 'yes'}}]}

    Attributes:
        bootable (NetworkBooleanYesno): Boolean value represented as yes/no Example: yes.
        ip_addresses (list[NetworkInterfaceIpAddressesItem]):  Example: [{'ip_address': {'address': '10.0.0.10',
            'family': 'IPv4', 'floating': 'no', 'release_policy': 'keep', 'dhcp_provided': 'yes'}}].
        mac (str):
        network (str):
        source_ip_filtering (NetworkBooleanYesno): Boolean value represented as yes/no Example: yes.
        type_ (NetworkType): Network access type Example: public.
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        server (UUID | Unset): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
    """

    bootable: NetworkBooleanYesno
    ip_addresses: list[NetworkInterfaceIpAddressesItem]
    mac: str
    network: str
    source_ip_filtering: NetworkBooleanYesno
    type_: NetworkType
    uuid: UUID
    server: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bootable = self.bootable.value

        ip_addresses = []
        for ip_addresses_item_data in self.ip_addresses:
            ip_addresses_item = ip_addresses_item_data.to_dict()
            ip_addresses.append(ip_addresses_item)

        mac = self.mac

        network = self.network

        source_ip_filtering = self.source_ip_filtering.value

        type_ = self.type_.value

        uuid = str(self.uuid)

        server: str | Unset = UNSET
        if not isinstance(self.server, Unset):
            server = str(self.server)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bootable": bootable,
                "ip_addresses": ip_addresses,
                "mac": mac,
                "network": network,
                "source_ip_filtering": source_ip_filtering,
                "type": type_,
                "uuid": uuid,
            }
        )
        if server is not UNSET:
            field_dict["server"] = server

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.network_interface_ip_addresses_item import NetworkInterfaceIpAddressesItem  # noqa: PLC0415

        d = dict(src_dict)
        bootable = NetworkBooleanYesno(d.pop("bootable"))

        ip_addresses = []
        _ip_addresses = d.pop("ip_addresses")
        for ip_addresses_item_data in _ip_addresses:
            ip_addresses_item = NetworkInterfaceIpAddressesItem.from_dict(ip_addresses_item_data)

            ip_addresses.append(ip_addresses_item)

        mac = d.pop("mac")

        network = d.pop("network")

        source_ip_filtering = NetworkBooleanYesno(d.pop("source_ip_filtering"))

        type_ = NetworkType(d.pop("type"))

        uuid = UUID(d.pop("uuid"))

        _server = d.pop("server", UNSET)
        server: UUID | Unset
        if isinstance(_server, Unset):
            server = UNSET
        else:
            server = UUID(_server)

        network_interface = cls(
            bootable=bootable,
            ip_addresses=ip_addresses,
            mac=mac,
            network=network,
            source_ip_filtering=source_ip_filtering,
            type_=type_,
            uuid=uuid,
            server=server,
        )

        network_interface.additional_properties = d
        return network_interface

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
