from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.get_server_list_servers import GetServerListServers


T = TypeVar("T", bound="GetServerList")


@_attrs_define
class GetServerList:
    """Schema for the Cloud Server list response.

    Example:
        {'servers': {'server': [{'core_number': '2', 'created': 1705320000, 'hostname': 'web-1.example.com', 'license':
            '0', 'memory_amount': '2048', 'plan': '2xCPU-2GB', 'labels': {'label': [{'key': 'env', 'value': 'production'}]},
            'plan_ipv4_bytes': '34253332', 'plan_ipv6_bytes': '0', 'simple_backup': '0100,dailies', 'state': 'started',
            'tags': {'tag': ['production', 'web']}, 'title': 'Production web server', 'uuid':
            '007bf7bd-e3cf-4a10-bf01-4251dc7f3b65', 'zone': 'fi-hel1'}]}}

    Attributes:
        servers (GetServerListServers):
    """

    servers: GetServerListServers

    def to_dict(self) -> dict[str, Any]:
        servers = self.servers.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "servers": servers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_server_list_servers import GetServerListServers  # noqa: PLC0415

        d = dict(src_dict)
        servers = GetServerListServers.from_dict(d.pop("servers"))

        get_server_list = cls(
            servers=servers,
        )

        return get_server_list
