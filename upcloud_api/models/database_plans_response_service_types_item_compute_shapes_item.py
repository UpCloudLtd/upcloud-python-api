from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.database_plans_response_service_types_item_compute_shapes_item_backups_item import (
    DatabasePlansResponseServiceTypesItemComputeShapesItemBackupsItem,
)
from ..models.database_plans_response_service_types_item_compute_shapes_item_family import (
    DatabasePlansResponseServiceTypesItemComputeShapesItemFamily,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_plans_response_service_types_item_compute_shapes_item_storage_type_0 import (
        DatabasePlansResponseServiceTypesItemComputeShapesItemStorageType0,
    )


T = TypeVar("T", bound="DatabasePlansResponseServiceTypesItemComputeShapesItem")


@_attrs_define
class DatabasePlansResponseServiceTypesItemComputeShapesItem:
    """
    Attributes:
        compute (str): Compute shape name, usable as plan_compute in requests.
        family (DatabasePlansResponseServiceTypesItemComputeShapesItemFamily): Compute family.
        cpu (int): CPU cores per node.
        memory_gb (int): Memory per node in GB.
        dynamic_storage_supported (bool): Whether the storage total can be scaled beyond the base storage via dynamic
            storage.
        node_counts (list[int]): Node counts available for this compute shape.
        backups (list[DatabasePlansResponseServiceTypesItemComputeShapesItemBackupsItem] | Unset): Backup tiers
            available for this compute shape. Omitted when the shape exposes no named backup tiers.
        storage (DatabasePlansResponseServiceTypesItemComputeShapesItemStorageType0 | None | Unset): Storage choices for
            this compute shape: the distinct base sizes with the total each scales to, plus the shared dynamic-storage
            rules. Null for shapes without customer storage.
    """

    compute: str
    family: DatabasePlansResponseServiceTypesItemComputeShapesItemFamily
    cpu: int
    memory_gb: int
    dynamic_storage_supported: bool
    node_counts: list[int]
    backups: list[DatabasePlansResponseServiceTypesItemComputeShapesItemBackupsItem] | Unset = UNSET
    storage: DatabasePlansResponseServiceTypesItemComputeShapesItemStorageType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.database_plans_response_service_types_item_compute_shapes_item_storage_type_0 import (
            DatabasePlansResponseServiceTypesItemComputeShapesItemStorageType0,  # noqa: PLC0415
        )

        compute = self.compute

        family = self.family.value

        cpu = self.cpu

        memory_gb = self.memory_gb

        dynamic_storage_supported = self.dynamic_storage_supported

        node_counts = self.node_counts

        backups: list[str] | Unset = UNSET
        if not isinstance(self.backups, Unset):
            backups = []
            for backups_item_data in self.backups:
                backups_item = backups_item_data.value
                backups.append(backups_item)

        storage: dict[str, Any] | None | Unset
        if isinstance(self.storage, Unset):
            storage = UNSET
        elif isinstance(self.storage, DatabasePlansResponseServiceTypesItemComputeShapesItemStorageType0):
            storage = self.storage.to_dict()
        else:
            storage = self.storage

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "compute": compute,
                "family": family,
                "cpu": cpu,
                "memory_gb": memory_gb,
                "dynamic_storage_supported": dynamic_storage_supported,
                "node_counts": node_counts,
            }
        )
        if backups is not UNSET:
            field_dict["backups"] = backups
        if storage is not UNSET:
            field_dict["storage"] = storage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_plans_response_service_types_item_compute_shapes_item_storage_type_0 import (
            DatabasePlansResponseServiceTypesItemComputeShapesItemStorageType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        compute = d.pop("compute")

        family = DatabasePlansResponseServiceTypesItemComputeShapesItemFamily(d.pop("family"))

        cpu = d.pop("cpu")

        memory_gb = d.pop("memory_gb")

        dynamic_storage_supported = d.pop("dynamic_storage_supported")

        node_counts = cast(list[int], d.pop("node_counts"))

        _backups = d.pop("backups", UNSET)
        backups: list[DatabasePlansResponseServiceTypesItemComputeShapesItemBackupsItem] | Unset = UNSET
        if _backups is not UNSET:
            backups = []
            for backups_item_data in _backups:
                backups_item = DatabasePlansResponseServiceTypesItemComputeShapesItemBackupsItem(backups_item_data)

                backups.append(backups_item)

        def _parse_storage(
            data: object,
        ) -> DatabasePlansResponseServiceTypesItemComputeShapesItemStorageType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                storage_type_0 = DatabasePlansResponseServiceTypesItemComputeShapesItemStorageType0.from_dict(data)

                return storage_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatabasePlansResponseServiceTypesItemComputeShapesItemStorageType0 | None | Unset, data)

        storage = _parse_storage(d.pop("storage", UNSET))

        database_plans_response_service_types_item_compute_shapes_item = cls(
            compute=compute,
            family=family,
            cpu=cpu,
            memory_gb=memory_gb,
            dynamic_storage_supported=dynamic_storage_supported,
            node_counts=node_counts,
            backups=backups,
            storage=storage,
        )

        return database_plans_response_service_types_item_compute_shapes_item
