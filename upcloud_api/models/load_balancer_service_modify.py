from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.load_balancer_maintenance_day_of_week import LoadBalancerMaintenanceDayOfWeek
from ..models.load_balancer_service_configured_status import LoadBalancerServiceConfiguredStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.load_balancer_backend_create import LoadBalancerBackendCreate
    from ..models.load_balancer_frontend_create import LoadBalancerFrontendCreate
    from ..models.load_balancer_ip_address_create import LoadBalancerIpAddressCreate
    from ..models.load_balancer_label_create import LoadBalancerLabelCreate
    from ..models.load_balancer_resolver_create import LoadBalancerResolverCreate


T = TypeVar("T", bound="LoadBalancerServiceModify")


@_attrs_define
class LoadBalancerServiceModify:
    """Load Balancer Service

    Attributes:
        name (str | Unset): Name of the service Example: updated-loadbalancer.
        plan (str | Unset): Plan Example: production.
        configured_status (LoadBalancerServiceConfiguredStatus | Unset): Service configured status Example: started.
        frontends (list[LoadBalancerFrontendCreate] | None | Unset): Service frontends
        backends (list[LoadBalancerBackendCreate] | None | Unset): Service backends
        resolvers (list[LoadBalancerResolverCreate] | None | Unset): Service resolvers
        labels (list[LoadBalancerLabelCreate] | None | Unset): Labels
        maintenance_dow (LoadBalancerMaintenanceDayOfWeek | Unset): Day of week Example: monday.
        maintenance_time (str | Unset): Maintenance time Example: 03:15:00Z.
        ip_addresses (list[LoadBalancerIpAddressCreate] | Unset): List of IP addresses for the network
    """

    name: str | Unset = UNSET
    plan: str | Unset = UNSET
    configured_status: LoadBalancerServiceConfiguredStatus | Unset = UNSET
    frontends: list[LoadBalancerFrontendCreate] | None | Unset = UNSET
    backends: list[LoadBalancerBackendCreate] | None | Unset = UNSET
    resolvers: list[LoadBalancerResolverCreate] | None | Unset = UNSET
    labels: list[LoadBalancerLabelCreate] | None | Unset = UNSET
    maintenance_dow: LoadBalancerMaintenanceDayOfWeek | Unset = UNSET
    maintenance_time: str | Unset = UNSET
    ip_addresses: list[LoadBalancerIpAddressCreate] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        plan = self.plan

        configured_status: str | Unset = UNSET
        if not isinstance(self.configured_status, Unset):
            configured_status = self.configured_status.value

        frontends: list[dict[str, Any]] | None | Unset
        if isinstance(self.frontends, Unset):
            frontends = UNSET
        elif isinstance(self.frontends, list):
            frontends = []
            for frontends_type_0_item_data in self.frontends:
                frontends_type_0_item = frontends_type_0_item_data.to_dict()
                frontends.append(frontends_type_0_item)

        else:
            frontends = self.frontends

        backends: list[dict[str, Any]] | None | Unset
        if isinstance(self.backends, Unset):
            backends = UNSET
        elif isinstance(self.backends, list):
            backends = []
            for backends_type_0_item_data in self.backends:
                backends_type_0_item = backends_type_0_item_data.to_dict()
                backends.append(backends_type_0_item)

        else:
            backends = self.backends

        resolvers: list[dict[str, Any]] | None | Unset
        if isinstance(self.resolvers, Unset):
            resolvers = UNSET
        elif isinstance(self.resolvers, list):
            resolvers = []
            for resolvers_type_0_item_data in self.resolvers:
                resolvers_type_0_item = resolvers_type_0_item_data.to_dict()
                resolvers.append(resolvers_type_0_item)

        else:
            resolvers = self.resolvers

        labels: list[dict[str, Any]] | None | Unset
        if isinstance(self.labels, Unset):
            labels = UNSET
        elif isinstance(self.labels, list):
            labels = []
            for labels_type_0_item_data in self.labels:
                labels_type_0_item = labels_type_0_item_data.to_dict()
                labels.append(labels_type_0_item)

        else:
            labels = self.labels

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

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if plan is not UNSET:
            field_dict["plan"] = plan
        if configured_status is not UNSET:
            field_dict["configured_status"] = configured_status
        if frontends is not UNSET:
            field_dict["frontends"] = frontends
        if backends is not UNSET:
            field_dict["backends"] = backends
        if resolvers is not UNSET:
            field_dict["resolvers"] = resolvers
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
        from ..models.load_balancer_resolver_create import LoadBalancerResolverCreate  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        plan = d.pop("plan", UNSET)

        _configured_status = d.pop("configured_status", UNSET)
        configured_status: LoadBalancerServiceConfiguredStatus | Unset
        if isinstance(_configured_status, Unset):
            configured_status = UNSET
        else:
            configured_status = LoadBalancerServiceConfiguredStatus(_configured_status)

        def _parse_frontends(data: object) -> list[LoadBalancerFrontendCreate] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                frontends_type_0 = []
                _frontends_type_0 = data
                for frontends_type_0_item_data in _frontends_type_0:
                    frontends_type_0_item = LoadBalancerFrontendCreate.from_dict(frontends_type_0_item_data)

                    frontends_type_0.append(frontends_type_0_item)

                return frontends_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[LoadBalancerFrontendCreate] | None | Unset, data)

        frontends = _parse_frontends(d.pop("frontends", UNSET))

        def _parse_backends(data: object) -> list[LoadBalancerBackendCreate] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                backends_type_0 = []
                _backends_type_0 = data
                for backends_type_0_item_data in _backends_type_0:
                    backends_type_0_item = LoadBalancerBackendCreate.from_dict(backends_type_0_item_data)

                    backends_type_0.append(backends_type_0_item)

                return backends_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[LoadBalancerBackendCreate] | None | Unset, data)

        backends = _parse_backends(d.pop("backends", UNSET))

        def _parse_resolvers(data: object) -> list[LoadBalancerResolverCreate] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                resolvers_type_0 = []
                _resolvers_type_0 = data
                for resolvers_type_0_item_data in _resolvers_type_0:
                    resolvers_type_0_item = LoadBalancerResolverCreate.from_dict(resolvers_type_0_item_data)

                    resolvers_type_0.append(resolvers_type_0_item)

                return resolvers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[LoadBalancerResolverCreate] | None | Unset, data)

        resolvers = _parse_resolvers(d.pop("resolvers", UNSET))

        def _parse_labels(data: object) -> list[LoadBalancerLabelCreate] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                labels_type_0 = []
                _labels_type_0 = data
                for labels_type_0_item_data in _labels_type_0:
                    labels_type_0_item = LoadBalancerLabelCreate.from_dict(labels_type_0_item_data)

                    labels_type_0.append(labels_type_0_item)

                return labels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[LoadBalancerLabelCreate] | None | Unset, data)

        labels = _parse_labels(d.pop("labels", UNSET))

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

        load_balancer_service_modify = cls(
            name=name,
            plan=plan,
            configured_status=configured_status,
            frontends=frontends,
            backends=backends,
            resolvers=resolvers,
            labels=labels,
            maintenance_dow=maintenance_dow,
            maintenance_time=maintenance_time,
            ip_addresses=ip_addresses,
        )

        return load_balancer_service_modify
