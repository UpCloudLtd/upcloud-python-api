from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.load_balancer_action_use_backend_create import LoadBalancerActionUseBackendCreate


T = TypeVar("T", bound="LoadBalancerActionCreateType0")


@_attrs_define
class LoadBalancerActionCreateType0:
    """
    Attributes:
        type_ (Literal['use_backend']):
        action_use_backend (LoadBalancerActionUseBackendCreate): Forwarding rule use backend action Example: {'backend':
            'backend-1'}.
    """

    type_: Literal["use_backend"]
    action_use_backend: LoadBalancerActionUseBackendCreate

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        action_use_backend = self.action_use_backend.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "action_use_backend": action_use_backend,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.load_balancer_action_use_backend_create import LoadBalancerActionUseBackendCreate  # noqa: PLC0415

        d = dict(src_dict)
        type_ = cast(Literal["use_backend"], d.pop("type"))
        if type_ != "use_backend":
            raise ValueError(f"type must match const 'use_backend', got '{type_}'")

        action_use_backend = LoadBalancerActionUseBackendCreate.from_dict(d.pop("action_use_backend"))

        load_balancer_action_create_type_0 = cls(
            type_=type_,
            action_use_backend=action_use_backend,
        )

        return load_balancer_action_create_type_0
