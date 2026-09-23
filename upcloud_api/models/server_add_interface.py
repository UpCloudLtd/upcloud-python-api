from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.server_add_interface_interface import ServerAddInterfaceInterface


T = TypeVar("T", bound="ServerAddInterface")


@_attrs_define
class ServerAddInterface:
    """Add network interface request

    Example:
        {'interface': {'ip_addresses': {'ip_address': [{'address': '10.0.0.20', 'dhcp_provided': 'yes', 'family':
            'IPv4'}]}, 'network': '0374ce47-4303-4490-987d-32dc96cfd79b', 'source_ip_filtering': 'yes', 'type': 'private'}}

    Attributes:
        interface (ServerAddInterfaceInterface):
    """

    interface: ServerAddInterfaceInterface

    def to_dict(self) -> dict[str, Any]:
        interface = self.interface.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "interface": interface,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_add_interface_interface import ServerAddInterfaceInterface  # noqa: PLC0415

        d = dict(src_dict)
        interface = ServerAddInterfaceInterface.from_dict(d.pop("interface"))

        server_add_interface = cls(
            interface=interface,
        )

        return server_add_interface
