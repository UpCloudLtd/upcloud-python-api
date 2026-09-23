from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.server_boolean_yesno import ServerBooleanYesno
from ..models.server_network_type import ServerNetworkType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.server_interface_ip_addresses import ServerInterfaceIpAddresses


T = TypeVar("T", bound="ServerInterface")


@_attrs_define
class ServerInterface:
    """Network interface attached to a Cloud Server

    Example:
        {'bootable': 'no', 'index': 4, 'ip_addresses': {'ip_address': [{'address': '10.0.0.20', 'dhcp_provided': 'yes',
            'family': 'IPv4', 'floating': 'no', 'release_policy': 'release'}]}, 'mac': 'de:ff:ff:ff:cc:20', 'network':
            '0374ce47-4303-4490-987d-32dc96cfd79b', 'source_ip_filtering': 'yes', 'type': 'private'}

    Attributes:
        network (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        bootable (ServerBooleanYesno | Unset): Boolean value represented as yes/no Example: yes.
        index (int | Unset): Index that identifies and orders the interface
        ip_addresses (ServerInterfaceIpAddresses | Unset): IP addresses attached to the interface
        mac (str | Unset): MAC address Example: de:ff:ff:ff:cc:20.
        source_ip_filtering (ServerBooleanYesno | Unset): Boolean value represented as yes/no Example: yes.
        type_ (ServerNetworkType | Unset): Network access type Example: public.
    """

    network: UUID
    bootable: ServerBooleanYesno | Unset = UNSET
    index: int | Unset = UNSET
    ip_addresses: ServerInterfaceIpAddresses | Unset = UNSET
    mac: str | Unset = UNSET
    source_ip_filtering: ServerBooleanYesno | Unset = UNSET
    type_: ServerNetworkType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        network = str(self.network)

        bootable: str | Unset = UNSET
        if not isinstance(self.bootable, Unset):
            bootable = self.bootable.value

        index = self.index

        ip_addresses: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ip_addresses, Unset):
            ip_addresses = self.ip_addresses.to_dict()

        mac = self.mac

        source_ip_filtering: str | Unset = UNSET
        if not isinstance(self.source_ip_filtering, Unset):
            source_ip_filtering = self.source_ip_filtering.value

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "network": network,
            }
        )
        if bootable is not UNSET:
            field_dict["bootable"] = bootable
        if index is not UNSET:
            field_dict["index"] = index
        if ip_addresses is not UNSET:
            field_dict["ip_addresses"] = ip_addresses
        if mac is not UNSET:
            field_dict["mac"] = mac
        if source_ip_filtering is not UNSET:
            field_dict["source_ip_filtering"] = source_ip_filtering
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_interface_ip_addresses import ServerInterfaceIpAddresses  # noqa: PLC0415

        d = dict(src_dict)
        network = UUID(d.pop("network"))

        _bootable = d.pop("bootable", UNSET)
        bootable: ServerBooleanYesno | Unset
        if isinstance(_bootable, Unset):
            bootable = UNSET
        else:
            bootable = ServerBooleanYesno(_bootable)

        index = d.pop("index", UNSET)

        _ip_addresses = d.pop("ip_addresses", UNSET)
        ip_addresses: ServerInterfaceIpAddresses | Unset
        if isinstance(_ip_addresses, Unset):
            ip_addresses = UNSET
        else:
            ip_addresses = ServerInterfaceIpAddresses.from_dict(_ip_addresses)

        mac = d.pop("mac", UNSET)

        _source_ip_filtering = d.pop("source_ip_filtering", UNSET)
        source_ip_filtering: ServerBooleanYesno | Unset
        if isinstance(_source_ip_filtering, Unset):
            source_ip_filtering = UNSET
        else:
            source_ip_filtering = ServerBooleanYesno(_source_ip_filtering)

        _type_ = d.pop("type", UNSET)
        type_: ServerNetworkType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ServerNetworkType(_type_)

        server_interface = cls(
            network=network,
            bootable=bootable,
            index=index,
            ip_addresses=ip_addresses,
            mac=mac,
            source_ip_filtering=source_ip_filtering,
            type_=type_,
        )

        server_interface.additional_properties = d
        return server_interface

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
