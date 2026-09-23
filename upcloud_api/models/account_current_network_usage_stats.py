from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.account_current_network_usage_stats_current_network_usage import (
        AccountCurrentNetworkUsageStatsCurrentNetworkUsage,
    )


T = TypeVar("T", bound="AccountCurrentNetworkUsageStats")


@_attrs_define
class AccountCurrentNetworkUsageStats:
    """
    Attributes:
        current_network_usage (AccountCurrentNetworkUsageStatsCurrentNetworkUsage):
    """

    current_network_usage: AccountCurrentNetworkUsageStatsCurrentNetworkUsage

    def to_dict(self) -> dict[str, Any]:
        current_network_usage = self.current_network_usage.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "current_network_usage": current_network_usage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_current_network_usage_stats_current_network_usage import (
            AccountCurrentNetworkUsageStatsCurrentNetworkUsage,  # noqa: PLC0415
        )

        d = dict(src_dict)
        current_network_usage = AccountCurrentNetworkUsageStatsCurrentNetworkUsage.from_dict(
            d.pop("current_network_usage")
        )

        account_current_network_usage_stats = cls(
            current_network_usage=current_network_usage,
        )

        return account_current_network_usage_stats
