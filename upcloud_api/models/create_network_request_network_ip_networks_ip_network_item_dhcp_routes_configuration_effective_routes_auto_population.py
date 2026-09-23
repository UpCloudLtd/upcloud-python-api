from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.network_boolean_yesno import NetworkBooleanYesno
from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="CreateNetworkRequestNetworkIpNetworksIpNetworkItemDhcpRoutesConfigurationEffectiveRoutesAutoPopulation"
)


@_attrs_define
class CreateNetworkRequestNetworkIpNetworksIpNetworkItemDhcpRoutesConfigurationEffectiveRoutesAutoPopulation:
    """
    Attributes:
        enabled (NetworkBooleanYesno | Unset): Boolean value represented as yes/no Example: yes.
        exclude_by_source (list[str] | Unset):
        filter_by_destination (list[str] | Unset):
        filter_by_route_type (list[str] | Unset):
    """

    enabled: NetworkBooleanYesno | Unset = UNSET
    exclude_by_source: list[str] | Unset = UNSET
    filter_by_destination: list[str] | Unset = UNSET
    filter_by_route_type: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled: str | Unset = UNSET
        if not isinstance(self.enabled, Unset):
            enabled = self.enabled.value

        exclude_by_source: list[str] | Unset = UNSET
        if not isinstance(self.exclude_by_source, Unset):
            exclude_by_source = self.exclude_by_source

        filter_by_destination: list[str] | Unset = UNSET
        if not isinstance(self.filter_by_destination, Unset):
            filter_by_destination = self.filter_by_destination

        filter_by_route_type: list[str] | Unset = UNSET
        if not isinstance(self.filter_by_route_type, Unset):
            filter_by_route_type = self.filter_by_route_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if exclude_by_source is not UNSET:
            field_dict["exclude_by_source"] = exclude_by_source
        if filter_by_destination is not UNSET:
            field_dict["filter_by_destination"] = filter_by_destination
        if filter_by_route_type is not UNSET:
            field_dict["filter_by_route_type"] = filter_by_route_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _enabled = d.pop("enabled", UNSET)
        enabled: NetworkBooleanYesno | Unset
        if isinstance(_enabled, Unset):
            enabled = UNSET
        else:
            enabled = NetworkBooleanYesno(_enabled)

        exclude_by_source = cast(list[str], d.pop("exclude_by_source", UNSET))

        filter_by_destination = cast(list[str], d.pop("filter_by_destination", UNSET))

        filter_by_route_type = cast(list[str], d.pop("filter_by_route_type", UNSET))

        create_network_request_network_ip_networks_ip_network_item_dhcp_routes_configuration_effective_routes_auto_population = cls(
            enabled=enabled,
            exclude_by_source=exclude_by_source,
            filter_by_destination=filter_by_destination,
            filter_by_route_type=filter_by_route_type,
        )

        create_network_request_network_ip_networks_ip_network_item_dhcp_routes_configuration_effective_routes_auto_population.additional_properties = d
        return create_network_request_network_ip_networks_ip_network_item_dhcp_routes_configuration_effective_routes_auto_population

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
