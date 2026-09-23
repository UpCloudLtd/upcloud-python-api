from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.server_load_cdrom_storage_device import ServerLoadCdromStorageDevice


T = TypeVar("T", bound="ServerLoadCdrom")


@_attrs_define
class ServerLoadCdrom:
    """Parameters for loading a storage into a Cloud Server's CD-ROM device.

    Example:
        {'storage_device': {'storage': '01000000-0000-4000-8000-000060010101'}}

    Attributes:
        storage_device (ServerLoadCdromStorageDevice): Storage to load into the attached CD-ROM device.
    """

    storage_device: ServerLoadCdromStorageDevice

    def to_dict(self) -> dict[str, Any]:
        storage_device = self.storage_device.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "storage_device": storage_device,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_load_cdrom_storage_device import ServerLoadCdromStorageDevice  # noqa: PLC0415

        d = dict(src_dict)
        storage_device = ServerLoadCdromStorageDevice.from_dict(d.pop("storage_device"))

        server_load_cdrom = cls(
            storage_device=storage_device,
        )

        return server_load_cdrom
