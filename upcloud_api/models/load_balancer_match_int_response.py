from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.load_balancer_match_int_response_method import LoadBalancerMatchIntResponseMethod
from ..types import UNSET, Unset

T = TypeVar("T", bound="LoadBalancerMatchIntResponse")


@_attrs_define
class LoadBalancerMatchIntResponse:
    """Defines integer matching criteria for requests or responses.

    Example:
        {'method': 'greater_or_equal', 'value': 100, 'range_start': 0, 'range_end': 1024}

    Attributes:
        method (LoadBalancerMatchIntResponseMethod): Comparison method used to evaluate the integer value. Example:
            greater_or_equal.
        value (int): Integer value to compare against using the specified comparison method.
        range_start (int | Unset): Starting value of the range for range-based integer matching. Example: 0.
        range_end (int | Unset): Ending value of the range for range-based integer matching. Example: 1024.
    """

    method: LoadBalancerMatchIntResponseMethod
    value: int
    range_start: int | Unset = UNSET
    range_end: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method = self.method.value

        value = self.value

        range_start = self.range_start

        range_end = self.range_end

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "method": method,
                "value": value,
            }
        )
        if range_start is not UNSET:
            field_dict["range_start"] = range_start
        if range_end is not UNSET:
            field_dict["range_end"] = range_end

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        method = LoadBalancerMatchIntResponseMethod(d.pop("method"))

        value = d.pop("value")

        range_start = d.pop("range_start", UNSET)

        range_end = d.pop("range_end", UNSET)

        load_balancer_match_int_response = cls(
            method=method,
            value=value,
            range_start=range_start,
            range_end=range_end,
        )

        load_balancer_match_int_response.additional_properties = d
        return load_balancer_match_int_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
