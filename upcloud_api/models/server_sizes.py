from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.server_sizes_server_sizes import ServerSizesServerSizes


T = TypeVar("T", bound="ServerSizes")


@_attrs_define
class ServerSizes:
    """List of server sizes

    Example:
        {'server_sizes': {'server_size': [{'core_number': '2', 'memory_amount': '4096'}, {'core_number': '4',
            'memory_amount': '8192'}]}}

    Attributes:
        server_sizes (ServerSizesServerSizes):  Example: {'server_size': [{'core_number': '2', 'memory_amount':
            '4096'}]}.
    """

    server_sizes: ServerSizesServerSizes

    def to_dict(self) -> dict[str, Any]:
        server_sizes = self.server_sizes.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "server_sizes": server_sizes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_sizes_server_sizes import ServerSizesServerSizes  # noqa: PLC0415

        d = dict(src_dict)
        server_sizes = ServerSizesServerSizes.from_dict(d.pop("server_sizes"))

        server_sizes = cls(
            server_sizes=server_sizes,
        )

        return server_sizes
