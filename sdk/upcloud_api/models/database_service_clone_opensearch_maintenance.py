from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.database_maintenance_dow import DatabaseMaintenanceDow

T = TypeVar("T", bound="DatabaseServiceCloneOpensearchMaintenance")


@_attrs_define
class DatabaseServiceCloneOpensearchMaintenance:
    """Maintenance

    Attributes:
        dow (DatabaseMaintenanceDow): Day of the week for maintenance window
        time (str): Time of day for maintenance window in HH:MM:SS format
    """

    dow: DatabaseMaintenanceDow
    time: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dow = self.dow.value

        time = self.time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dow": dow,
                "time": time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dow = DatabaseMaintenanceDow(d.pop("dow"))

        time = d.pop("time")

        database_service_clone_opensearch_maintenance = cls(
            dow=dow,
            time=time,
        )

        database_service_clone_opensearch_maintenance.additional_properties = d
        return database_service_clone_opensearch_maintenance

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
