from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_metrics_column_header_response import DatabaseMetricsColumnHeaderResponse


T = TypeVar("T", bound="DatabaseMetricsDataResponse")


@_attrs_define
class DatabaseMetricsDataResponse:
    """Schema for metrics data response.

    Attributes:
        cols (list[DatabaseMetricsColumnHeaderResponse] | Unset):
        rows (list[list[Any]] | Unset):
    """

    cols: list[DatabaseMetricsColumnHeaderResponse] | Unset = UNSET
    rows: list[list[Any]] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cols: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.cols, Unset):
            cols = []
            for cols_item_data in self.cols:
                cols_item = cols_item_data.to_dict()
                cols.append(cols_item)

        rows: list[list[Any]] | Unset = UNSET
        if not isinstance(self.rows, Unset):
            rows = []
            for rows_item_data in self.rows:
                rows_item = rows_item_data

                rows.append(rows_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cols is not UNSET:
            field_dict["cols"] = cols
        if rows is not UNSET:
            field_dict["rows"] = rows

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_metrics_column_header_response import (
            DatabaseMetricsColumnHeaderResponse,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _cols = d.pop("cols", UNSET)
        cols: list[DatabaseMetricsColumnHeaderResponse] | Unset = UNSET
        if _cols is not UNSET:
            cols = []
            for cols_item_data in _cols:
                cols_item = DatabaseMetricsColumnHeaderResponse.from_dict(cols_item_data)

                cols.append(cols_item)

        _rows = d.pop("rows", UNSET)
        rows: list[list[Any]] | Unset = UNSET
        if _rows is not UNSET:
            rows = []
            for rows_item_data in _rows:
                rows_item = cast(list[Any], rows_item_data)

                rows.append(rows_item)

        database_metrics_data_response = cls(
            cols=cols,
            rows=rows,
        )

        database_metrics_data_response.additional_properties = d
        return database_metrics_data_response

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
