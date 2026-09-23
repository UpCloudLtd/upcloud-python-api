from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseLabelModify")


@_attrs_define
class DatabaseLabelModify:
    """Schema for modifying a label with a key and/or value.

    Attributes:
        key (str | Unset): The key of a label.
        value (str | Unset): The value of a label.
    """

    key: str | Unset = UNSET
    value: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key", UNSET)

        value = d.pop("value", UNSET)

        database_label_modify = cls(
            key=key,
            value=value,
        )

        return database_label_modify
