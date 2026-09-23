from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="LoadBalancerMemberMetricsSeriesResponse")


@_attrs_define
class LoadBalancerMemberMetricsSeriesResponse:
    """Aggregated time-series metrics for backend members, showing request and response statistics, connection health, and
    server performance during a given time window.

        Attributes:
            start_at (datetime.datetime): Timestamp marking the start of the metrics collection period.
            end_at (datetime.datetime): Timestamp marking the end of the metrics collection period.
            members (list[str]): List of backend member identifiers included in the metrics series. Example: ['backend-
                member-1', 'backend-member-2'].
            request_bytes (int | Unset): Total number of request bytes processed by all members in the series. Example:
                12345678.
            response_bytes (int | Unset): Total number of response bytes sent by all members. Example: 11876543.
            denied_responses (int | Unset): Total number of denied responses returned during the period. Example: 12.
            http_responses_1xx (int | Unset): Count of HTTP 1xx informational responses. Example: 2.
            http_responses_2xx (int | Unset): Count of HTTP 2xx successful responses. Example: 9500.
            http_responses_3xx (int | Unset): Count of HTTP 3xx redirection responses. Example: 35.
            http_responses_4xx (int | Unset): Count of HTTP 4xx client error responses. Example: 18.
            http_responses_5xx (int | Unset): Count of HTTP 5xx server error responses. Example: 6.
            http_responses_other (int | Unset): Count of HTTP responses outside the 1xx–5xx range. Example: 0.
            sessions (int | Unset): Total number of active or completed sessions during the metrics window. Example: 220.
            downtime (int | Unset): Total downtime duration in seconds. Example: 45.
            failed_checks_transitions (int | Unset): Number of transitions from healthy to failed health checks detected
                during the period. Example: 3.
            client_aborted (int | Unset): Number of connections aborted by the client. Example: 7.
            failed_connections (int | Unset): Number of backend connection attempts that failed. Example: 2.
            invalid_responses (int | Unset): Number of invalid or malformed responses detected. Example: 1.
            routed_requests (int | Unset): Total number of requests successfully routed to the backend members. Example:
                10234.
            server_aborted (int | Unset): Number of connections aborted by the backend server. Example: 4.
            server_redispatches (int | Unset): Number of requests redispatched to another backend member after an initial
                failure. Example: 5.
            server_connection_retries (int | Unset): Number of backend connection retry attempts. Example: 9.
            failed_checks (int | Unset): Total number of failed health checks for all members combined. Example: 15.
    """

    start_at: datetime.datetime
    end_at: datetime.datetime
    members: list[str]
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
    failed_checks: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        start_at = self.start_at.isoformat()

        end_at = self.end_at.isoformat()

        members = self.members

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

        failed_checks = self.failed_checks

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "start_at": start_at,
                "end_at": end_at,
                "members": members,
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
        if failed_checks is not UNSET:
            field_dict["failed_checks"] = failed_checks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start_at = datetime.datetime.fromisoformat(d.pop("start_at"))

        end_at = datetime.datetime.fromisoformat(d.pop("end_at"))

        members = cast(list[str], d.pop("members"))

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

        failed_checks = d.pop("failed_checks", UNSET)

        load_balancer_member_metrics_series_response = cls(
            start_at=start_at,
            end_at=end_at,
            members=members,
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
            failed_checks=failed_checks,
        )

        return load_balancer_member_metrics_series_response
