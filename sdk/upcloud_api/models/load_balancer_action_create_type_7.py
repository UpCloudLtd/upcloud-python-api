from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.load_balancer_action_http_rewrite_path_create import LoadBalancerActionHttpRewritePathCreate


T = TypeVar("T", bound="LoadBalancerActionCreateType7")


@_attrs_define
class LoadBalancerActionCreateType7:
    """
    Attributes:
        type_ (Literal['http_rewrite_path']):
        action_http_rewrite_path (LoadBalancerActionHttpRewritePathCreate): Rewrite HTTP request path using regex
            pattern
    """

    type_: Literal["http_rewrite_path"]
    action_http_rewrite_path: LoadBalancerActionHttpRewritePathCreate

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        action_http_rewrite_path = self.action_http_rewrite_path.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "action_http_rewrite_path": action_http_rewrite_path,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.load_balancer_action_http_rewrite_path_create import (
            LoadBalancerActionHttpRewritePathCreate,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = cast(Literal["http_rewrite_path"], d.pop("type"))
        if type_ != "http_rewrite_path":
            raise ValueError(f"type must match const 'http_rewrite_path', got '{type_}'")

        action_http_rewrite_path = LoadBalancerActionHttpRewritePathCreate.from_dict(d.pop("action_http_rewrite_path"))

        load_balancer_action_create_type_7 = cls(
            type_=type_,
            action_http_rewrite_path=action_http_rewrite_path,
        )

        return load_balancer_action_create_type_7
