from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseOpenSearchSecurityPluginStatusResponse")


@_attrs_define
class DatabaseOpenSearchSecurityPluginStatusResponse:
    """OpenSearch security plugin status response

    Attributes:
        security_plugin_admin_enabled (bool | Unset): Indicates if the security plugin admin is enabled Example: True.
        security_plugin_available (bool | Unset): Indicates if the security plugin is available Example: True.
        security_plugin_enabled (bool | Unset): Indicates if the security plugin is enabled Example: True.
    """

    security_plugin_admin_enabled: bool | Unset = UNSET
    security_plugin_available: bool | Unset = UNSET
    security_plugin_enabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        security_plugin_admin_enabled = self.security_plugin_admin_enabled

        security_plugin_available = self.security_plugin_available

        security_plugin_enabled = self.security_plugin_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if security_plugin_admin_enabled is not UNSET:
            field_dict["security_plugin_admin_enabled"] = security_plugin_admin_enabled
        if security_plugin_available is not UNSET:
            field_dict["security_plugin_available"] = security_plugin_available
        if security_plugin_enabled is not UNSET:
            field_dict["security_plugin_enabled"] = security_plugin_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        security_plugin_admin_enabled = d.pop("security_plugin_admin_enabled", UNSET)

        security_plugin_available = d.pop("security_plugin_available", UNSET)

        security_plugin_enabled = d.pop("security_plugin_enabled", UNSET)

        database_open_search_security_plugin_status_response = cls(
            security_plugin_admin_enabled=security_plugin_admin_enabled,
            security_plugin_available=security_plugin_available,
            security_plugin_enabled=security_plugin_enabled,
        )

        database_open_search_security_plugin_status_response.additional_properties = d
        return database_open_search_security_plugin_status_response

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
