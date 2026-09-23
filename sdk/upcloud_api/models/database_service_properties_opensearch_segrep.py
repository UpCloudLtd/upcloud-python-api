from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseServicePropertiesOpensearchSegrep")


@_attrs_define
class DatabaseServicePropertiesOpensearchSegrep:
    """
    Attributes:
        pressure_checkpoint_limit (int | Unset): The maximum number of indexing checkpoints that a replica shard can
            fall behind when copying from primary. Once `segrep.pressure.checkpoint.limit` is breached along with
            `segrep.pressure.time.limit`, the segment replication backpressure mechanism is initiated. Default is 4
            checkpoints.
        pressure_enabled (bool | Unset): Enables the segment replication backpressure mechanism. Default is false.
        pressure_replica_stale_limit (float | Unset): The maximum number of stale replica shards that can exist in a
            replication group. Once `segrep.pressure.replica.stale.limit` is breached, the segment replication backpressure
            mechanism is initiated. Default is .5, which is 50% of a replication group.
        pressure_time_limit (str | Unset): The maximum amount of time that a replica shard can take to copy from the
            primary shard. Once segrep.pressure.time.limit is breached along with segrep.pressure.checkpoint.limit, the
            segment replication backpressure mechanism is initiated. Default is 5 minutes.
    """

    pressure_checkpoint_limit: int | Unset = UNSET
    pressure_enabled: bool | Unset = UNSET
    pressure_replica_stale_limit: float | Unset = UNSET
    pressure_time_limit: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        pressure_checkpoint_limit = self.pressure_checkpoint_limit

        pressure_enabled = self.pressure_enabled

        pressure_replica_stale_limit = self.pressure_replica_stale_limit

        pressure_time_limit = self.pressure_time_limit

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if pressure_checkpoint_limit is not UNSET:
            field_dict["pressure.checkpoint.limit"] = pressure_checkpoint_limit
        if pressure_enabled is not UNSET:
            field_dict["pressure.enabled"] = pressure_enabled
        if pressure_replica_stale_limit is not UNSET:
            field_dict["pressure.replica.stale.limit"] = pressure_replica_stale_limit
        if pressure_time_limit is not UNSET:
            field_dict["pressure.time.limit"] = pressure_time_limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pressure_checkpoint_limit = d.pop("pressure.checkpoint.limit", UNSET)

        pressure_enabled = d.pop("pressure.enabled", UNSET)

        pressure_replica_stale_limit = d.pop("pressure.replica.stale.limit", UNSET)

        pressure_time_limit = d.pop("pressure.time.limit", UNSET)

        database_service_properties_opensearch_segrep = cls(
            pressure_checkpoint_limit=pressure_checkpoint_limit,
            pressure_enabled=pressure_enabled,
            pressure_replica_stale_limit=pressure_replica_stale_limit,
            pressure_time_limit=pressure_time_limit,
        )

        return database_service_properties_opensearch_segrep
