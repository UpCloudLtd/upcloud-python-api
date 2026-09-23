from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gateway_service_configured_status import GatewayServiceConfiguredStatus
from ..models.gateway_service_features import GatewayServiceFeatures
from ..models.gateway_service_operational_state import GatewayServiceOperationalState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gateway_address_details_response import GatewayAddressDetailsResponse
    from ..models.gateway_connection_details_response import GatewayConnectionDetailsResponse
    from ..models.gateway_label_details_response import GatewayLabelDetailsResponse
    from ..models.gateway_router_details_response import GatewayRouterDetailsResponse


T = TypeVar("T", bound="GatewayServiceDetailsResponse")


@_attrs_define
class GatewayServiceDetailsResponse:
    """Gateway service

    Attributes:
        uuid (UUID | Unset): The unique identifier for the resource.
        name (str | Unset): Name of the service
        zone (str | Unset): Zone of the service
        plan (str | Unset): Plan
        features (list[GatewayServiceFeatures] | Unset): Active features
        routers (GatewayRouterDetailsResponse | Unset): Response schema for gateway router details.
        addresses (list[GatewayAddressDetailsResponse] | Unset):
        connections (list[GatewayConnectionDetailsResponse] | Unset):
        configured_status (GatewayServiceConfiguredStatus | Unset): Service configured status
        operational_state (GatewayServiceOperationalState | Unset): Service operational state
        automatic_tunnel_internal_ip_allocation (bool | Unset): Allocate and use tunnel internal IPs automatically
        labels (list[GatewayLabelDetailsResponse] | Unset): Labels
        created_at (datetime.datetime | Unset): Timestamp of when the service was created.
        updated_at (datetime.datetime | Unset): Timestamp of when the service was last updated.
    """

    uuid: UUID | Unset = UNSET
    name: str | Unset = UNSET
    zone: str | Unset = UNSET
    plan: str | Unset = UNSET
    features: list[GatewayServiceFeatures] | Unset = UNSET
    routers: GatewayRouterDetailsResponse | Unset = UNSET
    addresses: list[GatewayAddressDetailsResponse] | Unset = UNSET
    connections: list[GatewayConnectionDetailsResponse] | Unset = UNSET
    configured_status: GatewayServiceConfiguredStatus | Unset = UNSET
    operational_state: GatewayServiceOperationalState | Unset = UNSET
    automatic_tunnel_internal_ip_allocation: bool | Unset = UNSET
    labels: list[GatewayLabelDetailsResponse] | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid: str | Unset = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        name = self.name

        zone = self.zone

        plan = self.plan

        features: list[str] | Unset = UNSET
        if not isinstance(self.features, Unset):
            features = []
            for features_item_data in self.features:
                features_item = features_item_data.value
                features.append(features_item)

        routers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.routers, Unset):
            routers = self.routers.to_dict()

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

        configured_status: str | Unset = UNSET
        if not isinstance(self.configured_status, Unset):
            configured_status = self.configured_status.value

        operational_state: str | Unset = UNSET
        if not isinstance(self.operational_state, Unset):
            operational_state = self.operational_state.value

        automatic_tunnel_internal_ip_allocation = self.automatic_tunnel_internal_ip_allocation

        labels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()
                labels.append(labels_item)

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if name is not UNSET:
            field_dict["name"] = name
        if zone is not UNSET:
            field_dict["zone"] = zone
        if plan is not UNSET:
            field_dict["plan"] = plan
        if features is not UNSET:
            field_dict["features"] = features
        if routers is not UNSET:
            field_dict["routers"] = routers
        if addresses is not UNSET:
            field_dict["addresses"] = addresses
        if connections is not UNSET:
            field_dict["connections"] = connections
        if configured_status is not UNSET:
            field_dict["configured_status"] = configured_status
        if operational_state is not UNSET:
            field_dict["operational_state"] = operational_state
        if automatic_tunnel_internal_ip_allocation is not UNSET:
            field_dict["automatic_tunnel_internal_ip_allocation"] = automatic_tunnel_internal_ip_allocation
        if labels is not UNSET:
            field_dict["labels"] = labels
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gateway_address_details_response import GatewayAddressDetailsResponse  # noqa: PLC0415
        from ..models.gateway_connection_details_response import GatewayConnectionDetailsResponse  # noqa: PLC0415
        from ..models.gateway_label_details_response import GatewayLabelDetailsResponse  # noqa: PLC0415
        from ..models.gateway_router_details_response import GatewayRouterDetailsResponse  # noqa: PLC0415

        d = dict(src_dict)
        _uuid = d.pop("uuid", UNSET)
        uuid: UUID | Unset
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = UUID(_uuid)

        name = d.pop("name", UNSET)

        zone = d.pop("zone", UNSET)

        plan = d.pop("plan", UNSET)

        _features = d.pop("features", UNSET)
        features: list[GatewayServiceFeatures] | Unset = UNSET
        if _features is not UNSET:
            features = []
            for features_item_data in _features:
                features_item = GatewayServiceFeatures(features_item_data)

                features.append(features_item)

        _routers = d.pop("routers", UNSET)
        routers: GatewayRouterDetailsResponse | Unset
        if isinstance(_routers, Unset):
            routers = UNSET
        else:
            routers = GatewayRouterDetailsResponse.from_dict(_routers)

        _addresses = d.pop("addresses", UNSET)
        addresses: list[GatewayAddressDetailsResponse] | Unset = UNSET
        if _addresses is not UNSET:
            addresses = []
            for addresses_item_data in _addresses:
                addresses_item = GatewayAddressDetailsResponse.from_dict(addresses_item_data)

                addresses.append(addresses_item)

        _connections = d.pop("connections", UNSET)
        connections: list[GatewayConnectionDetailsResponse] | Unset = UNSET
        if _connections is not UNSET:
            connections = []
            for connections_item_data in _connections:
                connections_item = GatewayConnectionDetailsResponse.from_dict(connections_item_data)

                connections.append(connections_item)

        _configured_status = d.pop("configured_status", UNSET)
        configured_status: GatewayServiceConfiguredStatus | Unset
        if isinstance(_configured_status, Unset):
            configured_status = UNSET
        else:
            configured_status = GatewayServiceConfiguredStatus(_configured_status)

        _operational_state = d.pop("operational_state", UNSET)
        operational_state: GatewayServiceOperationalState | Unset
        if isinstance(_operational_state, Unset):
            operational_state = UNSET
        else:
            operational_state = GatewayServiceOperationalState(_operational_state)

        automatic_tunnel_internal_ip_allocation = d.pop("automatic_tunnel_internal_ip_allocation", UNSET)

        _labels = d.pop("labels", UNSET)
        labels: list[GatewayLabelDetailsResponse] | Unset = UNSET
        if _labels is not UNSET:
            labels = []
            for labels_item_data in _labels:
                labels_item = GatewayLabelDetailsResponse.from_dict(labels_item_data)

                labels.append(labels_item)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)

        gateway_service_details_response = cls(
            uuid=uuid,
            name=name,
            zone=zone,
            plan=plan,
            features=features,
            routers=routers,
            addresses=addresses,
            connections=connections,
            configured_status=configured_status,
            operational_state=operational_state,
            automatic_tunnel_internal_ip_allocation=automatic_tunnel_internal_ip_allocation,
            labels=labels,
            created_at=created_at,
            updated_at=updated_at,
        )

        gateway_service_details_response.additional_properties = d
        return gateway_service_details_response

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
