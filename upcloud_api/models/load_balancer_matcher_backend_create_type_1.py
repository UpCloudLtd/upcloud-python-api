from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LoadBalancerMatcherBackendCreateType1")


@_attrs_define
class LoadBalancerMatcherBackendCreateType1:
    """
    Attributes:
        range_start (None | Unset):
        range_end (None | Unset):
    """

    range_start: None | Unset = UNSET
    range_end: None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        range_start = self.range_start

        range_end = self.range_end

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if range_start is not UNSET:
            field_dict["range_start"] = range_start
        if range_end is not UNSET:
            field_dict["range_end"] = range_end

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        range_start = d.pop("range_start", UNSET)

        range_end = d.pop("range_end", UNSET)

        load_balancer_matcher_backend_create_type_1 = cls(
            range_start=range_start,
            range_end=range_end,
        )

        load_balancer_matcher_backend_create_type_1.additional_properties = d
        return load_balancer_matcher_backend_create_type_1

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
