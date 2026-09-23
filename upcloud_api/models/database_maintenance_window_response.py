from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_maintenance_pending_updates_response import DatabaseMaintenancePendingUpdatesResponse


T = TypeVar("T", bound="DatabaseMaintenanceWindowResponse")


@_attrs_define
class DatabaseMaintenanceWindowResponse:
    """Schema for a maintenance window response.

    Attributes:
        dow (str | Unset): Day of the week when maintenance occurs (e.g., Monday, Tuesday).
        time (str | Unset): Time of day when maintenance should start (e.g., HH:MM:SS format).
        pending_updates (list[DatabaseMaintenancePendingUpdatesResponse] | Unset): List of updates pending during this
            maintenance window.
    """

    dow: str | Unset = UNSET
    time: str | Unset = UNSET
    pending_updates: list[DatabaseMaintenancePendingUpdatesResponse] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dow = self.dow

        time = self.time

        pending_updates: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pending_updates, Unset):
            pending_updates = []
            for pending_updates_item_data in self.pending_updates:
                pending_updates_item = pending_updates_item_data.to_dict()
                pending_updates.append(pending_updates_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dow is not UNSET:
            field_dict["dow"] = dow
        if time is not UNSET:
            field_dict["time"] = time
        if pending_updates is not UNSET:
            field_dict["pending_updates"] = pending_updates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_maintenance_pending_updates_response import (
            DatabaseMaintenancePendingUpdatesResponse,  # noqa: PLC0415
        )

        d = dict(src_dict)
        dow = d.pop("dow", UNSET)

        time = d.pop("time", UNSET)

        _pending_updates = d.pop("pending_updates", UNSET)
        pending_updates: list[DatabaseMaintenancePendingUpdatesResponse] | Unset = UNSET
        if _pending_updates is not UNSET:
            pending_updates = []
            for pending_updates_item_data in _pending_updates:
                pending_updates_item = DatabaseMaintenancePendingUpdatesResponse.from_dict(pending_updates_item_data)

                pending_updates.append(pending_updates_item)

        database_maintenance_window_response = cls(
            dow=dow,
            time=time,
            pending_updates=pending_updates,
        )

        database_maintenance_window_response.additional_properties = d
        return database_maintenance_window_response

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
