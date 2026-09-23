from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.database_integration_endpoint import DatabaseIntegrationEndpoint
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_integration_endpoint_create_properties import DatabaseIntegrationEndpointCreateProperties


T = TypeVar("T", bound="DatabaseIntegrationEndpointCreate")


@_attrs_define
class DatabaseIntegrationEndpointCreate:
    """Schema for creating an integration endpoint.

    Attributes:
        type_ (DatabaseIntegrationEndpoint): The type of integration endpoint.
        name (str): The name of the integration endpoint.
        properties (DatabaseIntegrationEndpointCreateProperties | Unset): A key-value map of properties specific to the
            integration endpoint type.
    """

    type_: DatabaseIntegrationEndpoint
    name: str
    properties: DatabaseIntegrationEndpointCreateProperties | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        name = self.name

        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "name": name,
            }
        )
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_integration_endpoint_create_properties import (
            DatabaseIntegrationEndpointCreateProperties,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = DatabaseIntegrationEndpoint(d.pop("type"))

        name = d.pop("name")

        _properties = d.pop("properties", UNSET)
        properties: DatabaseIntegrationEndpointCreateProperties | Unset
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = DatabaseIntegrationEndpointCreateProperties.from_dict(_properties)

        database_integration_endpoint_create = cls(
            type_=type_,
            name=name,
            properties=properties,
        )

        return database_integration_endpoint_create
