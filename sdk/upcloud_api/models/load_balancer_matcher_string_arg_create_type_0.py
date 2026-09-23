from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.load_balancer_string_matcher_methods import LoadBalancerStringMatcherMethods
from ..types import UNSET, Unset

T = TypeVar("T", bound="LoadBalancerMatcherStringArgCreateType0")


@_attrs_define
class LoadBalancerMatcherStringArgCreateType0:
    """
    Attributes:
        method (LoadBalancerStringMatcherMethods): String matcher methods Example: substring.
        name (str): Name of the parameter
        value (str): Value
        ignore_case (bool | Unset): Ignore case
    """

    method: LoadBalancerStringMatcherMethods
    name: str
    value: str
    ignore_case: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        method = self.method.value

        name = self.name

        value = self.value

        ignore_case = self.ignore_case

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "method": method,
                "name": name,
                "value": value,
            }
        )
        if ignore_case is not UNSET:
            field_dict["ignore_case"] = ignore_case

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        method = LoadBalancerStringMatcherMethods(d.pop("method"))

        name = d.pop("name")

        value = d.pop("value")

        ignore_case = d.pop("ignore_case", UNSET)

        load_balancer_matcher_string_arg_create_type_0 = cls(
            method=method,
            name=name,
            value=value,
            ignore_case=ignore_case,
        )

        return load_balancer_matcher_string_arg_create_type_0
