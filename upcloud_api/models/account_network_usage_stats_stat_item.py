from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="AccountNetworkUsageStatsStatItem")


@_attrs_define
class AccountNetworkUsageStatsStatItem:
    """
    Attributes:
        start_time (datetime.datetime): Datetime in RFC 3339 format
        sent_bytes (int):
        total_sent_bytes (int):
        accumulated_quota_bytes (int):
        projected_monthly_quota_bytes (int):
        quota_increase_bytes (int):
    """

    start_time: datetime.datetime
    sent_bytes: int
    total_sent_bytes: int
    accumulated_quota_bytes: int
    projected_monthly_quota_bytes: int
    quota_increase_bytes: int

    def to_dict(self) -> dict[str, Any]:
        start_time = self.start_time.isoformat()

        sent_bytes = self.sent_bytes

        total_sent_bytes = self.total_sent_bytes

        accumulated_quota_bytes = self.accumulated_quota_bytes

        projected_monthly_quota_bytes = self.projected_monthly_quota_bytes

        quota_increase_bytes = self.quota_increase_bytes

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "start_time": start_time,
                "sent_bytes": sent_bytes,
                "total_sent_bytes": total_sent_bytes,
                "accumulated_quota_bytes": accumulated_quota_bytes,
                "projected_monthly_quota_bytes": projected_monthly_quota_bytes,
                "quota_increase_bytes": quota_increase_bytes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start_time = datetime.datetime.fromisoformat(d.pop("start_time"))

        sent_bytes = d.pop("sent_bytes")

        total_sent_bytes = d.pop("total_sent_bytes")

        accumulated_quota_bytes = d.pop("accumulated_quota_bytes")

        projected_monthly_quota_bytes = d.pop("projected_monthly_quota_bytes")

        quota_increase_bytes = d.pop("quota_increase_bytes")

        account_network_usage_stats_stat_item = cls(
            start_time=start_time,
            sent_bytes=sent_bytes,
            total_sent_bytes=total_sent_bytes,
            accumulated_quota_bytes=accumulated_quota_bytes,
            projected_monthly_quota_bytes=projected_monthly_quota_bytes,
            quota_increase_bytes=quota_increase_bytes,
        )

        return account_network_usage_stats_stat_item
