from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ObjectStorage2AssumeRolePolicyRequest")


@_attrs_define
class ObjectStorage2AssumeRolePolicyRequest:
    """Schema for the request to assume a role with a policy document.

    Attributes:
        document (str): The assume role policy document that grants an entity permission to assume the role. Example: {"
            Version":"2012-10-
            17","Statement":[{"Effect":"Allow","Principal":{"Service":"backup.upcloud.com"},"Action":"sts:AssumeRole"}]}.
    """

    document: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        document = self.document

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "document": document,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        document = d.pop("document")

        object_storage_2_assume_role_policy_request = cls(
            document=document,
        )

        object_storage_2_assume_role_policy_request.additional_properties = d
        return object_storage_2_assume_role_policy_request

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
