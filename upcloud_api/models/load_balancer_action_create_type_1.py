from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.load_balancer_action_http_return_create import LoadBalancerActionHttpReturnCreate


T = TypeVar("T", bound="LoadBalancerActionCreateType1")


@_attrs_define
class LoadBalancerActionCreateType1:
    """
    Attributes:
        type_ (Literal['http_return']):
        action_http_return (LoadBalancerActionHttpReturnCreate): Forwarding rule HTTP Return action
    """

    type_: Literal["http_return"]
    action_http_return: LoadBalancerActionHttpReturnCreate

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        action_http_return = self.action_http_return.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "action_http_return": action_http_return,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.load_balancer_action_http_return_create import LoadBalancerActionHttpReturnCreate  # noqa: PLC0415

        d = dict(src_dict)
        type_ = cast(Literal["http_return"], d.pop("type"))
        if type_ != "http_return":
            raise ValueError(f"type must match const 'http_return', got '{type_}'")

        action_http_return = LoadBalancerActionHttpReturnCreate.from_dict(d.pop("action_http_return"))

        load_balancer_action_create_type_1 = cls(
            type_=type_,
            action_http_return=action_http_return,
        )

        return load_balancer_action_create_type_1
