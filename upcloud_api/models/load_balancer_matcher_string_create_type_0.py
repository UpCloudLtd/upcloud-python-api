from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.load_balancer_string_matcher_methods import LoadBalancerStringMatcherMethods
from ..types import UNSET, Unset

T = TypeVar("T", bound="LoadBalancerMatcherStringCreateType0")


@_attrs_define
class LoadBalancerMatcherStringCreateType0:
    """
    Attributes:
        method (LoadBalancerStringMatcherMethods): String matcher methods Example: substring.
        value (str): Value
        ignore_case (bool | Unset): Ignore case
    """

    method: LoadBalancerStringMatcherMethods
    value: str
    ignore_case: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        method = self.method.value

        value = self.value

        ignore_case = self.ignore_case

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "method": method,
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

        value = d.pop("value")

        ignore_case = d.pop("ignore_case", UNSET)

        load_balancer_matcher_string_create_type_0 = cls(
            method=method,
            value=value,
            ignore_case=ignore_case,
        )

        return load_balancer_matcher_string_create_type_0
