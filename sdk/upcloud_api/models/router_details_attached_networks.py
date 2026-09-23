from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.router_details_attached_networks_network_item import RouterDetailsAttachedNetworksNetworkItem


T = TypeVar("T", bound="RouterDetailsAttachedNetworks")


@_attrs_define
class RouterDetailsAttachedNetworks:
    """Networks attached to the router.

    Example:
        {'network': [{'uuid': '03804f7f-828a-4610-867f-9d62cf9fc14f'}]}

    Attributes:
        network (list[RouterDetailsAttachedNetworksNetworkItem]):
    """

    network: list[RouterDetailsAttachedNetworksNetworkItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        network = []
        for network_item_data in self.network:
            network_item = network_item_data.to_dict()
            network.append(network_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "network": network,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.router_details_attached_networks_network_item import (
            RouterDetailsAttachedNetworksNetworkItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        network = []
        _network = d.pop("network")
        for network_item_data in _network:
            network_item = RouterDetailsAttachedNetworksNetworkItem.from_dict(network_item_data)

            network.append(network_item)

        router_details_attached_networks = cls(
            network=network,
        )

        router_details_attached_networks.additional_properties = d
        return router_details_attached_networks

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
