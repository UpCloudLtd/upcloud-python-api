from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.database_plans_response_service_types_item_backup_tiers_item import (
    DatabasePlansResponseServiceTypesItemBackupTiersItem,
)
from ..models.database_plans_response_service_types_item_type import DatabasePlansResponseServiceTypesItemType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_plans_response_service_types_item_compute_shapes_item import (
        DatabasePlansResponseServiceTypesItemComputeShapesItem,
    )


T = TypeVar("T", bound="DatabasePlansResponseServiceTypesItem")


@_attrs_define
class DatabasePlansResponseServiceTypesItem:
    """
    Attributes:
        type_ (DatabasePlansResponseServiceTypesItemType): Service type identifier.
        componentised (bool): Always true for entries in this response; kept as an explicit indicator of componentised
            plans.
        zones (list[str]): Zones where this service type is available.
        node_counts (list[int]): Distinct node counts offered across this service type's plans.
        compute_shapes (list[DatabasePlansResponseServiceTypesItemComputeShapesItem]): Distinct compute shapes offered
            for this service type.
        latest_version (str | Unset): Latest available major version for this service type. Omitted when not applicable.
        backup_tiers (list[DatabasePlansResponseServiceTypesItemBackupTiersItem] | Unset): Backup tiers offered across
            this service type's plans. Omitted when the service type exposes no named backup tiers.
    """

    type_: DatabasePlansResponseServiceTypesItemType
    componentised: bool
    zones: list[str]
    node_counts: list[int]
    compute_shapes: list[DatabasePlansResponseServiceTypesItemComputeShapesItem]
    latest_version: str | Unset = UNSET
    backup_tiers: list[DatabasePlansResponseServiceTypesItemBackupTiersItem] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        componentised = self.componentised

        zones = self.zones

        node_counts = self.node_counts

        compute_shapes = []
        for compute_shapes_item_data in self.compute_shapes:
            compute_shapes_item = compute_shapes_item_data.to_dict()
            compute_shapes.append(compute_shapes_item)

        latest_version = self.latest_version

        backup_tiers: list[str] | Unset = UNSET
        if not isinstance(self.backup_tiers, Unset):
            backup_tiers = []
            for backup_tiers_item_data in self.backup_tiers:
                backup_tiers_item = backup_tiers_item_data.value
                backup_tiers.append(backup_tiers_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "componentised": componentised,
                "zones": zones,
                "node_counts": node_counts,
                "compute_shapes": compute_shapes,
            }
        )
        if latest_version is not UNSET:
            field_dict["latest_version"] = latest_version
        if backup_tiers is not UNSET:
            field_dict["backup_tiers"] = backup_tiers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_plans_response_service_types_item_compute_shapes_item import (
            DatabasePlansResponseServiceTypesItemComputeShapesItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = DatabasePlansResponseServiceTypesItemType(d.pop("type"))

        componentised = d.pop("componentised")

        zones = cast(list[str], d.pop("zones"))

        node_counts = cast(list[int], d.pop("node_counts"))

        compute_shapes = []
        _compute_shapes = d.pop("compute_shapes")
        for compute_shapes_item_data in _compute_shapes:
            compute_shapes_item = DatabasePlansResponseServiceTypesItemComputeShapesItem.from_dict(
                compute_shapes_item_data
            )

            compute_shapes.append(compute_shapes_item)

        latest_version = d.pop("latest_version", UNSET)

        _backup_tiers = d.pop("backup_tiers", UNSET)
        backup_tiers: list[DatabasePlansResponseServiceTypesItemBackupTiersItem] | Unset = UNSET
        if _backup_tiers is not UNSET:
            backup_tiers = []
            for backup_tiers_item_data in _backup_tiers:
                backup_tiers_item = DatabasePlansResponseServiceTypesItemBackupTiersItem(backup_tiers_item_data)

                backup_tiers.append(backup_tiers_item)

        database_plans_response_service_types_item = cls(
            type_=type_,
            componentised=componentised,
            zones=zones,
            node_counts=node_counts,
            compute_shapes=compute_shapes,
            latest_version=latest_version,
            backup_tiers=backup_tiers,
        )

        return database_plans_response_service_types_item
