from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="LoadBalancerFrontendMetricsResponse")


@_attrs_define
class LoadBalancerFrontendMetricsResponse:
    """Represents aggregated performance and traffic metrics for a load balancer frontend, including connection statistics,
    HTTP response counts, and per-second request rates. Combines general metrics, request-specific metrics, and creation
    timestamps for observability and monitoring purposes.

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
            total_http_requests (int): Total number of HTTP requests processed. Example: 12500.
            total_denied_requests (int): Total number of denied HTTP requests. Example: 35.
            total_intercepted_requests (int): Total number of intercepted HTTP requests by internal rules or actions.
                Example: 12.
            frontend_id (int): Unique identifier for the frontend. Example: 301.
            name (str): Human-readable name of the frontend. Example: frontend-http.
            request_rate (int): Rate of incoming requests per second. Example: 120.
            total_denied_connections (int): Total number of denied client connections. Example: 5.
            total_denied_sessions (int): Total number of denied sessions due to connection or rule constraints. Example: 3.
            total_invalid_requests (int): Total number of malformed or invalid HTTP requests received. Example: 7.
            created_at (datetime.datetime): Timestamp indicating when the frontend metrics entry was created.
            updated_at (datetime.datetime): Timestamp indicating when the frontend metrics entry was last updated.
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
    total_http_requests: int
    total_denied_requests: int
    total_intercepted_requests: int
    frontend_id: int
    name: str
    request_rate: int
    total_denied_connections: int
    total_denied_sessions: int
    total_invalid_requests: int
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

        total_http_requests = self.total_http_requests

        total_denied_requests = self.total_denied_requests

        total_intercepted_requests = self.total_intercepted_requests

        frontend_id = self.frontend_id

        name = self.name

        request_rate = self.request_rate

        total_denied_connections = self.total_denied_connections

        total_denied_sessions = self.total_denied_sessions

        total_invalid_requests = self.total_invalid_requests

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
                "total_http_requests": total_http_requests,
                "total_denied_requests": total_denied_requests,
                "total_intercepted_requests": total_intercepted_requests,
                "frontend_id": frontend_id,
                "name": name,
                "request_rate": request_rate,
                "total_denied_connections": total_denied_connections,
                "total_denied_sessions": total_denied_sessions,
                "total_invalid_requests": total_invalid_requests,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

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

        total_http_requests = d.pop("total_http_requests")

        total_denied_requests = d.pop("total_denied_requests")

        total_intercepted_requests = d.pop("total_intercepted_requests")

        frontend_id = d.pop("frontend_id")

        name = d.pop("name")

        request_rate = d.pop("request_rate")

        total_denied_connections = d.pop("total_denied_connections")

        total_denied_sessions = d.pop("total_denied_sessions")

        total_invalid_requests = d.pop("total_invalid_requests")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        load_balancer_frontend_metrics_response = cls(
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
            total_http_requests=total_http_requests,
            total_denied_requests=total_denied_requests,
            total_intercepted_requests=total_intercepted_requests,
            frontend_id=frontend_id,
            name=name,
            request_rate=request_rate,
            total_denied_connections=total_denied_connections,
            total_denied_sessions=total_denied_sessions,
            total_invalid_requests=total_invalid_requests,
            created_at=created_at,
            updated_at=updated_at,
        )

        return load_balancer_frontend_metrics_response
