from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.load_balancer_backend_metrics_response import LoadBalancerBackendMetricsResponse
    from ..models.load_balancer_frontend_metrics_response import LoadBalancerFrontendMetricsResponse


T = TypeVar("T", bound="LoadBalancerMetrics")


@_attrs_define
class LoadBalancerMetrics:
    """Represents a snapshot of load balancer metrics collected by the monitoring agent, including frontend and backend
    statistics for a given service at a specific timestamp.

        Attributes:
            frontends (list[LoadBalancerFrontendMetricsResponse]): List of frontend metrics.
            backends (list[LoadBalancerBackendMetricsResponse]): List of backend metrics.
    """

    frontends: list[LoadBalancerFrontendMetricsResponse]
    backends: list[LoadBalancerBackendMetricsResponse]

    def to_dict(self) -> dict[str, Any]:
        frontends = []
        for frontends_item_data in self.frontends:
            frontends_item = frontends_item_data.to_dict()
            frontends.append(frontends_item)

        backends = []
        for backends_item_data in self.backends:
            backends_item = backends_item_data.to_dict()
            backends.append(backends_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "frontends": frontends,
                "backends": backends,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.load_balancer_backend_metrics_response import LoadBalancerBackendMetricsResponse  # noqa: PLC0415
        from ..models.load_balancer_frontend_metrics_response import (
            LoadBalancerFrontendMetricsResponse,  # noqa: PLC0415
        )

        d = dict(src_dict)
        frontends = []
        _frontends = d.pop("frontends")
        for frontends_item_data in _frontends:
            frontends_item = LoadBalancerFrontendMetricsResponse.from_dict(frontends_item_data)

            frontends.append(frontends_item)

        backends = []
        _backends = d.pop("backends")
        for backends_item_data in _backends:
            backends_item = LoadBalancerBackendMetricsResponse.from_dict(backends_item_data)

            backends.append(backends_item)

        load_balancer_metrics = cls(
            frontends=frontends,
            backends=backends,
        )

        return load_balancer_metrics
