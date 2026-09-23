from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.server_storage_devices_storage_device_item import ServerStorageDevicesStorageDeviceItem


T = TypeVar("T", bound="ServerStorageDevices")


@_attrs_define
class ServerStorageDevices:
    """Storage devices to create or attach to the Cloud Server

    Example:
        {'storage_device': [{'action': 'create', 'size': '20', 'title': 'Operating system disk'}]}

    Attributes:
        storage_device (list[ServerStorageDevicesStorageDeviceItem]):
    """

    storage_device: list[ServerStorageDevicesStorageDeviceItem]

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
        from ..models.server_storage_devices_storage_device_item import (
            ServerStorageDevicesStorageDeviceItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        storage_device = []
        _storage_device = d.pop("storage_device")
        for storage_device_item_data in _storage_device:
            storage_device_item = ServerStorageDevicesStorageDeviceItem.from_dict(storage_device_item_data)

            storage_device.append(storage_device_item)

        server_storage_devices = cls(
            storage_device=storage_device,
        )

        return server_storage_devices
