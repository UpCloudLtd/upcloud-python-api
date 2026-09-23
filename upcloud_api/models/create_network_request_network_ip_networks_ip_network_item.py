from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.network_boolean_yesno import NetworkBooleanYesno
from ..models.network_ip_family import NetworkIpFamily
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_network_request_network_ip_networks_ip_network_item_dhcp_routes_configuration import (
        CreateNetworkRequestNetworkIpNetworksIpNetworkItemDhcpRoutesConfiguration,
    )


T = TypeVar("T", bound="CreateNetworkRequestNetworkIpNetworksIpNetworkItem")


@_attrs_define
class CreateNetworkRequestNetworkIpNetworksIpNetworkItem:
    """
    Attributes:
        family (NetworkIpFamily): IP address family Example: IPv4.
        address (str): IP CIDR
        dhcp (NetworkBooleanYesno): Boolean value represented as yes/no Example: yes.
        gateway (str | Unset): IP address Example: 10.0.0.20.
        dhcp_default_route (NetworkBooleanYesno | Unset): Boolean value represented as yes/no Example: yes.
        dhcp_dns (list[str] | Unset):
        dhcp_routes (list[str] | Unset):
        dhcp_bootfile_url (str | Unset): HTTP or HTTPS URL for DHCP bootfile delivery.
        dhcp_routes_configuration (CreateNetworkRequestNetworkIpNetworksIpNetworkItemDhcpRoutesConfiguration | Unset):
    """

    family: NetworkIpFamily
    address: str
    dhcp: NetworkBooleanYesno
    gateway: str | Unset = UNSET
    dhcp_default_route: NetworkBooleanYesno | Unset = UNSET
    dhcp_dns: list[str] | Unset = UNSET
    dhcp_routes: list[str] | Unset = UNSET
    dhcp_bootfile_url: str | Unset = UNSET
    dhcp_routes_configuration: CreateNetworkRequestNetworkIpNetworksIpNetworkItemDhcpRoutesConfiguration | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        family = self.family.value

        address = self.address

        dhcp = self.dhcp.value

        gateway: str | Unset
        if isinstance(self.gateway, Unset):
            gateway = UNSET
        else:
            gateway = self.gateway

        dhcp_default_route: str | Unset = UNSET
        if not isinstance(self.dhcp_default_route, Unset):
            dhcp_default_route = self.dhcp_default_route.value

        dhcp_dns: list[str] | Unset = UNSET
        if not isinstance(self.dhcp_dns, Unset):
            dhcp_dns = []
            for dhcp_dns_item_data in self.dhcp_dns:
                dhcp_dns_item: str
                dhcp_dns_item = dhcp_dns_item_data
                dhcp_dns.append(dhcp_dns_item)

        dhcp_routes: list[str] | Unset = UNSET
        if not isinstance(self.dhcp_routes, Unset):
            dhcp_routes = self.dhcp_routes

        dhcp_bootfile_url = self.dhcp_bootfile_url

        dhcp_routes_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dhcp_routes_configuration, Unset):
            dhcp_routes_configuration = self.dhcp_routes_configuration.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "family": family,
                "address": address,
                "dhcp": dhcp,
            }
        )
        if gateway is not UNSET:
            field_dict["gateway"] = gateway
        if dhcp_default_route is not UNSET:
            field_dict["dhcp_default_route"] = dhcp_default_route
        if dhcp_dns is not UNSET:
            field_dict["dhcp_dns"] = dhcp_dns
        if dhcp_routes is not UNSET:
            field_dict["dhcp_routes"] = dhcp_routes
        if dhcp_bootfile_url is not UNSET:
            field_dict["dhcp_bootfile_url"] = dhcp_bootfile_url
        if dhcp_routes_configuration is not UNSET:
            field_dict["dhcp_routes_configuration"] = dhcp_routes_configuration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_network_request_network_ip_networks_ip_network_item_dhcp_routes_configuration import (
            CreateNetworkRequestNetworkIpNetworksIpNetworkItemDhcpRoutesConfiguration,  # noqa: PLC0415
        )

        d = dict(src_dict)
        family = NetworkIpFamily(d.pop("family"))

        address = d.pop("address")

        dhcp = NetworkBooleanYesno(d.pop("dhcp"))

        def _parse_gateway(data: object) -> str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(str | Unset, data)

        gateway = _parse_gateway(d.pop("gateway", UNSET))

        _dhcp_default_route = d.pop("dhcp_default_route", UNSET)
        dhcp_default_route: NetworkBooleanYesno | Unset
        if isinstance(_dhcp_default_route, Unset):
            dhcp_default_route = UNSET
        else:
            dhcp_default_route = NetworkBooleanYesno(_dhcp_default_route)

        _dhcp_dns = d.pop("dhcp_dns", UNSET)
        dhcp_dns: list[str] | Unset = UNSET
        if _dhcp_dns is not UNSET:
            dhcp_dns = []
            for dhcp_dns_item_data in _dhcp_dns:

                def _parse_dhcp_dns_item(data: object) -> str:
                    return cast(str, data)

                dhcp_dns_item = _parse_dhcp_dns_item(dhcp_dns_item_data)

                dhcp_dns.append(dhcp_dns_item)

        dhcp_routes = cast(list[str], d.pop("dhcp_routes", UNSET))

        dhcp_bootfile_url = d.pop("dhcp_bootfile_url", UNSET)

        _dhcp_routes_configuration = d.pop("dhcp_routes_configuration", UNSET)
        dhcp_routes_configuration: CreateNetworkRequestNetworkIpNetworksIpNetworkItemDhcpRoutesConfiguration | Unset
        if isinstance(_dhcp_routes_configuration, Unset):
            dhcp_routes_configuration = UNSET
        else:
            dhcp_routes_configuration = (
                CreateNetworkRequestNetworkIpNetworksIpNetworkItemDhcpRoutesConfiguration.from_dict(
                    _dhcp_routes_configuration
                )
            )

        create_network_request_network_ip_networks_ip_network_item = cls(
            family=family,
            address=address,
            dhcp=dhcp,
            gateway=gateway,
            dhcp_default_route=dhcp_default_route,
            dhcp_dns=dhcp_dns,
            dhcp_routes=dhcp_routes,
            dhcp_bootfile_url=dhcp_bootfile_url,
            dhcp_routes_configuration=dhcp_routes_configuration,
        )

        create_network_request_network_ip_networks_ip_network_item.additional_properties = d
        return create_network_request_network_ip_networks_ip_network_item

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
