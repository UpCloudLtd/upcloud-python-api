from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="LoadBalancerActionSetForwardedHeaders")


@_attrs_define
class LoadBalancerActionSetForwardedHeaders:
    """Forwarding rule Set forwarded headers

    Example:
        {}

    """

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        load_balancer_action_set_forwarded_headers = cls()

        return load_balancer_action_set_forwarded_headers
