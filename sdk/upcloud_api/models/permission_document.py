from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.permission_target_type import PermissionTargetType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.permission_document_options import PermissionDocumentOptions


T = TypeVar("T", bound="PermissionDocument")


@_attrs_define
class PermissionDocument:
    """Permission document defining access rights for a sub-account to a specific resource.

    Example:
        {'options': {'storage': 'yes'}, 'target_identifier': '00e1d79f-d2d8-40ca-a68d-812655b34766', 'target_type':
            'server', 'user': 'test'}

    Attributes:
        target_identifier (str): Target identifying string. This is type specific and in most cases is a UUID4. Wildcard
            value "*" can be used to
            reference all target resources.
        target_type (PermissionTargetType): Type of the target to grant permission to
        user (str): Username for an account.
        options (PermissionDocumentOptions | Unset): Target specific options.
    """

    target_identifier: str
    target_type: PermissionTargetType
    user: str
    options: PermissionDocumentOptions | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        target_identifier = self.target_identifier

        target_type = self.target_type.value

        user = self.user

        options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "target_identifier": target_identifier,
                "target_type": target_type,
                "user": user,
            }
        )
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.permission_document_options import PermissionDocumentOptions  # noqa: PLC0415

        d = dict(src_dict)
        target_identifier = d.pop("target_identifier")

        target_type = PermissionTargetType(d.pop("target_type"))

        user = d.pop("user")

        _options = d.pop("options", UNSET)
        options: PermissionDocumentOptions | Unset
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = PermissionDocumentOptions.from_dict(_options)

        permission_document = cls(
            target_identifier=target_identifier,
            target_type=target_type,
            user=user,
            options=options,
        )

        return permission_document
