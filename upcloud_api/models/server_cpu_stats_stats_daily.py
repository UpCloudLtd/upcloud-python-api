from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.server_cpu_stats_summary import ServerCpuStatsSummary


T = TypeVar("T", bound="ServerCpuStatsStatsDaily")


@_attrs_define
class ServerCpuStatsStatsDaily:
    """
    Attributes:
        summary (ServerCpuStatsSummary): Summarized CPU statistics values. Example: {'variable': [{'average': '12 %',
            'current': '8 %', 'maximum': '37 %', 'title': 'CPU usage %', 'total': '51 seconds'}]}.
    """

    summary: ServerCpuStatsSummary
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        summary = self.summary.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "summary": summary,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_cpu_stats_summary import ServerCpuStatsSummary  # noqa: PLC0415

        d = dict(src_dict)
        summary = ServerCpuStatsSummary.from_dict(d.pop("summary"))

        server_cpu_stats_stats_daily = cls(
            summary=summary,
        )

        server_cpu_stats_stats_daily.additional_properties = d
        return server_cpu_stats_stats_daily

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
