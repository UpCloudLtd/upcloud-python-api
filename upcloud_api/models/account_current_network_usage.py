from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.account_current_network_usage_stats import AccountCurrentNetworkUsageStats


T = TypeVar("T", bound="AccountCurrentNetworkUsage")


@_attrs_define
class AccountCurrentNetworkUsage:
    """Current Fair Transfer Policy usage for an account.

    Example:
        {'stats': {'current_network_usage': {'accumulated_quota_bytes': 3546328504778, 'hourly_quota_increase_bytes':
            10577635230, 'projected_monthly_quota_bytes': 7777382596778, 'total_sent_bytes': 13682943146, 'updated':
            '2020-10-15T07:00:00Z'}}}

    Attributes:
        stats (AccountCurrentNetworkUsageStats):
    """

    stats: AccountCurrentNetworkUsageStats

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
        from ..models.account_current_network_usage_stats import AccountCurrentNetworkUsageStats  # noqa: PLC0415

        d = dict(src_dict)
        stats = AccountCurrentNetworkUsageStats.from_dict(d.pop("stats"))

        account_current_network_usage = cls(
            stats=stats,
        )

        return account_current_network_usage
