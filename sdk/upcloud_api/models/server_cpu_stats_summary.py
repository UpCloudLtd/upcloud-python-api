from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.server_cpu_stats_summary_variable_item import ServerCpuStatsSummaryVariableItem


T = TypeVar("T", bound="ServerCpuStatsSummary")


@_attrs_define
class ServerCpuStatsSummary:
    """Summarized CPU statistics values.

    Example:
        {'variable': [{'average': '12 %', 'current': '8 %', 'maximum': '37 %', 'title': 'CPU usage %', 'total': '51
            seconds'}]}

    Attributes:
        variable (list[ServerCpuStatsSummaryVariableItem]):
    """

    variable: list[ServerCpuStatsSummaryVariableItem]

    def to_dict(self) -> dict[str, Any]:
        variable = []
        for variable_item_data in self.variable:
            variable_item = variable_item_data.to_dict()
            variable.append(variable_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "variable": variable,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_cpu_stats_summary_variable_item import ServerCpuStatsSummaryVariableItem  # noqa: PLC0415

        d = dict(src_dict)
        variable = []
        _variable = d.pop("variable")
        for variable_item_data in _variable:
            variable_item = ServerCpuStatsSummaryVariableItem.from_dict(variable_item_data)

            variable.append(variable_item)

        server_cpu_stats_summary = cls(
            variable=variable,
        )

        return server_cpu_stats_summary
