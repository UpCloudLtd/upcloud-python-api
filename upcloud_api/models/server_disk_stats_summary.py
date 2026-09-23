from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.server_disk_stats_summary_variable_item import ServerDiskStatsSummaryVariableItem


T = TypeVar("T", bound="ServerDiskStatsSummary")


@_attrs_define
class ServerDiskStatsSummary:
    """Summarized disk read and write statistics values.

    Example:
        {'variable': [{'average': '1.5 MiBps', 'current': '2.0 MiBps', 'maximum': '4.0 MiBps', 'title': 'Read', 'total':
            '8.0 GiB'}]}

    Attributes:
        variable (list[ServerDiskStatsSummaryVariableItem]):
    """

    variable: list[ServerDiskStatsSummaryVariableItem]

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
        from ..models.server_disk_stats_summary_variable_item import ServerDiskStatsSummaryVariableItem  # noqa: PLC0415

        d = dict(src_dict)
        variable = []
        _variable = d.pop("variable")
        for variable_item_data in _variable:
            variable_item = ServerDiskStatsSummaryVariableItem.from_dict(variable_item_data)

            variable.append(variable_item)

        server_disk_stats_summary = cls(
            variable=variable,
        )

        return server_disk_stats_summary
