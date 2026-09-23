from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseBackupConfigResponse")


@_attrs_define
class DatabaseBackupConfigResponse:
    """General backup configuration schema

    Attributes:
        interval (int | Unset): Backup interval
        max_count (int | Unset): Maximum number of backups to keep
        recovery_mode (str | Unset): Recovery mode for backups
    """

    interval: int | Unset = UNSET
    max_count: int | Unset = UNSET
    recovery_mode: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interval = self.interval

        max_count = self.max_count

        recovery_mode = self.recovery_mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interval is not UNSET:
            field_dict["interval"] = interval
        if max_count is not UNSET:
            field_dict["max_count"] = max_count
        if recovery_mode is not UNSET:
            field_dict["recovery_mode"] = recovery_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        interval = d.pop("interval", UNSET)

        max_count = d.pop("max_count", UNSET)

        recovery_mode = d.pop("recovery_mode", UNSET)

        database_backup_config_response = cls(
            interval=interval,
            max_count=max_count,
            recovery_mode=recovery_mode,
        )

        database_backup_config_response.additional_properties = d
        return database_backup_config_response

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
