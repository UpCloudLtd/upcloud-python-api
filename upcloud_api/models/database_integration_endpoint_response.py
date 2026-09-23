from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_integration_endpoint_response_properties import DatabaseIntegrationEndpointResponseProperties


T = TypeVar("T", bound="DatabaseIntegrationEndpointResponse")


@_attrs_define
class DatabaseIntegrationEndpointResponse:
    """Schema for an integration endpoint response.

    Attributes:
        uuid (UUID | Unset): The universally unique identifier (UUID) of the integration endpoint. Example:
            123e4567-e89b-12d3-a456-426614174000.
        name (str | Unset): The name of the integration endpoint. Example: rsyslog.
        type_ (str | Unset): The type of the integration endpoint. Example: rsyslog.
        properties (DatabaseIntegrationEndpointResponseProperties | Unset): A key-value map of properties specific to
            the integration endpoint type.
    """

    uuid: UUID | Unset = UNSET
    name: str | Unset = UNSET
    type_: str | Unset = UNSET
    properties: DatabaseIntegrationEndpointResponseProperties | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid: str | Unset = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        name = self.name

        type_ = self.type_

        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_integration_endpoint_response_properties import (
            DatabaseIntegrationEndpointResponseProperties,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _uuid = d.pop("uuid", UNSET)
        uuid: UUID | Unset
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = UUID(_uuid)

        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        _properties = d.pop("properties", UNSET)
        properties: DatabaseIntegrationEndpointResponseProperties | Unset
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = DatabaseIntegrationEndpointResponseProperties.from_dict(_properties)

        database_integration_endpoint_response = cls(
            uuid=uuid,
            name=name,
            type_=type_,
            properties=properties,
        )

        database_integration_endpoint_response.additional_properties = d
        return database_integration_endpoint_response

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
