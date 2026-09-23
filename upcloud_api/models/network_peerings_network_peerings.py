from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.network_peering import NetworkPeering


T = TypeVar("T", bound="NetworkPeeringsNetworkPeerings")


@_attrs_define
class NetworkPeeringsNetworkPeerings:
    """
    Example:
        {'network_peering': [{'configured_status': 'active', 'name': 'Peering A->B', 'network': {'uuid':
            '03126dc1-a69f-4bc2-8b24-e31c22d64712'}, 'peer_network': {'uuid': '03585987-bf7d-4544-8e9b-5a1b4d74a333'},
            'state': 'active', 'uuid': '0f7984bc-5d72-4aaf-b587-90e6a8f32efc', 'created_at': '2026-07-01T00:00:00Z'}]}

    Attributes:
        network_peering (list[NetworkPeering]):
    """

    network_peering: list[NetworkPeering]

    def to_dict(self) -> dict[str, Any]:
        network_peering = []
        for network_peering_item_data in self.network_peering:
            network_peering_item = network_peering_item_data.to_dict()
            network_peering.append(network_peering_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "network_peering": network_peering,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.network_peering import NetworkPeering  # noqa: PLC0415

        d = dict(src_dict)
        network_peering = []
        _network_peering = d.pop("network_peering")
        for network_peering_item_data in _network_peering:
            network_peering_item = NetworkPeering.from_dict(network_peering_item_data)

            network_peering.append(network_peering_item)

        network_peerings_network_peerings = cls(
            network_peering=network_peering,
        )

        return network_peerings_network_peerings
