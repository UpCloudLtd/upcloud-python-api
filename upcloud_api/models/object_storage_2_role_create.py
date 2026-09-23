from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.object_storage_2_role_tag import ObjectStorage2RoleTag


T = TypeVar("T", bound="ObjectStorage2RoleCreate")


@_attrs_define
class ObjectStorage2RoleCreate:
    """Schema for creating a new role.

    Attributes:
        name (str):  Example: test-role.
        assume_role_policy_document (str): The policy document that grants an entity permission to assume the role.
            Example: {"Version": "2012-10-17","Statement": [{"Action": "sts:AssumeRole","Principal": {"AWS":
            ["urn:ecs:iam::ns1:user/Demby"]},"Effect": "Allow","Resource": "*"}]}.
        description (str | Unset): Description of the role. Example: A test role..
        max_session_duration (int | Unset): Maximum session duration in seconds.
        permissions_boundary (str | Unset): Policy name to set as the permissions boundary. Example: test-policy.
        tags (list[ObjectStorage2RoleTag] | Unset): Tags to attach to the role (max 50).
    """

    name: str
    assume_role_policy_document: str
    description: str | Unset = UNSET
    max_session_duration: int | Unset = UNSET
    permissions_boundary: str | Unset = UNSET
    tags: list[ObjectStorage2RoleTag] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        assume_role_policy_document = self.assume_role_policy_document

        description = self.description

        max_session_duration = self.max_session_duration

        permissions_boundary = self.permissions_boundary

        tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "assume_role_policy_document": assume_role_policy_document,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if max_session_duration is not UNSET:
            field_dict["max_session_duration"] = max_session_duration
        if permissions_boundary is not UNSET:
            field_dict["permissions_boundary"] = permissions_boundary
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.object_storage_2_role_tag import ObjectStorage2RoleTag  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        assume_role_policy_document = d.pop("assume_role_policy_document")

        description = d.pop("description", UNSET)

        max_session_duration = d.pop("max_session_duration", UNSET)

        permissions_boundary = d.pop("permissions_boundary", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: list[ObjectStorage2RoleTag] | Unset = UNSET
        if _tags is not UNSET:
            tags = []
            for tags_item_data in _tags:
                tags_item = ObjectStorage2RoleTag.from_dict(tags_item_data)

                tags.append(tags_item)

        object_storage_2_role_create = cls(
            name=name,
            assume_role_policy_document=assume_role_policy_document,
            description=description,
            max_session_duration=max_session_duration,
            permissions_boundary=permissions_boundary,
            tags=tags,
        )

        return object_storage_2_role_create
