from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="LoadBalancerRequestMetricsResponse")


@_attrs_define
class LoadBalancerRequestMetricsResponse:
    """Represents basic HTTP request statistics collected by the load balancer, including the total number of processed,
    denied, and intercepted requests.

        Attributes:
            total_http_requests (int): Total number of HTTP requests processed. Example: 12500.
            total_denied_requests (int): Total number of denied HTTP requests. Example: 35.
            total_intercepted_requests (int): Total number of intercepted HTTP requests by internal rules or actions.
                Example: 12.
    """

    total_http_requests: int
    total_denied_requests: int
    total_intercepted_requests: int

    def to_dict(self) -> dict[str, Any]:
        total_http_requests = self.total_http_requests

        total_denied_requests = self.total_denied_requests

        total_intercepted_requests = self.total_intercepted_requests

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "total_http_requests": total_http_requests,
                "total_denied_requests": total_denied_requests,
                "total_intercepted_requests": total_intercepted_requests,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_http_requests = d.pop("total_http_requests")

        total_denied_requests = d.pop("total_denied_requests")

        total_intercepted_requests = d.pop("total_intercepted_requests")

        load_balancer_request_metrics_response = cls(
            total_http_requests=total_http_requests,
            total_denied_requests=total_denied_requests,
            total_intercepted_requests=total_intercepted_requests,
        )

        return load_balancer_request_metrics_response
