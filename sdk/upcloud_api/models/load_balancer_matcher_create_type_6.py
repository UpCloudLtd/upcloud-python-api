from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.load_balancer_matcher_http_method_create import LoadBalancerMatcherHttpMethodCreate


T = TypeVar("T", bound="LoadBalancerMatcherCreateType6")


@_attrs_define
class LoadBalancerMatcherCreateType6:
    """
    Attributes:
        type_ (Literal['http_method']):
        match_http_method (LoadBalancerMatcherHttpMethodCreate): Forwarding rule HTTP method matcher
        inverse (bool | Unset): Inverse rule
    """

    type_: Literal["http_method"]
    match_http_method: LoadBalancerMatcherHttpMethodCreate
    inverse: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        match_http_method = self.match_http_method.to_dict()

        inverse = self.inverse

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "match_http_method": match_http_method,
            }
        )
        if inverse is not UNSET:
            field_dict["inverse"] = inverse

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.load_balancer_matcher_http_method_create import (
            LoadBalancerMatcherHttpMethodCreate,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = cast(Literal["http_method"], d.pop("type"))
        if type_ != "http_method":
            raise ValueError(f"type must match const 'http_method', got '{type_}'")

        match_http_method = LoadBalancerMatcherHttpMethodCreate.from_dict(d.pop("match_http_method"))

        inverse = d.pop("inverse", UNSET)

        load_balancer_matcher_create_type_6 = cls(
            type_=type_,
            match_http_method=match_http_method,
            inverse=inverse,
        )

        return load_balancer_matcher_create_type_6
