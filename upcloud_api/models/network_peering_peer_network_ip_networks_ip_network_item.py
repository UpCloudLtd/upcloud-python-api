from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.network_peering_ip_family import NetworkPeeringIpFamily
from ..types import UNSET, Unset

T = TypeVar("T", bound="NetworkPeeringPeerNetworkIpNetworksIpNetworkItem")


@_attrs_define
class NetworkPeeringPeerNetworkIpNetworksIpNetworkItem:
    """
    Attributes:
        address (str | Unset): IP CIDR
        family (NetworkPeeringIpFamily | Unset): IP address family Example: IPv4.
    """

    address: str | Unset = UNSET
    family: NetworkPeeringIpFamily | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        family: str | Unset = UNSET
        if not isinstance(self.family, Unset):
            family = self.family.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if family is not UNSET:
            field_dict["family"] = family

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        address = d.pop("address", UNSET)

        _family = d.pop("family", UNSET)
        family: NetworkPeeringIpFamily | Unset
        if isinstance(_family, Unset):
            family = UNSET
        else:
            family = NetworkPeeringIpFamily(_family)

        network_peering_peer_network_ip_networks_ip_network_item = cls(
            address=address,
            family=family,
        )

        network_peering_peer_network_ip_networks_ip_network_item.additional_properties = d
        return network_peering_peer_network_ip_networks_ip_network_item

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
