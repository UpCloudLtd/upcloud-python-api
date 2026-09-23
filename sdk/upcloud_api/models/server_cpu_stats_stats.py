from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.server_cpu_stats_stats_daily import ServerCpuStatsStatsDaily
    from ..models.server_cpu_stats_stats_monthly import ServerCpuStatsStatsMonthly
    from ..models.server_cpu_stats_stats_weekly import ServerCpuStatsStatsWeekly
    from ..models.server_cpu_stats_stats_yearly import ServerCpuStatsStatsYearly


T = TypeVar("T", bound="ServerCpuStatsStats")


@_attrs_define
class ServerCpuStatsStats:
    """
    Attributes:
        daily (ServerCpuStatsStatsDaily | Unset):
        monthly (ServerCpuStatsStatsMonthly | Unset):
        yearly (ServerCpuStatsStatsYearly | Unset):
        weekly (ServerCpuStatsStatsWeekly | Unset):
    """

    daily: ServerCpuStatsStatsDaily | Unset = UNSET
    monthly: ServerCpuStatsStatsMonthly | Unset = UNSET
    yearly: ServerCpuStatsStatsYearly | Unset = UNSET
    weekly: ServerCpuStatsStatsWeekly | Unset = UNSET

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
        from ..models.server_cpu_stats_stats_daily import ServerCpuStatsStatsDaily  # noqa: PLC0415
        from ..models.server_cpu_stats_stats_monthly import ServerCpuStatsStatsMonthly  # noqa: PLC0415
        from ..models.server_cpu_stats_stats_weekly import ServerCpuStatsStatsWeekly  # noqa: PLC0415
        from ..models.server_cpu_stats_stats_yearly import ServerCpuStatsStatsYearly  # noqa: PLC0415

        d = dict(src_dict)
        _daily = d.pop("daily", UNSET)
        daily: ServerCpuStatsStatsDaily | Unset
        if isinstance(_daily, Unset):
            daily = UNSET
        else:
            daily = ServerCpuStatsStatsDaily.from_dict(_daily)

        _monthly = d.pop("monthly", UNSET)
        monthly: ServerCpuStatsStatsMonthly | Unset
        if isinstance(_monthly, Unset):
            monthly = UNSET
        else:
            monthly = ServerCpuStatsStatsMonthly.from_dict(_monthly)

        _yearly = d.pop("yearly", UNSET)
        yearly: ServerCpuStatsStatsYearly | Unset
        if isinstance(_yearly, Unset):
            yearly = UNSET
        else:
            yearly = ServerCpuStatsStatsYearly.from_dict(_yearly)

        _weekly = d.pop("weekly", UNSET)
        weekly: ServerCpuStatsStatsWeekly | Unset
        if isinstance(_weekly, Unset):
            weekly = UNSET
        else:
            weekly = ServerCpuStatsStatsWeekly.from_dict(_weekly)

        server_cpu_stats_stats = cls(
            daily=daily,
            monthly=monthly,
            yearly=yearly,
            weekly=weekly,
        )

        return server_cpu_stats_stats
