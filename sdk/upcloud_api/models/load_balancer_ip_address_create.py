from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="LoadBalancerIpAddressCreate")


@_attrs_define
class LoadBalancerIpAddressCreate:
    """IP address object

    Example:
        {'address': '192.168.1.10', 'network_name': 'private-net-1'}

    Attributes:
        address (str): IP address Example: 192.168.1.10.
        network_name (str | Unset): Name of the target network Example: private-net-1.
    """

    address: str
    network_name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        network_name = self.network_name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "address": address,
            }
        )
        if network_name is not UNSET:
            field_dict["network_name"] = network_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        address = d.pop("address")

        network_name = d.pop("network_name", UNSET)

        load_balancer_ip_address_create = cls(
            address=address,
            network_name=network_name,
        )

        return load_balancer_ip_address_create
