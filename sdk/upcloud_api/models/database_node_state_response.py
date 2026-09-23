from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_node_progress_update_response import DatabaseNodeProgressUpdateResponse


T = TypeVar("T", bound="DatabaseNodeStateResponse")


@_attrs_define
class DatabaseNodeStateResponse:
    """Schema for the state of a node in a service.

    Attributes:
        name (str | Unset): Name of the node. Example: node-1.
        role (str | Unset): Role of the node in the service. Example: master.
        state (str | Unset): Current state of the node. Example: running.
        progress_updates (list[DatabaseNodeProgressUpdateResponse] | Unset): Response schema for node progress updates
    """

    name: str | Unset = UNSET
    role: str | Unset = UNSET
    state: str | Unset = UNSET
    progress_updates: list[DatabaseNodeProgressUpdateResponse] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        role = self.role

        state = self.state

        progress_updates: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.progress_updates, Unset):
            progress_updates = []
            for componentsschemasdatabase_node_progress_updates_response_item_data in self.progress_updates:
                componentsschemasdatabase_node_progress_updates_response_item = (
                    componentsschemasdatabase_node_progress_updates_response_item_data.to_dict()
                )
                progress_updates.append(componentsschemasdatabase_node_progress_updates_response_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if role is not UNSET:
            field_dict["role"] = role
        if state is not UNSET:
            field_dict["state"] = state
        if progress_updates is not UNSET:
            field_dict["progress_updates"] = progress_updates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_node_progress_update_response import DatabaseNodeProgressUpdateResponse  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        role = d.pop("role", UNSET)

        state = d.pop("state", UNSET)

        _progress_updates = d.pop("progress_updates", UNSET)
        progress_updates: list[DatabaseNodeProgressUpdateResponse] | Unset = UNSET
        if _progress_updates is not UNSET:
            progress_updates = []
            for componentsschemasdatabase_node_progress_updates_response_item_data in _progress_updates:
                componentsschemasdatabase_node_progress_updates_response_item = (
                    DatabaseNodeProgressUpdateResponse.from_dict(
                        componentsschemasdatabase_node_progress_updates_response_item_data
                    )
                )

                progress_updates.append(componentsschemasdatabase_node_progress_updates_response_item)

        database_node_state_response = cls(
            name=name,
            role=role,
            state=state,
            progress_updates=progress_updates,
        )

        database_node_state_response.additional_properties = d
        return database_node_state_response

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
