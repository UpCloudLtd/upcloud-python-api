from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.load_balancer_string_matcher_methods_no_value import LoadBalancerStringMatcherMethodsNoValue

T = TypeVar("T", bound="LoadBalancerMatcherStringArgCreateType1")


@_attrs_define
class LoadBalancerMatcherStringArgCreateType1:
    """
    Attributes:
        method (LoadBalancerStringMatcherMethodsNoValue): String matcher methods (no value) Example: exists.
        name (str): Name of the parameter
    """

    method: LoadBalancerStringMatcherMethodsNoValue
    name: str

    def to_dict(self) -> dict[str, Any]:
        method = self.method.value

        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "method": method,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        method = LoadBalancerStringMatcherMethodsNoValue(d.pop("method"))

        name = d.pop("name")

        load_balancer_matcher_string_arg_create_type_1 = cls(
            method=method,
            name=name,
        )

        return load_balancer_matcher_string_arg_create_type_1
