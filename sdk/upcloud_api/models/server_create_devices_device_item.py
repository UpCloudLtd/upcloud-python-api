from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ServerCreateDevicesDeviceItem")


@_attrs_define
class ServerCreateDevicesDeviceItem:
    """
    Attributes:
        serial (str): Serial identifier of the attached device
        type_ (str): Type of passthrough device to attach
    """

    serial: str
    type_: str

    def to_dict(self) -> dict[str, Any]:
        serial = self.serial

        type_ = self.type_

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "serial": serial,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        serial = d.pop("serial")

        type_ = d.pop("type")

        server_create_devices_device_item = cls(
            serial=serial,
            type_=type_,
        )

        return server_create_devices_device_item
