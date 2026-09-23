from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="LoadBalancerActionHttpRedirectResponse")


@_attrs_define
class LoadBalancerActionHttpRedirectResponse:
    """Defines an HTTP redirection action used to redirect incoming requests to a specified URL with a given HTTP status
    code. Used when the action type is 'http_redirect'.

        Example:
            {'location': 'https://example.com', 'status': 301}

        Attributes:
            location (str): Absolute or relative URL to which requests are redirected. Example: https://example.com.
            status (int): HTTP status code for the redirection. Common values are 301 (permanent) or 302 (temporary).
                Example: 301.
    """

    location: str
    status: int

    def to_dict(self) -> dict[str, Any]:
        location = self.location

        status = self.status

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "location": location,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        location = d.pop("location")

        status = d.pop("status")

        load_balancer_action_http_redirect_response = cls(
            location=location,
            status=status,
        )

        return load_balancer_action_http_redirect_response
