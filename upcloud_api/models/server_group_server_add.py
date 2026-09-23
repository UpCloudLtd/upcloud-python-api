from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.server_group_server_add_server import ServerGroupServerAddServer


T = TypeVar("T", bound="ServerGroupServerAdd")


@_attrs_define
class ServerGroupServerAdd:
    """Schema for adding a server to a server group

    Attributes:
        server (ServerGroupServerAddServer):
    """

    server: ServerGroupServerAddServer

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
        from ..models.server_group_server_add_server import ServerGroupServerAddServer  # noqa: PLC0415

        d = dict(src_dict)
        server = ServerGroupServerAddServer.from_dict(d.pop("server"))

        server_group_server_add = cls(
            server=server,
        )

        return server_group_server_add
