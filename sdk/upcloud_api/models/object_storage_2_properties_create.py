from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ObjectStorage2PropertiesCreate")


@_attrs_define
class ObjectStorage2PropertiesCreate:
    """Schema for creating properties with an optional access control origin override.

    Attributes:
        access_control_origin_override (str | Unset):  Example: https://mycompany.com.
    """

    access_control_origin_override: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        access_control_origin_override = self.access_control_origin_override

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if access_control_origin_override is not UNSET:
            field_dict["access_control_origin_override"] = access_control_origin_override

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_control_origin_override = d.pop("access_control_origin_override", UNSET)

        object_storage_2_properties_create = cls(
            access_control_origin_override=access_control_origin_override,
        )

        return object_storage_2_properties_create
