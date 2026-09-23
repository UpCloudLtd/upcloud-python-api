from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.events_event_type import EventsEventType
from ..types import UNSET, Unset

T = TypeVar("T", bound="EventsEventsEventItem")


@_attrs_define
class EventsEventsEventItem:
    """
    Attributes:
        server (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        time (datetime.datetime): Timestamp of when the event occurred
        type_ (EventsEventType): Server event type
        email (str | Unset):
        first_name (str | Unset):
        last_name (str | Unset):
    """

    server: UUID
    time: datetime.datetime
    type_: EventsEventType
    email: str | Unset = UNSET
    first_name: str | Unset = UNSET
    last_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        server = str(self.server)

        time = self.time.isoformat()

        type_ = self.type_.value

        email = self.email

        first_name = self.first_name

        last_name = self.last_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "server": server,
                "time": time,
                "type": type_,
            }
        )
        if email is not UNSET:
            field_dict["email"] = email
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        server = UUID(d.pop("server"))

        time = datetime.datetime.fromisoformat(d.pop("time"))

        type_ = EventsEventType(d.pop("type"))

        email = d.pop("email", UNSET)

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        events_events_event_item = cls(
            server=server,
            time=time,
            type_=type_,
            email=email,
            first_name=first_name,
            last_name=last_name,
        )

        events_events_event_item.additional_properties = d
        return events_events_event_item

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
