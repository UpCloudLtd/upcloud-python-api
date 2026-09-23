from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.server_attach_storage_storage_device import ServerAttachStorageStorageDevice


T = TypeVar("T", bound="ServerAttachStorage")


@_attrs_define
class ServerAttachStorage:
    """Parameters for attaching a storage device to a Cloud Server.

    Example:
        {'storage_device': {'address': 'virtio:0', 'boot_disk': 1, 'storage': '012580a1-32a1-466e-a323-689ca16f2d43',
            'type': 'disk'}}

    Attributes:
        storage_device (ServerAttachStorageStorageDevice): Storage device to attach.
    """

    storage_device: ServerAttachStorageStorageDevice

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
        from ..models.server_attach_storage_storage_device import ServerAttachStorageStorageDevice  # noqa: PLC0415

        d = dict(src_dict)
        storage_device = ServerAttachStorageStorageDevice.from_dict(d.pop("storage_device"))

        server_attach_storage = cls(
            storage_device=storage_device,
        )

        return server_attach_storage
