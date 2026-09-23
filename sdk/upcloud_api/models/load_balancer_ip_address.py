from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LoadBalancerIpAddress")


@_attrs_define
class LoadBalancerIpAddress:
    """Represents an IP address associated with a network interface of the load balancer service, including addressing
    details and provisioning information.

        Attributes:
            address (str): IP address assigned to the load balancer service on this network. Example: 192.168.1.10.
            network_name (str): Name of the network to which this IP address belongs. Example: public-network.
            created_at (datetime.datetime): Timestamp when the IP address was created (RFC 3339 format).
            updated_at (datetime.datetime): Timestamp when the IP address was last updated (RFC 3339 format).
    """

    address: str
    network_name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        network_name = self.network_name

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "address": address,
                "network_name": network_name,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        address = d.pop("address")

        network_name = d.pop("network_name")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        load_balancer_ip_address = cls(
            address=address,
            network_name=network_name,
            created_at=created_at,
            updated_at=updated_at,
        )

        load_balancer_ip_address.additional_properties = d
        return load_balancer_ip_address

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
