from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="LoadBalancerActionUseBackendCreate")


@_attrs_define
class LoadBalancerActionUseBackendCreate:
    """Forwarding rule use backend action

    Example:
        {'backend': 'backend-1'}

    Attributes:
        backend (str): Name of the backend Example: backend-1.
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

        load_balancer_action_use_backend_create = cls(
            backend=backend,
        )

        return load_balancer_action_use_backend_create
