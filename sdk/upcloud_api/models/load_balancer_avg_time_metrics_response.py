from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="LoadBalancerAvgTimeMetricsResponse")


@_attrs_define
class LoadBalancerAvgTimeMetricsResponse:
    """Represents average timing statistics for backend performance, including connection establishment, queuing, server
    response, and total transaction times, all measured in milliseconds.

        Attributes:
            avg_connection_time_ms (int): Average time taken to establish a connection in milliseconds. Example: 12.
            avg_queue_time_ms (int): Average time spent in queue before being processed, in milliseconds. Example: 5.
            avg_server_response_time_ms (int): Average server response time in milliseconds. Example: 28.
            avg_total_time_ms (int): Average total time from connection start to response completion, in milliseconds.
                Example: 45.
    """

    avg_connection_time_ms: int
    avg_queue_time_ms: int
    avg_server_response_time_ms: int
    avg_total_time_ms: int

    def to_dict(self) -> dict[str, Any]:
        avg_connection_time_ms = self.avg_connection_time_ms

        avg_queue_time_ms = self.avg_queue_time_ms

        avg_server_response_time_ms = self.avg_server_response_time_ms

        avg_total_time_ms = self.avg_total_time_ms

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "avg_connection_time_ms": avg_connection_time_ms,
                "avg_queue_time_ms": avg_queue_time_ms,
                "avg_server_response_time_ms": avg_server_response_time_ms,
                "avg_total_time_ms": avg_total_time_ms,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        avg_connection_time_ms = d.pop("avg_connection_time_ms")

        avg_queue_time_ms = d.pop("avg_queue_time_ms")

        avg_server_response_time_ms = d.pop("avg_server_response_time_ms")

        avg_total_time_ms = d.pop("avg_total_time_ms")

        load_balancer_avg_time_metrics_response = cls(
            avg_connection_time_ms=avg_connection_time_ms,
            avg_queue_time_ms=avg_queue_time_ms,
            avg_server_response_time_ms=avg_server_response_time_ms,
            avg_total_time_ms=avg_total_time_ms,
        )

        return load_balancer_avg_time_metrics_response
