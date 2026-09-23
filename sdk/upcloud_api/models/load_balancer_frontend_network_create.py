from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="LoadBalancerFrontendNetworkCreate")


@_attrs_define
class LoadBalancerFrontendNetworkCreate:
    """Load Balancer Network

    Example:
        {'name': 'public-network-1'}

    Attributes:
        name (str): Name of the Network Example: public-network-1.
    """

    name: str

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        load_balancer_frontend_network_create = cls(
            name=name,
        )

        return load_balancer_frontend_network_create
