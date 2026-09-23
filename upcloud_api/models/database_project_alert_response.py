from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseProjectAlertResponse")


@_attrs_define
class DatabaseProjectAlertResponse:
    """Schema for a project alert response

    Attributes:
        create_time (datetime.datetime | Unset): Timestamp when the alert was created Example:
            2025-08-01T10:40:04.140473Z.
        event (str | Unset): Event type for the alert Example: pg-disk-full.
        uuid (UUID | Unset): Unique identifier for the alert Example: 123e4567-e89b-12d3-a456-426614174000.
        title (str | Unset): Optional title of the alert Example: pg-1x2xcpu-2.
        service_type (str | Unset): Service type related to the alert Example: pg.
        severity (str | Unset): Severity of the alert Example: critical.
    """

    create_time: datetime.datetime | Unset = UNSET
    event: str | Unset = UNSET
    uuid: UUID | Unset = UNSET
    title: str | Unset = UNSET
    service_type: str | Unset = UNSET
    severity: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        create_time: str | Unset = UNSET
        if not isinstance(self.create_time, Unset):
            create_time = self.create_time.isoformat()

        event = self.event

        uuid: str | Unset = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        title = self.title

        service_type = self.service_type

        severity = self.severity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if create_time is not UNSET:
            field_dict["create_time"] = create_time
        if event is not UNSET:
            field_dict["event"] = event
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if title is not UNSET:
            field_dict["title"] = title
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

        _uuid = d.pop("uuid", UNSET)
        uuid: UUID | Unset
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = UUID(_uuid)

        title = d.pop("title", UNSET)

        service_type = d.pop("service_type", UNSET)

        severity = d.pop("severity", UNSET)

        database_project_alert_response = cls(
            create_time=create_time,
            event=event,
            uuid=uuid,
            title=title,
            service_type=service_type,
            severity=severity,
        )

        database_project_alert_response.additional_properties = d
        return database_project_alert_response

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
