from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.start_server_server import StartServerServer


T = TypeVar("T", bound="StartServer")


@_attrs_define
class StartServer:
    """Start Cloud Server request

    Example:
        {'server': {'host': 8055964291, 'start_type': 'sync'}}

    Attributes:
        server (StartServerServer):
    """

    server: StartServerServer

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
        from ..models.start_server_server import StartServerServer  # noqa: PLC0415

        d = dict(src_dict)
        server = StartServerServer.from_dict(d.pop("server"))

        start_server = cls(
            server=server,
        )

        return start_server
