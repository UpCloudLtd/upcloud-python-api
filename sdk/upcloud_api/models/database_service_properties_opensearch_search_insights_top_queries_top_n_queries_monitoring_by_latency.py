from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseServicePropertiesOpensearchSearchInsightsTopQueriesTopNQueriesMonitoringByLatency")


@_attrs_define
class DatabaseServicePropertiesOpensearchSearchInsightsTopQueriesTopNQueriesMonitoringByLatency:
    """
    Attributes:
        enabled (bool | Unset): Enable or disable top N query monitoring by the metric Default: False.
        top_n_size (int | Unset):
        window_size (str | Unset): Configure the window size of the top N queries. The value should be a time value with
            unit, e.g. 1m, 5s, 1h.
    """

    enabled: bool | Unset = False
    top_n_size: int | Unset = UNSET
    window_size: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        top_n_size = self.top_n_size

        window_size = self.window_size

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if top_n_size is not UNSET:
            field_dict["top_n_size"] = top_n_size
        if window_size is not UNSET:
            field_dict["window_size"] = window_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        top_n_size = d.pop("top_n_size", UNSET)

        window_size = d.pop("window_size", UNSET)

        database_service_properties_opensearch_search_insights_top_queries_top_n_queries_monitoring_by_latency = cls(
            enabled=enabled,
            top_n_size=top_n_size,
            window_size=window_size,
        )

        return database_service_properties_opensearch_search_insights_top_queries_top_n_queries_monitoring_by_latency
