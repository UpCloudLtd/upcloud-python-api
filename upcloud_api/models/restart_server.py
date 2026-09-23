from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.restart_server_restart_server_type_0 import RestartServerRestartServerType0


T = TypeVar("T", bound="RestartServer")


@_attrs_define
class RestartServer:
    """Restart Cloud Server request

    Example:
        {'restart_server': {'stop_type': 'soft', 'timeout': '60', 'timeout_action': 'destroy'}}

    Attributes:
        restart_server (Any | RestartServerRestartServerType0):
    """

    restart_server: Any | RestartServerRestartServerType0

    def to_dict(self) -> dict[str, Any]:
        from ..models.restart_server_restart_server_type_0 import RestartServerRestartServerType0  # noqa: PLC0415

        restart_server: Any | dict[str, Any]
        if isinstance(self.restart_server, RestartServerRestartServerType0):
            restart_server = self.restart_server.to_dict()
        else:
            restart_server = self.restart_server

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "restart_server": restart_server,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.restart_server_restart_server_type_0 import RestartServerRestartServerType0  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_restart_server(data: object) -> Any | RestartServerRestartServerType0:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                restart_server_type_0 = RestartServerRestartServerType0.from_dict(data)

                return restart_server_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Any | RestartServerRestartServerType0, data)

        restart_server = _parse_restart_server(d.pop("restart_server"))

        restart_server = cls(
            restart_server=restart_server,
        )

        return restart_server
