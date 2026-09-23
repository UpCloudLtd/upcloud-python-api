from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="LoadBalancerActionHttpRewriteUriResponse")


@_attrs_define
class LoadBalancerActionHttpRewriteUriResponse:
    """Defines an action that rewrites the HTTP request URI using a regex pattern.

    Example:
        {'match_pattern': '^/api/(.*)$', 'rewrite_to': '/v2/\\\\1'}

    Attributes:
        match_pattern (str): Regex pattern to match against the full URI.
        rewrite_to (str): Replacement pattern (can use capture groups like \\1).
    """

    match_pattern: str
    rewrite_to: str

    def to_dict(self) -> dict[str, Any]:
        match_pattern = self.match_pattern

        rewrite_to = self.rewrite_to

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "match_pattern": match_pattern,
                "rewrite_to": rewrite_to,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        match_pattern = d.pop("match_pattern")

        rewrite_to = d.pop("rewrite_to")

        load_balancer_action_http_rewrite_uri_response = cls(
            match_pattern=match_pattern,
            rewrite_to=rewrite_to,
        )

        return load_balancer_action_http_rewrite_uri_response
