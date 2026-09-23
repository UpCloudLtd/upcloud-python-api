from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.load_balancer_action_tcp_reject_create import LoadBalancerActionTcpRejectCreate


T = TypeVar("T", bound="LoadBalancerActionCreateType3")


@_attrs_define
class LoadBalancerActionCreateType3:
    """
    Attributes:
        type_ (Literal['tcp_reject']):
        action_tcp_reject (LoadBalancerActionTcpRejectCreate): Forwarding rule TCP reject action Example: {}.
    """

    type_: Literal["tcp_reject"]
    action_tcp_reject: LoadBalancerActionTcpRejectCreate

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        action_tcp_reject = self.action_tcp_reject.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "action_tcp_reject": action_tcp_reject,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.load_balancer_action_tcp_reject_create import LoadBalancerActionTcpRejectCreate  # noqa: PLC0415

        d = dict(src_dict)
        type_ = cast(Literal["tcp_reject"], d.pop("type"))
        if type_ != "tcp_reject":
            raise ValueError(f"type must match const 'tcp_reject', got '{type_}'")

        action_tcp_reject = LoadBalancerActionTcpRejectCreate.from_dict(d.pop("action_tcp_reject"))

        load_balancer_action_create_type_3 = cls(
            type_=type_,
            action_tcp_reject=action_tcp_reject,
        )

        return load_balancer_action_create_type_3
