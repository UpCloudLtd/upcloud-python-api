from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.network_boolean_yesno import NetworkBooleanYesno
from ..models.network_ip_family import NetworkIpFamily
from ..types import UNSET, Unset

T = TypeVar("T", bound="NetworkDetailsIpNetworksIpNetworkItem")


@_attrs_define
class NetworkDetailsIpNetworksIpNetworkItem:
    """
    Attributes:
        address (str): IP CIDR
        family (NetworkIpFamily): IP address family Example: IPv4.
        dhcp (NetworkBooleanYesno | Unset): Boolean value represented as yes/no Example: yes.
        dhcp_bootfile_url (str | Unset): HTTP or HTTPS URL for DHCP bootfile delivery.
        dhcp_default_route (NetworkBooleanYesno | Unset): Boolean value represented as yes/no Example: yes.
        dhcp_dns (list[str] | Unset):
        dhcp_routes (list[str] | Unset):
        gateway (str | Unset): IP address Example: 10.0.0.20.
    """

    address: str
    family: NetworkIpFamily
    dhcp: NetworkBooleanYesno | Unset = UNSET
    dhcp_bootfile_url: str | Unset = UNSET
    dhcp_default_route: NetworkBooleanYesno | Unset = UNSET
    dhcp_dns: list[str] | Unset = UNSET
    dhcp_routes: list[str] | Unset = UNSET
    gateway: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        family = self.family.value

        dhcp: str | Unset = UNSET
        if not isinstance(self.dhcp, Unset):
            dhcp = self.dhcp.value

        dhcp_bootfile_url = self.dhcp_bootfile_url

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

        gateway: str | Unset
        if isinstance(self.gateway, Unset):
            gateway = UNSET
        else:
            gateway = self.gateway

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "address": address,
                "family": family,
            }
        )
        if dhcp is not UNSET:
            field_dict["dhcp"] = dhcp
        if dhcp_bootfile_url is not UNSET:
            field_dict["dhcp_bootfile_url"] = dhcp_bootfile_url
        if dhcp_default_route is not UNSET:
            field_dict["dhcp_default_route"] = dhcp_default_route
        if dhcp_dns is not UNSET:
            field_dict["dhcp_dns"] = dhcp_dns
        if dhcp_routes is not UNSET:
            field_dict["dhcp_routes"] = dhcp_routes
        if gateway is not UNSET:
            field_dict["gateway"] = gateway

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        address = d.pop("address")

        family = NetworkIpFamily(d.pop("family"))

        _dhcp = d.pop("dhcp", UNSET)
        dhcp: NetworkBooleanYesno | Unset
        if isinstance(_dhcp, Unset):
            dhcp = UNSET
        else:
            dhcp = NetworkBooleanYesno(_dhcp)

        dhcp_bootfile_url = d.pop("dhcp_bootfile_url", UNSET)

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

        def _parse_gateway(data: object) -> str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(str | Unset, data)

        gateway = _parse_gateway(d.pop("gateway", UNSET))

        network_details_ip_networks_ip_network_item = cls(
            address=address,
            family=family,
            dhcp=dhcp,
            dhcp_bootfile_url=dhcp_bootfile_url,
            dhcp_default_route=dhcp_default_route,
            dhcp_dns=dhcp_dns,
            dhcp_routes=dhcp_routes,
            gateway=gateway,
        )

        network_details_ip_networks_ip_network_item.additional_properties = d
        return network_details_ip_networks_ip_network_item

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
