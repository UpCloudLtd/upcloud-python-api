from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="LoadBalancerFrontendMetricsSeries")


@_attrs_define
class LoadBalancerFrontendMetricsSeries:
    """Aggregated time-series metrics for load balancer frontends, representing cumulative statistics between a start and
    end timestamp across one or more frontend instances.

        Attributes:
            start_at (datetime.datetime): Timestamp marking the beginning of the metrics aggregation period.
            end_at (datetime.datetime): Timestamp marking the end of the metrics aggregation period.
            frontends (list[str]): List of frontend names or identifiers included in the aggregated data. Example:
                ['frontend-http', 'frontend-https'].
            denied_connections (int | Unset): Total number of denied frontend connections within the time range. Example:
                15.
            denied_sessions (int | Unset): Total number of denied sessions during the period. Example: 8.
            invalid_requests (int | Unset): Number of malformed or invalid HTTP requests received. Example: 12.
            request_bytes (int | Unset): Total size of incoming request payloads, in bytes. Example: 15432000.
            response_bytes (int | Unset): Total size of outgoing response payloads, in bytes. Example: 14321000.
            denied_responses (int | Unset): Number of HTTP responses that were denied or rejected. Example: 6.
            http_responses_1xx (int | Unset): Count of informational (1xx) HTTP responses. Example: 2.
            http_responses_2xx (int | Unset): Count of successful (2xx) HTTP responses. Example: 940.
            http_responses_3xx (int | Unset): Count of redirection (3xx) HTTP responses. Example: 47.
            http_responses_4xx (int | Unset): Count of client error (4xx) HTTP responses. Example: 33.
            http_responses_5xx (int | Unset): Count of server error (5xx) HTTP responses. Example: 12.
            http_responses_other (int | Unset): Count of HTTP responses with codes outside the 1xx–5xx range. Example: 0.
            sessions (int | Unset): Total number of frontend sessions handled. Example: 1040.
            http_requests (int | Unset): Total number of HTTP requests processed during the aggregation period. Example:
                15000.
            denied_requests (int | Unset): Total number of HTTP requests denied. Example: 28.
            intercepted_requests (int | Unset): Number of requests intercepted before reaching the backend. Example: 9.
    """

    start_at: datetime.datetime
    end_at: datetime.datetime
    frontends: list[str]
    denied_connections: int | Unset = UNSET
    denied_sessions: int | Unset = UNSET
    invalid_requests: int | Unset = UNSET
    request_bytes: int | Unset = UNSET
    response_bytes: int | Unset = UNSET
    denied_responses: int | Unset = UNSET
    http_responses_1xx: int | Unset = UNSET
    http_responses_2xx: int | Unset = UNSET
    http_responses_3xx: int | Unset = UNSET
    http_responses_4xx: int | Unset = UNSET
    http_responses_5xx: int | Unset = UNSET
    http_responses_other: int | Unset = UNSET
    sessions: int | Unset = UNSET
    http_requests: int | Unset = UNSET
    denied_requests: int | Unset = UNSET
    intercepted_requests: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        start_at = self.start_at.isoformat()

        end_at = self.end_at.isoformat()

        frontends = self.frontends

        denied_connections = self.denied_connections

        denied_sessions = self.denied_sessions

        invalid_requests = self.invalid_requests

        request_bytes = self.request_bytes

        response_bytes = self.response_bytes

        denied_responses = self.denied_responses

        http_responses_1xx = self.http_responses_1xx

        http_responses_2xx = self.http_responses_2xx

        http_responses_3xx = self.http_responses_3xx

        http_responses_4xx = self.http_responses_4xx

        http_responses_5xx = self.http_responses_5xx

        http_responses_other = self.http_responses_other

        sessions = self.sessions

        http_requests = self.http_requests

        denied_requests = self.denied_requests

        intercepted_requests = self.intercepted_requests

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "start_at": start_at,
                "end_at": end_at,
                "frontends": frontends,
            }
        )
        if denied_connections is not UNSET:
            field_dict["denied_connections"] = denied_connections
        if denied_sessions is not UNSET:
            field_dict["denied_sessions"] = denied_sessions
        if invalid_requests is not UNSET:
            field_dict["invalid_requests"] = invalid_requests
        if request_bytes is not UNSET:
            field_dict["request_bytes"] = request_bytes
        if response_bytes is not UNSET:
            field_dict["response_bytes"] = response_bytes
        if denied_responses is not UNSET:
            field_dict["denied_responses"] = denied_responses
        if http_responses_1xx is not UNSET:
            field_dict["http_responses_1xx"] = http_responses_1xx
        if http_responses_2xx is not UNSET:
            field_dict["http_responses_2xx"] = http_responses_2xx
        if http_responses_3xx is not UNSET:
            field_dict["http_responses_3xx"] = http_responses_3xx
        if http_responses_4xx is not UNSET:
            field_dict["http_responses_4xx"] = http_responses_4xx
        if http_responses_5xx is not UNSET:
            field_dict["http_responses_5xx"] = http_responses_5xx
        if http_responses_other is not UNSET:
            field_dict["http_responses_other"] = http_responses_other
        if sessions is not UNSET:
            field_dict["sessions"] = sessions
        if http_requests is not UNSET:
            field_dict["http_requests"] = http_requests
        if denied_requests is not UNSET:
            field_dict["denied_requests"] = denied_requests
        if intercepted_requests is not UNSET:
            field_dict["intercepted_requests"] = intercepted_requests

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start_at = datetime.datetime.fromisoformat(d.pop("start_at"))

        end_at = datetime.datetime.fromisoformat(d.pop("end_at"))

        frontends = cast(list[str], d.pop("frontends"))

        denied_connections = d.pop("denied_connections", UNSET)

        denied_sessions = d.pop("denied_sessions", UNSET)

        invalid_requests = d.pop("invalid_requests", UNSET)

        request_bytes = d.pop("request_bytes", UNSET)

        response_bytes = d.pop("response_bytes", UNSET)

        denied_responses = d.pop("denied_responses", UNSET)

        http_responses_1xx = d.pop("http_responses_1xx", UNSET)

        http_responses_2xx = d.pop("http_responses_2xx", UNSET)

        http_responses_3xx = d.pop("http_responses_3xx", UNSET)

        http_responses_4xx = d.pop("http_responses_4xx", UNSET)

        http_responses_5xx = d.pop("http_responses_5xx", UNSET)

        http_responses_other = d.pop("http_responses_other", UNSET)

        sessions = d.pop("sessions", UNSET)

        http_requests = d.pop("http_requests", UNSET)

        denied_requests = d.pop("denied_requests", UNSET)

        intercepted_requests = d.pop("intercepted_requests", UNSET)

        load_balancer_frontend_metrics_series = cls(
            start_at=start_at,
            end_at=end_at,
            frontends=frontends,
            denied_connections=denied_connections,
            denied_sessions=denied_sessions,
            invalid_requests=invalid_requests,
            request_bytes=request_bytes,
            response_bytes=response_bytes,
            denied_responses=denied_responses,
            http_responses_1xx=http_responses_1xx,
            http_responses_2xx=http_responses_2xx,
            http_responses_3xx=http_responses_3xx,
            http_responses_4xx=http_responses_4xx,
            http_responses_5xx=http_responses_5xx,
            http_responses_other=http_responses_other,
            sessions=sessions,
            http_requests=http_requests,
            denied_requests=denied_requests,
            intercepted_requests=intercepted_requests,
        )

        return load_balancer_frontend_metrics_series
