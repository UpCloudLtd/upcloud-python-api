from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="ServerCpuStatsSummaryVariableItem")


@_attrs_define
class ServerCpuStatsSummaryVariableItem:
    """
    Attributes:
        average (str): Average CPU usage during the period.
        current (str): Most recent CPU usage.
        title (Literal['CPU usage %']):
        maximum (str): Maximum CPU usage during the period.
        total (str): Total CPU time consumed during the period.
    """

    average: str
    current: str
    title: Literal["CPU usage %"]
    maximum: str
    total: str

    def to_dict(self) -> dict[str, Any]:
        average = self.average

        current = self.current

        title = self.title

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

        title = cast(Literal["CPU usage %"], d.pop("title"))
        if title != "CPU usage %":
            raise ValueError(f"title must match const 'CPU usage %', got '{title}'")

        maximum = d.pop("maximum")

        total = d.pop("total")

        server_cpu_stats_summary_variable_item = cls(
            average=average,
            current=current,
            title=title,
            maximum=maximum,
            total=total,
        )

        return server_cpu_stats_summary_variable_item
