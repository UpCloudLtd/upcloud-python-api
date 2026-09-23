from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="LoadBalancerMatchIpResponse")


@_attrs_define
class LoadBalancerMatchIpResponse:
    """Defines a match condition based on the source IP address or subnet. Used when the matcher type is 'src_ip'.

    Example:
        {'value': '192.168.1.0/24'}

    Attributes:
        value (str): IP address or CIDR subnet to match against the source IP. Accepts IPv4, IPv6, or CIDR notation.
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

        load_balancer_match_ip_response = cls(
            value=value,
        )

        return load_balancer_match_ip_response
