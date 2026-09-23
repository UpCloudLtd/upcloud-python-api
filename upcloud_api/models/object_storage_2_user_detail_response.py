from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.object_storage_2_access_key_detail_response import ObjectStorage2AccessKeyDetailResponse
    from ..models.object_storage_2_policy_attachment_response import ObjectStorage2PolicyAttachmentResponse
    from ..models.object_storage_2_tag_response import ObjectStorage2TagResponse


T = TypeVar("T", bound="ObjectStorage2UserDetailResponse")


@_attrs_define
class ObjectStorage2UserDetailResponse:
    """Response schema for user details.

    Attributes:
        username (str | Unset):
        arn (str | Unset):
        created_at (datetime.datetime | Unset):
        access_keys (list[ObjectStorage2AccessKeyDetailResponse] | Unset):
        policies (list[ObjectStorage2PolicyAttachmentResponse] | Unset):
        tags (list[ObjectStorage2TagResponse] | Unset):
        permissions_boundary (str | Unset): Schema representing a permissions boundary response.
    """

    username: str | Unset = UNSET
    arn: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    access_keys: list[ObjectStorage2AccessKeyDetailResponse] | Unset = UNSET
    policies: list[ObjectStorage2PolicyAttachmentResponse] | Unset = UNSET
    tags: list[ObjectStorage2TagResponse] | Unset = UNSET
    permissions_boundary: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        arn = self.arn

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        access_keys: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.access_keys, Unset):
            access_keys = []
            for access_keys_item_data in self.access_keys:
                access_keys_item = access_keys_item_data.to_dict()
                access_keys.append(access_keys_item)

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

        permissions_boundary = self.permissions_boundary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if username is not UNSET:
            field_dict["username"] = username
        if arn is not UNSET:
            field_dict["arn"] = arn
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if access_keys is not UNSET:
            field_dict["access_keys"] = access_keys
        if policies is not UNSET:
            field_dict["policies"] = policies
        if tags is not UNSET:
            field_dict["tags"] = tags
        if permissions_boundary is not UNSET:
            field_dict["permissions_boundary"] = permissions_boundary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.object_storage_2_access_key_detail_response import (
            ObjectStorage2AccessKeyDetailResponse,  # noqa: PLC0415
        )
        from ..models.object_storage_2_policy_attachment_response import (
            ObjectStorage2PolicyAttachmentResponse,  # noqa: PLC0415
        )
        from ..models.object_storage_2_tag_response import ObjectStorage2TagResponse  # noqa: PLC0415

        d = dict(src_dict)
        username = d.pop("username", UNSET)

        arn = d.pop("arn", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        _access_keys = d.pop("access_keys", UNSET)
        access_keys: list[ObjectStorage2AccessKeyDetailResponse] | Unset = UNSET
        if _access_keys is not UNSET:
            access_keys = []
            for access_keys_item_data in _access_keys:
                access_keys_item = ObjectStorage2AccessKeyDetailResponse.from_dict(access_keys_item_data)

                access_keys.append(access_keys_item)

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

        permissions_boundary = d.pop("permissions_boundary", UNSET)

        object_storage_2_user_detail_response = cls(
            username=username,
            arn=arn,
            created_at=created_at,
            access_keys=access_keys,
            policies=policies,
            tags=tags,
            permissions_boundary=permissions_boundary,
        )

        object_storage_2_user_detail_response.additional_properties = d
        return object_storage_2_user_detail_response

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
