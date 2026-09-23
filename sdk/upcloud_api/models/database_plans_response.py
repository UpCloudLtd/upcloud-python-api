from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.database_plans_response_service_types_item import DatabasePlansResponseServiceTypesItem


T = TypeVar("T", bound="DatabasePlansResponse")


@_attrs_define
class DatabasePlansResponse:
    """Lists available componentised database plans.

    Attributes:
        service_types (list[DatabasePlansResponseServiceTypesItem]): Available service types that offer componentised
            plans.
    """

    service_types: list[DatabasePlansResponseServiceTypesItem]

    def to_dict(self) -> dict[str, Any]:
        service_types = []
        for service_types_item_data in self.service_types:
            service_types_item = service_types_item_data.to_dict()
            service_types.append(service_types_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "service_types": service_types,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_plans_response_service_types_item import (
            DatabasePlansResponseServiceTypesItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        service_types = []
        _service_types = d.pop("service_types")
        for service_types_item_data in _service_types:
            service_types_item = DatabasePlansResponseServiceTypesItem.from_dict(service_types_item_data)

            service_types.append(service_types_item)

        database_plans_response = cls(
            service_types=service_types,
        )

        return database_plans_response
