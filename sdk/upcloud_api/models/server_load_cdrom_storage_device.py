from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

T = TypeVar("T", bound="ServerLoadCdromStorageDevice")


@_attrs_define
class ServerLoadCdromStorageDevice:
    """Storage to load into the attached CD-ROM device.

    Attributes:
        storage (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
    """

    storage: UUID

    def to_dict(self) -> dict[str, Any]:
        storage = str(self.storage)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "storage": storage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        storage = UUID(d.pop("storage"))

        server_load_cdrom_storage_device = cls(
            storage=storage,
        )

        return server_load_cdrom_storage_device
