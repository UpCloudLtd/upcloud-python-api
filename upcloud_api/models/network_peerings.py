from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.network_peerings_network_peerings import NetworkPeeringsNetworkPeerings


T = TypeVar("T", bound="NetworkPeerings")


@_attrs_define
class NetworkPeerings:
    """Network peerings

    Example:
        {'network_peerings': {'network_peering': [{'configured_status': 'active', 'name': 'Peering A->B', 'network':
            {'uuid': '03126dc1-a69f-4bc2-8b24-e31c22d64712'}, 'peer_network': {'uuid':
            '03585987-bf7d-4544-8e9b-5a1b4d74a333'}, 'state': 'active', 'uuid': '0f7984bc-5d72-4aaf-b587-90e6a8f32efc',
            'created_at': '2026-07-01T00:00:00Z'}]}}

    Attributes:
        network_peerings (NetworkPeeringsNetworkPeerings):  Example: {'network_peering': [{'configured_status':
            'active', 'name': 'Peering A->B', 'network': {'uuid': '03126dc1-a69f-4bc2-8b24-e31c22d64712'}, 'peer_network':
            {'uuid': '03585987-bf7d-4544-8e9b-5a1b4d74a333'}, 'state': 'active', 'uuid':
            '0f7984bc-5d72-4aaf-b587-90e6a8f32efc', 'created_at': '2026-07-01T00:00:00Z'}]}.
    """

    network_peerings: NetworkPeeringsNetworkPeerings

    def to_dict(self) -> dict[str, Any]:
        network_peerings = self.network_peerings.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "network_peerings": network_peerings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.network_peerings_network_peerings import NetworkPeeringsNetworkPeerings  # noqa: PLC0415

        d = dict(src_dict)
        network_peerings = NetworkPeeringsNetworkPeerings.from_dict(d.pop("network_peerings"))

        network_peerings = cls(
            network_peerings=network_peerings,
        )

        return network_peerings
