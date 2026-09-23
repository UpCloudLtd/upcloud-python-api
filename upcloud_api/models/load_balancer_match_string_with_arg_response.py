from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.load_balancer_match_string_response_method import LoadBalancerMatchStringResponseMethod
from ..types import UNSET, Unset

T = TypeVar("T", bound="LoadBalancerMatchStringWithArgResponse")


@_attrs_define
class LoadBalancerMatchStringWithArgResponse:
    """Extends MatchString with an additional 'name' parameter, used for matchers that require a key-value pair (e.g.,
    matching headers, cookies, or URL parameters).

        Example:
            {'name': 'Authorization', 'method': 'contains', 'value': '/api', 'ignore_case': True}

        Attributes:
            name (str):  Example: Authorization.
            method (LoadBalancerMatchStringResponseMethod | Unset): String comparison method used to evaluate the match
                condition. Example: contains.
            value (str | Unset): String value or pattern to match against using the specified comparison method. Example:
                /api.
            ignore_case (bool | Unset): Indicates whether the string comparison should be case-insensitive. Example: True.
    """

    name: str
    method: LoadBalancerMatchStringResponseMethod | Unset = UNSET
    value: str | Unset = UNSET
    ignore_case: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        method: str | Unset = UNSET
        if not isinstance(self.method, Unset):
            method = self.method.value

        value = self.value

        ignore_case = self.ignore_case

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if method is not UNSET:
            field_dict["method"] = method
        if value is not UNSET:
            field_dict["value"] = value
        if ignore_case is not UNSET:
            field_dict["ignore_case"] = ignore_case

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        _method = d.pop("method", UNSET)
        method: LoadBalancerMatchStringResponseMethod | Unset
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = LoadBalancerMatchStringResponseMethod(_method)

        value = d.pop("value", UNSET)

        ignore_case = d.pop("ignore_case", UNSET)

        load_balancer_match_string_with_arg_response = cls(
            name=name,
            method=method,
            value=value,
            ignore_case=ignore_case,
        )

        load_balancer_match_string_with_arg_response.additional_properties = d
        return load_balancer_match_string_with_arg_response

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
