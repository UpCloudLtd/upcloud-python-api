from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ObjectStorage2BucketCreate")


@_attrs_define
class ObjectStorage2BucketCreate:
    """Schema for creating a new bucket.

    Attributes:
        name (str): Must be unique within the service, and should contain only alphanumeric, .,- and _. Example: my-
            bucket-1.
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

        object_storage_2_bucket_create = cls(
            name=name,
        )

        return object_storage_2_bucket_create
