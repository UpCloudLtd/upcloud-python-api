from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.file_storage_acl_create import FileStorageAclCreate


T = TypeVar("T", bound="FileStorageShareCreate")


@_attrs_define
class FileStorageShareCreate:
    """Schema for creating a new share with access control lists (ACLs).

    Attributes:
        name (str): A resource name.
        path (str): The absolute path of the share.
        acl (list[FileStorageAclCreate]):
    """

    name: str
    path: str
    acl: list[FileStorageAclCreate]

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        path = self.path

        acl = []
        for acl_item_data in self.acl:
            acl_item = acl_item_data.to_dict()
            acl.append(acl_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "path": path,
                "acl": acl,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_storage_acl_create import FileStorageAclCreate  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        path = d.pop("path")

        acl = []
        _acl = d.pop("acl")
        for acl_item_data in _acl:
            acl_item = FileStorageAclCreate.from_dict(acl_item_data)

            acl.append(acl_item)

        file_storage_share_create = cls(
            name=name,
            path=path,
            acl=acl,
        )

        return file_storage_share_create
