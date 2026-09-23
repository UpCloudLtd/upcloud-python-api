from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="DatabasePlansResponseServiceTypesItemComputeShapesItemStorageType0OptionsItem")


@_attrs_define
class DatabasePlansResponseServiceTypesItemComputeShapesItemStorageType0OptionsItem:
    """
    Attributes:
        base_gib (int): Base storage size, in GiB.
        max_gib (int): Largest total storage reachable from this base via dynamic storage (base plus multiplier times
            base), capped at total_cap_gib where it applies.
    """

    base_gib: int
    max_gib: int

    def to_dict(self) -> dict[str, Any]:
        base_gib = self.base_gib

        max_gib = self.max_gib

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "base_gib": base_gib,
                "max_gib": max_gib,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        base_gib = d.pop("base_gib")

        max_gib = d.pop("max_gib")

        database_plans_response_service_types_item_compute_shapes_item_storage_type_0_options_item = cls(
            base_gib=base_gib,
            max_gib=max_gib,
        )

        return database_plans_response_service_types_item_compute_shapes_item_storage_type_0_options_item
