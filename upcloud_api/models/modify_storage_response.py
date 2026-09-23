from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.storage_details import StorageDetails


T = TypeVar("T", bound="ModifyStorageResponse")


@_attrs_define
class ModifyStorageResponse:
    """Response schema for block storage modification operations.

    Example:
        {'storage': {'access': 'private', 'backup_rule': {}, 'backups': {'backup': []}, 'created':
            '2026-08-26T09:15:00Z', 'encrypted': 'no', 'labels': [], 'license': 0, 'servers': {'server': []}, 'size': 60,
            'state': 'online', 'tier': 'maxiops', 'title': 'Production data expanded', 'type': 'normal', 'uuid':
            '011d671f-e803-484d-920a-c25b4bb05c01', 'zone': 'fi-hel1'}}

    Attributes:
        storage (StorageDetails): Detailed information about a storage resource. Example: {'access': 'private',
            'backup_rule': {}, 'backups': {'backup': []}, 'created': '2026-08-26T09:15:00Z', 'encrypted': 'no', 'labels':
            [], 'license': 0, 'servers': {'server': []}, 'size': 50, 'state': 'online', 'tier': 'maxiops', 'title':
            'Production data', 'type': 'normal', 'uuid': '01d4fcd4-e446-433b-8a9c-551a1284952e', 'zone': 'fi-hel1'}.
        resize_backup (StorageDetails | Unset): Detailed information about a storage resource. Example: {'access':
            'private', 'backup_rule': {}, 'backups': {'backup': []}, 'created': '2026-08-26T09:15:00Z', 'encrypted': 'no',
            'labels': [], 'license': 0, 'servers': {'server': []}, 'size': 50, 'state': 'online', 'tier': 'maxiops',
            'title': 'Production data', 'type': 'normal', 'uuid': '01d4fcd4-e446-433b-8a9c-551a1284952e', 'zone': 'fi-
            hel1'}.
    """

    storage: StorageDetails
    resize_backup: StorageDetails | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        storage = self.storage.to_dict()

        resize_backup: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resize_backup, Unset):
            resize_backup = self.resize_backup.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "storage": storage,
            }
        )
        if resize_backup is not UNSET:
            field_dict["resize_backup"] = resize_backup

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.storage_details import StorageDetails  # noqa: PLC0415

        d = dict(src_dict)
        storage = StorageDetails.from_dict(d.pop("storage"))

        _resize_backup = d.pop("resize_backup", UNSET)
        resize_backup: StorageDetails | Unset
        if isinstance(_resize_backup, Unset):
            resize_backup = UNSET
        else:
            resize_backup = StorageDetails.from_dict(_resize_backup)

        modify_storage_response = cls(
            storage=storage,
            resize_backup=resize_backup,
        )

        return modify_storage_response
