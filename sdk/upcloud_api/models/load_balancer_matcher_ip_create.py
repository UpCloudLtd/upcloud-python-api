from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="LoadBalancerMatcherIpCreate")


@_attrs_define
class LoadBalancerMatcherIpCreate:
    """Forwarding rule IP matcher for matching source IP addresses. Accepts IPv4, IPv6 addresses or CIDR notation.

    Example:
        {'value': '192.168.1.1'}

    Attributes:
        value (str): IP address or CIDR to match against. Accepts IPv4 (e.g., 192.168.1.1), IPv6 (e.g., 2001:db8::1), or
            CIDR notation (e.g., 192.168.1.0/24). Example: 192.168.1.1.
    """

    value: str

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value")

        load_balancer_matcher_ip_create = cls(
            value=value,
        )

        return load_balancer_matcher_ip_create
