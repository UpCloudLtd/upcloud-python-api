from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.server_boolean_yesno import ServerBooleanYesno
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.server_modify_interface_interface_ip_addresses import ServerModifyInterfaceInterfaceIpAddresses


T = TypeVar("T", bound="ServerModifyInterfaceInterface")


@_attrs_define
class ServerModifyInterfaceInterface:
    """
    Attributes:
        bootable (ServerBooleanYesno | Unset): Boolean value represented as yes/no Example: yes.
        index (int | Unset): New index for the interface; defaults to the index in the request path
        ip_addresses (ServerModifyInterfaceInterfaceIpAddresses | Unset): Complete replacement list of IP addresses for
            the interface
        source_ip_filtering (ServerBooleanYesno | Unset): Boolean value represented as yes/no Example: yes.
    """

    bootable: ServerBooleanYesno | Unset = UNSET
    index: int | Unset = UNSET
    ip_addresses: ServerModifyInterfaceInterfaceIpAddresses | Unset = UNSET
    source_ip_filtering: ServerBooleanYesno | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        bootable: str | Unset = UNSET
        if not isinstance(self.bootable, Unset):
            bootable = self.bootable.value

        index = self.index

        ip_addresses: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ip_addresses, Unset):
            ip_addresses = self.ip_addresses.to_dict()

        source_ip_filtering: str | Unset = UNSET
        if not isinstance(self.source_ip_filtering, Unset):
            source_ip_filtering = self.source_ip_filtering.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if bootable is not UNSET:
            field_dict["bootable"] = bootable
        if index is not UNSET:
            field_dict["index"] = index
        if ip_addresses is not UNSET:
            field_dict["ip_addresses"] = ip_addresses
        if source_ip_filtering is not UNSET:
            field_dict["source_ip_filtering"] = source_ip_filtering

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_modify_interface_interface_ip_addresses import (
            ServerModifyInterfaceInterfaceIpAddresses,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _bootable = d.pop("bootable", UNSET)
        bootable: ServerBooleanYesno | Unset
        if isinstance(_bootable, Unset):
            bootable = UNSET
        else:
            bootable = ServerBooleanYesno(_bootable)

        index = d.pop("index", UNSET)

        _ip_addresses = d.pop("ip_addresses", UNSET)
        ip_addresses: ServerModifyInterfaceInterfaceIpAddresses | Unset
        if isinstance(_ip_addresses, Unset):
            ip_addresses = UNSET
        else:
            ip_addresses = ServerModifyInterfaceInterfaceIpAddresses.from_dict(_ip_addresses)

        _source_ip_filtering = d.pop("source_ip_filtering", UNSET)
        source_ip_filtering: ServerBooleanYesno | Unset
        if isinstance(_source_ip_filtering, Unset):
            source_ip_filtering = UNSET
        else:
            source_ip_filtering = ServerBooleanYesno(_source_ip_filtering)

        server_modify_interface_interface = cls(
            bootable=bootable,
            index=index,
            ip_addresses=ip_addresses,
            source_ip_filtering=source_ip_filtering,
        )

        return server_modify_interface_interface
