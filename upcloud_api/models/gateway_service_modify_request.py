from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.gateway_service_configured_status import GatewayServiceConfiguredStatus
from ..models.gateway_service_features import GatewayServiceFeatures
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gateway_connection_modify_request import GatewayConnectionModifyRequest
    from ..models.gateway_label_create_request import GatewayLabelCreateRequest


T = TypeVar("T", bound="GatewayServiceModifyRequest")


@_attrs_define
class GatewayServiceModifyRequest:
    """Request to modify a gateway service

    Attributes:
        name (str | Unset): Name of the service
        features (list[GatewayServiceFeatures] | Unset): Active features
        plan (str | Unset): Plan
        configured_status (GatewayServiceConfiguredStatus | Unset): Service configured status
        connections (list[GatewayConnectionModifyRequest] | Unset): Service connections
        labels (list[GatewayLabelCreateRequest] | Unset): Labels
        automatic_tunnel_internal_ip_allocation (bool | Unset): Allocate and use tunnel internal IPs automatically
    """

    name: str | Unset = UNSET
    features: list[GatewayServiceFeatures] | Unset = UNSET
    plan: str | Unset = UNSET
    configured_status: GatewayServiceConfiguredStatus | Unset = UNSET
    connections: list[GatewayConnectionModifyRequest] | Unset = UNSET
    labels: list[GatewayLabelCreateRequest] | Unset = UNSET
    automatic_tunnel_internal_ip_allocation: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        features: list[str] | Unset = UNSET
        if not isinstance(self.features, Unset):
            features = []
            for features_item_data in self.features:
                features_item = features_item_data.value
                features.append(features_item)

        plan = self.plan

        configured_status: str | Unset = UNSET
        if not isinstance(self.configured_status, Unset):
            configured_status = self.configured_status.value

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

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if features is not UNSET:
            field_dict["features"] = features
        if plan is not UNSET:
            field_dict["plan"] = plan
        if configured_status is not UNSET:
            field_dict["configured_status"] = configured_status
        if connections is not UNSET:
            field_dict["connections"] = connections
        if labels is not UNSET:
            field_dict["labels"] = labels
        if automatic_tunnel_internal_ip_allocation is not UNSET:
            field_dict["automatic_tunnel_internal_ip_allocation"] = automatic_tunnel_internal_ip_allocation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gateway_connection_modify_request import GatewayConnectionModifyRequest  # noqa: PLC0415
        from ..models.gateway_label_create_request import GatewayLabelCreateRequest  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _features = d.pop("features", UNSET)
        features: list[GatewayServiceFeatures] | Unset = UNSET
        if _features is not UNSET:
            features = []
            for features_item_data in _features:
                features_item = GatewayServiceFeatures(features_item_data)

                features.append(features_item)

        plan = d.pop("plan", UNSET)

        _configured_status = d.pop("configured_status", UNSET)
        configured_status: GatewayServiceConfiguredStatus | Unset
        if isinstance(_configured_status, Unset):
            configured_status = UNSET
        else:
            configured_status = GatewayServiceConfiguredStatus(_configured_status)

        _connections = d.pop("connections", UNSET)
        connections: list[GatewayConnectionModifyRequest] | Unset = UNSET
        if _connections is not UNSET:
            connections = []
            for connections_item_data in _connections:
                connections_item = GatewayConnectionModifyRequest.from_dict(connections_item_data)

                connections.append(connections_item)

        _labels = d.pop("labels", UNSET)
        labels: list[GatewayLabelCreateRequest] | Unset = UNSET
        if _labels is not UNSET:
            labels = []
            for labels_item_data in _labels:
                labels_item = GatewayLabelCreateRequest.from_dict(labels_item_data)

                labels.append(labels_item)

        automatic_tunnel_internal_ip_allocation = d.pop("automatic_tunnel_internal_ip_allocation", UNSET)

        gateway_service_modify_request = cls(
            name=name,
            features=features,
            plan=plan,
            configured_status=configured_status,
            connections=connections,
            labels=labels,
            automatic_tunnel_internal_ip_allocation=automatic_tunnel_internal_ip_allocation,
        )

        return gateway_service_modify_request
