from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.server_disk_stats_summary import ServerDiskStatsSummary


T = TypeVar("T", bound="ServerDiskStatsStatsWeekly")


@_attrs_define
class ServerDiskStatsStatsWeekly:
    """
    Attributes:
        summary (ServerDiskStatsSummary): Summarized disk read and write statistics values. Example: {'variable':
            [{'average': '1.5 MiBps', 'current': '2.0 MiBps', 'maximum': '4.0 MiBps', 'title': 'Read', 'total': '8.0
            GiB'}]}.
    """

    summary: ServerDiskStatsSummary
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
        from ..models.server_disk_stats_summary import ServerDiskStatsSummary  # noqa: PLC0415

        d = dict(src_dict)
        summary = ServerDiskStatsSummary.from_dict(d.pop("summary"))

        server_disk_stats_stats_weekly = cls(
            summary=summary,
        )

        server_disk_stats_stats_weekly.additional_properties = d
        return server_disk_stats_stats_weekly

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
