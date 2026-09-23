from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.load_balancer_matcher_int_create_type_0 import LoadBalancerMatcherIntCreateType0
    from ..models.load_balancer_matcher_int_create_type_1 import LoadBalancerMatcherIntCreateType1


T = TypeVar("T", bound="LoadBalancerMatcherCreateType2")


@_attrs_define
class LoadBalancerMatcherCreateType2:
    """
    Attributes:
        type_ (Literal['body_size']):
        match_body_size (LoadBalancerMatcherIntCreateType0 | LoadBalancerMatcherIntCreateType1): Forwarding rule integer
            matcher
        inverse (bool | Unset): Inverse rule
    """

    type_: Literal["body_size"]
    match_body_size: LoadBalancerMatcherIntCreateType0 | LoadBalancerMatcherIntCreateType1
    inverse: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.load_balancer_matcher_int_create_type_0 import LoadBalancerMatcherIntCreateType0  # noqa: PLC0415

        type_ = self.type_

        match_body_size: dict[str, Any]
        if isinstance(self.match_body_size, LoadBalancerMatcherIntCreateType0):
            match_body_size = self.match_body_size.to_dict()
        else:
            match_body_size = self.match_body_size.to_dict()

        inverse = self.inverse

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "match_body_size": match_body_size,
            }
        )
        if inverse is not UNSET:
            field_dict["inverse"] = inverse

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.load_balancer_matcher_int_create_type_0 import LoadBalancerMatcherIntCreateType0  # noqa: PLC0415
        from ..models.load_balancer_matcher_int_create_type_1 import LoadBalancerMatcherIntCreateType1  # noqa: PLC0415

        d = dict(src_dict)
        type_ = cast(Literal["body_size"], d.pop("type"))
        if type_ != "body_size":
            raise ValueError(f"type must match const 'body_size', got '{type_}'")

        def _parse_match_body_size(
            data: object,
        ) -> LoadBalancerMatcherIntCreateType0 | LoadBalancerMatcherIntCreateType1:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasload_balancer_matcher_int_create_type_0 = LoadBalancerMatcherIntCreateType0.from_dict(
                    data
                )

                return componentsschemasload_balancer_matcher_int_create_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemasload_balancer_matcher_int_create_type_1 = LoadBalancerMatcherIntCreateType1.from_dict(data)

            return componentsschemasload_balancer_matcher_int_create_type_1

        match_body_size = _parse_match_body_size(d.pop("match_body_size"))

        inverse = d.pop("inverse", UNSET)

        load_balancer_matcher_create_type_2 = cls(
            type_=type_,
            match_body_size=match_body_size,
            inverse=inverse,
        )

        return load_balancer_matcher_create_type_2
