from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.network_details import NetworkDetails


T = TypeVar("T", bound="NetworksNetworks")


@_attrs_define
class NetworksNetworks:
    """Container object for network items.

    Example:
        {'network': [{'uuid': '8f6d1ec2-8f5e-4b67-8fcb-6fa9c1a8a001', 'name': 'backend-net', 'type': 'private', 'zone':
            'fi-hel2'}]}

    Attributes:
        network (list[NetworkDetails]):
    """

    network: list[NetworkDetails]

    def to_dict(self) -> dict[str, Any]:
        network = []
        for network_item_data in self.network:
            network_item = network_item_data.to_dict()
            network.append(network_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "network": network,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.network_details import NetworkDetails  # noqa: PLC0415

        d = dict(src_dict)
        network = []
        _network = d.pop("network")
        for network_item_data in _network:
            network_item = NetworkDetails.from_dict(network_item_data)

            network.append(network_item)

        networks_networks = cls(
            network=network,
        )

        return networks_networks
