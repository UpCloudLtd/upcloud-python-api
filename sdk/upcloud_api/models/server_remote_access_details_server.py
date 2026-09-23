from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..models.server_remote_access_enabled import ServerRemoteAccessEnabled
from ..models.server_remote_access_type import ServerRemoteAccessType
from ..models.server_state import ServerState

T = TypeVar("T", bound="ServerRemoteAccessDetailsServer")


@_attrs_define
class ServerRemoteAccessDetailsServer:
    """
    Attributes:
        state (ServerState): Current state of the Cloud Server Example: started.
        vnc_host (str): VNC host IP address or noVNC proxy hostname. Empty when no VNC endpoint is assigned. Example:
            94.237.1.20.
        vnc_password (str): VNC password Example: A1b2C3d4.
        vnc_port (int | Literal['']): VNC or noVNC proxy port. Empty when no VNC endpoint is assigned. Example: 5901.
        remote_access_type (ServerRemoteAccessType): Protocol used for remote access Example: vnc.
        remote_access_enabled (ServerRemoteAccessEnabled): Whether remote access is enabled Example: yes.
        remote_access_password (str): Eight-character alphanumeric password used to authenticate remote access Example:
            A1b2C3d4.
    """

    state: ServerState
    vnc_host: str
    vnc_password: str
    vnc_port: int | Literal[""]
    remote_access_type: ServerRemoteAccessType
    remote_access_enabled: ServerRemoteAccessEnabled
    remote_access_password: str

    def to_dict(self) -> dict[str, Any]:
        state = self.state.value

        vnc_host = self.vnc_host

        vnc_password = self.vnc_password

        vnc_port: int | Literal[""]
        vnc_port = self.vnc_port

        remote_access_type = self.remote_access_type.value

        remote_access_enabled = self.remote_access_enabled.value

        remote_access_password = self.remote_access_password

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "state": state,
                "vnc_host": vnc_host,
                "vnc_password": vnc_password,
                "vnc_port": vnc_port,
                "remote_access_type": remote_access_type,
                "remote_access_enabled": remote_access_enabled,
                "remote_access_password": remote_access_password,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        state = ServerState(d.pop("state"))

        vnc_host = d.pop("vnc_host")

        vnc_password = d.pop("vnc_password")

        def _parse_vnc_port(data: object) -> int | Literal[""]:
            componentsschemasserver_vnc_port_type_1 = cast(Literal[""], data)
            if componentsschemasserver_vnc_port_type_1 != "":
                raise ValueError(
                    f"/components/schemas/serverVncPort_type_1 must match const '', got '{componentsschemasserver_vnc_port_type_1}'"
                )
            return componentsschemasserver_vnc_port_type_1
            return cast(int | Literal[""], data)

        vnc_port = _parse_vnc_port(d.pop("vnc_port"))

        remote_access_type = ServerRemoteAccessType(d.pop("remote_access_type"))

        remote_access_enabled = ServerRemoteAccessEnabled(d.pop("remote_access_enabled"))

        remote_access_password = d.pop("remote_access_password")

        server_remote_access_details_server = cls(
            state=state,
            vnc_host=vnc_host,
            vnc_password=vnc_password,
            vnc_port=vnc_port,
            remote_access_type=remote_access_type,
            remote_access_enabled=remote_access_enabled,
            remote_access_password=remote_access_password,
        )

        return server_remote_access_details_server
