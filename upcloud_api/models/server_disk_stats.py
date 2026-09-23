from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.server_disk_stats_stats import ServerDiskStatsStats


T = TypeVar("T", bound="ServerDiskStats")


@_attrs_define
class ServerDiskStats:
    """Aggregate disk read and write statistics grouped by period

    Example:
        {'stats': {'daily': {'summary': {'variable': [{'average': '1.5 MiBps', 'current': '2.0 MiBps', 'maximum': '4.0
            MiBps', 'title': 'Read', 'total': '8.0 GiB'}]}}}}

    Attributes:
        stats (ServerDiskStatsStats):
    """

    stats: ServerDiskStatsStats

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
        from ..models.server_disk_stats_stats import ServerDiskStatsStats  # noqa: PLC0415

        d = dict(src_dict)
        stats = ServerDiskStatsStats.from_dict(d.pop("stats"))

        server_disk_stats = cls(
            stats=stats,
        )

        return server_disk_stats
