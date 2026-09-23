from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.load_balancer_problem_response import LoadBalancerProblemResponse


T = TypeVar("T", bound="LoadBalancerChallengeProblemResponse")


@_attrs_define
class LoadBalancerChallengeProblemResponse:
    """Represents a problem encountered during ACME challenge validation for a specific hostname. Includes detailed error
    information following the Problem Details (RFC7807) format.

        Example:
            {'hostname': 'example.com', 'problem': {'type': 'https://api.example.com/problems/dns-lookup-failed', 'title':
                'DNS lookup failed', 'detail': "The DNS resolver could not resolve the domain name 'example.com'.", 'status':
                400, 'correlation_id': 'req-7b39a1c9b6a14e07b9d4c2a4c5d8b7f2'}}

        Attributes:
            hostname (str): The hostname for which the ACME challenge validation failed or encountered an error. Example:
                example.com.
            problem (LoadBalancerProblemResponse): Represents an error object following the Problem Details specification
                (RFC7807). Provides machine-readable and human-readable information about an error that occurred while
                processing a request. Example: {'type': 'https://api.example.com/problems/invalid-request', 'title': 'Invalid
                request', 'detail': 'The provided domain name is not valid.', 'status': 400, 'invalid_params': [{'name':
                'hostnames[0]', 'reason': 'Invalid domain name format'}], 'correlation_id':
                'req-8b29d3a6a4cf4d22a17e2b8e31cd4a12'}.
    """

    hostname: str
    problem: LoadBalancerProblemResponse

    def to_dict(self) -> dict[str, Any]:
        hostname = self.hostname

        problem = self.problem.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "hostname": hostname,
                "problem": problem,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.load_balancer_problem_response import LoadBalancerProblemResponse  # noqa: PLC0415

        d = dict(src_dict)
        hostname = d.pop("hostname")

        problem = LoadBalancerProblemResponse.from_dict(d.pop("problem"))

        load_balancer_challenge_problem_response = cls(
            hostname=hostname,
            problem=problem,
        )

        return load_balancer_challenge_problem_response
