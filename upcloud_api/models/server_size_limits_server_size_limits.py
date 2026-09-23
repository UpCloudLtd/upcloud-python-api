from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ServerSizeLimitsServerSizeLimits")


@_attrs_define
class ServerSizeLimitsServerSizeLimits:
    """
    Example:
        {'core_number_min': 1, 'core_number_max': 64, 'memory_amount_min': 1024, 'memory_amount_max': 524288,
            'memory_amount_step': 1024}

    Attributes:
        core_number_min (int): Minimum number of CPU cores
        core_number_max (int): Maximum number of CPU cores
        memory_amount_min (int): Minimum amount of memory in MB
        memory_amount_max (int): Maximum amount of memory in MB
        memory_amount_step (int): Step size for memory allocation in MB
    """

    core_number_min: int
    core_number_max: int
    memory_amount_min: int
    memory_amount_max: int
    memory_amount_step: int

    def to_dict(self) -> dict[str, Any]:
        core_number_min = self.core_number_min

        core_number_max = self.core_number_max

        memory_amount_min = self.memory_amount_min

        memory_amount_max = self.memory_amount_max

        memory_amount_step = self.memory_amount_step

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "core_number_min": core_number_min,
                "core_number_max": core_number_max,
                "memory_amount_min": memory_amount_min,
                "memory_amount_max": memory_amount_max,
                "memory_amount_step": memory_amount_step,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        core_number_min = d.pop("core_number_min")

        core_number_max = d.pop("core_number_max")

        memory_amount_min = d.pop("memory_amount_min")

        memory_amount_max = d.pop("memory_amount_max")

        memory_amount_step = d.pop("memory_amount_step")

        server_size_limits_server_size_limits = cls(
            core_number_min=core_number_min,
            core_number_max=core_number_max,
            memory_amount_min=memory_amount_min,
            memory_amount_max=memory_amount_max,
            memory_amount_step=memory_amount_step,
        )

        return server_size_limits_server_size_limits
