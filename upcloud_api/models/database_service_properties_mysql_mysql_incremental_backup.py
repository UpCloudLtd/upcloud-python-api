from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseServicePropertiesMysqlMysqlIncrementalBackup")


@_attrs_define
class DatabaseServicePropertiesMysqlMysqlIncrementalBackup:
    """
    Attributes:
        enabled (bool): Enable periodic incremental backups. When enabled, full_backup_week_schedule must be set.
            Incremental backups only store changes since the last backup, making them faster and more storage-efficient than
            full backups. This is particularly useful for large databases where daily full backups would be too time-
            consuming or expensive.
        full_backup_week_schedule (None | str | Unset): Comma-separated list of days of the week when full backups
            should be created. Valid values: mon, tue, wed, thu, fri, sat, sun
    """

    enabled: bool
    full_backup_week_schedule: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        full_backup_week_schedule: None | str | Unset
        if isinstance(self.full_backup_week_schedule, Unset):
            full_backup_week_schedule = UNSET
        else:
            full_backup_week_schedule = self.full_backup_week_schedule

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "enabled": enabled,
            }
        )
        if full_backup_week_schedule is not UNSET:
            field_dict["full_backup_week_schedule"] = full_backup_week_schedule

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled")

        def _parse_full_backup_week_schedule(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        full_backup_week_schedule = _parse_full_backup_week_schedule(d.pop("full_backup_week_schedule", UNSET))

        database_service_properties_mysql_mysql_incremental_backup = cls(
            enabled=enabled,
            full_backup_week_schedule=full_backup_week_schedule,
        )

        return database_service_properties_mysql_mysql_incremental_backup
