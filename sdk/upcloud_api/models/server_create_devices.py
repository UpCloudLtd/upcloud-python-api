from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.server_create_devices_device_item import ServerCreateDevicesDeviceItem


T = TypeVar("T", bound="ServerCreateDevices")


@_attrs_define
class ServerCreateDevices:
    """Passthrough devices requested for a new Cloud Server

    Example:
        {'device': [{'serial': '1723925007011', 'type': 'gpu'}]}

    Attributes:
        device (list[ServerCreateDevicesDeviceItem]):
    """

    device: list[ServerCreateDevicesDeviceItem]

    def to_dict(self) -> dict[str, Any]:
        device = []
        for device_item_data in self.device:
            device_item = device_item_data.to_dict()
            device.append(device_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "device": device,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_create_devices_device_item import ServerCreateDevicesDeviceItem  # noqa: PLC0415

        d = dict(src_dict)
        device = []
        _device = d.pop("device")
        for device_item_data in _device:
            device_item = ServerCreateDevicesDeviceItem.from_dict(device_item_data)

            device.append(device_item)

        server_create_devices = cls(
            device=device,
        )

        return server_create_devices
