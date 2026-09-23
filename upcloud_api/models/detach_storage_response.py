from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.storage_details import StorageDetails


T = TypeVar("T", bound="DetachStorageResponse")


@_attrs_define
class DetachStorageResponse:
    """Response containing the detached storage resource.

    Example:
        {'storage': {'access': 'private', 'backup_rule': {}, 'backups': {'backup': []}, 'created':
            '2026-08-26T09:15:00Z', 'encrypted': 'yes', 'labels': [{'key': 'environment', 'value': 'production'}],
            'license': 0, 'servers': {'server': []}, 'size': 50, 'state': 'online', 'tier': 'maxiops', 'title': 'Production
            data', 'type': 'normal', 'uuid': '01d4fcd4-e446-433b-8a9c-551a1284952e', 'zone': 'fi-hel1'}}

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

        detach_storage_response = cls(
            storage=storage,
        )

        return detach_storage_response
