from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ObjectStorage2BucketDetailResponse")


@_attrs_define
class ObjectStorage2BucketDetailResponse:
    """Response schema for bucket details.

    Attributes:
        name (str | Unset):  Example: my-bucket-1.
        total_objects (int | Unset):
        total_size_bytes (int | Unset):
        deleted (bool | Unset):  Example: False.
    """

    name: str | Unset = UNSET
    total_objects: int | Unset = UNSET
    total_size_bytes: int | Unset = UNSET
    deleted: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        total_objects = self.total_objects

        total_size_bytes = self.total_size_bytes

        deleted = self.deleted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if total_objects is not UNSET:
            field_dict["total_objects"] = total_objects
        if total_size_bytes is not UNSET:
            field_dict["total_size_bytes"] = total_size_bytes
        if deleted is not UNSET:
            field_dict["deleted"] = deleted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        total_objects = d.pop("total_objects", UNSET)

        total_size_bytes = d.pop("total_size_bytes", UNSET)

        deleted = d.pop("deleted", UNSET)

        object_storage_2_bucket_detail_response = cls(
            name=name,
            total_objects=total_objects,
            total_size_bytes=total_size_bytes,
            deleted=deleted,
        )

        object_storage_2_bucket_detail_response.additional_properties = d
        return object_storage_2_bucket_detail_response

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
