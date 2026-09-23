from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

T = TypeVar("T", bound="ServerGroupServers")


@_attrs_define
class ServerGroupServers:
    """List of server UUIDs in the server group

    Example:
        {'servers': ['00fce2f9-f9f4-46ff-86af-9e60f131f5cb', '0414e0d7-4436-4037-9dd8-6eaf47dce599']}

    Attributes:
        servers (list[UUID]):
    """

    servers: list[UUID]

    def to_dict(self) -> dict[str, Any]:
        servers = []
        for servers_item_data in self.servers:
            servers_item = str(servers_item_data)
            servers.append(servers_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "servers": servers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        servers = []
        _servers = d.pop("servers")
        for servers_item_data in _servers:
            servers_item = UUID(servers_item_data)

            servers.append(servers_item)

        server_group_servers = cls(
            servers=servers,
        )

        return server_group_servers
