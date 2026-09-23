from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseServiceAlertResponse")


@_attrs_define
class DatabaseServiceAlertResponse:
    """Schema for a service alert

    Attributes:
        create_time (datetime.datetime | Unset): The time when the alert was created. Example: 2023-10-05T14:48:00Z.
        event (str | Unset): A brief description of the alert event. Example: user_alert_os_too_many_shards..
        service_type (str | Unset): The type of service associated with the alert. Example: opensearch.
        severity (str | Unset): The severity level of the alert. Example: warning.
    """

    create_time: datetime.datetime | Unset = UNSET
    event: str | Unset = UNSET
    service_type: str | Unset = UNSET
    severity: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        create_time: str | Unset = UNSET
        if not isinstance(self.create_time, Unset):
            create_time = self.create_time.isoformat()

        event = self.event

        service_type = self.service_type

        severity = self.severity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if create_time is not UNSET:
            field_dict["create_time"] = create_time
        if event is not UNSET:
            field_dict["event"] = event
        if service_type is not UNSET:
            field_dict["service_type"] = service_type
        if severity is not UNSET:
            field_dict["severity"] = severity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _create_time = d.pop("create_time", UNSET)
        create_time: datetime.datetime | Unset
        if isinstance(_create_time, Unset):
            create_time = UNSET
        else:
            create_time = datetime.datetime.fromisoformat(_create_time)

        event = d.pop("event", UNSET)

        service_type = d.pop("service_type", UNSET)

        severity = d.pop("severity", UNSET)

        database_service_alert_response = cls(
            create_time=create_time,
            event=event,
            service_type=service_type,
            severity=severity,
        )

        database_service_alert_response.additional_properties = d
        return database_service_alert_response

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
