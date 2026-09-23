from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.load_balancer_service_maintenance_dow import LoadBalancerServiceMaintenanceDow
from ..models.load_balancer_service_operational_state import LoadBalancerServiceOperationalState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.load_balancer_backend import LoadBalancerBackend
    from ..models.load_balancer_frontend import LoadBalancerFrontend
    from ..models.load_balancer_ip_address import LoadBalancerIpAddress
    from ..models.load_balancer_label_response import LoadBalancerLabelResponse
    from ..models.load_balancer_network import LoadBalancerNetwork
    from ..models.load_balancer_resolver import LoadBalancerResolver


T = TypeVar("T", bound="LoadBalancerService")


@_attrs_define
class LoadBalancerService:
    """Represents a load balancer service instance that groups together frontends, backends, and related agents. It defines
    the service plan, network configuration, and operational state across all nodes.

        Attributes:
            uuid (UUID): Unique identifier of the service. Example: b7a3f6a4-4a8f-4a5c-b7a5-9c9a1e5a6d3e.
            name (str): Human-readable name assigned to the service. Example: loadbalancer-prod-eu.
            zone (str): UpCloud zone where the service is deployed. Example: de-fra1.
            plan (str): Selected load balancer plan defining node size, performance, and pricing tier. Example: medium.
            configured_status (str): Configuration status of the service (e.g., whether all components are correctly
                provisioned). Example: configured.
            created_at (datetime.datetime): Timestamp when the service was created.
            updated_at (datetime.datetime): Timestamp when the service was last updated.
            operational_state (LoadBalancerServiceOperationalState | Unset): Current operational state of the service,
                describing its runtime behavior and availability. Example: running.
            frontends (list[LoadBalancerFrontend] | Unset): List of frontend configurations associated with the service.
            backends (list[LoadBalancerBackend] | Unset): List of backend configurations linked to this service.
            resolvers (list[LoadBalancerResolver] | Unset): DNS resolvers available for this service.
            networks (list[LoadBalancerNetwork] | Unset): Networks attached to this service.
            ip_addresses (list[LoadBalancerIpAddress] | Unset): IP addresses assigned to this service.
            labels (list[LoadBalancerLabelResponse] | Unset): Labels associated with the service for metadata tagging and
                identification.
            maintenance_dow (LoadBalancerServiceMaintenanceDow | Unset): Day of week scheduled for maintenance operations.
                Example: tuesday.
            maintenance_time (str | Unset): Time of day (in UTC) scheduled for maintenance operations.
            network_uuid (str | Unset): Deprecated: old field replaced by the networks array.
            dns_name (str | Unset): Deprecated: legacy DNS field replaced by service-level IP addressing.
    """

    uuid: UUID
    name: str
    zone: str
    plan: str
    configured_status: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    operational_state: LoadBalancerServiceOperationalState | Unset = UNSET
    frontends: list[LoadBalancerFrontend] | Unset = UNSET
    backends: list[LoadBalancerBackend] | Unset = UNSET
    resolvers: list[LoadBalancerResolver] | Unset = UNSET
    networks: list[LoadBalancerNetwork] | Unset = UNSET
    ip_addresses: list[LoadBalancerIpAddress] | Unset = UNSET
    labels: list[LoadBalancerLabelResponse] | Unset = UNSET
    maintenance_dow: LoadBalancerServiceMaintenanceDow | Unset = UNSET
    maintenance_time: str | Unset = UNSET
    network_uuid: str | Unset = UNSET
    dns_name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        name = self.name

        zone = self.zone

        plan = self.plan

        configured_status = self.configured_status

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        operational_state: str | Unset = UNSET
        if not isinstance(self.operational_state, Unset):
            operational_state = self.operational_state.value

        frontends: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.frontends, Unset):
            frontends = []
            for frontends_item_data in self.frontends:
                frontends_item = frontends_item_data.to_dict()
                frontends.append(frontends_item)

        backends: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.backends, Unset):
            backends = []
            for backends_item_data in self.backends:
                backends_item = backends_item_data.to_dict()
                backends.append(backends_item)

        resolvers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.resolvers, Unset):
            resolvers = []
            for resolvers_item_data in self.resolvers:
                resolvers_item = resolvers_item_data.to_dict()
                resolvers.append(resolvers_item)

        networks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.networks, Unset):
            networks = []
            for networks_item_data in self.networks:
                networks_item = networks_item_data.to_dict()
                networks.append(networks_item)

        ip_addresses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ip_addresses, Unset):
            ip_addresses = []
            for ip_addresses_item_data in self.ip_addresses:
                ip_addresses_item = ip_addresses_item_data.to_dict()
                ip_addresses.append(ip_addresses_item)

        labels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()
                labels.append(labels_item)

        maintenance_dow: str | Unset = UNSET
        if not isinstance(self.maintenance_dow, Unset):
            maintenance_dow = self.maintenance_dow.value

        maintenance_time = self.maintenance_time

        network_uuid = self.network_uuid

        dns_name = self.dns_name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "uuid": uuid,
                "name": name,
                "zone": zone,
                "plan": plan,
                "configured_status": configured_status,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if operational_state is not UNSET:
            field_dict["operational_state"] = operational_state
        if frontends is not UNSET:
            field_dict["frontends"] = frontends
        if backends is not UNSET:
            field_dict["backends"] = backends
        if resolvers is not UNSET:
            field_dict["resolvers"] = resolvers
        if networks is not UNSET:
            field_dict["networks"] = networks
        if ip_addresses is not UNSET:
            field_dict["ip_addresses"] = ip_addresses
        if labels is not UNSET:
            field_dict["labels"] = labels
        if maintenance_dow is not UNSET:
            field_dict["maintenance_dow"] = maintenance_dow
        if maintenance_time is not UNSET:
            field_dict["maintenance_time"] = maintenance_time
        if network_uuid is not UNSET:
            field_dict["network_uuid"] = network_uuid
        if dns_name is not UNSET:
            field_dict["dns_name"] = dns_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.load_balancer_backend import LoadBalancerBackend  # noqa: PLC0415
        from ..models.load_balancer_frontend import LoadBalancerFrontend  # noqa: PLC0415
        from ..models.load_balancer_ip_address import LoadBalancerIpAddress  # noqa: PLC0415
        from ..models.load_balancer_label_response import LoadBalancerLabelResponse  # noqa: PLC0415
        from ..models.load_balancer_network import LoadBalancerNetwork  # noqa: PLC0415
        from ..models.load_balancer_resolver import LoadBalancerResolver  # noqa: PLC0415

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        name = d.pop("name")

        zone = d.pop("zone")

        plan = d.pop("plan")

        configured_status = d.pop("configured_status")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        _operational_state = d.pop("operational_state", UNSET)
        operational_state: LoadBalancerServiceOperationalState | Unset
        if isinstance(_operational_state, Unset):
            operational_state = UNSET
        else:
            operational_state = LoadBalancerServiceOperationalState(_operational_state)

        _frontends = d.pop("frontends", UNSET)
        frontends: list[LoadBalancerFrontend] | Unset = UNSET
        if _frontends is not UNSET:
            frontends = []
            for frontends_item_data in _frontends:
                frontends_item = LoadBalancerFrontend.from_dict(frontends_item_data)

                frontends.append(frontends_item)

        _backends = d.pop("backends", UNSET)
        backends: list[LoadBalancerBackend] | Unset = UNSET
        if _backends is not UNSET:
            backends = []
            for backends_item_data in _backends:
                backends_item = LoadBalancerBackend.from_dict(backends_item_data)

                backends.append(backends_item)

        _resolvers = d.pop("resolvers", UNSET)
        resolvers: list[LoadBalancerResolver] | Unset = UNSET
        if _resolvers is not UNSET:
            resolvers = []
            for resolvers_item_data in _resolvers:
                resolvers_item = LoadBalancerResolver.from_dict(resolvers_item_data)

                resolvers.append(resolvers_item)

        _networks = d.pop("networks", UNSET)
        networks: list[LoadBalancerNetwork] | Unset = UNSET
        if _networks is not UNSET:
            networks = []
            for networks_item_data in _networks:
                networks_item = LoadBalancerNetwork.from_dict(networks_item_data)

                networks.append(networks_item)

        _ip_addresses = d.pop("ip_addresses", UNSET)
        ip_addresses: list[LoadBalancerIpAddress] | Unset = UNSET
        if _ip_addresses is not UNSET:
            ip_addresses = []
            for ip_addresses_item_data in _ip_addresses:
                ip_addresses_item = LoadBalancerIpAddress.from_dict(ip_addresses_item_data)

                ip_addresses.append(ip_addresses_item)

        _labels = d.pop("labels", UNSET)
        labels: list[LoadBalancerLabelResponse] | Unset = UNSET
        if _labels is not UNSET:
            labels = []
            for labels_item_data in _labels:
                labels_item = LoadBalancerLabelResponse.from_dict(labels_item_data)

                labels.append(labels_item)

        _maintenance_dow = d.pop("maintenance_dow", UNSET)
        maintenance_dow: LoadBalancerServiceMaintenanceDow | Unset
        if isinstance(_maintenance_dow, Unset):
            maintenance_dow = UNSET
        else:
            maintenance_dow = LoadBalancerServiceMaintenanceDow(_maintenance_dow)

        maintenance_time = d.pop("maintenance_time", UNSET)

        network_uuid = d.pop("network_uuid", UNSET)

        dns_name = d.pop("dns_name", UNSET)

        load_balancer_service = cls(
            uuid=uuid,
            name=name,
            zone=zone,
            plan=plan,
            configured_status=configured_status,
            created_at=created_at,
            updated_at=updated_at,
            operational_state=operational_state,
            frontends=frontends,
            backends=backends,
            resolvers=resolvers,
            networks=networks,
            ip_addresses=ip_addresses,
            labels=labels,
            maintenance_dow=maintenance_dow,
            maintenance_time=maintenance_time,
            network_uuid=network_uuid,
            dns_name=dns_name,
        )

        return load_balancer_service
