from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.network_peering_state import NetworkPeeringState
from ..types import UNSET, Unset

T = TypeVar("T", bound="NetworkDetailsPeeringsPeeringItem")


@_attrs_define
class NetworkDetailsPeeringsPeeringItem:
    """
    Attributes:
        name (str | Unset): Name of a network peering relationship.
        state (NetworkPeeringState | Unset): Current lifecycle state of a network peering.
        uuid (UUID | Unset): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
    """

    name: str | Unset = UNSET
    state: NetworkPeeringState | Unset = UNSET
    uuid: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        uuid: str | Unset = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if state is not UNSET:
            field_dict["state"] = state
        if uuid is not UNSET:
            field_dict["uuid"] = uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _state = d.pop("state", UNSET)
        state: NetworkPeeringState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = NetworkPeeringState(_state)

        _uuid = d.pop("uuid", UNSET)
        uuid: UUID | Unset
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = UUID(_uuid)

        network_details_peerings_peering_item = cls(
            name=name,
            state=state,
            uuid=uuid,
        )

        network_details_peerings_peering_item.additional_properties = d
        return network_details_peerings_peering_item

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
