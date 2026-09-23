from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.file_storage_permission import FileStoragePermission
from ..types import UNSET, Unset

T = TypeVar("T", bound="FileStorageAclModify")


@_attrs_define
class FileStorageAclModify:
    """Schema for modifying an existing ACL.

    Attributes:
        name (str | Unset): A resource name.
        target (str | Unset): The target of the ACL entry. It can be an IP Address, Network Prefix or a wildcard.
        permission (FileStoragePermission | Unset): The permission level for the ACL target.
    """

    name: str | Unset = UNSET
    target: str | Unset = UNSET
    permission: FileStoragePermission | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        target = self.target

        permission: str | Unset = UNSET
        if not isinstance(self.permission, Unset):
            permission = self.permission.value

        field_dict: dict[str, Any] = {}

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

        _permission = d.pop("permission", UNSET)
        permission: FileStoragePermission | Unset
        if isinstance(_permission, Unset):
            permission = UNSET
        else:
            permission = FileStoragePermission(_permission)

        file_storage_acl_modify = cls(
            name=name,
            target=target,
            permission=permission,
        )

        return file_storage_acl_modify
