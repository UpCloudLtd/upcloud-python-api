from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.events_events_event_item import EventsEventsEventItem


T = TypeVar("T", bound="EventsEvents")


@_attrs_define
class EventsEvents:
    """
    Attributes:
        event (list[EventsEventsEventItem]): List of events associated with servers
    """

    event: list[EventsEventsEventItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event = []
        for event_item_data in self.event:
            event_item = event_item_data.to_dict()
            event.append(event_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event": event,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.events_events_event_item import EventsEventsEventItem  # noqa: PLC0415

        d = dict(src_dict)
        event = []
        _event = d.pop("event")
        for event_item_data in _event:
            event_item = EventsEventsEventItem.from_dict(event_item_data)

            event.append(event_item)

        events_events = cls(
            event=event,
        )

        events_events.additional_properties = d
        return events_events

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
