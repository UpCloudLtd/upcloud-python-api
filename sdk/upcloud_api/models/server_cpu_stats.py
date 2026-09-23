from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.server_cpu_stats_stats import ServerCpuStatsStats


T = TypeVar("T", bound="ServerCpuStats")


@_attrs_define
class ServerCpuStats:
    """CPU usage statistics grouped by period

    Example:
        {'stats': {'daily': {'summary': {'variable': [{'average': '12 %', 'current': '8 %', 'maximum': '37 %', 'title':
            'CPU usage %', 'total': '51 seconds'}]}}}}

    Attributes:
        stats (ServerCpuStatsStats):
    """

    stats: ServerCpuStatsStats

    def to_dict(self) -> dict[str, Any]:
        stats = self.stats.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "stats": stats,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_cpu_stats_stats import ServerCpuStatsStats  # noqa: PLC0415

        d = dict(src_dict)
        stats = ServerCpuStatsStats.from_dict(d.pop("stats"))

        server_cpu_stats = cls(
            stats=stats,
        )

        return server_cpu_stats
