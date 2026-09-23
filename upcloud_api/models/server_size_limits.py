from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.server_size_limits_server_size_limits import ServerSizeLimitsServerSizeLimits


T = TypeVar("T", bound="ServerSizeLimits")


@_attrs_define
class ServerSizeLimits:
    """Schema for server size limits

    Example:
        {'server_size_limits': {'core_number_min': 1, 'core_number_max': 64, 'memory_amount_min': 1024,
            'memory_amount_max': 524288, 'memory_amount_step': 1024}}

    Attributes:
        server_size_limits (ServerSizeLimitsServerSizeLimits):  Example: {'core_number_min': 1, 'core_number_max': 64,
            'memory_amount_min': 1024, 'memory_amount_max': 524288, 'memory_amount_step': 1024}.
    """

    server_size_limits: ServerSizeLimitsServerSizeLimits

    def to_dict(self) -> dict[str, Any]:
        server_size_limits = self.server_size_limits.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "server_size_limits": server_size_limits,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_size_limits_server_size_limits import ServerSizeLimitsServerSizeLimits  # noqa: PLC0415

        d = dict(src_dict)
        server_size_limits = ServerSizeLimitsServerSizeLimits.from_dict(d.pop("server_size_limits"))

        server_size_limits = cls(
            server_size_limits=server_size_limits,
        )

        return server_size_limits
