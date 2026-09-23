from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.account_network_usage_stats_stat_item import AccountNetworkUsageStatsStatItem


T = TypeVar("T", bound="AccountNetworkUsageStats")


@_attrs_define
class AccountNetworkUsageStats:
    """
    Attributes:
        stat (list[AccountNetworkUsageStatsStatItem]):
    """

    stat: list[AccountNetworkUsageStatsStatItem]

    def to_dict(self) -> dict[str, Any]:
        stat = []
        for stat_item_data in self.stat:
            stat_item = stat_item_data.to_dict()
            stat.append(stat_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "stat": stat,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_network_usage_stats_stat_item import AccountNetworkUsageStatsStatItem  # noqa: PLC0415

        d = dict(src_dict)
        stat = []
        _stat = d.pop("stat")
        for stat_item_data in _stat:
            stat_item = AccountNetworkUsageStatsStatItem.from_dict(stat_item_data)

            stat.append(stat_item)

        account_network_usage_stats = cls(
            stat=stat,
        )

        return account_network_usage_stats
