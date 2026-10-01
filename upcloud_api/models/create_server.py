from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.create_server_server import CreateServerServer


T = TypeVar("T", bound="CreateServer")


@_attrs_define
class CreateServer:
    """Cloud Server creation parameters

    Example:
        {'server': {'hostname': 'my-server.example.com', 'title': 'My Server', 'zone': 'fi-hel1', 'plan': '1xCPU-1GB',
            'metadata': 'yes', 'networking': {'interfaces': {'interface': [{'ip_addresses': {'ip_address': [{'family':
            'IPv4'}]}, 'type': 'public'}, {'ip_addresses': {'ip_address': [{'family': 'IPv4'}]}, 'type': 'utility'},
            {'ip_addresses': {'ip_address': [{'family': 'IPv4'}]}, 'network': '03000000-0000-4000-8000-000000000000',
            'type': 'private'}]}}, 'login_user': {'username': 'upclouduser', 'ssh_keys': {'ssh_key': ['ssh-ed25519
            AAAAC3NzaC1lZDI1NTE5AAAAIO3t5AQcuv4+KxJ5rC75N8bW/e7eOq0k5Y2L7V1oH3Z5 user@example.com']}}, 'storage_devices':
            {'storage_device': [{'action': 'clone', 'storage': '01000000-0000-4000-8000-000020080100', 'size': 30, 'tier':
            'maxiops', 'title': 'Debian Trixie'}]}}}

    Attributes:
        server (CreateServerServer):
    """

    server: CreateServerServer

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
        from ..models.create_server_server import CreateServerServer  # noqa: PLC0415

        d = dict(src_dict)
        server = CreateServerServer.from_dict(d.pop("server"))

        create_server = cls(
            server=server,
        )

        return create_server
