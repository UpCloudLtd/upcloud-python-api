from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.database_service_create_open_api_plan_backups import DatabaseServiceCreateOpenAPIPlanBackups
from ..models.database_service_type import DatabaseServiceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_label_create import DatabaseLabelCreate
    from ..models.database_network_create import DatabaseNetworkCreate
    from ..models.database_service_create_open_api_maintenance import DatabaseServiceCreateOpenAPIMaintenance
    from ..models.database_service_integration_create import DatabaseServiceIntegrationCreate
    from ..models.database_service_properties_mysql import DatabaseServicePropertiesMysql
    from ..models.database_service_properties_opensearch import DatabaseServicePropertiesOpensearch
    from ..models.database_service_properties_pg import DatabaseServicePropertiesPg
    from ..models.database_service_properties_redis import DatabaseServicePropertiesRedis
    from ..models.database_service_properties_valkey import DatabaseServicePropertiesValkey


T = TypeVar("T", bound="DatabaseServiceCreateOpenAPI")


@_attrs_define
class DatabaseServiceCreateOpenAPI:
    """Schema for creating a service — OpenAPI version.

    Attributes:
        hostname_prefix (str): Hostname prefix for the service nodes.
        title (str): Human-readable title for the service.
        type_ (DatabaseServiceType): The type of service.
        zone (str): Zone where the service is created.
        set_service_uuid (UUID | Unset): Optional UUID to assign to the created service.
        plan (str | Unset): Deprecated: prefer the plan_* selection fields (plan_compute, plan_node_count,
            plan_storage_gib, plan_backups) for PostgreSQL and MySQL. The plan name remains supported, and required for
            engines without componentised plans. For componentised (rdb.*) plans the storage segment is the desired TOTAL
            storage per node: any total reachable from a catalog plan's included storage in the plan's storage steps (within
            its cap) is a valid plan name, e.g. rdb.standard.2x-2CPU-8GB-120GB-regular selects the 80GB catalog plan with a
            40GB dynamic top-up.
        plan_compute (str | Unset): Plan selection: compute shape combining family, CPU and memory as one token, as
            listed in the plan catalog components. PostgreSQL and MySQL only.
        plan_node_count (int | Unset): Plan selection: number of nodes.
        plan_storage_gib (int | Unset): Plan selection: desired TOTAL storage per node in GiB. Resolution picks the plan
            whose included storage matches, or tops the closest plan up with dynamic additional storage within the allowed
            limits. Mutually exclusive with additional_disk_space_gib.
        plan_backups (DatabaseServiceCreateOpenAPIPlanBackups | Unset): Plan selection: backup tier. PostgreSQL and
            MySQL tiered plans only.
        additional_disk_space_gib (int | Unset): Additional disk space in GiB. Legacy plans only: componentised (rdb.*)
            plans set storage as a total via plan_storage_gib or the plan name.
        termination_protection (bool | Unset): When enabled, the service cannot be deleted until termination protection
            is disabled.
        maintenance (DatabaseServiceCreateOpenAPIMaintenance | Unset): Weekly maintenance window.
        networks (list[DatabaseNetworkCreate] | None | Unset): SDN networks to attach to the service.
        labels (list[DatabaseLabelCreate] | Unset): Labels used for service filtering.
        service_integrations (list[DatabaseServiceIntegrationCreate] | None | Unset): Service integrations to configure
            on creation.
        properties (DatabaseServicePropertiesMysql | DatabaseServicePropertiesOpensearch | DatabaseServicePropertiesPg |
            DatabaseServicePropertiesRedis | DatabaseServicePropertiesValkey | Unset): Engine-specific configuration
            properties. The allowed keys depend on the selected service type; provide the property set matching the chosen
            type.
    """

    hostname_prefix: str
    title: str
    type_: DatabaseServiceType
    zone: str
    set_service_uuid: UUID | Unset = UNSET
    plan: str | Unset = UNSET
    plan_compute: str | Unset = UNSET
    plan_node_count: int | Unset = UNSET
    plan_storage_gib: int | Unset = UNSET
    plan_backups: DatabaseServiceCreateOpenAPIPlanBackups | Unset = UNSET
    additional_disk_space_gib: int | Unset = UNSET
    termination_protection: bool | Unset = UNSET
    maintenance: DatabaseServiceCreateOpenAPIMaintenance | Unset = UNSET
    networks: list[DatabaseNetworkCreate] | None | Unset = UNSET
    labels: list[DatabaseLabelCreate] | Unset = UNSET
    service_integrations: list[DatabaseServiceIntegrationCreate] | None | Unset = UNSET
    properties: (
        DatabaseServicePropertiesMysql
        | DatabaseServicePropertiesOpensearch
        | DatabaseServicePropertiesPg
        | DatabaseServicePropertiesRedis
        | DatabaseServicePropertiesValkey
        | Unset
    ) = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.database_service_properties_mysql import DatabaseServicePropertiesMysql  # noqa: PLC0415
        from ..models.database_service_properties_opensearch import DatabaseServicePropertiesOpensearch  # noqa: PLC0415
        from ..models.database_service_properties_pg import DatabaseServicePropertiesPg  # noqa: PLC0415
        from ..models.database_service_properties_redis import DatabaseServicePropertiesRedis  # noqa: PLC0415

        hostname_prefix = self.hostname_prefix

        title = self.title

        type_ = self.type_.value

        zone = self.zone

        set_service_uuid: str | Unset = UNSET
        if not isinstance(self.set_service_uuid, Unset):
            set_service_uuid = str(self.set_service_uuid)

        plan = self.plan

        plan_compute = self.plan_compute

        plan_node_count = self.plan_node_count

        plan_storage_gib = self.plan_storage_gib

        plan_backups: str | Unset = UNSET
        if not isinstance(self.plan_backups, Unset):
            plan_backups = self.plan_backups.value

        additional_disk_space_gib = self.additional_disk_space_gib

        termination_protection = self.termination_protection

        maintenance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.maintenance, Unset):
            maintenance = self.maintenance.to_dict()

        networks: list[dict[str, Any]] | None | Unset
        if isinstance(self.networks, Unset):
            networks = UNSET
        elif isinstance(self.networks, list):
            networks = []
            for networks_type_0_item_data in self.networks:
                networks_type_0_item = networks_type_0_item_data.to_dict()
                networks.append(networks_type_0_item)

        else:
            networks = self.networks

        labels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()
                labels.append(labels_item)

        service_integrations: list[dict[str, Any]] | None | Unset
        if isinstance(self.service_integrations, Unset):
            service_integrations = UNSET
        elif isinstance(self.service_integrations, list):
            service_integrations = []
            for service_integrations_type_0_item_data in self.service_integrations:
                service_integrations_type_0_item = service_integrations_type_0_item_data.to_dict()
                service_integrations.append(service_integrations_type_0_item)

        else:
            service_integrations = self.service_integrations

        properties: dict[str, Any] | Unset
        if isinstance(self.properties, Unset):
            properties = UNSET
        elif isinstance(self.properties, DatabaseServicePropertiesMysql):
            properties = self.properties.to_dict()
        elif isinstance(self.properties, DatabaseServicePropertiesPg):
            properties = self.properties.to_dict()
        elif isinstance(self.properties, DatabaseServicePropertiesRedis):
            properties = self.properties.to_dict()
        elif isinstance(self.properties, DatabaseServicePropertiesOpensearch):
            properties = self.properties.to_dict()
        else:
            properties = self.properties.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "hostname_prefix": hostname_prefix,
                "title": title,
                "type": type_,
                "zone": zone,
            }
        )
        if set_service_uuid is not UNSET:
            field_dict["set_service_uuid"] = set_service_uuid
        if plan is not UNSET:
            field_dict["plan"] = plan
        if plan_compute is not UNSET:
            field_dict["plan_compute"] = plan_compute
        if plan_node_count is not UNSET:
            field_dict["plan_node_count"] = plan_node_count
        if plan_storage_gib is not UNSET:
            field_dict["plan_storage_gib"] = plan_storage_gib
        if plan_backups is not UNSET:
            field_dict["plan_backups"] = plan_backups
        if additional_disk_space_gib is not UNSET:
            field_dict["additional_disk_space_gib"] = additional_disk_space_gib
        if termination_protection is not UNSET:
            field_dict["termination_protection"] = termination_protection
        if maintenance is not UNSET:
            field_dict["maintenance"] = maintenance
        if networks is not UNSET:
            field_dict["networks"] = networks
        if labels is not UNSET:
            field_dict["labels"] = labels
        if service_integrations is not UNSET:
            field_dict["service_integrations"] = service_integrations
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_label_create import DatabaseLabelCreate  # noqa: PLC0415
        from ..models.database_network_create import DatabaseNetworkCreate  # noqa: PLC0415
        from ..models.database_service_create_open_api_maintenance import (
            DatabaseServiceCreateOpenAPIMaintenance,  # noqa: PLC0415
        )
        from ..models.database_service_integration_create import DatabaseServiceIntegrationCreate  # noqa: PLC0415
        from ..models.database_service_properties_mysql import DatabaseServicePropertiesMysql  # noqa: PLC0415
        from ..models.database_service_properties_opensearch import DatabaseServicePropertiesOpensearch  # noqa: PLC0415
        from ..models.database_service_properties_pg import DatabaseServicePropertiesPg  # noqa: PLC0415
        from ..models.database_service_properties_redis import DatabaseServicePropertiesRedis  # noqa: PLC0415
        from ..models.database_service_properties_valkey import DatabaseServicePropertiesValkey  # noqa: PLC0415

        d = dict(src_dict)
        hostname_prefix = d.pop("hostname_prefix")

        title = d.pop("title")

        type_ = DatabaseServiceType(d.pop("type"))

        zone = d.pop("zone")

        _set_service_uuid = d.pop("set_service_uuid", UNSET)
        set_service_uuid: UUID | Unset
        if isinstance(_set_service_uuid, Unset):
            set_service_uuid = UNSET
        else:
            set_service_uuid = UUID(_set_service_uuid)

        plan = d.pop("plan", UNSET)

        plan_compute = d.pop("plan_compute", UNSET)

        plan_node_count = d.pop("plan_node_count", UNSET)

        plan_storage_gib = d.pop("plan_storage_gib", UNSET)

        _plan_backups = d.pop("plan_backups", UNSET)
        plan_backups: DatabaseServiceCreateOpenAPIPlanBackups | Unset
        if isinstance(_plan_backups, Unset):
            plan_backups = UNSET
        else:
            plan_backups = DatabaseServiceCreateOpenAPIPlanBackups(_plan_backups)

        additional_disk_space_gib = d.pop("additional_disk_space_gib", UNSET)

        termination_protection = d.pop("termination_protection", UNSET)

        _maintenance = d.pop("maintenance", UNSET)
        maintenance: DatabaseServiceCreateOpenAPIMaintenance | Unset
        if isinstance(_maintenance, Unset):
            maintenance = UNSET
        else:
            maintenance = DatabaseServiceCreateOpenAPIMaintenance.from_dict(_maintenance)

        def _parse_networks(data: object) -> list[DatabaseNetworkCreate] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                networks_type_0 = []
                _networks_type_0 = data
                for networks_type_0_item_data in _networks_type_0:
                    networks_type_0_item = DatabaseNetworkCreate.from_dict(networks_type_0_item_data)

                    networks_type_0.append(networks_type_0_item)

                return networks_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DatabaseNetworkCreate] | None | Unset, data)

        networks = _parse_networks(d.pop("networks", UNSET))

        _labels = d.pop("labels", UNSET)
        labels: list[DatabaseLabelCreate] | Unset = UNSET
        if _labels is not UNSET:
            labels = []
            for labels_item_data in _labels:
                labels_item = DatabaseLabelCreate.from_dict(labels_item_data)

                labels.append(labels_item)

        def _parse_service_integrations(data: object) -> list[DatabaseServiceIntegrationCreate] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                service_integrations_type_0 = []
                _service_integrations_type_0 = data
                for service_integrations_type_0_item_data in _service_integrations_type_0:
                    service_integrations_type_0_item = DatabaseServiceIntegrationCreate.from_dict(
                        service_integrations_type_0_item_data
                    )

                    service_integrations_type_0.append(service_integrations_type_0_item)

                return service_integrations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DatabaseServiceIntegrationCreate] | None | Unset, data)

        service_integrations = _parse_service_integrations(d.pop("service_integrations", UNSET))

        def _parse_properties(
            data: object,
        ) -> (
            DatabaseServicePropertiesMysql
            | DatabaseServicePropertiesOpensearch
            | DatabaseServicePropertiesPg
            | DatabaseServicePropertiesRedis
            | DatabaseServicePropertiesValkey
            | Unset
        ):
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_0 = DatabaseServicePropertiesMysql.from_dict(data)

                return properties_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_1 = DatabaseServicePropertiesPg.from_dict(data)

                return properties_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_2 = DatabaseServicePropertiesRedis.from_dict(data)

                return properties_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_3 = DatabaseServicePropertiesOpensearch.from_dict(data)

                return properties_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            properties_type_4 = DatabaseServicePropertiesValkey.from_dict(data)

            return properties_type_4

        properties = _parse_properties(d.pop("properties", UNSET))

        database_service_create_open_api = cls(
            hostname_prefix=hostname_prefix,
            title=title,
            type_=type_,
            zone=zone,
            set_service_uuid=set_service_uuid,
            plan=plan,
            plan_compute=plan_compute,
            plan_node_count=plan_node_count,
            plan_storage_gib=plan_storage_gib,
            plan_backups=plan_backups,
            additional_disk_space_gib=additional_disk_space_gib,
            termination_protection=termination_protection,
            maintenance=maintenance,
            networks=networks,
            labels=labels,
            service_integrations=service_integrations,
            properties=properties,
        )

        return database_service_create_open_api
