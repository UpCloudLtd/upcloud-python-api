from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="LoadBalancerBackendMetricsSeries")


@_attrs_define
class LoadBalancerBackendMetricsSeries:
    """Aggregated performance, availability, and traffic statistics for a load balancer backend, including member metrics
    and average timing metrics.

        Attributes:
            start_at (datetime.datetime): Timestamp marking the start of the metrics collection period.
            end_at (datetime.datetime): Timestamp marking the end of the metrics collection period.
            backends (list[str]): List of backend identifiers included in the metrics series. Example: ['backend-api',
                'backend-web'].
            request_bytes (int | Unset): Total number of request bytes processed. Example: 12345678.
            response_bytes (int | Unset): Total number of response bytes sent. Example: 11876543.
            denied_responses (int | Unset): Total number of denied responses. Example: 12.
            http_responses_1xx (int | Unset): Count of HTTP 1xx informational responses. Example: 2.
            http_responses_2xx (int | Unset): Count of HTTP 2xx successful responses. Example: 9500.
            http_responses_3xx (int | Unset): Count of HTTP 3xx redirection responses. Example: 35.
            http_responses_4xx (int | Unset): Count of HTTP 4xx client error responses. Example: 18.
            http_responses_5xx (int | Unset): Count of HTTP 5xx server error responses. Example: 6.
            http_responses_other (int | Unset): Count of HTTP responses outside the 1xx–5xx range. Example: 0.
            sessions (int | Unset): Total number of sessions. Example: 220.
            downtime (int | Unset): Total downtime in seconds. Example: 45.
            failed_checks_transitions (int | Unset): Number of transitions from healthy to failed health checks. Example: 3.
            client_aborted (int | Unset): Number of client-aborted connections. Example: 5.
            failed_connections (int | Unset): Number of failed connections. Example: 2.
            invalid_responses (int | Unset): Number of invalid responses. Example: 1.
            routed_requests (int | Unset): Number of routed requests. Example: 15200.
            server_aborted (int | Unset): Number of server-aborted connections. Example: 2.
            server_redispatches (int | Unset): Number of server redispatches. Example: 3.
            server_connection_retries (int | Unset): Number of server connection retries. Example: 4.
    """

    start_at: datetime.datetime
    end_at: datetime.datetime
    backends: list[str]
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
    downtime: int | Unset = UNSET
    failed_checks_transitions: int | Unset = UNSET
    client_aborted: int | Unset = UNSET
    failed_connections: int | Unset = UNSET
    invalid_responses: int | Unset = UNSET
    routed_requests: int | Unset = UNSET
    server_aborted: int | Unset = UNSET
    server_redispatches: int | Unset = UNSET
    server_connection_retries: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        start_at = self.start_at.isoformat()

        end_at = self.end_at.isoformat()

        backends = self.backends

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

        downtime = self.downtime

        failed_checks_transitions = self.failed_checks_transitions

        client_aborted = self.client_aborted

        failed_connections = self.failed_connections

        invalid_responses = self.invalid_responses

        routed_requests = self.routed_requests

        server_aborted = self.server_aborted

        server_redispatches = self.server_redispatches

        server_connection_retries = self.server_connection_retries

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "start_at": start_at,
                "end_at": end_at,
                "backends": backends,
            }
        )
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
        if downtime is not UNSET:
            field_dict["downtime"] = downtime
        if failed_checks_transitions is not UNSET:
            field_dict["failed_checks_transitions"] = failed_checks_transitions
        if client_aborted is not UNSET:
            field_dict["client_aborted"] = client_aborted
        if failed_connections is not UNSET:
            field_dict["failed_connections"] = failed_connections
        if invalid_responses is not UNSET:
            field_dict["invalid_responses"] = invalid_responses
        if routed_requests is not UNSET:
            field_dict["routed_requests"] = routed_requests
        if server_aborted is not UNSET:
            field_dict["server_aborted"] = server_aborted
        if server_redispatches is not UNSET:
            field_dict["server_redispatches"] = server_redispatches
        if server_connection_retries is not UNSET:
            field_dict["server_connection_retries"] = server_connection_retries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start_at = datetime.datetime.fromisoformat(d.pop("start_at"))

        end_at = datetime.datetime.fromisoformat(d.pop("end_at"))

        backends = cast(list[str], d.pop("backends"))

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

        downtime = d.pop("downtime", UNSET)

        failed_checks_transitions = d.pop("failed_checks_transitions", UNSET)

        client_aborted = d.pop("client_aborted", UNSET)

        failed_connections = d.pop("failed_connections", UNSET)

        invalid_responses = d.pop("invalid_responses", UNSET)

        routed_requests = d.pop("routed_requests", UNSET)

        server_aborted = d.pop("server_aborted", UNSET)

        server_redispatches = d.pop("server_redispatches", UNSET)

        server_connection_retries = d.pop("server_connection_retries", UNSET)

        load_balancer_backend_metrics_series = cls(
            start_at=start_at,
            end_at=end_at,
            backends=backends,
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
            downtime=downtime,
            failed_checks_transitions=failed_checks_transitions,
            client_aborted=client_aborted,
            failed_connections=failed_connections,
            invalid_responses=invalid_responses,
            routed_requests=routed_requests,
            server_aborted=server_aborted,
            server_redispatches=server_redispatches,
            server_connection_retries=server_connection_retries,
        )

        return load_balancer_backend_metrics_series
