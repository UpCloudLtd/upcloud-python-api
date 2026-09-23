from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.network_peering_peer_network_ip_networks import NetworkPeeringPeerNetworkIpNetworks


T = TypeVar("T", bound="NetworkPeeringPeerNetwork")


@_attrs_define
class NetworkPeeringPeerNetwork:
    """Describes the peer side of the peering

    Attributes:
        ip_networks (NetworkPeeringPeerNetworkIpNetworks | Unset): note: only visible if both sides have a peering
            defined
        uuid (UUID | Unset): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
    """

    ip_networks: NetworkPeeringPeerNetworkIpNetworks | Unset = UNSET
    uuid: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ip_networks: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ip_networks, Unset):
            ip_networks = self.ip_networks.to_dict()

        uuid: str | Unset = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ip_networks is not UNSET:
            field_dict["ip_networks"] = ip_networks
        if uuid is not UNSET:
            field_dict["uuid"] = uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.network_peering_peer_network_ip_networks import (
            NetworkPeeringPeerNetworkIpNetworks,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _ip_networks = d.pop("ip_networks", UNSET)
        ip_networks: NetworkPeeringPeerNetworkIpNetworks | Unset
        if isinstance(_ip_networks, Unset):
            ip_networks = UNSET
        else:
            ip_networks = NetworkPeeringPeerNetworkIpNetworks.from_dict(_ip_networks)

        _uuid = d.pop("uuid", UNSET)
        uuid: UUID | Unset
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = UUID(_uuid)

        network_peering_peer_network = cls(
            ip_networks=ip_networks,
            uuid=uuid,
        )

        network_peering_peer_network.additional_properties = d
        return network_peering_peer_network

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
