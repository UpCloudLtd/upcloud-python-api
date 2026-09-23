from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.server_disk_stats_stats_daily import ServerDiskStatsStatsDaily
    from ..models.server_disk_stats_stats_monthly import ServerDiskStatsStatsMonthly
    from ..models.server_disk_stats_stats_weekly import ServerDiskStatsStatsWeekly
    from ..models.server_disk_stats_stats_yearly import ServerDiskStatsStatsYearly


T = TypeVar("T", bound="ServerDiskStatsStats")


@_attrs_define
class ServerDiskStatsStats:
    """
    Attributes:
        daily (ServerDiskStatsStatsDaily | Unset):
        monthly (ServerDiskStatsStatsMonthly | Unset):
        yearly (ServerDiskStatsStatsYearly | Unset):
        weekly (ServerDiskStatsStatsWeekly | Unset):
    """

    daily: ServerDiskStatsStatsDaily | Unset = UNSET
    monthly: ServerDiskStatsStatsMonthly | Unset = UNSET
    yearly: ServerDiskStatsStatsYearly | Unset = UNSET
    weekly: ServerDiskStatsStatsWeekly | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        daily: dict[str, Any] | Unset = UNSET
        if not isinstance(self.daily, Unset):
            daily = self.daily.to_dict()

        monthly: dict[str, Any] | Unset = UNSET
        if not isinstance(self.monthly, Unset):
            monthly = self.monthly.to_dict()

        yearly: dict[str, Any] | Unset = UNSET
        if not isinstance(self.yearly, Unset):
            yearly = self.yearly.to_dict()

        weekly: dict[str, Any] | Unset = UNSET
        if not isinstance(self.weekly, Unset):
            weekly = self.weekly.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if daily is not UNSET:
            field_dict["daily"] = daily
        if monthly is not UNSET:
            field_dict["monthly"] = monthly
        if yearly is not UNSET:
            field_dict["yearly"] = yearly
        if weekly is not UNSET:
            field_dict["weekly"] = weekly

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_disk_stats_stats_daily import ServerDiskStatsStatsDaily  # noqa: PLC0415
        from ..models.server_disk_stats_stats_monthly import ServerDiskStatsStatsMonthly  # noqa: PLC0415
        from ..models.server_disk_stats_stats_weekly import ServerDiskStatsStatsWeekly  # noqa: PLC0415
        from ..models.server_disk_stats_stats_yearly import ServerDiskStatsStatsYearly  # noqa: PLC0415

        d = dict(src_dict)
        _daily = d.pop("daily", UNSET)
        daily: ServerDiskStatsStatsDaily | Unset
        if isinstance(_daily, Unset):
            daily = UNSET
        else:
            daily = ServerDiskStatsStatsDaily.from_dict(_daily)

        _monthly = d.pop("monthly", UNSET)
        monthly: ServerDiskStatsStatsMonthly | Unset
        if isinstance(_monthly, Unset):
            monthly = UNSET
        else:
            monthly = ServerDiskStatsStatsMonthly.from_dict(_monthly)

        _yearly = d.pop("yearly", UNSET)
        yearly: ServerDiskStatsStatsYearly | Unset
        if isinstance(_yearly, Unset):
            yearly = UNSET
        else:
            yearly = ServerDiskStatsStatsYearly.from_dict(_yearly)

        _weekly = d.pop("weekly", UNSET)
        weekly: ServerDiskStatsStatsWeekly | Unset
        if isinstance(_weekly, Unset):
            weekly = UNSET
        else:
            weekly = ServerDiskStatsStatsWeekly.from_dict(_weekly)

        server_disk_stats_stats = cls(
            daily=daily,
            monthly=monthly,
            yearly=yearly,
            weekly=weekly,
        )

        return server_disk_stats_stats
