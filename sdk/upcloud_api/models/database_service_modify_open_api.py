from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.database_service_modify_open_api_plan_backups import DatabaseServiceModifyOpenAPIPlanBackups
from ..models.database_service_type import DatabaseServiceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_label_create import DatabaseLabelCreate
    from ..models.database_network_create import DatabaseNetworkCreate
    from ..models.database_service_modify_open_api_maintenance import DatabaseServiceModifyOpenAPIMaintenance
    from ..models.database_service_properties_mysql import DatabaseServicePropertiesMysql
    from ..models.database_service_properties_opensearch import DatabaseServicePropertiesOpensearch
    from ..models.database_service_properties_pg import DatabaseServicePropertiesPg
    from ..models.database_service_properties_redis import DatabaseServicePropertiesRedis
    from ..models.database_service_properties_valkey import DatabaseServicePropertiesValkey


T = TypeVar("T", bound="DatabaseServiceModifyOpenAPI")


@_attrs_define
class DatabaseServiceModifyOpenAPI:
    """Schema for modifying a service — OpenAPI version.

    Attributes:
        title (str | Unset): Human-readable title for the service.
        type_ (DatabaseServiceType | Unset): The type of service.
        powered (bool | Unset): Desired power state of the service.
        zone (str | Unset): Zone to migrate the service to.
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
        plan_backups (DatabaseServiceModifyOpenAPIPlanBackups | Unset): Plan selection: backup tier. PostgreSQL and
            MySQL tiered plans only.
        additional_disk_space_gib (int | Unset): Additional disk space in GiB. Legacy plans only: componentised (rdb.*)
            plans set storage as a total via plan_storage_gib or the plan name.
        termination_protection (bool | Unset): When enabled, the service cannot be deleted until termination protection
            is disabled.
        maintenance (DatabaseServiceModifyOpenAPIMaintenance | Unset): Weekly maintenance window.
        networks (list[DatabaseNetworkCreate] | None | Unset): SDN networks attached to the service.
        labels (list[DatabaseLabelCreate] | Unset): Labels used for service filtering.
        properties (DatabaseServicePropertiesMysql | DatabaseServicePropertiesOpensearch | DatabaseServicePropertiesPg |
            DatabaseServicePropertiesRedis | DatabaseServicePropertiesValkey | Unset): Engine-specific configuration
            properties. The allowed keys depend on the service type; provide the property set matching the service's type.
    """

    title: str | Unset = UNSET
    type_: DatabaseServiceType | Unset = UNSET
    powered: bool | Unset = UNSET
    zone: str | Unset = UNSET
    plan: str | Unset = UNSET
    plan_compute: str | Unset = UNSET
    plan_node_count: int | Unset = UNSET
    plan_storage_gib: int | Unset = UNSET
    plan_backups: DatabaseServiceModifyOpenAPIPlanBackups | Unset = UNSET
    additional_disk_space_gib: int | Unset = UNSET
    termination_protection: bool | Unset = UNSET
    maintenance: DatabaseServiceModifyOpenAPIMaintenance | Unset = UNSET
    networks: list[DatabaseNetworkCreate] | None | Unset = UNSET
    labels: list[DatabaseLabelCreate] | Unset = UNSET
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

        title = self.title

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        powered = self.powered

        zone = self.zone

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

        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_
        if powered is not UNSET:
            field_dict["powered"] = powered
        if zone is not UNSET:
            field_dict["zone"] = zone
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
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_label_create import DatabaseLabelCreate  # noqa: PLC0415
        from ..models.database_network_create import DatabaseNetworkCreate  # noqa: PLC0415
        from ..models.database_service_modify_open_api_maintenance import (
            DatabaseServiceModifyOpenAPIMaintenance,  # noqa: PLC0415
        )
        from ..models.database_service_properties_mysql import DatabaseServicePropertiesMysql  # noqa: PLC0415
        from ..models.database_service_properties_opensearch import DatabaseServicePropertiesOpensearch  # noqa: PLC0415
        from ..models.database_service_properties_pg import DatabaseServicePropertiesPg  # noqa: PLC0415
        from ..models.database_service_properties_redis import DatabaseServicePropertiesRedis  # noqa: PLC0415
        from ..models.database_service_properties_valkey import DatabaseServicePropertiesValkey  # noqa: PLC0415

        d = dict(src_dict)
        title = d.pop("title", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: DatabaseServiceType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = DatabaseServiceType(_type_)

        powered = d.pop("powered", UNSET)

        zone = d.pop("zone", UNSET)

        plan = d.pop("plan", UNSET)

        plan_compute = d.pop("plan_compute", UNSET)

        plan_node_count = d.pop("plan_node_count", UNSET)

        plan_storage_gib = d.pop("plan_storage_gib", UNSET)

        _plan_backups = d.pop("plan_backups", UNSET)
        plan_backups: DatabaseServiceModifyOpenAPIPlanBackups | Unset
        if isinstance(_plan_backups, Unset):
            plan_backups = UNSET
        else:
            plan_backups = DatabaseServiceModifyOpenAPIPlanBackups(_plan_backups)

        additional_disk_space_gib = d.pop("additional_disk_space_gib", UNSET)

        termination_protection = d.pop("termination_protection", UNSET)

        _maintenance = d.pop("maintenance", UNSET)
        maintenance: DatabaseServiceModifyOpenAPIMaintenance | Unset
        if isinstance(_maintenance, Unset):
            maintenance = UNSET
        else:
            maintenance = DatabaseServiceModifyOpenAPIMaintenance.from_dict(_maintenance)

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

        database_service_modify_open_api = cls(
            title=title,
            type_=type_,
            powered=powered,
            zone=zone,
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
            properties=properties,
        )

        return database_service_modify_open_api
