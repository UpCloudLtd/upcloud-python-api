from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

T = TypeVar("T", bound="StorageDetailsBackups")


@_attrs_define
class StorageDetailsBackups:
    """Backups associated with this storage resource.

    Attributes:
        backup (list[UUID]): UUIDs of backups associated with this storage resource.
    """

    backup: list[UUID]

    def to_dict(self) -> dict[str, Any]:
        backup = []
        for backup_item_data in self.backup:
            backup_item = str(backup_item_data)
            backup.append(backup_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "backup": backup,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        backup = []
        _backup = d.pop("backup")
        for backup_item_data in _backup:
            backup_item = UUID(backup_item_data)

            backup.append(backup_item)

        storage_details_backups = cls(
            backup=backup,
        )

        return storage_details_backups
