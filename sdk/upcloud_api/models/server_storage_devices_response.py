from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.server_storage_devices_response_storage_device_item import (
        ServerStorageDevicesResponseStorageDeviceItem,
    )


T = TypeVar("T", bound="ServerStorageDevicesResponse")


@_attrs_define
class ServerStorageDevicesResponse:
    """Storage devices attached to a Cloud Server

    Example:
        {'storage_device': [{'address': 'virtio:0', 'boot_disk': '1', 'labels': [], 'storage':
            '012580a1-32a1-466e-a323-689ca16f2d43', 'storage_encrypted': 'yes', 'storage_size': 20, 'storage_title':
            'Operating system disk', 'type': 'disk'}]}

    Attributes:
        storage_device (list[ServerStorageDevicesResponseStorageDeviceItem]):
    """

    storage_device: list[ServerStorageDevicesResponseStorageDeviceItem]

    def to_dict(self) -> dict[str, Any]:
        storage_device = []
        for storage_device_item_data in self.storage_device:
            storage_device_item = storage_device_item_data.to_dict()
            storage_device.append(storage_device_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "storage_device": storage_device,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_storage_devices_response_storage_device_item import (
            ServerStorageDevicesResponseStorageDeviceItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        storage_device = []
        _storage_device = d.pop("storage_device")
        for storage_device_item_data in _storage_device:
            storage_device_item = ServerStorageDevicesResponseStorageDeviceItem.from_dict(storage_device_item_data)

            storage_device.append(storage_device_item)

        server_storage_devices_response = cls(
            storage_device=storage_device,
        )

        return server_storage_devices_response
