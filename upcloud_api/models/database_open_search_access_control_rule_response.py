from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseOpenSearchAccessControlRuleResponse")


@_attrs_define
class DatabaseOpenSearchAccessControlRuleResponse:
    """Schema for OpenSearch access control rule response.

    Attributes:
        index (str | Unset): Index name or pattern (e.g., 'log-*' for all indices starting with 'log-') Example: log-*.
        permission (str | Unset): Permission level for the specified index Example: read.
    """

    index: str | Unset = UNSET
    permission: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        index = self.index

        permission = self.permission

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if index is not UNSET:
            field_dict["index"] = index
        if permission is not UNSET:
            field_dict["permission"] = permission

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        index = d.pop("index", UNSET)

        permission = d.pop("permission", UNSET)

        database_open_search_access_control_rule_response = cls(
            index=index,
            permission=permission,
        )

        database_open_search_access_control_rule_response.additional_properties = d
        return database_open_search_access_control_rule_response

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
