from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServerStorageDevicesStorageDeviceItemBackupRule")


@_attrs_define
class ServerStorageDevicesStorageDeviceItemBackupRule:
    """
    Attributes:
        interval (str | Unset): Backup weekday, or daily to create a backup every day
        retention (int | Unset): Number of days before an automatic backup is deleted
        time (str | Unset): UTC backup start time in HHMM format
    """

    interval: str | Unset = UNSET
    retention: int | Unset = UNSET
    time: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interval = self.interval

        retention = self.retention

        time = self.time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interval is not UNSET:
            field_dict["interval"] = interval
        if retention is not UNSET:
            field_dict["retention"] = retention
        if time is not UNSET:
            field_dict["time"] = time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        interval = d.pop("interval", UNSET)

        retention = d.pop("retention", UNSET)

        time = d.pop("time", UNSET)

        server_storage_devices_storage_device_item_backup_rule = cls(
            interval=interval,
            retention=retention,
            time=time,
        )

        server_storage_devices_storage_device_item_backup_rule.additional_properties = d
        return server_storage_devices_storage_device_item_backup_rule

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
