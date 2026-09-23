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
        {'server': {'hostname': 'my-server.example.com', 'title': 'My Server', 'zone': 'fi-hel1', 'storage_devices':
            {'storage_device': [{'action': 'clone', 'storage': '01234567-89ab-cdef-0123-456789abcdef', 'title': 'Operating
            System'}]}}}

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
