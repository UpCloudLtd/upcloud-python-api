from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.gateway_service_configured_status import GatewayServiceConfiguredStatus
from ..models.gateway_service_features import GatewayServiceFeatures
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gateway_address_create_request import GatewayAddressCreateRequest
    from ..models.gateway_connection_create_request import GatewayConnectionCreateRequest
    from ..models.gateway_label_create_request import GatewayLabelCreateRequest
    from ..models.gateway_router_create_request import GatewayRouterCreateRequest


T = TypeVar("T", bound="GatewayServiceCreateRequest")


@_attrs_define
class GatewayServiceCreateRequest:
    """Gateway service

    Attributes:
        name (str): Name of the service
        plan (str): Plan
        zone (str): Zone
        features (list[GatewayServiceFeatures]): Active features
        routers (list[GatewayRouterCreateRequest]): Service routers
        configured_status (GatewayServiceConfiguredStatus): Service configured status
        addresses (list[GatewayAddressCreateRequest] | Unset): Service addresses
        connections (list[GatewayConnectionCreateRequest] | Unset): Service connections
        labels (list[GatewayLabelCreateRequest] | Unset): Labels
        automatic_tunnel_internal_ip_allocation (bool | Unset): Allocate and use tunnel internal IPs automatically
            Default: True.
    """

    name: str
    plan: str
    zone: str
    features: list[GatewayServiceFeatures]
    routers: list[GatewayRouterCreateRequest]
    configured_status: GatewayServiceConfiguredStatus
    addresses: list[GatewayAddressCreateRequest] | Unset = UNSET
    connections: list[GatewayConnectionCreateRequest] | Unset = UNSET
    labels: list[GatewayLabelCreateRequest] | Unset = UNSET
    automatic_tunnel_internal_ip_allocation: bool | Unset = True

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        plan = self.plan

        zone = self.zone

        features = []
        for features_item_data in self.features:
            features_item = features_item_data.value
            features.append(features_item)

        routers = []
        for routers_item_data in self.routers:
            routers_item = routers_item_data.to_dict()
            routers.append(routers_item)

        configured_status = self.configured_status.value

        addresses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.addresses, Unset):
            addresses = []
            for addresses_item_data in self.addresses:
                addresses_item = addresses_item_data.to_dict()
                addresses.append(addresses_item)

        connections: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.connections, Unset):
            connections = []
            for connections_item_data in self.connections:
                connections_item = connections_item_data.to_dict()
                connections.append(connections_item)

        labels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()
                labels.append(labels_item)

        automatic_tunnel_internal_ip_allocation = self.automatic_tunnel_internal_ip_allocation

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "plan": plan,
                "zone": zone,
                "features": features,
                "routers": routers,
                "configured_status": configured_status,
            }
        )
        if addresses is not UNSET:
            field_dict["addresses"] = addresses
        if connections is not UNSET:
            field_dict["connections"] = connections
        if labels is not UNSET:
            field_dict["labels"] = labels
        if automatic_tunnel_internal_ip_allocation is not UNSET:
            field_dict["automatic_tunnel_internal_ip_allocation"] = automatic_tunnel_internal_ip_allocation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gateway_address_create_request import GatewayAddressCreateRequest  # noqa: PLC0415
        from ..models.gateway_connection_create_request import GatewayConnectionCreateRequest  # noqa: PLC0415
        from ..models.gateway_label_create_request import GatewayLabelCreateRequest  # noqa: PLC0415
        from ..models.gateway_router_create_request import GatewayRouterCreateRequest  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        plan = d.pop("plan")

        zone = d.pop("zone")

        features = []
        _features = d.pop("features")
        for features_item_data in _features:
            features_item = GatewayServiceFeatures(features_item_data)

            features.append(features_item)

        routers = []
        _routers = d.pop("routers")
        for routers_item_data in _routers:
            routers_item = GatewayRouterCreateRequest.from_dict(routers_item_data)

            routers.append(routers_item)

        configured_status = GatewayServiceConfiguredStatus(d.pop("configured_status"))

        _addresses = d.pop("addresses", UNSET)
        addresses: list[GatewayAddressCreateRequest] | Unset = UNSET
        if _addresses is not UNSET:
            addresses = []
            for addresses_item_data in _addresses:
                addresses_item = GatewayAddressCreateRequest.from_dict(addresses_item_data)

                addresses.append(addresses_item)

        _connections = d.pop("connections", UNSET)
        connections: list[GatewayConnectionCreateRequest] | Unset = UNSET
        if _connections is not UNSET:
            connections = []
            for connections_item_data in _connections:
                connections_item = GatewayConnectionCreateRequest.from_dict(connections_item_data)

                connections.append(connections_item)

        _labels = d.pop("labels", UNSET)
        labels: list[GatewayLabelCreateRequest] | Unset = UNSET
        if _labels is not UNSET:
            labels = []
            for labels_item_data in _labels:
                labels_item = GatewayLabelCreateRequest.from_dict(labels_item_data)

                labels.append(labels_item)

        automatic_tunnel_internal_ip_allocation = d.pop("automatic_tunnel_internal_ip_allocation", UNSET)

        gateway_service_create_request = cls(
            name=name,
            plan=plan,
            zone=zone,
            features=features,
            routers=routers,
            configured_status=configured_status,
            addresses=addresses,
            connections=connections,
            labels=labels,
            automatic_tunnel_internal_ip_allocation=automatic_tunnel_internal_ip_allocation,
        )

        return gateway_service_create_request
