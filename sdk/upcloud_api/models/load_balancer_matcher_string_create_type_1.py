from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.load_balancer_string_matcher_methods_no_value import LoadBalancerStringMatcherMethodsNoValue

T = TypeVar("T", bound="LoadBalancerMatcherStringCreateType1")


@_attrs_define
class LoadBalancerMatcherStringCreateType1:
    """
    Attributes:
        method (LoadBalancerStringMatcherMethodsNoValue): String matcher methods (no value) Example: exists.
    """

    method: LoadBalancerStringMatcherMethodsNoValue

    def to_dict(self) -> dict[str, Any]:
        method = self.method.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "method": method,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        method = LoadBalancerStringMatcherMethodsNoValue(d.pop("method"))

        load_balancer_matcher_string_create_type_1 = cls(
            method=method,
        )

        return load_balancer_matcher_string_create_type_1
