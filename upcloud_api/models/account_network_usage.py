from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.account_network_usage_stats import AccountNetworkUsageStats


T = TypeVar("T", bound="AccountNetworkUsage")


@_attrs_define
class AccountNetworkUsage:
    """Account network usage and Fair Transfer Policy quota statistics.

    Example:
        {'stats': {'stat': [{'accumulated_quota_bytes': 6352371508013, 'projected_monthly_quota_bytes': 6362243967561,
            'quota_increase_bytes': 9872459548, 'sent_bytes': 1254, 'start_time': '2020-09-30T22:00:00Z',
            'total_sent_bytes': 225149331390}, {'accumulated_quota_bytes': 6362243967561, 'projected_monthly_quota_bytes':
            6362243967561, 'quota_increase_bytes': 9872459548, 'sent_bytes': 1254, 'start_time': '2020-09-30T23:00:00Z',
            'total_sent_bytes': 225149332644}, {'accumulated_quota_bytes': 9872459548, 'projected_monthly_quota_bytes':
            7345109903712, 'quota_increase_bytes': 9872459548, 'sent_bytes': 906, 'start_time': '2020-10-01T00:00:00Z',
            'total_sent_bytes': 906}]}}

    Attributes:
        stats (AccountNetworkUsageStats):
    """

    stats: AccountNetworkUsageStats

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
        from ..models.account_network_usage_stats import AccountNetworkUsageStats  # noqa: PLC0415

        d = dict(src_dict)
        stats = AccountNetworkUsageStats.from_dict(d.pop("stats"))

        account_network_usage = cls(
            stats=stats,
        )

        return account_network_usage
