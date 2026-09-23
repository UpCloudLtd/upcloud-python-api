from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="CreateStorageTemplateRequestStorage")


@_attrs_define
class CreateStorageTemplateRequestStorage:
    """Parameters for creating a template from the block storage.

    Attributes:
        title (str): A short, informational description of the template.
    """

    title: str

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "title": title,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        create_storage_template_request_storage = cls(
            title=title,
        )

        return create_storage_template_request_storage
