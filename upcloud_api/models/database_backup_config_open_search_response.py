from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseBackupConfigOpenSearchResponse")


@_attrs_define
class DatabaseBackupConfigOpenSearchResponse:
    """OpenSearch specific backup configuration response

    Attributes:
        frequent_interval_minutes (int | Unset): Frequent backup interval in minutes Example: 15.
        frequent_oldest_age_minutes (int | Unset): Oldest age for frequent backups in minutes Example: 60.
        infrequent_interval_minutes (int | Unset): Infrequent backup interval in minutes Example: 240.
        infrequent_oldest_age_minutes (int | Unset): Oldest age for infrequent backups in minutes Example: 1440.
        recovery_mode (str | Unset): Recovery mode for backups Example: point_in_time.
    """

    frequent_interval_minutes: int | Unset = UNSET
    frequent_oldest_age_minutes: int | Unset = UNSET
    infrequent_interval_minutes: int | Unset = UNSET
    infrequent_oldest_age_minutes: int | Unset = UNSET
    recovery_mode: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        frequent_interval_minutes = self.frequent_interval_minutes

        frequent_oldest_age_minutes = self.frequent_oldest_age_minutes

        infrequent_interval_minutes = self.infrequent_interval_minutes

        infrequent_oldest_age_minutes = self.infrequent_oldest_age_minutes

        recovery_mode = self.recovery_mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if frequent_interval_minutes is not UNSET:
            field_dict["frequent_interval_minutes"] = frequent_interval_minutes
        if frequent_oldest_age_minutes is not UNSET:
            field_dict["frequent_oldest_age_minutes"] = frequent_oldest_age_minutes
        if infrequent_interval_minutes is not UNSET:
            field_dict["infrequent_interval_minutes"] = infrequent_interval_minutes
        if infrequent_oldest_age_minutes is not UNSET:
            field_dict["infrequent_oldest_age_minutes"] = infrequent_oldest_age_minutes
        if recovery_mode is not UNSET:
            field_dict["recovery_mode"] = recovery_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        frequent_interval_minutes = d.pop("frequent_interval_minutes", UNSET)

        frequent_oldest_age_minutes = d.pop("frequent_oldest_age_minutes", UNSET)

        infrequent_interval_minutes = d.pop("infrequent_interval_minutes", UNSET)

        infrequent_oldest_age_minutes = d.pop("infrequent_oldest_age_minutes", UNSET)

        recovery_mode = d.pop("recovery_mode", UNSET)

        database_backup_config_open_search_response = cls(
            frequent_interval_minutes=frequent_interval_minutes,
            frequent_oldest_age_minutes=frequent_oldest_age_minutes,
            infrequent_interval_minutes=infrequent_interval_minutes,
            infrequent_oldest_age_minutes=infrequent_oldest_age_minutes,
            recovery_mode=recovery_mode,
        )

        database_backup_config_open_search_response.additional_properties = d
        return database_backup_config_open_search_response

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
