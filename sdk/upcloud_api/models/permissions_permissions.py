from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.permission_document import PermissionDocument


T = TypeVar("T", bound="PermissionsPermissions")


@_attrs_define
class PermissionsPermissions:
    """
    Attributes:
        permission (list[PermissionDocument]):
    """

    permission: list[PermissionDocument]

    def to_dict(self) -> dict[str, Any]:
        permission = []
        for permission_item_data in self.permission:
            permission_item = permission_item_data.to_dict()
            permission.append(permission_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "permission": permission,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.permission_document import PermissionDocument  # noqa: PLC0415

        d = dict(src_dict)
        permission = []
        _permission = d.pop("permission")
        for permission_item_data in _permission:
            permission_item = PermissionDocument.from_dict(permission_item_data)

            permission.append(permission_item)

        permissions_permissions = cls(
            permission=permission,
        )

        return permissions_permissions
