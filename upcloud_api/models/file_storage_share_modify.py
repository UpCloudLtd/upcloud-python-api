from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_storage_acl_create import FileStorageAclCreate


T = TypeVar("T", bound="FileStorageShareModify")


@_attrs_define
class FileStorageShareModify:
    """Schema for modifying an existing share.

    Attributes:
        name (str | Unset): A resource name.
        acl (list[FileStorageAclCreate] | Unset):
    """

    name: str | Unset = UNSET
    acl: list[FileStorageAclCreate] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        acl: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.acl, Unset):
            acl = []
            for acl_item_data in self.acl:
                acl_item = acl_item_data.to_dict()
                acl.append(acl_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if acl is not UNSET:
            field_dict["acl"] = acl

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_storage_acl_create import FileStorageAclCreate  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _acl = d.pop("acl", UNSET)
        acl: list[FileStorageAclCreate] | Unset = UNSET
        if _acl is not UNSET:
            acl = []
            for acl_item_data in _acl:
                acl_item = FileStorageAclCreate.from_dict(acl_item_data)

                acl.append(acl_item)

        file_storage_share_modify = cls(
            name=name,
            acl=acl,
        )

        return file_storage_share_modify
