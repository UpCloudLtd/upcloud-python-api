from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.load_balancer_matcher_ip_create import LoadBalancerMatcherIpCreate


T = TypeVar("T", bound="LoadBalancerMatcherCreateType0")


@_attrs_define
class LoadBalancerMatcherCreateType0:
    """
    Attributes:
        type_ (Literal['src_ip']):
        match_src_ip (LoadBalancerMatcherIpCreate): Forwarding rule IP matcher for matching source IP addresses. Accepts
            IPv4, IPv6 addresses or CIDR notation. Example: {'value': '192.168.1.1'}.
        inverse (bool | Unset): Inverse rule
    """

    type_: Literal["src_ip"]
    match_src_ip: LoadBalancerMatcherIpCreate
    inverse: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        match_src_ip = self.match_src_ip.to_dict()

        inverse = self.inverse

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "match_src_ip": match_src_ip,
            }
        )
        if inverse is not UNSET:
            field_dict["inverse"] = inverse

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.load_balancer_matcher_ip_create import LoadBalancerMatcherIpCreate  # noqa: PLC0415

        d = dict(src_dict)
        type_ = cast(Literal["src_ip"], d.pop("type"))
        if type_ != "src_ip":
            raise ValueError(f"type must match const 'src_ip', got '{type_}'")

        match_src_ip = LoadBalancerMatcherIpCreate.from_dict(d.pop("match_src_ip"))

        inverse = d.pop("inverse", UNSET)

        load_balancer_matcher_create_type_0 = cls(
            type_=type_,
            match_src_ip=match_src_ip,
            inverse=inverse,
        )

        return load_balancer_matcher_create_type_0
