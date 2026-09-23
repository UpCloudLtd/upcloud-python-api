from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.stop_server_stop_server import StopServerStopServer


T = TypeVar("T", bound="StopServer")


@_attrs_define
class StopServer:
    """Stop Cloud Server request

    Example:
        {'stop_server': {'stop_type': 'soft', 'timeout': '60'}}

    Attributes:
        stop_server (StopServerStopServer):
    """

    stop_server: StopServerStopServer

    def to_dict(self) -> dict[str, Any]:
        stop_server = self.stop_server.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "stop_server": stop_server,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.stop_server_stop_server import StopServerStopServer  # noqa: PLC0415

        d = dict(src_dict)
        stop_server = StopServerStopServer.from_dict(d.pop("stop_server"))

        stop_server = cls(
            stop_server=stop_server,
        )

        return stop_server
