from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_service_task_create_dataset_import import DatabaseServiceTaskCreateDatasetImport
    from ..models.database_service_task_create_migration_check import DatabaseServiceTaskCreateMigrationCheck
    from ..models.database_service_task_create_upgrade_check import DatabaseServiceTaskCreateUpgradeCheck


T = TypeVar("T", bound="DatabaseServiceTaskCreate")


@_attrs_define
class DatabaseServiceTaskCreate:
    """Schema for creating a service task with various operations such as dataset import and migration checks.

    Attributes:
        operation (str): The operation to be performed.
        dataset_import (DatabaseServiceTaskCreateDatasetImport | Unset):
        migration_check (DatabaseServiceTaskCreateMigrationCheck | Unset):
        upgrade_check (DatabaseServiceTaskCreateUpgradeCheck | Unset):
        target_version (str | Unset): The target version for upgrade operations.
    """

    operation: str
    dataset_import: DatabaseServiceTaskCreateDatasetImport | Unset = UNSET
    migration_check: DatabaseServiceTaskCreateMigrationCheck | Unset = UNSET
    upgrade_check: DatabaseServiceTaskCreateUpgradeCheck | Unset = UNSET
    target_version: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        operation = self.operation

        dataset_import: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dataset_import, Unset):
            dataset_import = self.dataset_import.to_dict()

        migration_check: dict[str, Any] | Unset = UNSET
        if not isinstance(self.migration_check, Unset):
            migration_check = self.migration_check.to_dict()

        upgrade_check: dict[str, Any] | Unset = UNSET
        if not isinstance(self.upgrade_check, Unset):
            upgrade_check = self.upgrade_check.to_dict()

        target_version = self.target_version

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "operation": operation,
            }
        )
        if dataset_import is not UNSET:
            field_dict["dataset_import"] = dataset_import
        if migration_check is not UNSET:
            field_dict["migration_check"] = migration_check
        if upgrade_check is not UNSET:
            field_dict["upgrade_check"] = upgrade_check
        if target_version is not UNSET:
            field_dict["target_version"] = target_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_service_task_create_dataset_import import (
            DatabaseServiceTaskCreateDatasetImport,  # noqa: PLC0415
        )
        from ..models.database_service_task_create_migration_check import (
            DatabaseServiceTaskCreateMigrationCheck,  # noqa: PLC0415
        )
        from ..models.database_service_task_create_upgrade_check import (
            DatabaseServiceTaskCreateUpgradeCheck,  # noqa: PLC0415
        )

        d = dict(src_dict)
        operation = d.pop("operation")

        _dataset_import = d.pop("dataset_import", UNSET)
        dataset_import: DatabaseServiceTaskCreateDatasetImport | Unset
        if isinstance(_dataset_import, Unset):
            dataset_import = UNSET
        else:
            dataset_import = DatabaseServiceTaskCreateDatasetImport.from_dict(_dataset_import)

        _migration_check = d.pop("migration_check", UNSET)
        migration_check: DatabaseServiceTaskCreateMigrationCheck | Unset
        if isinstance(_migration_check, Unset):
            migration_check = UNSET
        else:
            migration_check = DatabaseServiceTaskCreateMigrationCheck.from_dict(_migration_check)

        _upgrade_check = d.pop("upgrade_check", UNSET)
        upgrade_check: DatabaseServiceTaskCreateUpgradeCheck | Unset
        if isinstance(_upgrade_check, Unset):
            upgrade_check = UNSET
        else:
            upgrade_check = DatabaseServiceTaskCreateUpgradeCheck.from_dict(_upgrade_check)

        target_version = d.pop("target_version", UNSET)

        database_service_task_create = cls(
            operation=operation,
            dataset_import=dataset_import,
            migration_check=migration_check,
            upgrade_check=upgrade_check,
            target_version=target_version,
        )

        return database_service_task_create
