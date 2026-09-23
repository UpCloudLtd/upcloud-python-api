from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.create_storage_request_storage import CreateStorageRequestStorage


T = TypeVar("T", bound="CreateStorageRequest")


@_attrs_define
class CreateStorageRequest:
    """Request schema for creating block storage.

    Example:
        {'storage': {'backup_rule': {'interval': 'daily', 'retention': '7', 'time': '0400'}, 'encrypted': 'yes',
            'labels': [{'key': 'environment', 'value': 'production'}], 'size': 50, 'tier': 'maxiops', 'title': 'Block
            Storage 1', 'zone': 'fi-hel1'}}

    Attributes:
        storage (CreateStorageRequestStorage): Block storage creation parameters.
    """

    storage: CreateStorageRequestStorage

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
        from ..models.create_storage_request_storage import CreateStorageRequestStorage  # noqa: PLC0415

        d = dict(src_dict)
        storage = CreateStorageRequestStorage.from_dict(d.pop("storage"))

        create_storage_request = cls(
            storage=storage,
        )

        return create_storage_request
