from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_metrics_data_response import DatabaseMetricsDataResponse
    from ..models.database_metrics_item_response_hints import DatabaseMetricsItemResponseHints


T = TypeVar("T", bound="DatabaseMetricsItemResponse")


@_attrs_define
class DatabaseMetricsItemResponse:
    """Schema for a single metrics item response.

    Attributes:
        data (DatabaseMetricsDataResponse | Unset): Schema for metrics data response.
        hints (DatabaseMetricsItemResponseHints | Unset): Additional hints or metadata about the metric data.
    """

    data: DatabaseMetricsDataResponse | Unset = UNSET
    hints: DatabaseMetricsItemResponseHints | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        hints: dict[str, Any] | Unset = UNSET
        if not isinstance(self.hints, Unset):
            hints = self.hints.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if hints is not UNSET:
            field_dict["hints"] = hints

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_metrics_data_response import DatabaseMetricsDataResponse  # noqa: PLC0415
        from ..models.database_metrics_item_response_hints import DatabaseMetricsItemResponseHints  # noqa: PLC0415

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: DatabaseMetricsDataResponse | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = DatabaseMetricsDataResponse.from_dict(_data)

        _hints = d.pop("hints", UNSET)
        hints: DatabaseMetricsItemResponseHints | Unset
        if isinstance(_hints, Unset):
            hints = UNSET
        else:
            hints = DatabaseMetricsItemResponseHints.from_dict(_hints)

        database_metrics_item_response = cls(
            data=data,
            hints=hints,
        )

        database_metrics_item_response.additional_properties = d
        return database_metrics_item_response

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
