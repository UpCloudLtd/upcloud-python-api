from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.permission_document import PermissionDocument


T = TypeVar("T", bound="Permission")


@_attrs_define
class Permission:
    """A single permission object.

    Attributes:
        permission (PermissionDocument | Unset): Permission document defining access rights for a sub-account to a
            specific resource. Example: {'options': {'storage': 'yes'}, 'target_identifier':
            '00e1d79f-d2d8-40ca-a68d-812655b34766', 'target_type': 'server', 'user': 'test'}.
    """

    permission: PermissionDocument | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        permission: dict[str, Any] | Unset = UNSET
        if not isinstance(self.permission, Unset):
            permission = self.permission.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if permission is not UNSET:
            field_dict["permission"] = permission

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.permission_document import PermissionDocument  # noqa: PLC0415

        d = dict(src_dict)
        _permission = d.pop("permission", UNSET)
        permission: PermissionDocument | Unset
        if isinstance(_permission, Unset):
            permission = UNSET
        else:
            permission = PermissionDocument.from_dict(_permission)

        permission = cls(
            permission=permission,
        )

        permission.additional_properties = d
        return permission

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
