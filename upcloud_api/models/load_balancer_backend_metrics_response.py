from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.load_balancer_member_metrics_response import LoadBalancerMemberMetricsResponse


T = TypeVar("T", bound="LoadBalancerBackendMetricsResponse")


@_attrs_define
class LoadBalancerBackendMetricsResponse:
    """Represents collected performance, availability, and traffic statistics for a load balancer backend, including member
    activity, response times, and aggregated server metrics.

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
            backend_id (int): Unique identifier for the backend. Example: 401.
            name (str): Human-readable name of the backend. Example: backend-api.
            downtime_s (int): Total downtime duration in seconds. Example: 45.
            active_servers (int): Number of currently active servers in the backend. Example: 3.
            backup_servers (int): Number of backup servers available for failover. Example: 1.
            members (list[LoadBalancerMemberMetricsResponse]): List of metrics for individual backend members (servers).
            created_at (datetime.datetime): Timestamp when the backend metrics record was created.
            updated_at (datetime.datetime): Timestamp when the backend metrics record was last updated.
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
    backend_id: int
    name: str
    downtime_s: int
    active_servers: int
    backup_servers: int
    members: list[LoadBalancerMemberMetricsResponse]
    created_at: datetime.datetime
    updated_at: datetime.datetime

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

        backend_id = self.backend_id

        name = self.name

        downtime_s = self.downtime_s

        active_servers = self.active_servers

        backup_servers = self.backup_servers

        members = []
        for members_item_data in self.members:
            members_item = members_item_data.to_dict()
            members.append(members_item)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

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
                "backend_id": backend_id,
                "name": name,
                "downtime_s": downtime_s,
                "active_servers": active_servers,
                "backup_servers": backup_servers,
                "members": members,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.load_balancer_member_metrics_response import LoadBalancerMemberMetricsResponse  # noqa: PLC0415

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

        backend_id = d.pop("backend_id")

        name = d.pop("name")

        downtime_s = d.pop("downtime_s")

        active_servers = d.pop("active_servers")

        backup_servers = d.pop("backup_servers")

        members = []
        _members = d.pop("members")
        for members_item_data in _members:
            members_item = LoadBalancerMemberMetricsResponse.from_dict(members_item_data)

            members.append(members_item)

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        load_balancer_backend_metrics_response = cls(
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
            backend_id=backend_id,
            name=name,
            downtime_s=downtime_s,
            active_servers=active_servers,
            backup_servers=backup_servers,
            members=members,
            created_at=created_at,
            updated_at=updated_at,
        )

        return load_balancer_backend_metrics_response
