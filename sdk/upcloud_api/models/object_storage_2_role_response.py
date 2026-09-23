from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.object_storage_2_policy_attachment_response import ObjectStorage2PolicyAttachmentResponse
    from ..models.object_storage_2_role_response_inline_policies_item import (
        ObjectStorage2RoleResponseInlinePoliciesItem,
    )
    from ..models.object_storage_2_tag_response import ObjectStorage2TagResponse


T = TypeVar("T", bound="ObjectStorage2RoleResponse")


@_attrs_define
class ObjectStorage2RoleResponse:
    """Response schema for detailed information about a specific role.

    Attributes:
        arn (str | Unset):
        assume_role_policy_document (str | Unset):
        created_at (datetime.datetime | Unset):
        description (str | Unset):
        inline_policies (list[ObjectStorage2RoleResponseInlinePoliciesItem] | Unset):
        max_session_duration (int | Unset):
        name (str | Unset):
        permissions_boundary (str | Unset):
        policies (list[ObjectStorage2PolicyAttachmentResponse] | Unset):
        tags (list[ObjectStorage2TagResponse] | Unset):
    """

    arn: str | Unset = UNSET
    assume_role_policy_document: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    description: str | Unset = UNSET
    inline_policies: list[ObjectStorage2RoleResponseInlinePoliciesItem] | Unset = UNSET
    max_session_duration: int | Unset = UNSET
    name: str | Unset = UNSET
    permissions_boundary: str | Unset = UNSET
    policies: list[ObjectStorage2PolicyAttachmentResponse] | Unset = UNSET
    tags: list[ObjectStorage2TagResponse] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        arn = self.arn

        assume_role_policy_document = self.assume_role_policy_document

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        description = self.description

        inline_policies: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.inline_policies, Unset):
            inline_policies = []
            for inline_policies_item_data in self.inline_policies:
                inline_policies_item = inline_policies_item_data.to_dict()
                inline_policies.append(inline_policies_item)

        max_session_duration = self.max_session_duration

        name = self.name

        permissions_boundary = self.permissions_boundary

        policies: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.policies, Unset):
            policies = []
            for policies_item_data in self.policies:
                policies_item = policies_item_data.to_dict()
                policies.append(policies_item)

        tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if arn is not UNSET:
            field_dict["arn"] = arn
        if assume_role_policy_document is not UNSET:
            field_dict["assume_role_policy_document"] = assume_role_policy_document
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if description is not UNSET:
            field_dict["description"] = description
        if inline_policies is not UNSET:
            field_dict["inline_policies"] = inline_policies
        if max_session_duration is not UNSET:
            field_dict["max_session_duration"] = max_session_duration
        if name is not UNSET:
            field_dict["name"] = name
        if permissions_boundary is not UNSET:
            field_dict["permissions_boundary"] = permissions_boundary
        if policies is not UNSET:
            field_dict["policies"] = policies
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.object_storage_2_policy_attachment_response import (
            ObjectStorage2PolicyAttachmentResponse,  # noqa: PLC0415
        )
        from ..models.object_storage_2_role_response_inline_policies_item import (
            ObjectStorage2RoleResponseInlinePoliciesItem,  # noqa: PLC0415
        )
        from ..models.object_storage_2_tag_response import ObjectStorage2TagResponse  # noqa: PLC0415

        d = dict(src_dict)
        arn = d.pop("arn", UNSET)

        assume_role_policy_document = d.pop("assume_role_policy_document", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        description = d.pop("description", UNSET)

        _inline_policies = d.pop("inline_policies", UNSET)
        inline_policies: list[ObjectStorage2RoleResponseInlinePoliciesItem] | Unset = UNSET
        if _inline_policies is not UNSET:
            inline_policies = []
            for inline_policies_item_data in _inline_policies:
                inline_policies_item = ObjectStorage2RoleResponseInlinePoliciesItem.from_dict(inline_policies_item_data)

                inline_policies.append(inline_policies_item)

        max_session_duration = d.pop("max_session_duration", UNSET)

        name = d.pop("name", UNSET)

        permissions_boundary = d.pop("permissions_boundary", UNSET)

        _policies = d.pop("policies", UNSET)
        policies: list[ObjectStorage2PolicyAttachmentResponse] | Unset = UNSET
        if _policies is not UNSET:
            policies = []
            for policies_item_data in _policies:
                policies_item = ObjectStorage2PolicyAttachmentResponse.from_dict(policies_item_data)

                policies.append(policies_item)

        _tags = d.pop("tags", UNSET)
        tags: list[ObjectStorage2TagResponse] | Unset = UNSET
        if _tags is not UNSET:
            tags = []
            for tags_item_data in _tags:
                tags_item = ObjectStorage2TagResponse.from_dict(tags_item_data)

                tags.append(tags_item)

        object_storage_2_role_response = cls(
            arn=arn,
            assume_role_policy_document=assume_role_policy_document,
            created_at=created_at,
            description=description,
            inline_policies=inline_policies,
            max_session_duration=max_session_duration,
            name=name,
            permissions_boundary=permissions_boundary,
            policies=policies,
            tags=tags,
        )

        object_storage_2_role_response.additional_properties = d
        return object_storage_2_role_response

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
