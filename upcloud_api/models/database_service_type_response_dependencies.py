from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.database_dependency_response import DatabaseDependencyResponse


T = TypeVar("T", bound="DatabaseServiceTypeResponseDependencies")


@_attrs_define
class DatabaseServiceTypeResponseDependencies:
    additional_properties: dict[str, DatabaseDependencyResponse] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_dependency_response import DatabaseDependencyResponse  # noqa: PLC0415

        d = dict(src_dict)
        database_service_type_response_dependencies = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = DatabaseDependencyResponse.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        database_service_type_response_dependencies.additional_properties = additional_properties
        return database_service_type_response_dependencies

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> DatabaseDependencyResponse:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: DatabaseDependencyResponse) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
