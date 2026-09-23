from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.server_modify_interface_interface import ServerModifyInterfaceInterface


T = TypeVar("T", bound="ServerModifyInterface")


@_attrs_define
class ServerModifyInterface:
    """Modify network interface request

    Example:
        {'interface': {'bootable': 'yes', 'index': 5, 'source_ip_filtering': 'no'}}

    Attributes:
        interface (ServerModifyInterfaceInterface):
    """

    interface: ServerModifyInterfaceInterface

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
        from ..models.server_modify_interface_interface import ServerModifyInterfaceInterface  # noqa: PLC0415

        d = dict(src_dict)
        interface = ServerModifyInterfaceInterface.from_dict(d.pop("interface"))

        server_modify_interface = cls(
            interface=interface,
        )

        return server_modify_interface
