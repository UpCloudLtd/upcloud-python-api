from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FileStorageShareDetailResponseAclItem")


@_attrs_define
class FileStorageShareDetailResponseAclItem:
    """
    Attributes:
        name (str | Unset):
        target (str | Unset):
        permission (str | Unset):
    """

    name: str | Unset = UNSET
    target: str | Unset = UNSET
    permission: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        target = self.target

        permission = self.permission

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if target is not UNSET:
            field_dict["target"] = target
        if permission is not UNSET:
            field_dict["permission"] = permission

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        target = d.pop("target", UNSET)

        permission = d.pop("permission", UNSET)

        file_storage_share_detail_response_acl_item = cls(
            name=name,
            target=target,
            permission=permission,
        )

        file_storage_share_detail_response_acl_item.additional_properties = d
        return file_storage_share_detail_response_acl_item

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
