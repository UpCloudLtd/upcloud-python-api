from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ObjectStorage2PolicyCreate")


@_attrs_define
class ObjectStorage2PolicyCreate:
    """Schema for creating a policy with a name, description, and document.

    Attributes:
        name (str): Unique name of the policy. Example: example-policy.
        document (str): A valid, URL-encoded policy document. Example: %7B%22Version%22%3A%20%222012-10-
            17%22%2C%20%20%22Statement%22%3A%20%5B%7B%22Action%22%3A%20%5B%22iam%3AGetUser%22%5D%2C%20%22Resource%22%3A%20%2
            2%2A%22%2C%20%22Effect%22%3A%20%22Allow%22%2C%20%22Sid%22%3A%20%22editor%22%7D%5D%7D.
        description (str | Unset): The policy description. Example: example-description.
    """

    name: str
    document: str
    description: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        document = self.document

        description = self.description

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "document": document,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        document = d.pop("document")

        description = d.pop("description", UNSET)

        object_storage_2_policy_create = cls(
            name=name,
            document=document,
            description=description,
        )

        return object_storage_2_policy_create
