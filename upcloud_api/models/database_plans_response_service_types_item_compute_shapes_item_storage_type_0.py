from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.database_plans_response_service_types_item_compute_shapes_item_storage_type_0_options_item import (
        DatabasePlansResponseServiceTypesItemComputeShapesItemStorageType0OptionsItem,
    )


T = TypeVar("T", bound="DatabasePlansResponseServiceTypesItemComputeShapesItemStorageType0")


@_attrs_define
class DatabasePlansResponseServiceTypesItemComputeShapesItemStorageType0:
    """Storage choices for this compute shape: the distinct base sizes with the total each scales to, plus the shared
    dynamic-storage rules. Null for shapes without customer storage.

        Attributes:
            step_gib (int): Granularity, in GiB, at which dynamic storage can be adjusted.
            dynamic_max_multiplier (int): Maximum multiplier applied to a base size when scaling storage dynamically.
            total_cap_gib (int | None): Hard ceiling on base plus dynamic storage, in GiB, or null when the engine enforces
                no fixed total cap.
            options (list[DatabasePlansResponseServiceTypesItemComputeShapesItemStorageType0OptionsItem]): Base-storage
                options offered for this compute shape.
    """

    step_gib: int
    dynamic_max_multiplier: int
    total_cap_gib: int | None
    options: list[DatabasePlansResponseServiceTypesItemComputeShapesItemStorageType0OptionsItem]

    def to_dict(self) -> dict[str, Any]:
        step_gib = self.step_gib

        dynamic_max_multiplier = self.dynamic_max_multiplier

        total_cap_gib: int | None
        total_cap_gib = self.total_cap_gib

        options = []
        for options_item_data in self.options:
            options_item = options_item_data.to_dict()
            options.append(options_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "step_gib": step_gib,
                "dynamic_max_multiplier": dynamic_max_multiplier,
                "total_cap_gib": total_cap_gib,
                "options": options,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_plans_response_service_types_item_compute_shapes_item_storage_type_0_options_item import (
            DatabasePlansResponseServiceTypesItemComputeShapesItemStorageType0OptionsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        step_gib = d.pop("step_gib")

        dynamic_max_multiplier = d.pop("dynamic_max_multiplier")

        def _parse_total_cap_gib(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        total_cap_gib = _parse_total_cap_gib(d.pop("total_cap_gib"))

        options = []
        _options = d.pop("options")
        for options_item_data in _options:
            options_item = DatabasePlansResponseServiceTypesItemComputeShapesItemStorageType0OptionsItem.from_dict(
                options_item_data
            )

            options.append(options_item)

        database_plans_response_service_types_item_compute_shapes_item_storage_type_0 = cls(
            step_gib=step_gib,
            dynamic_max_multiplier=dynamic_max_multiplier,
            total_cap_gib=total_cap_gib,
            options=options,
        )

        return database_plans_response_service_types_item_compute_shapes_item_storage_type_0
