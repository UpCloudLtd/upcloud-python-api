from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_service_properties_opensearch_shard_indexing_pressure_primary_parameter_node import (
        DatabaseServicePropertiesOpensearchShardIndexingPressurePrimaryParameterNode,
    )
    from ..models.database_service_properties_opensearch_shard_indexing_pressure_primary_parameter_shard import (
        DatabaseServicePropertiesOpensearchShardIndexingPressurePrimaryParameterShard,
    )


T = TypeVar("T", bound="DatabaseServicePropertiesOpensearchShardIndexingPressurePrimaryParameter")


@_attrs_define
class DatabaseServicePropertiesOpensearchShardIndexingPressurePrimaryParameter:
    """
    Attributes:
        node (DatabaseServicePropertiesOpensearchShardIndexingPressurePrimaryParameterNode | Unset):
        shard (DatabaseServicePropertiesOpensearchShardIndexingPressurePrimaryParameterShard | Unset):
    """

    node: DatabaseServicePropertiesOpensearchShardIndexingPressurePrimaryParameterNode | Unset = UNSET
    shard: DatabaseServicePropertiesOpensearchShardIndexingPressurePrimaryParameterShard | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        node: dict[str, Any] | Unset = UNSET
        if not isinstance(self.node, Unset):
            node = self.node.to_dict()

        shard: dict[str, Any] | Unset = UNSET
        if not isinstance(self.shard, Unset):
            shard = self.shard.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if node is not UNSET:
            field_dict["node"] = node
        if shard is not UNSET:
            field_dict["shard"] = shard

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_service_properties_opensearch_shard_indexing_pressure_primary_parameter_node import (
            DatabaseServicePropertiesOpensearchShardIndexingPressurePrimaryParameterNode,  # noqa: PLC0415
        )
        from ..models.database_service_properties_opensearch_shard_indexing_pressure_primary_parameter_shard import (
            DatabaseServicePropertiesOpensearchShardIndexingPressurePrimaryParameterShard,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _node = d.pop("node", UNSET)
        node: DatabaseServicePropertiesOpensearchShardIndexingPressurePrimaryParameterNode | Unset
        if isinstance(_node, Unset):
            node = UNSET
        else:
            node = DatabaseServicePropertiesOpensearchShardIndexingPressurePrimaryParameterNode.from_dict(_node)

        _shard = d.pop("shard", UNSET)
        shard: DatabaseServicePropertiesOpensearchShardIndexingPressurePrimaryParameterShard | Unset
        if isinstance(_shard, Unset):
            shard = UNSET
        else:
            shard = DatabaseServicePropertiesOpensearchShardIndexingPressurePrimaryParameterShard.from_dict(_shard)

        database_service_properties_opensearch_shard_indexing_pressure_primary_parameter = cls(
            node=node,
            shard=shard,
        )

        return database_service_properties_opensearch_shard_indexing_pressure_primary_parameter
