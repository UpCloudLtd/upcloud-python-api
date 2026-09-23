from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.server_network_stats_stats import ServerNetworkStatsStats


T = TypeVar("T", bound="ServerNetworkStats")


@_attrs_define
class ServerNetworkStats:
    """Aggregate inbound and outbound network statistics grouped by period

    Example:
        {'stats': {'daily': {'summary': {'variable': [{'average': '12 Mbps', 'current': '8.5 Mbps', 'maximum': '24
            Mbps', 'title': 'In', 'total': '8.0 GiB'}]}}}}

    Attributes:
        stats (ServerNetworkStatsStats):
    """

    stats: ServerNetworkStatsStats

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
        from ..models.server_network_stats_stats import ServerNetworkStatsStats  # noqa: PLC0415

        d = dict(src_dict)
        stats = ServerNetworkStatsStats.from_dict(d.pop("stats"))

        server_network_stats = cls(
            stats=stats,
        )

        return server_network_stats
