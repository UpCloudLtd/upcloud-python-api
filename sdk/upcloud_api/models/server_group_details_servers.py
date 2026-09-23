from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

T = TypeVar("T", bound="ServerGroupDetailsServers")


@_attrs_define
class ServerGroupDetailsServers:
    """List of servers associated with the server group.

    Attributes:
        server (list[UUID]):
    """

    server: list[UUID]

    def to_dict(self) -> dict[str, Any]:
        server = []
        for server_item_data in self.server:
            server_item = str(server_item_data)
            server.append(server_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "server": server,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        server = []
        _server = d.pop("server")
        for server_item_data in _server:
            server_item = UUID(server_item_data)

            server.append(server_item)

        server_group_details_servers = cls(
            server=server,
        )

        return server_group_details_servers
