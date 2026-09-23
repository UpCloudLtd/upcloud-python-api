from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseServicePropertiesOpensearchShardIndexingPressurePrimaryParameterNode")


@_attrs_define
class DatabaseServicePropertiesOpensearchShardIndexingPressurePrimaryParameterNode:
    """
    Attributes:
        soft_limit (float | Unset): Define the percentage of the node-level memory
                                        threshold that acts as a soft indicator for strain on a node.
                                        Default is 0.7
    """

    soft_limit: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        soft_limit = self.soft_limit

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if soft_limit is not UNSET:
            field_dict["soft_limit"] = soft_limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        soft_limit = d.pop("soft_limit", UNSET)

        database_service_properties_opensearch_shard_indexing_pressure_primary_parameter_node = cls(
            soft_limit=soft_limit,
        )

        return database_service_properties_opensearch_shard_indexing_pressure_primary_parameter_node
