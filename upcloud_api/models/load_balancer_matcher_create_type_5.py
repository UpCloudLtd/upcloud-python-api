from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.load_balancer_matcher_string_arg_create_type_0 import LoadBalancerMatcherStringArgCreateType0
    from ..models.load_balancer_matcher_string_arg_create_type_1 import LoadBalancerMatcherStringArgCreateType1


T = TypeVar("T", bound="LoadBalancerMatcherCreateType5")


@_attrs_define
class LoadBalancerMatcherCreateType5:
    """
    Attributes:
        type_ (Literal['url_param']):
        match_url_param (LoadBalancerMatcherStringArgCreateType0 | LoadBalancerMatcherStringArgCreateType1): Forwarding
            rule string matcher
        inverse (bool | Unset): Inverse rule
    """

    type_: Literal["url_param"]
    match_url_param: LoadBalancerMatcherStringArgCreateType0 | LoadBalancerMatcherStringArgCreateType1
    inverse: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.load_balancer_matcher_string_arg_create_type_0 import (
            LoadBalancerMatcherStringArgCreateType0,  # noqa: PLC0415
        )

        type_ = self.type_

        match_url_param: dict[str, Any]
        if isinstance(self.match_url_param, LoadBalancerMatcherStringArgCreateType0):
            match_url_param = self.match_url_param.to_dict()
        else:
            match_url_param = self.match_url_param.to_dict()

        inverse = self.inverse

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "match_url_param": match_url_param,
            }
        )
        if inverse is not UNSET:
            field_dict["inverse"] = inverse

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.load_balancer_matcher_string_arg_create_type_0 import (
            LoadBalancerMatcherStringArgCreateType0,  # noqa: PLC0415
        )
        from ..models.load_balancer_matcher_string_arg_create_type_1 import (
            LoadBalancerMatcherStringArgCreateType1,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = cast(Literal["url_param"], d.pop("type"))
        if type_ != "url_param":
            raise ValueError(f"type must match const 'url_param', got '{type_}'")

        def _parse_match_url_param(
            data: object,
        ) -> LoadBalancerMatcherStringArgCreateType0 | LoadBalancerMatcherStringArgCreateType1:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasload_balancer_matcher_string_arg_create_type_0 = (
                    LoadBalancerMatcherStringArgCreateType0.from_dict(data)
                )

                return componentsschemasload_balancer_matcher_string_arg_create_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemasload_balancer_matcher_string_arg_create_type_1 = (
                LoadBalancerMatcherStringArgCreateType1.from_dict(data)
            )

            return componentsschemasload_balancer_matcher_string_arg_create_type_1

        match_url_param = _parse_match_url_param(d.pop("match_url_param"))

        inverse = d.pop("inverse", UNSET)

        load_balancer_matcher_create_type_5 = cls(
            type_=type_,
            match_url_param=match_url_param,
            inverse=inverse,
        )

        return load_balancer_matcher_create_type_5
