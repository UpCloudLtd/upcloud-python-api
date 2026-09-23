from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.file_storage_permission import FileStoragePermission

T = TypeVar("T", bound="FileStorageAclCreate")


@_attrs_define
class FileStorageAclCreate:
    """Schema for creating an ACL entry.

    Attributes:
        name (str): A resource name.
        target (str): The target of the ACL entry. It can be an IP Address, Network Prefix or a wildcard.
        permission (FileStoragePermission): The permission level for the ACL target.
    """

    name: str
    target: str
    permission: FileStoragePermission

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        target = self.target

        permission = self.permission.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "target": target,
                "permission": permission,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        target = d.pop("target")

        permission = FileStoragePermission(d.pop("permission"))

        file_storage_acl_create = cls(
            name=name,
            target=target,
            permission=permission,
        )

        return file_storage_acl_create
