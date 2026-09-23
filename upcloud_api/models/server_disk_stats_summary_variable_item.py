from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.server_disk_stats_summary_variable_item_title import ServerDiskStatsSummaryVariableItemTitle

T = TypeVar("T", bound="ServerDiskStatsSummaryVariableItem")


@_attrs_define
class ServerDiskStatsSummaryVariableItem:
    """
    Attributes:
        average (str): Average transfer rate or request rate during the period.
        current (str): Most recent transfer rate or request rate.
        title (ServerDiskStatsSummaryVariableItemTitle):
        maximum (str): Maximum transfer rate or request rate during the period.
        total (str): Total transferred data or I/O requests during the period.
    """

    average: str
    current: str
    title: ServerDiskStatsSummaryVariableItemTitle
    maximum: str
    total: str

    def to_dict(self) -> dict[str, Any]:
        average = self.average

        current = self.current

        title = self.title.value

        maximum = self.maximum

        total = self.total

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "average": average,
                "current": current,
                "title": title,
                "maximum": maximum,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        average = d.pop("average")

        current = d.pop("current")

        title = ServerDiskStatsSummaryVariableItemTitle(d.pop("title"))

        maximum = d.pop("maximum")

        total = d.pop("total")

        server_disk_stats_summary_variable_item = cls(
            average=average,
            current=current,
            title=title,
            maximum=maximum,
            total=total,
        )

        return server_disk_stats_summary_variable_item
