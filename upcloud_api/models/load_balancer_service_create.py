from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.load_balancer_maintenance_day_of_week import LoadBalancerMaintenanceDayOfWeek
from ..models.load_balancer_service_configured_status import LoadBalancerServiceConfiguredStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.load_balancer_backend_create import LoadBalancerBackendCreate
    from ..models.load_balancer_frontend_create import LoadBalancerFrontendCreate
    from ..models.load_balancer_ip_address_create import LoadBalancerIpAddressCreate
    from ..models.load_balancer_label_create import LoadBalancerLabelCreate
    from ..models.load_balancer_network_create import LoadBalancerNetworkCreate
    from ..models.load_balancer_resolver_create import LoadBalancerResolverCreate


T = TypeVar("T", bound="LoadBalancerServiceCreate")


@_attrs_define
class LoadBalancerServiceCreate:
    """Load Balancer Service

    Attributes:
        name (str): Name of the service Example: my-loadbalancer.
        zone (str): Zone Example: fi-hel1.
        plan (str): Plan Example: production.
        configured_status (LoadBalancerServiceConfiguredStatus): Service configured status Example: started.
        frontends (list[LoadBalancerFrontendCreate]): Service frontends
        backends (list[LoadBalancerBackendCreate] | Unset): Service backends
        resolvers (list[LoadBalancerResolverCreate] | Unset): Service resolvers
        network_uuid (UUID | Unset): Private Network UUID Example: 01234567-89ab-cdef-0123-456789abcdef.
        networks (list[LoadBalancerNetworkCreate] | Unset): Service networks
        labels (list[LoadBalancerLabelCreate] | Unset): Labels
        maintenance_dow (LoadBalancerMaintenanceDayOfWeek | Unset): Day of week Example: monday.
        maintenance_time (str | Unset): Maintenance time Example: 03:15:00Z.
        ip_addresses (list[LoadBalancerIpAddressCreate] | Unset): List of IP addresses for the network
    """

    name: str
    zone: str
    plan: str
    configured_status: LoadBalancerServiceConfiguredStatus
    frontends: list[LoadBalancerFrontendCreate]
    backends: list[LoadBalancerBackendCreate] | Unset = UNSET
    resolvers: list[LoadBalancerResolverCreate] | Unset = UNSET
    network_uuid: UUID | Unset = UNSET
    networks: list[LoadBalancerNetworkCreate] | Unset = UNSET
    labels: list[LoadBalancerLabelCreate] | Unset = UNSET
    maintenance_dow: LoadBalancerMaintenanceDayOfWeek | Unset = UNSET
    maintenance_time: str | Unset = UNSET
    ip_addresses: list[LoadBalancerIpAddressCreate] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        zone = self.zone

        plan = self.plan

        configured_status = self.configured_status.value

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

        network_uuid: str | Unset = UNSET
        if not isinstance(self.network_uuid, Unset):
            network_uuid = str(self.network_uuid)

        networks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.networks, Unset):
            networks = []
            for networks_item_data in self.networks:
                networks_item = networks_item_data.to_dict()
                networks.append(networks_item)

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

        ip_addresses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ip_addresses, Unset):
            ip_addresses = []
            for ip_addresses_item_data in self.ip_addresses:
                ip_addresses_item = ip_addresses_item_data.to_dict()
                ip_addresses.append(ip_addresses_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "zone": zone,
                "plan": plan,
                "configured_status": configured_status,
                "frontends": frontends,
            }
        )
        if backends is not UNSET:
            field_dict["backends"] = backends
        if resolvers is not UNSET:
            field_dict["resolvers"] = resolvers
        if network_uuid is not UNSET:
            field_dict["network_uuid"] = network_uuid
        if networks is not UNSET:
            field_dict["networks"] = networks
        if labels is not UNSET:
            field_dict["labels"] = labels
        if maintenance_dow is not UNSET:
            field_dict["maintenance_dow"] = maintenance_dow
        if maintenance_time is not UNSET:
            field_dict["maintenance_time"] = maintenance_time
        if ip_addresses is not UNSET:
            field_dict["ip_addresses"] = ip_addresses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.load_balancer_backend_create import LoadBalancerBackendCreate  # noqa: PLC0415
        from ..models.load_balancer_frontend_create import LoadBalancerFrontendCreate  # noqa: PLC0415
        from ..models.load_balancer_ip_address_create import LoadBalancerIpAddressCreate  # noqa: PLC0415
        from ..models.load_balancer_label_create import LoadBalancerLabelCreate  # noqa: PLC0415
        from ..models.load_balancer_network_create import LoadBalancerNetworkCreate  # noqa: PLC0415
        from ..models.load_balancer_resolver_create import LoadBalancerResolverCreate  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        zone = d.pop("zone")

        plan = d.pop("plan")

        configured_status = LoadBalancerServiceConfiguredStatus(d.pop("configured_status"))

        frontends = []
        _frontends = d.pop("frontends")
        for frontends_item_data in _frontends:
            frontends_item = LoadBalancerFrontendCreate.from_dict(frontends_item_data)

            frontends.append(frontends_item)

        _backends = d.pop("backends", UNSET)
        backends: list[LoadBalancerBackendCreate] | Unset = UNSET
        if _backends is not UNSET:
            backends = []
            for backends_item_data in _backends:
                backends_item = LoadBalancerBackendCreate.from_dict(backends_item_data)

                backends.append(backends_item)

        _resolvers = d.pop("resolvers", UNSET)
        resolvers: list[LoadBalancerResolverCreate] | Unset = UNSET
        if _resolvers is not UNSET:
            resolvers = []
            for resolvers_item_data in _resolvers:
                resolvers_item = LoadBalancerResolverCreate.from_dict(resolvers_item_data)

                resolvers.append(resolvers_item)

        _network_uuid = d.pop("network_uuid", UNSET)
        network_uuid: UUID | Unset
        if isinstance(_network_uuid, Unset):
            network_uuid = UNSET
        else:
            network_uuid = UUID(_network_uuid)

        _networks = d.pop("networks", UNSET)
        networks: list[LoadBalancerNetworkCreate] | Unset = UNSET
        if _networks is not UNSET:
            networks = []
            for networks_item_data in _networks:
                networks_item = LoadBalancerNetworkCreate.from_dict(networks_item_data)

                networks.append(networks_item)

        _labels = d.pop("labels", UNSET)
        labels: list[LoadBalancerLabelCreate] | Unset = UNSET
        if _labels is not UNSET:
            labels = []
            for labels_item_data in _labels:
                labels_item = LoadBalancerLabelCreate.from_dict(labels_item_data)

                labels.append(labels_item)

        _maintenance_dow = d.pop("maintenance_dow", UNSET)
        maintenance_dow: LoadBalancerMaintenanceDayOfWeek | Unset
        if isinstance(_maintenance_dow, Unset):
            maintenance_dow = UNSET
        else:
            maintenance_dow = LoadBalancerMaintenanceDayOfWeek(_maintenance_dow)

        maintenance_time = d.pop("maintenance_time", UNSET)

        _ip_addresses = d.pop("ip_addresses", UNSET)
        ip_addresses: list[LoadBalancerIpAddressCreate] | Unset = UNSET
        if _ip_addresses is not UNSET:
            ip_addresses = []
            for ip_addresses_item_data in _ip_addresses:
                ip_addresses_item = LoadBalancerIpAddressCreate.from_dict(ip_addresses_item_data)

                ip_addresses.append(ip_addresses_item)

        load_balancer_service_create = cls(
            name=name,
            zone=zone,
            plan=plan,
            configured_status=configured_status,
            frontends=frontends,
            backends=backends,
            resolvers=resolvers,
            network_uuid=network_uuid,
            networks=networks,
            labels=labels,
            maintenance_dow=maintenance_dow,
            maintenance_time=maintenance_time,
            ip_addresses=ip_addresses,
        )

        return load_balancer_service_create
