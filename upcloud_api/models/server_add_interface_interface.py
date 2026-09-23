from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.server_boolean_yesno import ServerBooleanYesno
from ..models.server_network_type import ServerNetworkType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.server_add_interface_interface_ip_addresses import ServerAddInterfaceInterfaceIpAddresses


T = TypeVar("T", bound="ServerAddInterfaceInterface")


@_attrs_define
class ServerAddInterfaceInterface:
    """
    Attributes:
        ip_addresses (ServerAddInterfaceInterfaceIpAddresses): IP addresses to attach to the interface
        type_ (ServerNetworkType): Network access type Example: public.
        bootable (ServerBooleanYesno | Unset): Boolean value represented as yes/no Example: yes.
        index (int | Unset): Interface index; the next available index is used when omitted
        network (UUID | Unset): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        source_ip_filtering (ServerBooleanYesno | Unset): Boolean value represented as yes/no Example: yes.
    """

    ip_addresses: ServerAddInterfaceInterfaceIpAddresses
    type_: ServerNetworkType
    bootable: ServerBooleanYesno | Unset = UNSET
    index: int | Unset = UNSET
    network: UUID | Unset = UNSET
    source_ip_filtering: ServerBooleanYesno | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        ip_addresses = self.ip_addresses.to_dict()

        type_ = self.type_.value

        bootable: str | Unset = UNSET
        if not isinstance(self.bootable, Unset):
            bootable = self.bootable.value

        index = self.index

        network: str | Unset = UNSET
        if not isinstance(self.network, Unset):
            network = str(self.network)

        source_ip_filtering: str | Unset = UNSET
        if not isinstance(self.source_ip_filtering, Unset):
            source_ip_filtering = self.source_ip_filtering.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "ip_addresses": ip_addresses,
                "type": type_,
            }
        )
        if bootable is not UNSET:
            field_dict["bootable"] = bootable
        if index is not UNSET:
            field_dict["index"] = index
        if network is not UNSET:
            field_dict["network"] = network
        if source_ip_filtering is not UNSET:
            field_dict["source_ip_filtering"] = source_ip_filtering

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_add_interface_interface_ip_addresses import (
            ServerAddInterfaceInterfaceIpAddresses,  # noqa: PLC0415
        )

        d = dict(src_dict)
        ip_addresses = ServerAddInterfaceInterfaceIpAddresses.from_dict(d.pop("ip_addresses"))

        type_ = ServerNetworkType(d.pop("type"))

        _bootable = d.pop("bootable", UNSET)
        bootable: ServerBooleanYesno | Unset
        if isinstance(_bootable, Unset):
            bootable = UNSET
        else:
            bootable = ServerBooleanYesno(_bootable)

        index = d.pop("index", UNSET)

        _network = d.pop("network", UNSET)
        network: UUID | Unset
        if isinstance(_network, Unset):
            network = UNSET
        else:
            network = UUID(_network)

        _source_ip_filtering = d.pop("source_ip_filtering", UNSET)
        source_ip_filtering: ServerBooleanYesno | Unset
        if isinstance(_source_ip_filtering, Unset):
            source_ip_filtering = UNSET
        else:
            source_ip_filtering = ServerBooleanYesno(_source_ip_filtering)

        server_add_interface_interface = cls(
            ip_addresses=ip_addresses,
            type_=type_,
            bootable=bootable,
            index=index,
            network=network,
            source_ip_filtering=source_ip_filtering,
        )

        return server_add_interface_interface
