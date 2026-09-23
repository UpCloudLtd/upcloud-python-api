from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="LoadBalancerCommonMetricsResponse")


@_attrs_define
class LoadBalancerCommonMetricsResponse:
    """Represents general traffic and session statistics collected for a load balancer frontend or backend, including
    request and response byte counts, HTTP status distribution, and session activity metrics.

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

        load_balancer_common_metrics_response = cls(
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
        )

        return load_balancer_common_metrics_response
