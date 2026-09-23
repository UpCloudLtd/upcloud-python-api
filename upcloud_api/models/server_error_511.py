from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.server_error_511_error import ServerError511Error


T = TypeVar("T", bound="ServerError511")


@_attrs_define
class ServerError511:
    """Operation failed error

    Example:
        {'error': {'code': 'HOTPLUG_FAILED', 'message': 'The detach failed while the Cloud Server was started. Please
            stop the Cloud Server and try again.'}}

    Attributes:
        error (ServerError511Error):
    """

    error: ServerError511Error

    def to_dict(self) -> dict[str, Any]:
        error = self.error.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "error": error,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_error_511_error import ServerError511Error  # noqa: PLC0415

        d = dict(src_dict)
        error = ServerError511Error.from_dict(d.pop("error"))

        server_error_511 = cls(
            error=error,
        )

        return server_error_511
