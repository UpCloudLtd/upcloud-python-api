from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ObjectStorage2RoleTag")


@_attrs_define
class ObjectStorage2RoleTag:
    """Schema for tagging roles with key-value pairs.

    Attributes:
        key (str): The key of a tag.
        value (str | Unset): The value of a tag.
    """

    key: str
    value: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "key": key,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        value = d.pop("value", UNSET)

        object_storage_2_role_tag = cls(
            key=key,
            value=value,
        )

        return object_storage_2_role_tag
