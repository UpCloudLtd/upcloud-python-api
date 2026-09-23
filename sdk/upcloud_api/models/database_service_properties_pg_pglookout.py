from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseServicePropertiesPgPglookout")


@_attrs_define
class DatabaseServicePropertiesPgPglookout:
    """System-wide settings for pglookout.

    Attributes:
        max_failover_replication_time_lag (int | Unset): Number of seconds of master unavailability before triggering
            database failover to standby
    """

    max_failover_replication_time_lag: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_failover_replication_time_lag = self.max_failover_replication_time_lag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_failover_replication_time_lag is not UNSET:
            field_dict["max_failover_replication_time_lag"] = max_failover_replication_time_lag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        max_failover_replication_time_lag = d.pop("max_failover_replication_time_lag", UNSET)

        database_service_properties_pg_pglookout = cls(
            max_failover_replication_time_lag=max_failover_replication_time_lag,
        )

        database_service_properties_pg_pglookout.additional_properties = d
        return database_service_properties_pg_pglookout

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
