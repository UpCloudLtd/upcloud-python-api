from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ObjectStorage2UserCreate")


@_attrs_define
class ObjectStorage2UserCreate:
    """Schema for creating a new user.

    Attributes:
        username (str): The name of the user to create. Example: example_user.
    """

    username: str

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "username": username,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        username = d.pop("username")

        object_storage_2_user_create = cls(
            username=username,
        )

        return object_storage_2_user_create
