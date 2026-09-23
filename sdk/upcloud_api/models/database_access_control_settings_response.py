from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseAccessControlSettingsResponse")


@_attrs_define
class DatabaseAccessControlSettingsResponse:
    """Response schema for access control settings of a cluster.

    Attributes:
        access_control (bool | Unset): If true, access control is enabled for the cluster. Example: False.
        extended_access_control (bool | Unset): If true, extended access control features are enabled. Example: True.
    """

    access_control: bool | Unset = UNSET
    extended_access_control: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_control = self.access_control

        extended_access_control = self.extended_access_control

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_control is not UNSET:
            field_dict["access_control"] = access_control
        if extended_access_control is not UNSET:
            field_dict["extended_access_control"] = extended_access_control

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_control = d.pop("access_control", UNSET)

        extended_access_control = d.pop("extended_access_control", UNSET)

        database_access_control_settings_response = cls(
            access_control=access_control,
            extended_access_control=extended_access_control,
        )

        database_access_control_settings_response.additional_properties = d
        return database_access_control_settings_response

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
