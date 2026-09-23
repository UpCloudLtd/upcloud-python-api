from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.clone_storage_request_storage import CloneStorageRequestStorage


T = TypeVar("T", bound="CloneStorageRequest")


@_attrs_define
class CloneStorageRequest:
    """Request schema for cloning a block storage resource.

    Example:
        {'storage': {'encrypted': 'yes', 'tier': 'maxiops', 'title': 'Cloned Block Storage', 'zone': 'fi-hel1'}}

    Attributes:
        storage (CloneStorageRequestStorage): Parameters for the cloned block storage.
    """

    storage: CloneStorageRequestStorage

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
        from ..models.clone_storage_request_storage import CloneStorageRequestStorage  # noqa: PLC0415

        d = dict(src_dict)
        storage = CloneStorageRequestStorage.from_dict(d.pop("storage"))

        clone_storage_request = cls(
            storage=storage,
        )

        return clone_storage_request
