from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseServicePropertiesOpensearchRemoteStore")


@_attrs_define
class DatabaseServicePropertiesOpensearchRemoteStore:
    """
    Attributes:
        segment_pressure_bytes_lag_variance_factor (float | Unset): The variance factor that is used together with the
            moving average to calculate the dynamic bytes lag threshold for activating remote segment backpressure. Defaults
            to 10.
        segment_pressure_consecutive_failures_limit (int | Unset): The minimum consecutive failure count for activating
            remote segment backpressure. Defaults to 5.
        segment_pressure_enabled (bool | Unset): Enables remote segment backpressure. Default is `true`
        segment_pressure_time_lag_variance_factor (float | Unset): The variance factor that is used together with the
            moving average to calculate the dynamic time lag threshold for activating remote segment backpressure. Defaults
            to 10.
    """

    segment_pressure_bytes_lag_variance_factor: float | Unset = UNSET
    segment_pressure_consecutive_failures_limit: int | Unset = UNSET
    segment_pressure_enabled: bool | Unset = UNSET
    segment_pressure_time_lag_variance_factor: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        segment_pressure_bytes_lag_variance_factor = self.segment_pressure_bytes_lag_variance_factor

        segment_pressure_consecutive_failures_limit = self.segment_pressure_consecutive_failures_limit

        segment_pressure_enabled = self.segment_pressure_enabled

        segment_pressure_time_lag_variance_factor = self.segment_pressure_time_lag_variance_factor

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if segment_pressure_bytes_lag_variance_factor is not UNSET:
            field_dict["segment.pressure.bytes_lag.variance_factor"] = segment_pressure_bytes_lag_variance_factor
        if segment_pressure_consecutive_failures_limit is not UNSET:
            field_dict["segment.pressure.consecutive_failures.limit"] = segment_pressure_consecutive_failures_limit
        if segment_pressure_enabled is not UNSET:
            field_dict["segment.pressure.enabled"] = segment_pressure_enabled
        if segment_pressure_time_lag_variance_factor is not UNSET:
            field_dict["segment.pressure.time_lag.variance_factor"] = segment_pressure_time_lag_variance_factor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        segment_pressure_bytes_lag_variance_factor = d.pop("segment.pressure.bytes_lag.variance_factor", UNSET)

        segment_pressure_consecutive_failures_limit = d.pop("segment.pressure.consecutive_failures.limit", UNSET)

        segment_pressure_enabled = d.pop("segment.pressure.enabled", UNSET)

        segment_pressure_time_lag_variance_factor = d.pop("segment.pressure.time_lag.variance_factor", UNSET)

        database_service_properties_opensearch_remote_store = cls(
            segment_pressure_bytes_lag_variance_factor=segment_pressure_bytes_lag_variance_factor,
            segment_pressure_consecutive_failures_limit=segment_pressure_consecutive_failures_limit,
            segment_pressure_enabled=segment_pressure_enabled,
            segment_pressure_time_lag_variance_factor=segment_pressure_time_lag_variance_factor,
        )

        return database_service_properties_opensearch_remote_store
