from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.load_balancer_member_metrics_response_check_status import LoadBalancerMemberMetricsResponseCheckStatus
from ..models.load_balancer_member_metrics_response_status import LoadBalancerMemberMetricsResponseStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="LoadBalancerMemberMetricsResponse")


@_attrs_define
class LoadBalancerMemberMetricsResponse:
    """Represents detailed performance and health metrics for an individual backend member (server) within a load balancer.
    Includes operational status, health check results, and aggregated traffic and timing statistics.

        Attributes:
            total_request_bytes (int): Total number of request bytes processed. Example: 12543000.
            total_response_bytes (int): Total number of response bytes processed. Example: 11789000.
            total_denied_responses (int): Total number of denied responses. Example: 2.
            total_http_responses_1xx (int): Total number of HTTP 1xx informational responses. Example: 5.
            total_http_responses_2xx (int): Total number of HTTP 2xx successful responses. Example: 984.
            total_http_responses_3xx (int): Total number of HTTP 3xx redirection responses. Example: 45.
            total_http_responses_4xx (int): Total number of HTTP 4xx client error responses. Example: 22.
            total_http_responses_5xx (int): Total number of HTTP 5xx server error responses. Example: 8.
            total_http_responses_other (int): Total number of HTTP responses outside the standard 1xx–5xx range. Example: 0.
            total_sessions (int): Total number of sessions handled. Example: 1100.
            session_rate (int): Average rate of sessions per second. Example: 25.
            current_sessions (int): Current number of active sessions. Example: 4.
            total_failed_checks_transitions (int): Total number of times the server transitioned from healthy to failed
                state due to failed health checks. Example: 3.
            total_client_aborted (int): Total number of sessions aborted by clients before completion. Example: 12.
            total_failed_connections (int): Total number of failed connection attempts to the server. Example: 5.
            total_invalid_responses (int): Total number of invalid responses received from the server. Example: 2.
            total_routed_requests (int): Total number of requests successfully routed to the server. Example: 14892.
            total_server_aborted (int): Total number of sessions aborted by the server before completion. Example: 4.
            total_server_redispatches (int): Total number of requests that were redispatched to another server after
                failure. Example: 7.
            total_server_connection_retries (int): Total number of retries attempted for failed server connections. Example:
                9.
            connections_waiting (int): Current number of connections waiting for a server slot. Example: 1.
            avg_connection_time_ms (int): Average time taken to establish a connection in milliseconds. Example: 12.
            avg_queue_time_ms (int): Average time spent in queue before being processed, in milliseconds. Example: 5.
            avg_server_response_time_ms (int): Average server response time in milliseconds. Example: 28.
            avg_total_time_ms (int): Average total time from connection start to response completion, in milliseconds.
                Example: 45.
            member_id (int): Unique identifier of the backend member. Example: 101.
            name (str): Human-readable name of the backend member. Example: backend-member-1.
            backend_id (int): Identifier of the backend this member belongs to. Example: 401.
            status (LoadBalancerMemberMetricsResponseStatus): Current operational status of the member. Example: up.
            check_status (LoadBalancerMemberMetricsResponseCheckStatus): Result of the latest health check for the member.
                Example: passing.
            check_http_code (int): HTTP status code returned by the last health check (if applicable). Example: 200.
            total_failed_checks (int): Total number of failed health checks recorded for this member. Example: 2.
            created_at (datetime.datetime): Timestamp of when the member was created.
            updated_at (datetime.datetime): Timestamp of when the member metrics were last updated.
            last_check_content (str | Unset): Response content returned by the last health check. Example: OK.
            last_check_desc (str | Unset): Description or additional diagnostic information from the last health check.
                Example: Health check passed successfully..
    """

    total_request_bytes: int
    total_response_bytes: int
    total_denied_responses: int
    total_http_responses_1xx: int
    total_http_responses_2xx: int
    total_http_responses_3xx: int
    total_http_responses_4xx: int
    total_http_responses_5xx: int
    total_http_responses_other: int
    total_sessions: int
    session_rate: int
    current_sessions: int
    total_failed_checks_transitions: int
    total_client_aborted: int
    total_failed_connections: int
    total_invalid_responses: int
    total_routed_requests: int
    total_server_aborted: int
    total_server_redispatches: int
    total_server_connection_retries: int
    connections_waiting: int
    avg_connection_time_ms: int
    avg_queue_time_ms: int
    avg_server_response_time_ms: int
    avg_total_time_ms: int
    member_id: int
    name: str
    backend_id: int
    status: LoadBalancerMemberMetricsResponseStatus
    check_status: LoadBalancerMemberMetricsResponseCheckStatus
    check_http_code: int
    total_failed_checks: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    last_check_content: str | Unset = UNSET
    last_check_desc: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        total_request_bytes = self.total_request_bytes

        total_response_bytes = self.total_response_bytes

        total_denied_responses = self.total_denied_responses

        total_http_responses_1xx = self.total_http_responses_1xx

        total_http_responses_2xx = self.total_http_responses_2xx

        total_http_responses_3xx = self.total_http_responses_3xx

        total_http_responses_4xx = self.total_http_responses_4xx

        total_http_responses_5xx = self.total_http_responses_5xx

        total_http_responses_other = self.total_http_responses_other

        total_sessions = self.total_sessions

        session_rate = self.session_rate

        current_sessions = self.current_sessions

        total_failed_checks_transitions = self.total_failed_checks_transitions

        total_client_aborted = self.total_client_aborted

        total_failed_connections = self.total_failed_connections

        total_invalid_responses = self.total_invalid_responses

        total_routed_requests = self.total_routed_requests

        total_server_aborted = self.total_server_aborted

        total_server_redispatches = self.total_server_redispatches

        total_server_connection_retries = self.total_server_connection_retries

        connections_waiting = self.connections_waiting

        avg_connection_time_ms = self.avg_connection_time_ms

        avg_queue_time_ms = self.avg_queue_time_ms

        avg_server_response_time_ms = self.avg_server_response_time_ms

        avg_total_time_ms = self.avg_total_time_ms

        member_id = self.member_id

        name = self.name

        backend_id = self.backend_id

        status = self.status.value

        check_status = self.check_status.value

        check_http_code = self.check_http_code

        total_failed_checks = self.total_failed_checks

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        last_check_content = self.last_check_content

        last_check_desc = self.last_check_desc

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "total_request_bytes": total_request_bytes,
                "total_response_bytes": total_response_bytes,
                "total_denied_responses": total_denied_responses,
                "total_http_responses_1xx": total_http_responses_1xx,
                "total_http_responses_2xx": total_http_responses_2xx,
                "total_http_responses_3xx": total_http_responses_3xx,
                "total_http_responses_4xx": total_http_responses_4xx,
                "total_http_responses_5xx": total_http_responses_5xx,
                "total_http_responses_other": total_http_responses_other,
                "total_sessions": total_sessions,
                "session_rate": session_rate,
                "current_sessions": current_sessions,
                "total_failed_checks_transitions": total_failed_checks_transitions,
                "total_client_aborted": total_client_aborted,
                "total_failed_connections": total_failed_connections,
                "total_invalid_responses": total_invalid_responses,
                "total_routed_requests": total_routed_requests,
                "total_server_aborted": total_server_aborted,
                "total_server_redispatches": total_server_redispatches,
                "total_server_connection_retries": total_server_connection_retries,
                "connections_waiting": connections_waiting,
                "avg_connection_time_ms": avg_connection_time_ms,
                "avg_queue_time_ms": avg_queue_time_ms,
                "avg_server_response_time_ms": avg_server_response_time_ms,
                "avg_total_time_ms": avg_total_time_ms,
                "member_id": member_id,
                "name": name,
                "backend_id": backend_id,
                "status": status,
                "check_status": check_status,
                "check_http_code": check_http_code,
                "total_failed_checks": total_failed_checks,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if last_check_content is not UNSET:
            field_dict["last_check_content"] = last_check_content
        if last_check_desc is not UNSET:
            field_dict["last_check_desc"] = last_check_desc

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_request_bytes = d.pop("total_request_bytes")

        total_response_bytes = d.pop("total_response_bytes")

        total_denied_responses = d.pop("total_denied_responses")

        total_http_responses_1xx = d.pop("total_http_responses_1xx")

        total_http_responses_2xx = d.pop("total_http_responses_2xx")

        total_http_responses_3xx = d.pop("total_http_responses_3xx")

        total_http_responses_4xx = d.pop("total_http_responses_4xx")

        total_http_responses_5xx = d.pop("total_http_responses_5xx")

        total_http_responses_other = d.pop("total_http_responses_other")

        total_sessions = d.pop("total_sessions")

        session_rate = d.pop("session_rate")

        current_sessions = d.pop("current_sessions")

        total_failed_checks_transitions = d.pop("total_failed_checks_transitions")

        total_client_aborted = d.pop("total_client_aborted")

        total_failed_connections = d.pop("total_failed_connections")

        total_invalid_responses = d.pop("total_invalid_responses")

        total_routed_requests = d.pop("total_routed_requests")

        total_server_aborted = d.pop("total_server_aborted")

        total_server_redispatches = d.pop("total_server_redispatches")

        total_server_connection_retries = d.pop("total_server_connection_retries")

        connections_waiting = d.pop("connections_waiting")

        avg_connection_time_ms = d.pop("avg_connection_time_ms")

        avg_queue_time_ms = d.pop("avg_queue_time_ms")

        avg_server_response_time_ms = d.pop("avg_server_response_time_ms")

        avg_total_time_ms = d.pop("avg_total_time_ms")

        member_id = d.pop("member_id")

        name = d.pop("name")

        backend_id = d.pop("backend_id")

        status = LoadBalancerMemberMetricsResponseStatus(d.pop("status"))

        check_status = LoadBalancerMemberMetricsResponseCheckStatus(d.pop("check_status"))

        check_http_code = d.pop("check_http_code")

        total_failed_checks = d.pop("total_failed_checks")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        last_check_content = d.pop("last_check_content", UNSET)

        last_check_desc = d.pop("last_check_desc", UNSET)

        load_balancer_member_metrics_response = cls(
            total_request_bytes=total_request_bytes,
            total_response_bytes=total_response_bytes,
            total_denied_responses=total_denied_responses,
            total_http_responses_1xx=total_http_responses_1xx,
            total_http_responses_2xx=total_http_responses_2xx,
            total_http_responses_3xx=total_http_responses_3xx,
            total_http_responses_4xx=total_http_responses_4xx,
            total_http_responses_5xx=total_http_responses_5xx,
            total_http_responses_other=total_http_responses_other,
            total_sessions=total_sessions,
            session_rate=session_rate,
            current_sessions=current_sessions,
            total_failed_checks_transitions=total_failed_checks_transitions,
            total_client_aborted=total_client_aborted,
            total_failed_connections=total_failed_connections,
            total_invalid_responses=total_invalid_responses,
            total_routed_requests=total_routed_requests,
            total_server_aborted=total_server_aborted,
            total_server_redispatches=total_server_redispatches,
            total_server_connection_retries=total_server_connection_retries,
            connections_waiting=connections_waiting,
            avg_connection_time_ms=avg_connection_time_ms,
            avg_queue_time_ms=avg_queue_time_ms,
            avg_server_response_time_ms=avg_server_response_time_ms,
            avg_total_time_ms=avg_total_time_ms,
            member_id=member_id,
            name=name,
            backend_id=backend_id,
            status=status,
            check_status=check_status,
            check_http_code=check_http_code,
            total_failed_checks=total_failed_checks,
            created_at=created_at,
            updated_at=updated_at,
            last_check_content=last_check_content,
            last_check_desc=last_check_desc,
        )

        return load_balancer_member_metrics_response
