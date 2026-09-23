from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.load_balancer_action_http_rewrite_uri_create import LoadBalancerActionHttpRewriteUriCreate


T = TypeVar("T", bound="LoadBalancerActionCreateType8")


@_attrs_define
class LoadBalancerActionCreateType8:
    """
    Attributes:
        type_ (Literal['http_rewrite_uri']):
        action_http_rewrite_uri (LoadBalancerActionHttpRewriteUriCreate): Rewrite HTTP request URI using regex pattern
    """

    type_: Literal["http_rewrite_uri"]
    action_http_rewrite_uri: LoadBalancerActionHttpRewriteUriCreate

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        action_http_rewrite_uri = self.action_http_rewrite_uri.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "action_http_rewrite_uri": action_http_rewrite_uri,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.load_balancer_action_http_rewrite_uri_create import (
            LoadBalancerActionHttpRewriteUriCreate,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = cast(Literal["http_rewrite_uri"], d.pop("type"))
        if type_ != "http_rewrite_uri":
            raise ValueError(f"type must match const 'http_rewrite_uri', got '{type_}'")

        action_http_rewrite_uri = LoadBalancerActionHttpRewriteUriCreate.from_dict(d.pop("action_http_rewrite_uri"))

        load_balancer_action_create_type_8 = cls(
            type_=type_,
            action_http_rewrite_uri=action_http_rewrite_uri,
        )

        return load_balancer_action_create_type_8
