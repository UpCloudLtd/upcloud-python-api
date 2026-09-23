from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ObjectStorage2PolicyAttachmentCreate")


@_attrs_define
class ObjectStorage2PolicyAttachmentCreate:
    """Schema for creating a policy attachment.

    Attributes:
        name (str): Name of the policy to attach. Example: test-policy.
    """

    name: str

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        object_storage_2_policy_attachment_create = cls(
            name=name,
        )

        return object_storage_2_policy_attachment_create
