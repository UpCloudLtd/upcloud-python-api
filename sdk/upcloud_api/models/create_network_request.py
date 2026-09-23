from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.create_network_request_network import CreateNetworkRequestNetwork


T = TypeVar("T", bound="CreateNetworkRequest")


@_attrs_define
class CreateNetworkRequest:
    """Request schema for creating a network

    Example:
        {'network': {'type': 'private', 'name': 'backend-net', 'zone': 'fi-hel2', 'ip_networks': {'ip_network':
            [{'family': 'IPv4', 'address': '10.0.0.0/24', 'dhcp': 'yes'}]}}}

    Attributes:
        network (CreateNetworkRequestNetwork):  Example: {'type': 'private', 'name': 'backend-net', 'zone': 'fi-hel2',
            'ip_networks': {'ip_network': [{'family': 'IPv4', 'address': '10.0.0.0/24', 'dhcp': 'yes'}]}}.
    """

    network: CreateNetworkRequestNetwork
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        network = self.network.to_dict()

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
        from ..models.create_network_request_network import CreateNetworkRequestNetwork  # noqa: PLC0415

        d = dict(src_dict)
        network = CreateNetworkRequestNetwork.from_dict(d.pop("network"))

        create_network_request = cls(
            network=network,
        )

        create_network_request.additional_properties = d
        return create_network_request

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
