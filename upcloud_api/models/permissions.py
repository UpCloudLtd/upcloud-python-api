from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.permissions_permissions import PermissionsPermissions


T = TypeVar("T", bound="Permissions")


@_attrs_define
class Permissions:
    """List of permissions.

    Example:
        {'permissions': {'permission': [{'user': 'subaccount1', 'target_type': 'server', 'target_identifier':
            '00e1d79f-d2d8-40ca-a68d-812655b34766', 'options': {'storage': 'yes'}}, {'user': 'subaccount2', 'target_type':
            'storage', 'target_identifier': '01f6d5e3-c3b2-41ba-912a-723ab2c12345'}]}}

    Attributes:
        permissions (PermissionsPermissions):
    """

    permissions: PermissionsPermissions

    def to_dict(self) -> dict[str, Any]:
        permissions = self.permissions.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "permissions": permissions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.permissions_permissions import PermissionsPermissions  # noqa: PLC0415

        d = dict(src_dict)
        permissions = PermissionsPermissions.from_dict(d.pop("permissions"))

        permissions = cls(
            permissions=permissions,
        )

        return permissions
