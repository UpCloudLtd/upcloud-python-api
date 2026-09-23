from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseNodeProgressUpdateResponse")


@_attrs_define
class DatabaseNodeProgressUpdateResponse:
    """Schema for node progress update response.

    Attributes:
        completed (bool | Unset): Indicates whether the progress is fully completed. Example: False.
        current (int | Unset): The current progress value. Example: 45.
        max_ (int | Unset): The maximum value for the progress range. Example: 100.
        min_ (int | Unset): The minimum value for the progress range. Example: 0.
        phase (str | Unset): The current node progress. Example: prepare.
        unit (str | Unset): The unit of measurement for the progress values (e.g., percent, MB). Example:
            bytes_uncompressed.
    """

    completed: bool | Unset = UNSET
    current: int | Unset = UNSET
    max_: int | Unset = UNSET
    min_: int | Unset = UNSET
    phase: str | Unset = UNSET
    unit: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        completed = self.completed

        current = self.current

        max_ = self.max_

        min_ = self.min_

        phase = self.phase

        unit = self.unit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if completed is not UNSET:
            field_dict["completed"] = completed
        if current is not UNSET:
            field_dict["current"] = current
        if max_ is not UNSET:
            field_dict["max"] = max_
        if min_ is not UNSET:
            field_dict["min"] = min_
        if phase is not UNSET:
            field_dict["phase"] = phase
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        completed = d.pop("completed", UNSET)

        current = d.pop("current", UNSET)

        max_ = d.pop("max", UNSET)

        min_ = d.pop("min", UNSET)

        phase = d.pop("phase", UNSET)

        unit = d.pop("unit", UNSET)

        database_node_progress_update_response = cls(
            completed=completed,
            current=current,
            max_=max_,
            min_=min_,
            phase=phase,
            unit=unit,
        )

        database_node_progress_update_response.additional_properties = d
        return database_node_progress_update_response

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
