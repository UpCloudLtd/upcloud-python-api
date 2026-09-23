from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="AccountCurrentNetworkUsageStatsCurrentNetworkUsage")


@_attrs_define
class AccountCurrentNetworkUsageStatsCurrentNetworkUsage:
    """
    Attributes:
        updated (datetime.datetime): Datetime in RFC 3339 format
        accumulated_quota_bytes (int):
        total_sent_bytes (int):
        hourly_quota_increase_bytes (int):
        projected_monthly_quota_bytes (int):
    """

    updated: datetime.datetime
    accumulated_quota_bytes: int
    total_sent_bytes: int
    hourly_quota_increase_bytes: int
    projected_monthly_quota_bytes: int

    def to_dict(self) -> dict[str, Any]:
        updated = self.updated.isoformat()

        accumulated_quota_bytes = self.accumulated_quota_bytes

        total_sent_bytes = self.total_sent_bytes

        hourly_quota_increase_bytes = self.hourly_quota_increase_bytes

        projected_monthly_quota_bytes = self.projected_monthly_quota_bytes

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "updated": updated,
                "accumulated_quota_bytes": accumulated_quota_bytes,
                "total_sent_bytes": total_sent_bytes,
                "hourly_quota_increase_bytes": hourly_quota_increase_bytes,
                "projected_monthly_quota_bytes": projected_monthly_quota_bytes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        updated = datetime.datetime.fromisoformat(d.pop("updated"))

        accumulated_quota_bytes = d.pop("accumulated_quota_bytes")

        total_sent_bytes = d.pop("total_sent_bytes")

        hourly_quota_increase_bytes = d.pop("hourly_quota_increase_bytes")

        projected_monthly_quota_bytes = d.pop("projected_monthly_quota_bytes")

        account_current_network_usage_stats_current_network_usage = cls(
            updated=updated,
            accumulated_quota_bytes=accumulated_quota_bytes,
            total_sent_bytes=total_sent_bytes,
            hourly_quota_increase_bytes=hourly_quota_increase_bytes,
            projected_monthly_quota_bytes=projected_monthly_quota_bytes,
        )

        return account_current_network_usage_stats_current_network_usage
