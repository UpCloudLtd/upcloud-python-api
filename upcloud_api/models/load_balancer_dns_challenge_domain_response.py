from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="LoadBalancerDnsChallengeDomainResponse")


@_attrs_define
class LoadBalancerDnsChallengeDomainResponse:
    """Response schema for DNS challenge domain information.

    Attributes:
        domain (str): The DNS challenge domain to use for ACME validation. Example: _acme-
            challenge.example.upcloudlb.com.
    """

    domain: str

    def to_dict(self) -> dict[str, Any]:
        domain = self.domain

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "domain": domain,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        domain = d.pop("domain")

        load_balancer_dns_challenge_domain_response = cls(
            domain=domain,
        )

        return load_balancer_dns_challenge_domain_response
