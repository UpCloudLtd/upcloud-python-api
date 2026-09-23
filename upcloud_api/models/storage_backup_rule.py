from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.storage_backup_rule_interval import StorageBackupRuleInterval

T = TypeVar("T", bound="StorageBackupRule")


@_attrs_define
class StorageBackupRule:
    """Schedule for automatic block storage backups.

    Example:
        {'interval': 'daily', 'retention': '7', 'time': '0400'}

    Attributes:
        interval (StorageBackupRuleInterval): Weekday when the backup is created, or `daily` to create a backup every
            day at the same time.
        time (str): UTC time of day when the backup is created, in `HHMM` format.
        retention (str): Number of days before the backup is automatically deleted, from 1 through 1095.
    """

    interval: StorageBackupRuleInterval
    time: str
    retention: str

    def to_dict(self) -> dict[str, Any]:
        interval = self.interval.value

        time = self.time

        retention = self.retention

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "interval": interval,
                "time": time,
                "retention": retention,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        interval = StorageBackupRuleInterval(d.pop("interval"))

        time = d.pop("time")

        retention = d.pop("retention")

        storage_backup_rule = cls(
            interval=interval,
            time=time,
            retention=retention,
        )

        return storage_backup_rule
