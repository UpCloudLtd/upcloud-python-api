from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.server_interface import ServerInterface


T = TypeVar("T", bound="ServerNetworkingInterfaces")


@_attrs_define
class ServerNetworkingInterfaces:
    """Network interfaces attached to the Cloud Server

    Attributes:
        interface (list[ServerInterface]): Network interfaces ordered by interface index
    """

    interface: list[ServerInterface]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interface = []
        for interface_item_data in self.interface:
            interface_item = interface_item_data.to_dict()
            interface.append(interface_item)

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
        from ..models.server_interface import ServerInterface  # noqa: PLC0415

        d = dict(src_dict)
        interface = []
        _interface = d.pop("interface")
        for interface_item_data in _interface:
            interface_item = ServerInterface.from_dict(interface_item_data)

            interface.append(interface_item)

        server_networking_interfaces = cls(
            interface=interface,
        )

        server_networking_interfaces.additional_properties = d
        return server_networking_interfaces

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
