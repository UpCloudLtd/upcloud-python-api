from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseServicePropertiesOpensearchSearchBackpressureSearchTaskSettings")


@_attrs_define
class DatabaseServicePropertiesOpensearchSearchBackpressureSearchTaskSettings:
    """
    Attributes:
        cancellation_burst (float | Unset): The maximum number of search tasks to cancel in a single iteration of the
            observer thread. Default is 5.0
        cancellation_rate (float | Unset): The maximum number of search tasks to cancel per millisecond of elapsed time.
            Default is 0.003
        cancellation_ratio (float | Unset): The maximum number of search tasks to cancel, as a percentage of successful
            search task completions. Default is 0.1
        cpu_time_millis_threshold (int | Unset): The CPU usage threshold (in milliseconds) required for an individual
            parent task before it is considered for cancellation. Default is 30000
        elapsed_time_millis_threshold (int | Unset): The elapsed time threshold (in milliseconds) required for an
            individual parent task before it is considered for cancellation. Default is 45000
        heap_moving_average_window_size (int | Unset): The window size used to calculate the rolling average of the heap
            usage for the completed parent tasks. Default is 10
        heap_percent_threshold (float | Unset): The heap usage threshold (as a percentage) required for an individual
            parent task before it is considered for cancellation. Default is 0.2
        heap_variance (float | Unset): The heap usage variance required for an individual parent task before it is
            considered for cancellation. A task is considered for cancellation when taskHeapUsage is greater than or equal
            to heapUsageMovingAverage * variance. Default is 2.0
        total_heap_percent_threshold (float | Unset): The heap usage threshold (as a percentage) required for the sum of
            heap usages of all search tasks before cancellation is applied. Default is 0.5
    """

    cancellation_burst: float | Unset = UNSET
    cancellation_rate: float | Unset = UNSET
    cancellation_ratio: float | Unset = UNSET
    cpu_time_millis_threshold: int | Unset = UNSET
    elapsed_time_millis_threshold: int | Unset = UNSET
    heap_moving_average_window_size: int | Unset = UNSET
    heap_percent_threshold: float | Unset = UNSET
    heap_variance: float | Unset = UNSET
    total_heap_percent_threshold: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        cancellation_burst = self.cancellation_burst

        cancellation_rate = self.cancellation_rate

        cancellation_ratio = self.cancellation_ratio

        cpu_time_millis_threshold = self.cpu_time_millis_threshold

        elapsed_time_millis_threshold = self.elapsed_time_millis_threshold

        heap_moving_average_window_size = self.heap_moving_average_window_size

        heap_percent_threshold = self.heap_percent_threshold

        heap_variance = self.heap_variance

        total_heap_percent_threshold = self.total_heap_percent_threshold

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if cancellation_burst is not UNSET:
            field_dict["cancellation_burst"] = cancellation_burst
        if cancellation_rate is not UNSET:
            field_dict["cancellation_rate"] = cancellation_rate
        if cancellation_ratio is not UNSET:
            field_dict["cancellation_ratio"] = cancellation_ratio
        if cpu_time_millis_threshold is not UNSET:
            field_dict["cpu_time_millis_threshold"] = cpu_time_millis_threshold
        if elapsed_time_millis_threshold is not UNSET:
            field_dict["elapsed_time_millis_threshold"] = elapsed_time_millis_threshold
        if heap_moving_average_window_size is not UNSET:
            field_dict["heap_moving_average_window_size"] = heap_moving_average_window_size
        if heap_percent_threshold is not UNSET:
            field_dict["heap_percent_threshold"] = heap_percent_threshold
        if heap_variance is not UNSET:
            field_dict["heap_variance"] = heap_variance
        if total_heap_percent_threshold is not UNSET:
            field_dict["total_heap_percent_threshold"] = total_heap_percent_threshold

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cancellation_burst = d.pop("cancellation_burst", UNSET)

        cancellation_rate = d.pop("cancellation_rate", UNSET)

        cancellation_ratio = d.pop("cancellation_ratio", UNSET)

        cpu_time_millis_threshold = d.pop("cpu_time_millis_threshold", UNSET)

        elapsed_time_millis_threshold = d.pop("elapsed_time_millis_threshold", UNSET)

        heap_moving_average_window_size = d.pop("heap_moving_average_window_size", UNSET)

        heap_percent_threshold = d.pop("heap_percent_threshold", UNSET)

        heap_variance = d.pop("heap_variance", UNSET)

        total_heap_percent_threshold = d.pop("total_heap_percent_threshold", UNSET)

        database_service_properties_opensearch_search_backpressure_search_task_settings = cls(
            cancellation_burst=cancellation_burst,
            cancellation_rate=cancellation_rate,
            cancellation_ratio=cancellation_ratio,
            cpu_time_millis_threshold=cpu_time_millis_threshold,
            elapsed_time_millis_threshold=elapsed_time_millis_threshold,
            heap_moving_average_window_size=heap_moving_average_window_size,
            heap_percent_threshold=heap_percent_threshold,
            heap_variance=heap_variance,
            total_heap_percent_threshold=total_heap_percent_threshold,
        )

        return database_service_properties_opensearch_search_backpressure_search_task_settings
