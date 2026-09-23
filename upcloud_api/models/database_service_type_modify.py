from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="DatabaseServiceTypeModify")


@_attrs_define
class DatabaseServiceTypeModify:
    """Schema for modifying the service type

    Attributes:
        target_type (str): Service type
    """

    target_type: str

    def to_dict(self) -> dict[str, Any]:
        target_type = self.target_type

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "target_type": target_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        target_type = d.pop("target_type")

        database_service_type_modify = cls(
            target_type=target_type,
        )

        return database_service_type_modify
