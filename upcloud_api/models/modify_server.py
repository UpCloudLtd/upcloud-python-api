from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.modify_server_server import ModifyServerServer


T = TypeVar("T", bound="ModifyServer")


@_attrs_define
class ModifyServer:
    """Fields that can be changed on an existing Cloud Server

    Example:
        {'server': {'core_number': 8, 'memory_amount': 16384, 'plan': 'custom'}}

    Attributes:
        server (ModifyServerServer):
    """

    server: ModifyServerServer

    def to_dict(self) -> dict[str, Any]:
        server = self.server.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "server": server,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.modify_server_server import ModifyServerServer  # noqa: PLC0415

        d = dict(src_dict)
        server = ModifyServerServer.from_dict(d.pop("server"))

        modify_server = cls(
            server=server,
        )

        return modify_server
