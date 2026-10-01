from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.storage_import import StorageImport


T = TypeVar("T", bound="StorageImportResponse")


@_attrs_define
class StorageImportResponse:
    """Response containing a storage import task.

    Example:
        {'storage_import': {'client_content_length': 0, 'client_content_type': '', 'completed': '', 'created':
            '2020-06-26T08:51:07Z', 'direct_upload_url': 'https://fi-
            hel1.img.upcloud.com/uploader/session/07a6c9a3-300e-4d0e-b935-624f3dbdff3f', 'error_code': '', 'error_message':
            '', 'md5sum': '', 'read_bytes': 0, 'sha256sum': '', 'source': 'direct_upload', 'state': 'prepared', 'uuid':
            '07a6c9a3-300e-4d0e-b935-624f3dbdff3f', 'written_bytes': 0}}

    Attributes:
        storage_import (StorageImport): Details and progress of a storage import task. Example:
            {'client_content_length': 0, 'client_content_type': '', 'completed': '', 'created': '2020-06-26T08:51:07Z',
            'error_code': '', 'error_message': '', 'md5sum': '', 'read_bytes': 0, 'sha256sum': '', 'source': 'http_import',
            'source_location': 'https://example.com/disk.raw', 'state': 'pending', 'uuid':
            '07a6c9a3-300e-4d0e-b935-624f3dbdff3f', 'written_bytes': 0}.
    """

    storage_import: StorageImport

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
        from ..models.storage_import import StorageImport  # noqa: PLC0415

        d = dict(src_dict)
        storage_import = StorageImport.from_dict(d.pop("storage_import"))

        storage_import_response = cls(
            storage_import=storage_import,
        )

        return storage_import_response
