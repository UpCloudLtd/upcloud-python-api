from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_service_plan_response import DatabaseServicePlanResponse
    from ..models.database_service_type_response_dependencies import DatabaseServiceTypeResponseDependencies
    from ..models.database_service_type_response_properties import DatabaseServiceTypeResponseProperties


T = TypeVar("T", bound="DatabaseServiceTypeResponse")


@_attrs_define
class DatabaseServiceTypeResponse:
    """Response schema for available service types

    Attributes:
        name (str | Unset): The name of the service type Example: postgresql.
        description (str | Unset): The  description of the service type Example: PostgreSQL - Object-Relational Database
            Management System.
        latest_available_version (str | Unset): The latest available version of the service type Example: 18.1.
        service_plans (list[DatabaseServicePlanResponse] | Unset):
        properties (DatabaseServiceTypeResponseProperties | Unset):
        dependencies (DatabaseServiceTypeResponseDependencies | Unset):
    """

    name: str | Unset = UNSET
    description: str | Unset = UNSET
    latest_available_version: str | Unset = UNSET
    service_plans: list[DatabaseServicePlanResponse] | Unset = UNSET
    properties: DatabaseServiceTypeResponseProperties | Unset = UNSET
    dependencies: DatabaseServiceTypeResponseDependencies | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        latest_available_version = self.latest_available_version

        service_plans: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.service_plans, Unset):
            service_plans = []
            for service_plans_item_data in self.service_plans:
                service_plans_item = service_plans_item_data.to_dict()
                service_plans.append(service_plans_item)

        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        dependencies: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dependencies, Unset):
            dependencies = self.dependencies.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if latest_available_version is not UNSET:
            field_dict["latest_available_version"] = latest_available_version
        if service_plans is not UNSET:
            field_dict["service_plans"] = service_plans
        if properties is not UNSET:
            field_dict["properties"] = properties
        if dependencies is not UNSET:
            field_dict["dependencies"] = dependencies

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_service_plan_response import DatabaseServicePlanResponse  # noqa: PLC0415
        from ..models.database_service_type_response_dependencies import (
            DatabaseServiceTypeResponseDependencies,  # noqa: PLC0415
        )
        from ..models.database_service_type_response_properties import (
            DatabaseServiceTypeResponseProperties,  # noqa: PLC0415
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        latest_available_version = d.pop("latest_available_version", UNSET)

        _service_plans = d.pop("service_plans", UNSET)
        service_plans: list[DatabaseServicePlanResponse] | Unset = UNSET
        if _service_plans is not UNSET:
            service_plans = []
            for service_plans_item_data in _service_plans:
                service_plans_item = DatabaseServicePlanResponse.from_dict(service_plans_item_data)

                service_plans.append(service_plans_item)

        _properties = d.pop("properties", UNSET)
        properties: DatabaseServiceTypeResponseProperties | Unset
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = DatabaseServiceTypeResponseProperties.from_dict(_properties)

        _dependencies = d.pop("dependencies", UNSET)
        dependencies: DatabaseServiceTypeResponseDependencies | Unset
        if isinstance(_dependencies, Unset):
            dependencies = UNSET
        else:
            dependencies = DatabaseServiceTypeResponseDependencies.from_dict(_dependencies)

        database_service_type_response = cls(
            name=name,
            description=description,
            latest_available_version=latest_available_version,
            service_plans=service_plans,
            properties=properties,
            dependencies=dependencies,
        )

        database_service_type_response.additional_properties = d
        return database_service_type_response

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
