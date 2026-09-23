from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabasePlanComponentsResponseBackupsFrequent")


@_attrs_define
class DatabasePlanComponentsResponseBackupsFrequent:
    """Frequent backup window, OpenSearch only

    Attributes:
        interval_minutes (int | Unset):  Example: 60.
        retention_days (int | Unset):  Example: 1.
    """

    interval_minutes: int | Unset = UNSET
    retention_days: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interval_minutes = self.interval_minutes

        retention_days = self.retention_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interval_minutes is not UNSET:
            field_dict["interval_minutes"] = interval_minutes
        if retention_days is not UNSET:
            field_dict["retention_days"] = retention_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        interval_minutes = d.pop("interval_minutes", UNSET)

        retention_days = d.pop("retention_days", UNSET)

        database_plan_components_response_backups_frequent = cls(
            interval_minutes=interval_minutes,
            retention_days=retention_days,
        )

        database_plan_components_response_backups_frequent.additional_properties = d
        return database_plan_components_response_backups_frequent

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
