from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.network_peering_configured_status import NetworkPeeringConfiguredStatus
from ..models.network_peering_state import NetworkPeeringState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.network_peering_network import NetworkPeeringNetwork
    from ..models.network_peering_peer_network import NetworkPeeringPeerNetwork


T = TypeVar("T", bound="NetworkPeering")


@_attrs_define
class NetworkPeering:
    """Network peering object describes a peering relationship between two networks

    Example:
        {'configured_status': 'active', 'name': 'Peering A->B', 'network': {'ip_networks': {'ip_network': [{'address':
            '192.168.0.0/24', 'family': 'IPv4'}, {'address': 'fc02:c4f3::/64', 'family': 'IPv6'}]}, 'uuid':
            '03126dc1-a69f-4bc2-8b24-e31c22d64712'}, 'peer_network': {'ip_networks': {'ip_network': [{'address':
            '192.168.99.0/24', 'family': 'IPv4'}, {'address': 'fc02:c4f3:99::/64', 'family': 'IPv6'}]}, 'uuid':
            '03585987-bf7d-4544-8e9b-5a1b4d74a333'}, 'state': 'active', 'uuid': '0f7984bc-5d72-4aaf-b587-90e6a8f32efc',
            'created_at': '2026-07-01T00:00:00Z'}

    Attributes:
        configured_status (NetworkPeeringConfiguredStatus | Unset):
        name (str | Unset): Name of a network peering relationship.
        network (NetworkPeeringNetwork | Unset): Describes the local side of the peering
        peer_network (NetworkPeeringPeerNetwork | Unset): Describes the peer side of the peering
        state (NetworkPeeringState | Unset): Current lifecycle state of a network peering.
        uuid (UUID | Unset): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        created_at (datetime.datetime | None | Unset): When the network peering was created
        updated_at (datetime.datetime | None | Unset): When the network peering was last updated. Null until the first
            modification.
    """

    configured_status: NetworkPeeringConfiguredStatus | Unset = UNSET
    name: str | Unset = UNSET
    network: NetworkPeeringNetwork | Unset = UNSET
    peer_network: NetworkPeeringPeerNetwork | Unset = UNSET
    state: NetworkPeeringState | Unset = UNSET
    uuid: UUID | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        configured_status: str | Unset = UNSET
        if not isinstance(self.configured_status, Unset):
            configured_status = self.configured_status.value

        name = self.name

        network: dict[str, Any] | Unset = UNSET
        if not isinstance(self.network, Unset):
            network = self.network.to_dict()

        peer_network: dict[str, Any] | Unset = UNSET
        if not isinstance(self.peer_network, Unset):
            peer_network = self.peer_network.to_dict()

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        uuid: str | Unset = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if configured_status is not UNSET:
            field_dict["configured_status"] = configured_status
        if name is not UNSET:
            field_dict["name"] = name
        if network is not UNSET:
            field_dict["network"] = network
        if peer_network is not UNSET:
            field_dict["peer_network"] = peer_network
        if state is not UNSET:
            field_dict["state"] = state
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.network_peering_network import NetworkPeeringNetwork  # noqa: PLC0415
        from ..models.network_peering_peer_network import NetworkPeeringPeerNetwork  # noqa: PLC0415

        d = dict(src_dict)
        _configured_status = d.pop("configured_status", UNSET)
        configured_status: NetworkPeeringConfiguredStatus | Unset
        if isinstance(_configured_status, Unset):
            configured_status = UNSET
        else:
            configured_status = NetworkPeeringConfiguredStatus(_configured_status)

        name = d.pop("name", UNSET)

        _network = d.pop("network", UNSET)
        network: NetworkPeeringNetwork | Unset
        if isinstance(_network, Unset):
            network = UNSET
        else:
            network = NetworkPeeringNetwork.from_dict(_network)

        _peer_network = d.pop("peer_network", UNSET)
        peer_network: NetworkPeeringPeerNetwork | Unset
        if isinstance(_peer_network, Unset):
            peer_network = UNSET
        else:
            peer_network = NetworkPeeringPeerNetwork.from_dict(_peer_network)

        _state = d.pop("state", UNSET)
        state: NetworkPeeringState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = NetworkPeeringState(_state)

        _uuid = d.pop("uuid", UNSET)
        uuid: UUID | Unset
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = UUID(_uuid)

        def _parse_created_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = datetime.datetime.fromisoformat(data)

                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))

        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = datetime.datetime.fromisoformat(data)

                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))

        network_peering = cls(
            configured_status=configured_status,
            name=name,
            network=network,
            peer_network=peer_network,
            state=state,
            uuid=uuid,
            created_at=created_at,
            updated_at=updated_at,
        )

        network_peering.additional_properties = d
        return network_peering

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
