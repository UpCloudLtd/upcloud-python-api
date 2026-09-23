from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="LoadBalancerActionSetForwardedHeadersResponse")


@_attrs_define
class LoadBalancerActionSetForwardedHeadersResponse:
    """Defines an action that automatically adds standard X-Forwarded-* headers (such as X-Forwarded-For and X-Forwarded-
    Proto) to requests before forwarding them to the backend. Used when the action type is 'set_forwarded_headers'.

        Example:
            {}

    """

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        load_balancer_action_set_forwarded_headers_response = cls()

        return load_balancer_action_set_forwarded_headers_response
