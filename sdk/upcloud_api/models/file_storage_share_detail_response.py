from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_storage_share_detail_response_acl_item import FileStorageShareDetailResponseAclItem


T = TypeVar("T", bound="FileStorageShareDetailResponse")


@_attrs_define
class FileStorageShareDetailResponse:
    """Schema for the detailed response of a share.

    Attributes:
        name (str | Unset):
        path (str | Unset):
        acl (list[FileStorageShareDetailResponseAclItem] | Unset):
    """

    name: str | Unset = UNSET
    path: str | Unset = UNSET
    acl: list[FileStorageShareDetailResponseAclItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        path = self.path

        acl: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.acl, Unset):
            acl = []
            for acl_item_data in self.acl:
                acl_item = acl_item_data.to_dict()
                acl.append(acl_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if path is not UNSET:
            field_dict["path"] = path
        if acl is not UNSET:
            field_dict["acl"] = acl

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_storage_share_detail_response_acl_item import (
            FileStorageShareDetailResponseAclItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        path = d.pop("path", UNSET)

        _acl = d.pop("acl", UNSET)
        acl: list[FileStorageShareDetailResponseAclItem] | Unset = UNSET
        if _acl is not UNSET:
            acl = []
            for acl_item_data in _acl:
                acl_item = FileStorageShareDetailResponseAclItem.from_dict(acl_item_data)

                acl.append(acl_item)

        file_storage_share_detail_response = cls(
            name=name,
            path=path,
            acl=acl,
        )

        file_storage_share_detail_response.additional_properties = d
        return file_storage_share_detail_response

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
