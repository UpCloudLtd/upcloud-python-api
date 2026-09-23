from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ObjectStorage2ServiceDetailResponseUsage")


@_attrs_define
class ObjectStorage2ServiceDetailResponseUsage:
    """
    Attributes:
        total_size_bytes (int | Unset):  Example: 32414921734.
        total_objects (int | Unset):  Example: 310499.
    """

    total_size_bytes: int | Unset = UNSET
    total_objects: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_size_bytes = self.total_size_bytes

        total_objects = self.total_objects

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_size_bytes is not UNSET:
            field_dict["total_size_bytes"] = total_size_bytes
        if total_objects is not UNSET:
            field_dict["total_objects"] = total_objects

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_size_bytes = d.pop("total_size_bytes", UNSET)

        total_objects = d.pop("total_objects", UNSET)

        object_storage_2_service_detail_response_usage = cls(
            total_size_bytes=total_size_bytes,
            total_objects=total_objects,
        )

        object_storage_2_service_detail_response_usage.additional_properties = d
        return object_storage_2_service_detail_response_usage

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
