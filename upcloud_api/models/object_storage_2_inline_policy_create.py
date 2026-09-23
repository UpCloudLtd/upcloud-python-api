from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ObjectStorage2InlinePolicyCreate")


@_attrs_define
class ObjectStorage2InlinePolicyCreate:
    """Schema for creating an inline policy.

    Attributes:
        name (str): Name of the inline policy. Example: ECSS3FullAccess.
        document (str): A valid policy document. Example:
            {"Version":"2012-10-17","Statement":[{"Action":"sts:AssumeRole","Effect":"Allow","Resource":"*"}]}.
    """

    name: str
    document: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        document = self.document

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "document": document,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        document = d.pop("document")

        object_storage_2_inline_policy_create = cls(
            name=name,
            document=document,
        )

        object_storage_2_inline_policy_create.additional_properties = d
        return object_storage_2_inline_policy_create

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
