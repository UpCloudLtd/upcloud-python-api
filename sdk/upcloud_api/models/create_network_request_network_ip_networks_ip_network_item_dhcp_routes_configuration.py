from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_network_request_network_ip_networks_ip_network_item_dhcp_routes_configuration_effective_routes_auto_population import (
        CreateNetworkRequestNetworkIpNetworksIpNetworkItemDhcpRoutesConfigurationEffectiveRoutesAutoPopulation,
    )


T = TypeVar("T", bound="CreateNetworkRequestNetworkIpNetworksIpNetworkItemDhcpRoutesConfiguration")


@_attrs_define
class CreateNetworkRequestNetworkIpNetworksIpNetworkItemDhcpRoutesConfiguration:
    """
    Attributes:
        effective_routes_auto_population
            (CreateNetworkRequestNetworkIpNetworksIpNetworkItemDhcpRoutesConfigurationEffectiveRoutesAutoPopulation |
            Unset):
    """

    effective_routes_auto_population: (
        CreateNetworkRequestNetworkIpNetworksIpNetworkItemDhcpRoutesConfigurationEffectiveRoutesAutoPopulation | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        effective_routes_auto_population: dict[str, Any] | Unset = UNSET
        if not isinstance(self.effective_routes_auto_population, Unset):
            effective_routes_auto_population = self.effective_routes_auto_population.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if effective_routes_auto_population is not UNSET:
            field_dict["effective_routes_auto_population"] = effective_routes_auto_population

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_network_request_network_ip_networks_ip_network_item_dhcp_routes_configuration_effective_routes_auto_population import (
            CreateNetworkRequestNetworkIpNetworksIpNetworkItemDhcpRoutesConfigurationEffectiveRoutesAutoPopulation,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _effective_routes_auto_population = d.pop("effective_routes_auto_population", UNSET)
        effective_routes_auto_population: (
            CreateNetworkRequestNetworkIpNetworksIpNetworkItemDhcpRoutesConfigurationEffectiveRoutesAutoPopulation
            | Unset
        )
        if isinstance(_effective_routes_auto_population, Unset):
            effective_routes_auto_population = UNSET
        else:
            effective_routes_auto_population = CreateNetworkRequestNetworkIpNetworksIpNetworkItemDhcpRoutesConfigurationEffectiveRoutesAutoPopulation.from_dict(
                _effective_routes_auto_population
            )

        create_network_request_network_ip_networks_ip_network_item_dhcp_routes_configuration = cls(
            effective_routes_auto_population=effective_routes_auto_population,
        )

        create_network_request_network_ip_networks_ip_network_item_dhcp_routes_configuration.additional_properties = d
        return create_network_request_network_ip_networks_ip_network_item_dhcp_routes_configuration

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
