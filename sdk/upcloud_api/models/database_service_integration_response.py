from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_integration_node_state_response import DatabaseIntegrationNodeStateResponse
    from ..models.database_service_integration_response_properties import DatabaseServiceIntegrationResponseProperties


T = TypeVar("T", bound="DatabaseServiceIntegrationResponse")


@_attrs_define
class DatabaseServiceIntegrationResponse:
    """Schema for a service integration response.

    Attributes:
        uuid (UUID | Unset): The UUID of the service integration. Example: 123e4567-e89b-12d3-a456-426614174000.
        type_ (str | Unset): The type of service integration. Example: rsyslog.
        source_name (str | Unset): The name of the source service. Example: my-database.
        source_uuid (UUID | Unset): The UUID of the source service. Example: 123e4567-e89b-12d3-a456-426614174000.
        destination_name (str | Unset): The name of the destination service. Example: my-rsyslog-server.
        destination_uuid (UUID | Unset): The UUID of the destination service. Example:
            123e4567-e89b-12d3-a456-426614174000.
        state (str | Unset): The current state of the service integration. Example: active.
        state_error (list[Any] | Unset): A list of errors related to the service integration state.
        node_states (list[DatabaseIntegrationNodeStateResponse] | Unset): The states of individual nodes in the service
            integration.
        properties (DatabaseServiceIntegrationResponseProperties | Unset): A map of additional properties for the
            service integration.
    """

    uuid: UUID | Unset = UNSET
    type_: str | Unset = UNSET
    source_name: str | Unset = UNSET
    source_uuid: UUID | Unset = UNSET
    destination_name: str | Unset = UNSET
    destination_uuid: UUID | Unset = UNSET
    state: str | Unset = UNSET
    state_error: list[Any] | Unset = UNSET
    node_states: list[DatabaseIntegrationNodeStateResponse] | Unset = UNSET
    properties: DatabaseServiceIntegrationResponseProperties | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid: str | Unset = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        type_ = self.type_

        source_name = self.source_name

        source_uuid: str | Unset = UNSET
        if not isinstance(self.source_uuid, Unset):
            source_uuid = str(self.source_uuid)

        destination_name = self.destination_name

        destination_uuid: str | Unset = UNSET
        if not isinstance(self.destination_uuid, Unset):
            destination_uuid = str(self.destination_uuid)

        state = self.state

        state_error: list[Any] | Unset = UNSET
        if not isinstance(self.state_error, Unset):
            state_error = self.state_error

        node_states: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.node_states, Unset):
            node_states = []
            for node_states_item_data in self.node_states:
                node_states_item = node_states_item_data.to_dict()
                node_states.append(node_states_item)

        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if type_ is not UNSET:
            field_dict["type"] = type_
        if source_name is not UNSET:
            field_dict["source_name"] = source_name
        if source_uuid is not UNSET:
            field_dict["source_uuid"] = source_uuid
        if destination_name is not UNSET:
            field_dict["destination_name"] = destination_name
        if destination_uuid is not UNSET:
            field_dict["destination_uuid"] = destination_uuid
        if state is not UNSET:
            field_dict["state"] = state
        if state_error is not UNSET:
            field_dict["state_error"] = state_error
        if node_states is not UNSET:
            field_dict["node_states"] = node_states
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_integration_node_state_response import (
            DatabaseIntegrationNodeStateResponse,  # noqa: PLC0415
        )
        from ..models.database_service_integration_response_properties import (
            DatabaseServiceIntegrationResponseProperties,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _uuid = d.pop("uuid", UNSET)
        uuid: UUID | Unset
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = UUID(_uuid)

        type_ = d.pop("type", UNSET)

        source_name = d.pop("source_name", UNSET)

        _source_uuid = d.pop("source_uuid", UNSET)
        source_uuid: UUID | Unset
        if isinstance(_source_uuid, Unset):
            source_uuid = UNSET
        else:
            source_uuid = UUID(_source_uuid)

        destination_name = d.pop("destination_name", UNSET)

        _destination_uuid = d.pop("destination_uuid", UNSET)
        destination_uuid: UUID | Unset
        if isinstance(_destination_uuid, Unset):
            destination_uuid = UNSET
        else:
            destination_uuid = UUID(_destination_uuid)

        state = d.pop("state", UNSET)

        state_error = cast(list[Any], d.pop("state_error", UNSET))

        _node_states = d.pop("node_states", UNSET)
        node_states: list[DatabaseIntegrationNodeStateResponse] | Unset = UNSET
        if _node_states is not UNSET:
            node_states = []
            for node_states_item_data in _node_states:
                node_states_item = DatabaseIntegrationNodeStateResponse.from_dict(node_states_item_data)

                node_states.append(node_states_item)

        _properties = d.pop("properties", UNSET)
        properties: DatabaseServiceIntegrationResponseProperties | Unset
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = DatabaseServiceIntegrationResponseProperties.from_dict(_properties)

        database_service_integration_response = cls(
            uuid=uuid,
            type_=type_,
            source_name=source_name,
            source_uuid=source_uuid,
            destination_name=destination_name,
            destination_uuid=destination_uuid,
            state=state,
            state_error=state_error,
            node_states=node_states,
            properties=properties,
        )

        database_service_integration_response.additional_properties = d
        return database_service_integration_response

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
