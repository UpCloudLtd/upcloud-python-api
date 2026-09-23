from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="FileStorageLabelCreate")


@_attrs_define
class FileStorageLabelCreate:
    """Schema for creating a new label.

    Attributes:
        key (str): Represents the label identifier. The key is unique within a service.
        value (None | str): Represents the label value.
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

        file_storage_label_create = cls(
            key=key,
            value=value,
        )

        return file_storage_label_create
