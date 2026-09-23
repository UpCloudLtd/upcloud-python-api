from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_service_properties_opensearch_search_insights_top_queries_top_n_queries_monitoring_by_cpu import (
        DatabaseServicePropertiesOpensearchSearchInsightsTopQueriesTopNQueriesMonitoringByCPU,
    )
    from ..models.database_service_properties_opensearch_search_insights_top_queries_top_n_queries_monitoring_by_latency import (
        DatabaseServicePropertiesOpensearchSearchInsightsTopQueriesTopNQueriesMonitoringByLatency,
    )
    from ..models.database_service_properties_opensearch_search_insights_top_queries_top_n_queries_monitoring_by_memory import (
        DatabaseServicePropertiesOpensearchSearchInsightsTopQueriesTopNQueriesMonitoringByMemory,
    )


T = TypeVar("T", bound="DatabaseServicePropertiesOpensearchSearchInsightsTopQueries")


@_attrs_define
class DatabaseServicePropertiesOpensearchSearchInsightsTopQueries:
    """
    Attributes:
        cpu (DatabaseServicePropertiesOpensearchSearchInsightsTopQueriesTopNQueriesMonitoringByCPU | Unset):
        latency (DatabaseServicePropertiesOpensearchSearchInsightsTopQueriesTopNQueriesMonitoringByLatency | Unset):
        memory (DatabaseServicePropertiesOpensearchSearchInsightsTopQueriesTopNQueriesMonitoringByMemory | Unset):
    """

    cpu: DatabaseServicePropertiesOpensearchSearchInsightsTopQueriesTopNQueriesMonitoringByCPU | Unset = UNSET
    latency: DatabaseServicePropertiesOpensearchSearchInsightsTopQueriesTopNQueriesMonitoringByLatency | Unset = UNSET
    memory: DatabaseServicePropertiesOpensearchSearchInsightsTopQueriesTopNQueriesMonitoringByMemory | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        cpu: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cpu, Unset):
            cpu = self.cpu.to_dict()

        latency: dict[str, Any] | Unset = UNSET
        if not isinstance(self.latency, Unset):
            latency = self.latency.to_dict()

        memory: dict[str, Any] | Unset = UNSET
        if not isinstance(self.memory, Unset):
            memory = self.memory.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if cpu is not UNSET:
            field_dict["cpu"] = cpu
        if latency is not UNSET:
            field_dict["latency"] = latency
        if memory is not UNSET:
            field_dict["memory"] = memory

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_service_properties_opensearch_search_insights_top_queries_top_n_queries_monitoring_by_cpu import (
            DatabaseServicePropertiesOpensearchSearchInsightsTopQueriesTopNQueriesMonitoringByCPU,  # noqa: PLC0415
        )
        from ..models.database_service_properties_opensearch_search_insights_top_queries_top_n_queries_monitoring_by_latency import (
            DatabaseServicePropertiesOpensearchSearchInsightsTopQueriesTopNQueriesMonitoringByLatency,  # noqa: PLC0415
        )
        from ..models.database_service_properties_opensearch_search_insights_top_queries_top_n_queries_monitoring_by_memory import (
            DatabaseServicePropertiesOpensearchSearchInsightsTopQueriesTopNQueriesMonitoringByMemory,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _cpu = d.pop("cpu", UNSET)
        cpu: DatabaseServicePropertiesOpensearchSearchInsightsTopQueriesTopNQueriesMonitoringByCPU | Unset
        if isinstance(_cpu, Unset):
            cpu = UNSET
        else:
            cpu = DatabaseServicePropertiesOpensearchSearchInsightsTopQueriesTopNQueriesMonitoringByCPU.from_dict(_cpu)

        _latency = d.pop("latency", UNSET)
        latency: DatabaseServicePropertiesOpensearchSearchInsightsTopQueriesTopNQueriesMonitoringByLatency | Unset
        if isinstance(_latency, Unset):
            latency = UNSET
        else:
            latency = (
                DatabaseServicePropertiesOpensearchSearchInsightsTopQueriesTopNQueriesMonitoringByLatency.from_dict(
                    _latency
                )
            )

        _memory = d.pop("memory", UNSET)
        memory: DatabaseServicePropertiesOpensearchSearchInsightsTopQueriesTopNQueriesMonitoringByMemory | Unset
        if isinstance(_memory, Unset):
            memory = UNSET
        else:
            memory = DatabaseServicePropertiesOpensearchSearchInsightsTopQueriesTopNQueriesMonitoringByMemory.from_dict(
                _memory
            )

        database_service_properties_opensearch_search_insights_top_queries = cls(
            cpu=cpu,
            latency=latency,
            memory=memory,
        )

        return database_service_properties_opensearch_search_insights_top_queries
