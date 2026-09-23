from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.load_balancer_matcher_string_arg_create_type_0 import LoadBalancerMatcherStringArgCreateType0
    from ..models.load_balancer_matcher_string_arg_create_type_1 import LoadBalancerMatcherStringArgCreateType1


T = TypeVar("T", bound="LoadBalancerMatcherCreateType4")


@_attrs_define
class LoadBalancerMatcherCreateType4:
    """
    Attributes:
        type_ (Literal['header']):
        match_header (LoadBalancerMatcherStringArgCreateType0 | LoadBalancerMatcherStringArgCreateType1): Forwarding
            rule string matcher
        inverse (bool | Unset): Inverse rule
    """

    type_: Literal["header"]
    match_header: LoadBalancerMatcherStringArgCreateType0 | LoadBalancerMatcherStringArgCreateType1
    inverse: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.load_balancer_matcher_string_arg_create_type_0 import (
            LoadBalancerMatcherStringArgCreateType0,  # noqa: PLC0415
        )

        type_ = self.type_

        match_header: dict[str, Any]
        if isinstance(self.match_header, LoadBalancerMatcherStringArgCreateType0):
            match_header = self.match_header.to_dict()
        else:
            match_header = self.match_header.to_dict()

        inverse = self.inverse

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "match_header": match_header,
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
        type_ = cast(Literal["header"], d.pop("type"))
        if type_ != "header":
            raise ValueError(f"type must match const 'header', got '{type_}'")

        def _parse_match_header(
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

        match_header = _parse_match_header(d.pop("match_header"))

        inverse = d.pop("inverse", UNSET)

        load_balancer_matcher_create_type_4 = cls(
            type_=type_,
            match_header=match_header,
            inverse=inverse,
        )

        return load_balancer_matcher_create_type_4
