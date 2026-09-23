from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.load_balancer_matcher_int_create_type_0 import LoadBalancerMatcherIntCreateType0
    from ..models.load_balancer_matcher_int_create_type_1 import LoadBalancerMatcherIntCreateType1


T = TypeVar("T", bound="LoadBalancerMatcherCreateType14")


@_attrs_define
class LoadBalancerMatcherCreateType14:
    """
    Attributes:
        type_ (Literal['http_status']):
        match_http_status (LoadBalancerMatcherIntCreateType0 | LoadBalancerMatcherIntCreateType1): Forwarding rule
            integer matcher
        inverse (bool | Unset): Inverse rule
    """

    type_: Literal["http_status"]
    match_http_status: LoadBalancerMatcherIntCreateType0 | LoadBalancerMatcherIntCreateType1
    inverse: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.load_balancer_matcher_int_create_type_0 import LoadBalancerMatcherIntCreateType0  # noqa: PLC0415

        type_ = self.type_

        match_http_status: dict[str, Any]
        if isinstance(self.match_http_status, LoadBalancerMatcherIntCreateType0):
            match_http_status = self.match_http_status.to_dict()
        else:
            match_http_status = self.match_http_status.to_dict()

        inverse = self.inverse

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "match_http_status": match_http_status,
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
        type_ = cast(Literal["http_status"], d.pop("type"))
        if type_ != "http_status":
            raise ValueError(f"type must match const 'http_status', got '{type_}'")

        def _parse_match_http_status(
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

        match_http_status = _parse_match_http_status(d.pop("match_http_status"))

        inverse = d.pop("inverse", UNSET)

        load_balancer_matcher_create_type_14 = cls(
            type_=type_,
            match_http_status=match_http_status,
            inverse=inverse,
        )

        return load_balancer_matcher_create_type_14
