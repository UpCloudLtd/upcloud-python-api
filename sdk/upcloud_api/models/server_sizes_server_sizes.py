from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.server_sizes_server_sizes_server_size_item import ServerSizesServerSizesServerSizeItem


T = TypeVar("T", bound="ServerSizesServerSizes")


@_attrs_define
class ServerSizesServerSizes:
    """
    Example:
        {'server_size': [{'core_number': '2', 'memory_amount': '4096'}]}

    Attributes:
        server_size (list[ServerSizesServerSizesServerSizeItem]):  Example: [{'core_number': '2', 'memory_amount':
            '4096'}].
    """

    server_size: list[ServerSizesServerSizesServerSizeItem]

    def to_dict(self) -> dict[str, Any]:
        server_size = []
        for server_size_item_data in self.server_size:
            server_size_item = server_size_item_data.to_dict()
            server_size.append(server_size_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "server_size": server_size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_sizes_server_sizes_server_size_item import (
            ServerSizesServerSizesServerSizeItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        server_size = []
        _server_size = d.pop("server_size")
        for server_size_item_data in _server_size:
            server_size_item = ServerSizesServerSizesServerSizeItem.from_dict(server_size_item_data)

            server_size.append(server_size_item)

        server_sizes_server_sizes = cls(
            server_size=server_size,
        )

        return server_sizes_server_sizes
