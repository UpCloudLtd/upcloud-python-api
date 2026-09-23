from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ObjectStorage2GroupCreate")


@_attrs_define
class ObjectStorage2GroupCreate:
    """Schema for creating a new IAM group.

    Attributes:
        name (str): A valid string to represent the name of the IAM group. Example: new-group.
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

        object_storage_2_group_create = cls(
            name=name,
        )

        return object_storage_2_group_create
