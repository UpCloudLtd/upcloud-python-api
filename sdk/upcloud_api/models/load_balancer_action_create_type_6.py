from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.load_balancer_action_set_header_create import LoadBalancerActionSetHeaderCreate


T = TypeVar("T", bound="LoadBalancerActionCreateType6")


@_attrs_define
class LoadBalancerActionCreateType6:
    """
    Attributes:
        type_ (Literal['set_response_header']):
        action_set_response_header (LoadBalancerActionSetHeaderCreate): Forwarding rule HTTP set header action Example:
            {'header': 'X-Custom-Header', 'value': 'CustomValue'}.
    """

    type_: Literal["set_response_header"]
    action_set_response_header: LoadBalancerActionSetHeaderCreate

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        action_set_response_header = self.action_set_response_header.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "action_set_response_header": action_set_response_header,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.load_balancer_action_set_header_create import LoadBalancerActionSetHeaderCreate  # noqa: PLC0415

        d = dict(src_dict)
        type_ = cast(Literal["set_response_header"], d.pop("type"))
        if type_ != "set_response_header":
            raise ValueError(f"type must match const 'set_response_header', got '{type_}'")

        action_set_response_header = LoadBalancerActionSetHeaderCreate.from_dict(d.pop("action_set_response_header"))

        load_balancer_action_create_type_6 = cls(
            type_=type_,
            action_set_response_header=action_set_response_header,
        )

        return load_balancer_action_create_type_6
