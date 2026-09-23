from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="ObjectStorage2LabelCreate")


@_attrs_define
class ObjectStorage2LabelCreate:
    """Schema for creating a label with a key-value pair.

    Attributes:
        key (str): The key of a label.
        value (None | str): Schema for a label value property, allowing a string or null with specific character
            constraints.
    """

    key: str
    value: None | str

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        value: None | str
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

        def _parse_value(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        value = _parse_value(d.pop("value"))

        object_storage_2_label_create = cls(
            key=key,
            value=value,
        )

        return object_storage_2_label_create
