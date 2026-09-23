from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.create_storage_template_request_storage import CreateStorageTemplateRequestStorage


T = TypeVar("T", bound="CreateStorageTemplateRequest")


@_attrs_define
class CreateStorageTemplateRequest:
    """Request schema for creating a template from a block storage resource.

    Example:
        {'storage': {'title': 'My server template'}}

    Attributes:
        storage (CreateStorageTemplateRequestStorage): Parameters for creating a template from the block storage.
    """

    storage: CreateStorageTemplateRequestStorage

    def to_dict(self) -> dict[str, Any]:
        storage = self.storage.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "storage": storage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_storage_template_request_storage import (
            CreateStorageTemplateRequestStorage,  # noqa: PLC0415
        )

        d = dict(src_dict)
        storage = CreateStorageTemplateRequestStorage.from_dict(d.pop("storage"))

        create_storage_template_request = cls(
            storage=storage,
        )

        return create_storage_template_request
