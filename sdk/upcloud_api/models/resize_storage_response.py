from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.storage_details import StorageDetails


T = TypeVar("T", bound="ResizeStorageResponse")


@_attrs_define
class ResizeStorageResponse:
    """Response containing the backup created before resizing the block storage partition and filesystem.

    Example:
        {'resize_backup': {'access': 'private', 'created': '2021-12-03T06:25:15Z', 'encrypted': 'no', 'labels': [],
            'license': 0, 'size': 100, 'state': 'online', 'origin': '017ca4cc-def2-458d-a797-7782959b30a7', 'servers':
            {'server': []}, 'tier': 'maxiops', 'title': 'Resize Backup', 'type': 'backup', 'uuid':
            '01beec3a-14ac-4f71-9c63-3338341121c3', 'zone': 'fi-hel1'}}

    Attributes:
        resize_backup (StorageDetails): Detailed information about a storage resource. Example: {'access': 'private',
            'backup_rule': {}, 'backups': {'backup': []}, 'created': '2026-08-26T09:15:00Z', 'encrypted': 'no', 'labels':
            [], 'license': 0, 'servers': {'server': []}, 'size': 50, 'state': 'online', 'tier': 'maxiops', 'title':
            'Production data', 'type': 'normal', 'uuid': '01d4fcd4-e446-433b-8a9c-551a1284952e', 'zone': 'fi-hel1'}.
    """

    resize_backup: StorageDetails

    def to_dict(self) -> dict[str, Any]:
        resize_backup = self.resize_backup.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "resize_backup": resize_backup,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.storage_details import StorageDetails  # noqa: PLC0415

        d = dict(src_dict)
        resize_backup = StorageDetails.from_dict(d.pop("resize_backup"))

        resize_storage_response = cls(
            resize_backup=resize_backup,
        )

        return resize_storage_response
