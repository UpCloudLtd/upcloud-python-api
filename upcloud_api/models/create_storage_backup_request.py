from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.create_storage_backup_request_storage import CreateStorageBackupRequestStorage


T = TypeVar("T", bound="CreateStorageBackupRequest")


@_attrs_define
class CreateStorageBackupRequest:
    """Request schema for creating an on-demand block storage backup.

    Example:
        {'storage': {'title': 'Manually created backup'}}

    Attributes:
        storage (CreateStorageBackupRequestStorage): Parameters for the point-in-time backup.
    """

    storage: CreateStorageBackupRequestStorage

    def to_dict(self) -> dict[str, Any]:
        storage = self.storage.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "storage": storage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_storage_backup_request_storage import CreateStorageBackupRequestStorage  # noqa: PLC0415

        d = dict(src_dict)
        storage = CreateStorageBackupRequestStorage.from_dict(d.pop("storage"))

        create_storage_backup_request = cls(
            storage=storage,
        )

        return create_storage_backup_request
