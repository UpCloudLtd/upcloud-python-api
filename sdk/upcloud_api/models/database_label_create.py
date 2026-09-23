from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="DatabaseLabelCreate")


@_attrs_define
class DatabaseLabelCreate:
    """Schema for creating a label with a key and value.

    Attributes:
        key (str): The key of a label.
        value (str): The value of a label.
    """

    key: str
    value: str

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "key": key,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        value = d.pop("value")

        database_label_create = cls(
            key=key,
            value=value,
        )

        return database_label_create
