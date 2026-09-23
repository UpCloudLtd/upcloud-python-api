from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GatewayMetricsDetailsResponse")


@_attrs_define
class GatewayMetricsDetailsResponse:
    """Response schema for gateway metrics details.

    Attributes:
        name (str | Unset): Name of the gateway
        active_connections (int | Unset): Number of active connections
        created_at (datetime.datetime | Unset): Timestamp of when the metrics was created.
        updated_at (datetime.datetime | Unset): Timestamp of when the metrics was last updated.
        total_accepted_connections (int | Unset): Number of accepted connections
        total_rejected_sessions (int | Unset): Number of rejected sessions
    """

    name: str | Unset = UNSET
    active_connections: int | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    total_accepted_connections: int | Unset = UNSET
    total_rejected_sessions: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        active_connections = self.active_connections

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        total_accepted_connections = self.total_accepted_connections

        total_rejected_sessions = self.total_rejected_sessions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if active_connections is not UNSET:
            field_dict["active_connections"] = active_connections
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if total_accepted_connections is not UNSET:
            field_dict["total_accepted_connections"] = total_accepted_connections
        if total_rejected_sessions is not UNSET:
            field_dict["total_rejected_sessions"] = total_rejected_sessions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        active_connections = d.pop("active_connections", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)

        total_accepted_connections = d.pop("total_accepted_connections", UNSET)

        total_rejected_sessions = d.pop("total_rejected_sessions", UNSET)

        gateway_metrics_details_response = cls(
            name=name,
            active_connections=active_connections,
            created_at=created_at,
            updated_at=updated_at,
            total_accepted_connections=total_accepted_connections,
            total_rejected_sessions=total_rejected_sessions,
        )

        gateway_metrics_details_response.additional_properties = d
        return gateway_metrics_details_response

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
