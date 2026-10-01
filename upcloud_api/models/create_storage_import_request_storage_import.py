from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.create_storage_import_request_storage_import_source import CreateStorageImportRequestStorageImportSource
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateStorageImportRequestStorageImport")


@_attrs_define
class CreateStorageImportRequestStorageImport:
    """Storage import parameters.

    Attributes:
        source (CreateStorageImportRequestStorageImportSource): Import mode. Use `http_import` to download an image or
            `direct_upload` to receive a temporary upload URL.
        source_location (str | Unset): Publicly reachable HTTP or HTTPS URL of the image. Required for `http_import`.
    """

    source: CreateStorageImportRequestStorageImportSource
    source_location: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        source = self.source.value

        source_location = self.source_location

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "source": source,
            }
        )
        if source_location is not UNSET:
            field_dict["source_location"] = source_location

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source = CreateStorageImportRequestStorageImportSource(d.pop("source"))

        source_location = d.pop("source_location", UNSET)

        create_storage_import_request_storage_import = cls(
            source=source,
            source_location=source_location,
        )

        return create_storage_import_request_storage_import
