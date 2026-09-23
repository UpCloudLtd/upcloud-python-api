from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.server_remote_access_details_server import ServerRemoteAccessDetailsServer


T = TypeVar("T", bound="ServerRemoteAccessDetails")


@_attrs_define
class ServerRemoteAccessDetails:
    """Remote access settings and VNC connection details for a Cloud Server

    Example:
        {'server': {'remote_access_enabled': 'yes', 'remote_access_password': 'A1b2C3d4', 'remote_access_type': 'vnc',
            'state': 'started', 'vnc_host': '94.237.1.20', 'vnc_password': 'A1b2C3d4', 'vnc_port': 5901}}

    Attributes:
        server (ServerRemoteAccessDetailsServer):
    """

    server: ServerRemoteAccessDetailsServer

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
        from ..models.server_remote_access_details_server import ServerRemoteAccessDetailsServer  # noqa: PLC0415

        d = dict(src_dict)
        server = ServerRemoteAccessDetailsServer.from_dict(d.pop("server"))

        server_remote_access_details = cls(
            server=server,
        )

        return server_remote_access_details
