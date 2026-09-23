from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ObjectStorage2InlinePolicyResponse")


@_attrs_define
class ObjectStorage2InlinePolicyResponse:
    """Schema representing an inline policy response.

    Attributes:
        document (str | Unset):  Example: ECSS3FullAccess.
        name (str | Unset):  Example:
            {"Version":"2012-10-17","Statement":[{"Action":"sts:AssumeRole","Effect":"Allow","Resource":"*"}]}.
    """

    document: str | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        document = self.document

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if document is not UNSET:
            field_dict["document"] = document
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        document = d.pop("document", UNSET)

        name = d.pop("name", UNSET)

        object_storage_2_inline_policy_response = cls(
            document=document,
            name=name,
        )

        object_storage_2_inline_policy_response.additional_properties = d
        return object_storage_2_inline_policy_response

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
