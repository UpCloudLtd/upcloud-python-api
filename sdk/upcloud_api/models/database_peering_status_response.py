from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabasePeeringStatusResponse")


@_attrs_define
class DatabasePeeringStatusResponse:
    """Schema for peering status response.

    Attributes:
        create_time (datetime.datetime | Unset): The time when the peering status was created. Example:
            2023-10-05T14:48:00.000Z.
        update_time (datetime.datetime | Unset): The time when the peering status was last updated. Example:
            2023-10-05T14:48:00.000Z.
        network_peer (UUID | Unset): The UUID of the network peer. Example: 03196597-b972-4815-ba3a-85bb18365ced.
        state (str | Unset): The current state of the peering connection. Example: active.
        state_info (str | Unset): Additional information about the current state of the peering connection. Example: The
            peering is in active state..
    """

    create_time: datetime.datetime | Unset = UNSET
    update_time: datetime.datetime | Unset = UNSET
    network_peer: UUID | Unset = UNSET
    state: str | Unset = UNSET
    state_info: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        create_time: str | Unset = UNSET
        if not isinstance(self.create_time, Unset):
            create_time = self.create_time.isoformat()

        update_time: str | Unset = UNSET
        if not isinstance(self.update_time, Unset):
            update_time = self.update_time.isoformat()

        network_peer: str | Unset = UNSET
        if not isinstance(self.network_peer, Unset):
            network_peer = str(self.network_peer)

        state = self.state

        state_info = self.state_info

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if create_time is not UNSET:
            field_dict["create_time"] = create_time
        if update_time is not UNSET:
            field_dict["update_time"] = update_time
        if network_peer is not UNSET:
            field_dict["network_peer"] = network_peer
        if state is not UNSET:
            field_dict["state"] = state
        if state_info is not UNSET:
            field_dict["state_info"] = state_info

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

        _update_time = d.pop("update_time", UNSET)
        update_time: datetime.datetime | Unset
        if isinstance(_update_time, Unset):
            update_time = UNSET
        else:
            update_time = datetime.datetime.fromisoformat(_update_time)

        _network_peer = d.pop("network_peer", UNSET)
        network_peer: UUID | Unset
        if isinstance(_network_peer, Unset):
            network_peer = UNSET
        else:
            network_peer = UUID(_network_peer)

        state = d.pop("state", UNSET)

        state_info = d.pop("state_info", UNSET)

        database_peering_status_response = cls(
            create_time=create_time,
            update_time=update_time,
            network_peer=network_peer,
            state=state,
            state_info=state_info,
        )

        database_peering_status_response.additional_properties = d
        return database_peering_status_response

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
