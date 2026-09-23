from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.load_balancer_matcher_host_create import LoadBalancerMatcherHostCreate


T = TypeVar("T", bound="LoadBalancerMatcherCreateType9")


@_attrs_define
class LoadBalancerMatcherCreateType9:
    """
    Attributes:
        type_ (Literal['host']):
        match_host (LoadBalancerMatcherHostCreate): Forwarding rule host matcher Example: {'value': 'example.com'}.
        inverse (bool | Unset): Inverse rule
    """

    type_: Literal["host"]
    match_host: LoadBalancerMatcherHostCreate
    inverse: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        match_host = self.match_host.to_dict()

        inverse = self.inverse

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "match_host": match_host,
            }
        )
        if inverse is not UNSET:
            field_dict["inverse"] = inverse

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.load_balancer_matcher_host_create import LoadBalancerMatcherHostCreate  # noqa: PLC0415

        d = dict(src_dict)
        type_ = cast(Literal["host"], d.pop("type"))
        if type_ != "host":
            raise ValueError(f"type must match const 'host', got '{type_}'")

        match_host = LoadBalancerMatcherHostCreate.from_dict(d.pop("match_host"))

        inverse = d.pop("inverse", UNSET)

        load_balancer_matcher_create_type_9 = cls(
            type_=type_,
            match_host=match_host,
            inverse=inverse,
        )

        return load_balancer_matcher_create_type_9
