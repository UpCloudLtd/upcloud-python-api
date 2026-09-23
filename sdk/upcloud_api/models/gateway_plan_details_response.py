from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gateway_service_features import GatewayServiceFeatures
from ..types import UNSET, Unset

T = TypeVar("T", bound="GatewayPlanDetailsResponse")


@_attrs_define
class GatewayPlanDetailsResponse:
    """Response schema for gateway plan details.

    Attributes:
        name (str | Unset): Name of the plan
        server_number (int | Unset): Number of nodes
        per_gateway_max_connections (int | Unset): Per gateway (agent node server) maximum conntrack connections
        supported_features (list[GatewayServiceFeatures] | Unset):
        vpn_tunnel_amount (int | Unset): Number of VPN tunnels this plan allows.
        per_gateway_bandwidth_mbps (int | Unset): Per gateway (agent node server) bandwidth in megabits per second.
        per_gateway_maximum_vpn_bandwidth_mbps (int | Unset): Per gateway (agent node server) maximum vpn bandwidth in
            megabits per second.
    """

    name: str | Unset = UNSET
    server_number: int | Unset = UNSET
    per_gateway_max_connections: int | Unset = UNSET
    supported_features: list[GatewayServiceFeatures] | Unset = UNSET
    vpn_tunnel_amount: int | Unset = UNSET
    per_gateway_bandwidth_mbps: int | Unset = UNSET
    per_gateway_maximum_vpn_bandwidth_mbps: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        server_number = self.server_number

        per_gateway_max_connections = self.per_gateway_max_connections

        supported_features: list[str] | Unset = UNSET
        if not isinstance(self.supported_features, Unset):
            supported_features = []
            for supported_features_item_data in self.supported_features:
                supported_features_item = supported_features_item_data.value
                supported_features.append(supported_features_item)

        vpn_tunnel_amount = self.vpn_tunnel_amount

        per_gateway_bandwidth_mbps = self.per_gateway_bandwidth_mbps

        per_gateway_maximum_vpn_bandwidth_mbps = self.per_gateway_maximum_vpn_bandwidth_mbps

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if server_number is not UNSET:
            field_dict["server_number"] = server_number
        if per_gateway_max_connections is not UNSET:
            field_dict["per_gateway_max_connections"] = per_gateway_max_connections
        if supported_features is not UNSET:
            field_dict["supported_features"] = supported_features
        if vpn_tunnel_amount is not UNSET:
            field_dict["vpn_tunnel_amount"] = vpn_tunnel_amount
        if per_gateway_bandwidth_mbps is not UNSET:
            field_dict["per_gateway_bandwidth_mbps"] = per_gateway_bandwidth_mbps
        if per_gateway_maximum_vpn_bandwidth_mbps is not UNSET:
            field_dict["per_gateway_maximum_vpn_bandwidth_mbps"] = per_gateway_maximum_vpn_bandwidth_mbps

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        server_number = d.pop("server_number", UNSET)

        per_gateway_max_connections = d.pop("per_gateway_max_connections", UNSET)

        _supported_features = d.pop("supported_features", UNSET)
        supported_features: list[GatewayServiceFeatures] | Unset = UNSET
        if _supported_features is not UNSET:
            supported_features = []
            for supported_features_item_data in _supported_features:
                supported_features_item = GatewayServiceFeatures(supported_features_item_data)

                supported_features.append(supported_features_item)

        vpn_tunnel_amount = d.pop("vpn_tunnel_amount", UNSET)

        per_gateway_bandwidth_mbps = d.pop("per_gateway_bandwidth_mbps", UNSET)

        per_gateway_maximum_vpn_bandwidth_mbps = d.pop("per_gateway_maximum_vpn_bandwidth_mbps", UNSET)

        gateway_plan_details_response = cls(
            name=name,
            server_number=server_number,
            per_gateway_max_connections=per_gateway_max_connections,
            supported_features=supported_features,
            vpn_tunnel_amount=vpn_tunnel_amount,
            per_gateway_bandwidth_mbps=per_gateway_bandwidth_mbps,
            per_gateway_maximum_vpn_bandwidth_mbps=per_gateway_maximum_vpn_bandwidth_mbps,
        )

        gateway_plan_details_response.additional_properties = d
        return gateway_plan_details_response

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
