from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseMaintenancePendingUpdatesResponse")


@_attrs_define
class DatabaseMaintenancePendingUpdatesResponse:
    """Response schema for pending maintenance updates.

    Attributes:
        deadline (datetime.datetime | Unset): The deadline by which the update must be applied Example:
            2022-01-21T12:21:00Z.
        description (str | Unset): A description of the pending update Example: description related to the update.
        start_after (datetime.datetime | Unset): The earliest time after which the update can start Example:
            2022-01-21T12:21:00Z.
        start_at (datetime.datetime | Unset): The exact scheduled start time for the update Example:
            2022-10-21T12:21:00Z.
    """

    deadline: datetime.datetime | Unset = UNSET
    description: str | Unset = UNSET
    start_after: datetime.datetime | Unset = UNSET
    start_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deadline: str | Unset = UNSET
        if not isinstance(self.deadline, Unset):
            deadline = self.deadline.isoformat()

        description = self.description

        start_after: str | Unset = UNSET
        if not isinstance(self.start_after, Unset):
            start_after = self.start_after.isoformat()

        start_at: str | Unset = UNSET
        if not isinstance(self.start_at, Unset):
            start_at = self.start_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if deadline is not UNSET:
            field_dict["deadline"] = deadline
        if description is not UNSET:
            field_dict["description"] = description
        if start_after is not UNSET:
            field_dict["start_after"] = start_after
        if start_at is not UNSET:
            field_dict["start_at"] = start_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _deadline = d.pop("deadline", UNSET)
        deadline: datetime.datetime | Unset
        if isinstance(_deadline, Unset):
            deadline = UNSET
        else:
            deadline = datetime.datetime.fromisoformat(_deadline)

        description = d.pop("description", UNSET)

        _start_after = d.pop("start_after", UNSET)
        start_after: datetime.datetime | Unset
        if isinstance(_start_after, Unset):
            start_after = UNSET
        else:
            start_after = datetime.datetime.fromisoformat(_start_after)

        _start_at = d.pop("start_at", UNSET)
        start_at: datetime.datetime | Unset
        if isinstance(_start_at, Unset):
            start_at = UNSET
        else:
            start_at = datetime.datetime.fromisoformat(_start_at)

        database_maintenance_pending_updates_response = cls(
            deadline=deadline,
            description=description,
            start_after=start_after,
            start_at=start_at,
        )

        database_maintenance_pending_updates_response.additional_properties = d
        return database_maintenance_pending_updates_response

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
