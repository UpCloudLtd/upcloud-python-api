from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="ServerDetachStorage")


@_attrs_define
class ServerDetachStorage:
    """Parameters for detaching a storage device from a Cloud Server.

    Example:
        {'storage_device': {'address': 'virtio:0'}}

    Attributes:
        storage_device (Any): Storage device to detach, identified by either its device address or storage resource
            UUID.
    """

    storage_device: Any

    def to_dict(self) -> dict[str, Any]:
        storage_device: Any
        storage_device = self.storage_device

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "storage_device": storage_device,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_storage_device(data: object) -> Any:
            return cast(Any, data)

        storage_device = _parse_storage_device(d.pop("storage_device"))

        server_detach_storage = cls(
            storage_device=storage_device,
        )

        return server_detach_storage
