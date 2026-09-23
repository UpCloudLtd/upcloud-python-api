from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseServicePropertiesOpensearchShardIndexingPressureOperatingFactor")


@_attrs_define
class DatabaseServicePropertiesOpensearchShardIndexingPressureOperatingFactor:
    """
    Attributes:
        lower (float | Unset): Specify the lower occupancy limit of the allocated quota of memory for the shard.
                                If the total memory usage of a shard is below this limit,
                                shard indexing backpressure decreases the current allocated memory for that shard.
                                Default is 0.75
        optimal (float | Unset): Specify the optimal occupancy of the allocated quota of memory for the shard.
                                If the total memory usage of a shard is at this level,
                                shard indexing backpressure doesn’t change the current allocated memory for that shard.
                                Default is 0.85
        upper (float | Unset): Specify the upper occupancy limit of the allocated quota of memory for the shard.
                                If the total memory usage of a shard is above this limit,
                                shard indexing backpressure increases the current allocated memory for that shard.
                                Default is 0.95
    """

    lower: float | Unset = UNSET
    optimal: float | Unset = UNSET
    upper: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        lower = self.lower

        optimal = self.optimal

        upper = self.upper

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if lower is not UNSET:
            field_dict["lower"] = lower
        if optimal is not UNSET:
            field_dict["optimal"] = optimal
        if upper is not UNSET:
            field_dict["upper"] = upper

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        lower = d.pop("lower", UNSET)

        optimal = d.pop("optimal", UNSET)

        upper = d.pop("upper", UNSET)

        database_service_properties_opensearch_shard_indexing_pressure_operating_factor = cls(
            lower=lower,
            optimal=optimal,
            upper=upper,
        )

        return database_service_properties_opensearch_shard_indexing_pressure_operating_factor
