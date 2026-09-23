from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ServerSizesServerSizesServerSizeItem")


@_attrs_define
class ServerSizesServerSizesServerSizeItem:
    """
    Attributes:
        core_number (str): Number of CPU cores
        memory_amount (str): Amount of memory in MB
    """

    core_number: str
    memory_amount: str

    def to_dict(self) -> dict[str, Any]:
        core_number = self.core_number

        memory_amount = self.memory_amount

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "core_number": core_number,
                "memory_amount": memory_amount,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        core_number = d.pop("core_number")

        memory_amount = d.pop("memory_amount")

        server_sizes_server_sizes_server_size_item = cls(
            core_number=core_number,
            memory_amount=memory_amount,
        )

        return server_sizes_server_sizes_server_size_item
