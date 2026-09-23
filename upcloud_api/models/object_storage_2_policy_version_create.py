from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ObjectStorage2PolicyVersionCreate")


@_attrs_define
class ObjectStorage2PolicyVersionCreate:
    """Schema for creating a new version of a policy.

    Attributes:
        document (str): A valid, URL-encoded policy document. Example:
            {"Version":"2012-10-17","Statement":[{"Action":["*"],"Effect":"Deny","Resource":"*"}]}.
        is_default (bool): Set this version as the default. Default: False.
    """

    document: str
    is_default: bool = False

    def to_dict(self) -> dict[str, Any]:
        document = self.document

        is_default = self.is_default

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "document": document,
                "is_default": is_default,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        document = d.pop("document")

        is_default = d.pop("is_default")

        object_storage_2_policy_version_create = cls(
            document=document,
            is_default=is_default,
        )

        return object_storage_2_policy_version_create
