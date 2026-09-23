from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseServicePropertiesOpensearchShardIndexingPressurePrimaryParameterShard")


@_attrs_define
class DatabaseServicePropertiesOpensearchShardIndexingPressurePrimaryParameterShard:
    """
    Attributes:
        min_limit (float | Unset): Specify the minimum assigned quota for a new shard in any role (coordinator, primary,
            or replica).
                                        Shard indexing backpressure increases or decreases this allocated quota based on the
            inflow of traffic for the shard.
                                        Default is 0.001
    """

    min_limit: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        min_limit = self.min_limit

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if min_limit is not UNSET:
            field_dict["min_limit"] = min_limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        min_limit = d.pop("min_limit", UNSET)

        database_service_properties_opensearch_shard_indexing_pressure_primary_parameter_shard = cls(
            min_limit=min_limit,
        )

        return database_service_properties_opensearch_shard_indexing_pressure_primary_parameter_shard
