from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.storage_details import StorageDetails


T = TypeVar("T", bound="CreateStorageBackupResponse")


@_attrs_define
class CreateStorageBackupResponse:
    """Response containing the on-demand backup being created.

    Example:
        {'storage': {'access': 'private', 'created': '2026-08-26T09:20:00Z', 'encrypted': 'yes', 'labels': [{'key':
            'environment', 'value': 'production'}], 'license': 0, 'origin': '01d4fcd4-e446-433b-8a9c-551a1284952e',
            'progress': '0', 'servers': {'server': []}, 'size': 50, 'state': 'maintenance', 'title': 'Manually created
            backup', 'type': 'backup', 'uuid': '016d343b-14de-4b61-91ca-433dd1ea6c47', 'zone': 'fi-hel1'}}

    Attributes:
        storage (StorageDetails): Detailed information about a storage resource. Example: {'access': 'private',
            'backup_rule': {}, 'backups': {'backup': []}, 'created': '2026-08-26T09:15:00Z', 'encrypted': 'no', 'labels':
            [], 'license': 0, 'servers': {'server': []}, 'size': 50, 'state': 'online', 'tier': 'maxiops', 'title':
            'Production data', 'type': 'normal', 'uuid': '01d4fcd4-e446-433b-8a9c-551a1284952e', 'zone': 'fi-hel1'}.
    """

    storage: StorageDetails

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
        from ..models.storage_details import StorageDetails  # noqa: PLC0415

        d = dict(src_dict)
        storage = StorageDetails.from_dict(d.pop("storage"))

        create_storage_backup_response = cls(
            storage=storage,
        )

        return create_storage_backup_response
