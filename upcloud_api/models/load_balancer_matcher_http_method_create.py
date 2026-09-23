from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.load_balancer_http_methods import LoadBalancerHttpMethods

T = TypeVar("T", bound="LoadBalancerMatcherHttpMethodCreate")


@_attrs_define
class LoadBalancerMatcherHttpMethodCreate:
    """Forwarding rule HTTP method matcher

    Attributes:
        value (LoadBalancerHttpMethods): HTTP methods
    """

    value: LoadBalancerHttpMethods

    def to_dict(self) -> dict[str, Any]:
        value = self.value.value

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
        value = LoadBalancerHttpMethods(d.pop("value"))

        load_balancer_matcher_http_method_create = cls(
            value=value,
        )

        return load_balancer_matcher_http_method_create
