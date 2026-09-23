from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.create_network_request_network_ip_networks_ip_network_item import (
        CreateNetworkRequestNetworkIpNetworksIpNetworkItem,
    )


T = TypeVar("T", bound="CreateNetworkRequestNetworkIpNetworks")


@_attrs_define
class CreateNetworkRequestNetworkIpNetworks:
    """
    Attributes:
        ip_network (list[CreateNetworkRequestNetworkIpNetworksIpNetworkItem]):
    """

    ip_network: list[CreateNetworkRequestNetworkIpNetworksIpNetworkItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ip_network = []
        for ip_network_item_data in self.ip_network:
            ip_network_item = ip_network_item_data.to_dict()
            ip_network.append(ip_network_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ip_network": ip_network,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_network_request_network_ip_networks_ip_network_item import (
            CreateNetworkRequestNetworkIpNetworksIpNetworkItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        ip_network = []
        _ip_network = d.pop("ip_network")
        for ip_network_item_data in _ip_network:
            ip_network_item = CreateNetworkRequestNetworkIpNetworksIpNetworkItem.from_dict(ip_network_item_data)

            ip_network.append(ip_network_item)

        create_network_request_network_ip_networks = cls(
            ip_network=ip_network,
        )

        create_network_request_network_ip_networks.additional_properties = d
        return create_network_request_network_ip_networks

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
