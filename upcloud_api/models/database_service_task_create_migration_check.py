from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseServiceTaskCreateMigrationCheck")


@_attrs_define
class DatabaseServiceTaskCreateMigrationCheck:
    """
    Attributes:
        source_service_uri (str): The URI of the source service for migration.
        ignore_dbs (str | Unset): Databases to ignore during the migration check, separated by commas.
        ignore_roles (str | Unset):
        method (str | Unset): The migration method to be used.
    """

    source_service_uri: str
    ignore_dbs: str | Unset = UNSET
    ignore_roles: str | Unset = UNSET
    method: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        source_service_uri = self.source_service_uri

        ignore_dbs = self.ignore_dbs

        ignore_roles = self.ignore_roles

        method = self.method

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "source_service_uri": source_service_uri,
            }
        )
        if ignore_dbs is not UNSET:
            field_dict["ignore_dbs"] = ignore_dbs
        if ignore_roles is not UNSET:
            field_dict["ignore_roles"] = ignore_roles
        if method is not UNSET:
            field_dict["method"] = method

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source_service_uri = d.pop("source_service_uri")

        ignore_dbs = d.pop("ignore_dbs", UNSET)

        ignore_roles = d.pop("ignore_roles", UNSET)

        method = d.pop("method", UNSET)

        database_service_task_create_migration_check = cls(
            source_service_uri=source_service_uri,
            ignore_dbs=ignore_dbs,
            ignore_roles=ignore_roles,
            method=method,
        )

        return database_service_task_create_migration_check
