from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.load_balancer_action_set_forwarded_headers import LoadBalancerActionSetForwardedHeaders


T = TypeVar("T", bound="LoadBalancerActionCreateType4")


@_attrs_define
class LoadBalancerActionCreateType4:
    """
    Attributes:
        type_ (Literal['set_forwarded_headers']):
        action_set_forwarded_headers (LoadBalancerActionSetForwardedHeaders): Forwarding rule Set forwarded headers
            Example: {}.
    """

    type_: Literal["set_forwarded_headers"]
    action_set_forwarded_headers: LoadBalancerActionSetForwardedHeaders

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        action_set_forwarded_headers = self.action_set_forwarded_headers.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "action_set_forwarded_headers": action_set_forwarded_headers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.load_balancer_action_set_forwarded_headers import (
            LoadBalancerActionSetForwardedHeaders,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = cast(Literal["set_forwarded_headers"], d.pop("type"))
        if type_ != "set_forwarded_headers":
            raise ValueError(f"type must match const 'set_forwarded_headers', got '{type_}'")

        action_set_forwarded_headers = LoadBalancerActionSetForwardedHeaders.from_dict(
            d.pop("action_set_forwarded_headers")
        )

        load_balancer_action_create_type_4 = cls(
            type_=type_,
            action_set_forwarded_headers=action_set_forwarded_headers,
        )

        return load_balancer_action_create_type_4
