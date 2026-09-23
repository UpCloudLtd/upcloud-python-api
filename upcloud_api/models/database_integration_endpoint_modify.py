from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_integration_endpoint_modify_properties import DatabaseIntegrationEndpointModifyProperties


T = TypeVar("T", bound="DatabaseIntegrationEndpointModify")


@_attrs_define
class DatabaseIntegrationEndpointModify:
    """Schema for modifying an integration endpoint.

    Attributes:
        properties (DatabaseIntegrationEndpointModifyProperties | Unset):  Example: {'server': '3.3.3.3', 'port': 514,
            'tls': True}.
    """

    properties: DatabaseIntegrationEndpointModifyProperties | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_integration_endpoint_modify_properties import (
            DatabaseIntegrationEndpointModifyProperties,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _properties = d.pop("properties", UNSET)
        properties: DatabaseIntegrationEndpointModifyProperties | Unset
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = DatabaseIntegrationEndpointModifyProperties.from_dict(_properties)

        database_integration_endpoint_modify = cls(
            properties=properties,
        )

        return database_integration_endpoint_modify
