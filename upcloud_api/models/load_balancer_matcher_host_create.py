from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="LoadBalancerMatcherHostCreate")


@_attrs_define
class LoadBalancerMatcherHostCreate:
    """Forwarding rule host matcher

    Example:
        {'value': 'example.com'}

    Attributes:
        value (str): Value
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

        load_balancer_matcher_host_create = cls(
            value=value,
        )

        return load_balancer_matcher_host_create
