from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.create_storage_import_request_storage_import import CreateStorageImportRequestStorageImport


T = TypeVar("T", bound="CreateStorageImportRequest")


@_attrs_define
class CreateStorageImportRequest:
    """Request schema for creating a storage import task.

    Example:
        {'storage_import': {'source': 'http_import', 'source_location': 'https://example.com/disk.raw'}}

    Attributes:
        storage_import (CreateStorageImportRequestStorageImport): Storage import parameters.
    """

    storage_import: CreateStorageImportRequestStorageImport

    def to_dict(self) -> dict[str, Any]:
        storage_import = self.storage_import.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "storage_import": storage_import,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_storage_import_request_storage_import import (
            CreateStorageImportRequestStorageImport,  # noqa: PLC0415
        )

        d = dict(src_dict)
        storage_import = CreateStorageImportRequestStorageImport.from_dict(d.pop("storage_import"))

        create_storage_import_request = cls(
            storage_import=storage_import,
        )

        return create_storage_import_request
