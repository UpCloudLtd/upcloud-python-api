from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.modify_storage_body_storage import ModifyStorageBodyStorage


T = TypeVar("T", bound="ModifyStorageBody")


@_attrs_define
class ModifyStorageBody:
    """Request schema for modifying block storage properties.

    Example:
        {'storage': {'size': 100, 'title': 'Production data expanded'}}

    Attributes:
        storage (ModifyStorageBodyStorage): Block storage properties to modify.
    """

    storage: ModifyStorageBodyStorage

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
        from ..models.modify_storage_body_storage import ModifyStorageBodyStorage  # noqa: PLC0415

        d = dict(src_dict)
        storage = ModifyStorageBodyStorage.from_dict(d.pop("storage"))

        modify_storage_body = cls(
            storage=storage,
        )

        return modify_storage_body
