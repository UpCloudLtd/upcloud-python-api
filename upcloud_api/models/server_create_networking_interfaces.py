from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.server_create_networking_interfaces_interface_item import (
        ServerCreateNetworkingInterfacesInterfaceItem,
    )


T = TypeVar("T", bound="ServerCreateNetworkingInterfaces")


@_attrs_define
class ServerCreateNetworkingInterfaces:
    """
    Attributes:
        interface (list[ServerCreateNetworkingInterfacesInterfaceItem]):
    """

    interface: list[ServerCreateNetworkingInterfacesInterfaceItem]

    def to_dict(self) -> dict[str, Any]:
        interface = []
        for interface_item_data in self.interface:
            interface_item = interface_item_data.to_dict()
            interface.append(interface_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "interface": interface,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_create_networking_interfaces_interface_item import (
            ServerCreateNetworkingInterfacesInterfaceItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        interface = []
        _interface = d.pop("interface")
        for interface_item_data in _interface:
            interface_item = ServerCreateNetworkingInterfacesInterfaceItem.from_dict(interface_item_data)

            interface.append(interface_item)

        server_create_networking_interfaces = cls(
            interface=interface,
        )

        return server_create_networking_interfaces
