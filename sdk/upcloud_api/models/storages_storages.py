from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.storage_list_item import StorageListItem


T = TypeVar("T", bound="StoragesStorages")


@_attrs_define
class StoragesStorages:
    """
    Attributes:
        storage (list[StorageListItem]):
    """

    storage: list[StorageListItem]

    def to_dict(self) -> dict[str, Any]:
        storage = []
        for storage_item_data in self.storage:
            storage_item = storage_item_data.to_dict()
            storage.append(storage_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "storage": storage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.storage_list_item import StorageListItem  # noqa: PLC0415

        d = dict(src_dict)
        storage = []
        _storage = d.pop("storage")
        for storage_item_data in _storage:
            storage_item = StorageListItem.from_dict(storage_item_data)

            storage.append(storage_item)

        storages_storages = cls(
            storage=storage,
        )

        return storages_storages
