from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="LoadBalancerServerMetricsResponse")


@_attrs_define
class LoadBalancerServerMetricsResponse:
    """Represents detailed server-level performance and reliability metrics, including connection errors, aborted sessions,
    and routing statistics for a load balancer backend member.

        Attributes:
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
    """

    total_failed_checks_transitions: int
    total_client_aborted: int
    total_failed_connections: int
    total_invalid_responses: int
    total_routed_requests: int
    total_server_aborted: int
    total_server_redispatches: int
    total_server_connection_retries: int
    connections_waiting: int

    def to_dict(self) -> dict[str, Any]:
        total_failed_checks_transitions = self.total_failed_checks_transitions

        total_client_aborted = self.total_client_aborted

        total_failed_connections = self.total_failed_connections

        total_invalid_responses = self.total_invalid_responses

        total_routed_requests = self.total_routed_requests

        total_server_aborted = self.total_server_aborted

        total_server_redispatches = self.total_server_redispatches

        total_server_connection_retries = self.total_server_connection_retries

        connections_waiting = self.connections_waiting

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "total_failed_checks_transitions": total_failed_checks_transitions,
                "total_client_aborted": total_client_aborted,
                "total_failed_connections": total_failed_connections,
                "total_invalid_responses": total_invalid_responses,
                "total_routed_requests": total_routed_requests,
                "total_server_aborted": total_server_aborted,
                "total_server_redispatches": total_server_redispatches,
                "total_server_connection_retries": total_server_connection_retries,
                "connections_waiting": connections_waiting,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_failed_checks_transitions = d.pop("total_failed_checks_transitions")

        total_client_aborted = d.pop("total_client_aborted")

        total_failed_connections = d.pop("total_failed_connections")

        total_invalid_responses = d.pop("total_invalid_responses")

        total_routed_requests = d.pop("total_routed_requests")

        total_server_aborted = d.pop("total_server_aborted")

        total_server_redispatches = d.pop("total_server_redispatches")

        total_server_connection_retries = d.pop("total_server_connection_retries")

        connections_waiting = d.pop("connections_waiting")

        load_balancer_server_metrics_response = cls(
            total_failed_checks_transitions=total_failed_checks_transitions,
            total_client_aborted=total_client_aborted,
            total_failed_connections=total_failed_connections,
            total_invalid_responses=total_invalid_responses,
            total_routed_requests=total_routed_requests,
            total_server_aborted=total_server_aborted,
            total_server_redispatches=total_server_redispatches,
            total_server_connection_retries=total_server_connection_retries,
            connections_waiting=connections_waiting,
        )

        return load_balancer_server_metrics_response
