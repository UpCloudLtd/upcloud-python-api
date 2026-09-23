from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="StorageLabel")


@_attrs_define
class StorageLabel:
    """A key/value pair to label and categorize resources

    Example:
        {'key': 'env', 'value': 'production'}

    Attributes:
        key (str): Label key used to classify the resource
        value (str): Value associated with the label key
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

        storage_label = cls(
            key=key,
            value=value,
        )

        return storage_label
