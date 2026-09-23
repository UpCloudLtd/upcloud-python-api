from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseBackupResponse")


@_attrs_define
class DatabaseBackupResponse:
    """Schema for a backup response.

    Attributes:
        backup_name (str | Unset): The name of the backup. Example: pg-backup-2024-01-01.
        backup_time (datetime.datetime | Unset): The time the backup was created. Example: 2024-01-01T12:00:00Z.
        data_size (int | Unset): The size of the backup data in bytes.
    """

    backup_name: str | Unset = UNSET
    backup_time: datetime.datetime | Unset = UNSET
    data_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backup_name = self.backup_name

        backup_time: str | Unset = UNSET
        if not isinstance(self.backup_time, Unset):
            backup_time = self.backup_time.isoformat()

        data_size = self.data_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if backup_name is not UNSET:
            field_dict["backup_name"] = backup_name
        if backup_time is not UNSET:
            field_dict["backup_time"] = backup_time
        if data_size is not UNSET:
            field_dict["data_size"] = data_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        backup_name = d.pop("backup_name", UNSET)

        _backup_time = d.pop("backup_time", UNSET)
        backup_time: datetime.datetime | Unset
        if isinstance(_backup_time, Unset):
            backup_time = UNSET
        else:
            backup_time = datetime.datetime.fromisoformat(_backup_time)

        data_size = d.pop("data_size", UNSET)

        database_backup_response = cls(
            backup_name=backup_name,
            backup_time=backup_time,
            data_size=data_size,
        )

        database_backup_response.additional_properties = d
        return database_backup_response

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
