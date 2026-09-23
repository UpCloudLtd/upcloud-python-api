from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="LoadBalancerActionSetHeaderCreate")


@_attrs_define
class LoadBalancerActionSetHeaderCreate:
    """Forwarding rule HTTP set header action

    Example:
        {'header': 'X-Custom-Header', 'value': 'CustomValue'}

    Attributes:
        header (str): Name of the HTTP header to set or modify in the request or response. Example: X-Custom-Header.
        value (str | Unset): Value to assign to the specified HTTP header. Example: CustomValue.
    """

    header: str
    value: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        header = self.header

        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "header": header,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        header = d.pop("header")

        value = d.pop("value", UNSET)

        load_balancer_action_set_header_create = cls(
            header=header,
            value=value,
        )

        return load_balancer_action_set_header_create
