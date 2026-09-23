from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.database_service_integration import DatabaseServiceIntegration
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_service_integration_create_properties import DatabaseServiceIntegrationCreateProperties


T = TypeVar("T", bound="DatabaseServiceIntegrationCreate")


@_attrs_define
class DatabaseServiceIntegrationCreate:
    """Schema for creating a service integration.

    Attributes:
        type_ (DatabaseServiceIntegration): The type of service integration.
        destination_uuid (UUID | Unset): The UUID of the destination where the service integration will send data.
        properties (DatabaseServiceIntegrationCreateProperties | Unset):
    """

    type_: DatabaseServiceIntegration
    destination_uuid: UUID | Unset = UNSET
    properties: DatabaseServiceIntegrationCreateProperties | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        destination_uuid: str | Unset = UNSET
        if not isinstance(self.destination_uuid, Unset):
            destination_uuid = str(self.destination_uuid)

        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
            }
        )
        if destination_uuid is not UNSET:
            field_dict["destination_uuid"] = destination_uuid
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_service_integration_create_properties import (
            DatabaseServiceIntegrationCreateProperties,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = DatabaseServiceIntegration(d.pop("type"))

        _destination_uuid = d.pop("destination_uuid", UNSET)
        destination_uuid: UUID | Unset
        if isinstance(_destination_uuid, Unset):
            destination_uuid = UNSET
        else:
            destination_uuid = UUID(_destination_uuid)

        _properties = d.pop("properties", UNSET)
        properties: DatabaseServiceIntegrationCreateProperties | Unset
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = DatabaseServiceIntegrationCreateProperties.from_dict(_properties)

        database_service_integration_create = cls(
            type_=type_,
            destination_uuid=destination_uuid,
            properties=properties,
        )

        return database_service_integration_create
