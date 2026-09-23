from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="LoadBalancerActionUseBackendResponse")


@_attrs_define
class LoadBalancerActionUseBackendResponse:
    """Defines the backend target to which the request should be routed when the rule matches. Used when the action type is
    'use_backend'.

        Example:
            {'backend': 'api-backend'}

        Attributes:
            backend (str): Name of the backend to which the request should be routed when this action executes. Example:
                api-backend.
    """

    backend: str

    def to_dict(self) -> dict[str, Any]:
        backend = self.backend

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "backend": backend,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        backend = d.pop("backend")

        load_balancer_action_use_backend_response = cls(
            backend=backend,
        )

        return load_balancer_action_use_backend_response
