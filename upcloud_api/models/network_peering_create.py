from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.network_peering_create_configured_status import NetworkPeeringCreateConfiguredStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.network_peering_create_network import NetworkPeeringCreateNetwork
    from ..models.network_peering_create_peer_network import NetworkPeeringCreatePeerNetwork


T = TypeVar("T", bound="NetworkPeeringCreate")


@_attrs_define
class NetworkPeeringCreate:
    """Describes the mutable properties when creating a network-peering between two networks

    Example:
        {'configured_status': 'active', 'name': 'Peering A->B', 'network': {'uuid':
            '03126dc1-a69f-4bc2-8b24-e31c22d64712'}, 'peer_network': {'uuid': '03585987-bf7d-4544-8e9b-5a1b4d74a333'}}

    Attributes:
        name (str):  Example: Peering A->B.
        network (NetworkPeeringCreateNetwork): Describes the local side of the peering
        peer_network (NetworkPeeringCreatePeerNetwork): Describes the peer side of the peering
        configured_status (NetworkPeeringCreateConfiguredStatus | Unset):  Default:
            NetworkPeeringCreateConfiguredStatus.ACTIVE.
    """

    name: str
    network: NetworkPeeringCreateNetwork
    peer_network: NetworkPeeringCreatePeerNetwork
    configured_status: NetworkPeeringCreateConfiguredStatus | Unset = NetworkPeeringCreateConfiguredStatus.ACTIVE

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        network = self.network.to_dict()

        peer_network = self.peer_network.to_dict()

        configured_status: str | Unset = UNSET
        if not isinstance(self.configured_status, Unset):
            configured_status = self.configured_status.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "network": network,
                "peer_network": peer_network,
            }
        )
        if configured_status is not UNSET:
            field_dict["configured_status"] = configured_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.network_peering_create_network import NetworkPeeringCreateNetwork  # noqa: PLC0415
        from ..models.network_peering_create_peer_network import NetworkPeeringCreatePeerNetwork  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        network = NetworkPeeringCreateNetwork.from_dict(d.pop("network"))

        peer_network = NetworkPeeringCreatePeerNetwork.from_dict(d.pop("peer_network"))

        _configured_status = d.pop("configured_status", UNSET)
        configured_status: NetworkPeeringCreateConfiguredStatus | Unset
        if isinstance(_configured_status, Unset):
            configured_status = UNSET
        else:
            configured_status = NetworkPeeringCreateConfiguredStatus(_configured_status)

        network_peering_create = cls(
            name=name,
            network=network,
            peer_network=peer_network,
            configured_status=configured_status,
        )

        return network_peering_create
