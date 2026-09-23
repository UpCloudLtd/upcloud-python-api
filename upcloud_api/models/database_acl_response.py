from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseAclResponse")


@_attrs_define
class DatabaseAclResponse:
    """Response schema for an Access Control List (ACL) entry.

    Attributes:
        id (UUID | Unset): Unique identifier for the ACL entry. Example: 123e4567-e89b-12d3-a456-426614174000.
        permission (str | Unset): The permission level for the ACL entry. Example: read-write.
        topic (str | Unset): The topic associated with the ACL entry. Example: sensors/temperature.
        username (str | Unset): The username associated with the ACL entry. Example: user123.
    """

    id: UUID | Unset = UNSET
    permission: str | Unset = UNSET
    topic: str | Unset = UNSET
    username: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        permission = self.permission

        topic = self.topic

        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if permission is not UNSET:
            field_dict["permission"] = permission
        if topic is not UNSET:
            field_dict["topic"] = topic
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        permission = d.pop("permission", UNSET)

        topic = d.pop("topic", UNSET)

        username = d.pop("username", UNSET)

        database_acl_response = cls(
            id=id,
            permission=permission,
            topic=topic,
            username=username,
        )

        database_acl_response.additional_properties = d
        return database_acl_response

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
