from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ObjectStorage2PolicyAttachmentResponse")


@_attrs_define
class ObjectStorage2PolicyAttachmentResponse:
    """Schema representing a policy attachment response.

    Attributes:
        arn (str | Unset):  Example: arn:upcloud:iam::01234567-89ab-cdef-0123-456789abcdef:policy/ECSReadOnlyAccess.
        name (str | Unset):  Example: ECSReadOnlyAccess.
    """

    arn: str | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        arn = self.arn

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if arn is not UNSET:
            field_dict["arn"] = arn
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        arn = d.pop("arn", UNSET)

        name = d.pop("name", UNSET)

        object_storage_2_policy_attachment_response = cls(
            arn=arn,
            name=name,
        )

        object_storage_2_policy_attachment_response.additional_properties = d
        return object_storage_2_policy_attachment_response

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
