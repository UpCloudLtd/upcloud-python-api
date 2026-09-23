from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.database_service_clone_redis_plan_backups import DatabaseServiceCloneRedisPlanBackups
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_label_create import DatabaseLabelCreate
    from ..models.database_network_create import DatabaseNetworkCreate
    from ..models.database_service_clone_redis_maintenance import DatabaseServiceCloneRedisMaintenance
    from ..models.database_service_properties_redis import DatabaseServicePropertiesRedis


T = TypeVar("T", bound="DatabaseServiceCloneRedis")


@_attrs_define
class DatabaseServiceCloneRedis:
    """Schema for cloning a Redis service.

    Attributes:
        hostname_prefix (str): Hostname prefix
        plan (str | Unset): Plan
        plan_compute (str | Unset): Plan selection: compute shape combining family, CPU and memory as one token, as
            listed in the plan catalog components. PostgreSQL and MySQL only.
        plan_node_count (int | Unset): Plan selection: number of nodes.
        plan_storage_gib (int | Unset): Plan selection: desired TOTAL storage per node in GiB. Resolution picks the plan
            whose included storage matches, or tops the closest plan up with dynamic additional storage within the allowed
            limits. Mutually exclusive with additional_disk_space_gib.
        plan_backups (DatabaseServiceCloneRedisPlanBackups | Unset): Plan selection: backup tier. PostgreSQL and MySQL
            tiered plans only.
        title (str | Unset): The title of an entity.
        clone_time (datetime.datetime | Unset): Clone time Example: 2024-01-30T15:04:05Z.
        backup_name (str | Unset): Backup name
        set_service_uuid (UUID | Unset): Title
        zone (str | Unset): Zone
        termination_protection (bool | Unset): Termination protection
        maintenance (DatabaseServiceCloneRedisMaintenance | Unset): Maintenance
        networks (list[DatabaseNetworkCreate] | Unset):
        labels (list[DatabaseLabelCreate] | Unset): Labels
        properties (DatabaseServicePropertiesRedis | Unset): redis properties
    """

    hostname_prefix: str
    plan: str | Unset = UNSET
    plan_compute: str | Unset = UNSET
    plan_node_count: int | Unset = UNSET
    plan_storage_gib: int | Unset = UNSET
    plan_backups: DatabaseServiceCloneRedisPlanBackups | Unset = UNSET
    title: str | Unset = UNSET
    clone_time: datetime.datetime | Unset = UNSET
    backup_name: str | Unset = UNSET
    set_service_uuid: UUID | Unset = UNSET
    zone: str | Unset = UNSET
    termination_protection: bool | Unset = UNSET
    maintenance: DatabaseServiceCloneRedisMaintenance | Unset = UNSET
    networks: list[DatabaseNetworkCreate] | Unset = UNSET
    labels: list[DatabaseLabelCreate] | Unset = UNSET
    properties: DatabaseServicePropertiesRedis | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        hostname_prefix = self.hostname_prefix

        plan = self.plan

        plan_compute = self.plan_compute

        plan_node_count = self.plan_node_count

        plan_storage_gib = self.plan_storage_gib

        plan_backups: str | Unset = UNSET
        if not isinstance(self.plan_backups, Unset):
            plan_backups = self.plan_backups.value

        title = self.title

        clone_time: str | Unset = UNSET
        if not isinstance(self.clone_time, Unset):
            clone_time = self.clone_time.isoformat()

        backup_name = self.backup_name

        set_service_uuid: str | Unset = UNSET
        if not isinstance(self.set_service_uuid, Unset):
            set_service_uuid = str(self.set_service_uuid)

        zone = self.zone

        termination_protection = self.termination_protection

        maintenance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.maintenance, Unset):
            maintenance = self.maintenance.to_dict()

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

        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "hostname_prefix": hostname_prefix,
            }
        )
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
        if title is not UNSET:
            field_dict["title"] = title
        if clone_time is not UNSET:
            field_dict["clone_time"] = clone_time
        if backup_name is not UNSET:
            field_dict["backup_name"] = backup_name
        if set_service_uuid is not UNSET:
            field_dict["set_service_uuid"] = set_service_uuid
        if zone is not UNSET:
            field_dict["zone"] = zone
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
        from ..models.database_service_clone_redis_maintenance import (
            DatabaseServiceCloneRedisMaintenance,  # noqa: PLC0415
        )
        from ..models.database_service_properties_redis import DatabaseServicePropertiesRedis  # noqa: PLC0415

        d = dict(src_dict)
        hostname_prefix = d.pop("hostname_prefix")

        plan = d.pop("plan", UNSET)

        plan_compute = d.pop("plan_compute", UNSET)

        plan_node_count = d.pop("plan_node_count", UNSET)

        plan_storage_gib = d.pop("plan_storage_gib", UNSET)

        _plan_backups = d.pop("plan_backups", UNSET)
        plan_backups: DatabaseServiceCloneRedisPlanBackups | Unset
        if isinstance(_plan_backups, Unset):
            plan_backups = UNSET
        else:
            plan_backups = DatabaseServiceCloneRedisPlanBackups(_plan_backups)

        title = d.pop("title", UNSET)

        _clone_time = d.pop("clone_time", UNSET)
        clone_time: datetime.datetime | Unset
        if isinstance(_clone_time, Unset):
            clone_time = UNSET
        else:
            clone_time = datetime.datetime.fromisoformat(_clone_time)

        backup_name = d.pop("backup_name", UNSET)

        _set_service_uuid = d.pop("set_service_uuid", UNSET)
        set_service_uuid: UUID | Unset
        if isinstance(_set_service_uuid, Unset):
            set_service_uuid = UNSET
        else:
            set_service_uuid = UUID(_set_service_uuid)

        zone = d.pop("zone", UNSET)

        termination_protection = d.pop("termination_protection", UNSET)

        _maintenance = d.pop("maintenance", UNSET)
        maintenance: DatabaseServiceCloneRedisMaintenance | Unset
        if isinstance(_maintenance, Unset):
            maintenance = UNSET
        else:
            maintenance = DatabaseServiceCloneRedisMaintenance.from_dict(_maintenance)

        _networks = d.pop("networks", UNSET)
        networks: list[DatabaseNetworkCreate] | Unset = UNSET
        if _networks is not UNSET:
            networks = []
            for networks_item_data in _networks:
                networks_item = DatabaseNetworkCreate.from_dict(networks_item_data)

                networks.append(networks_item)

        _labels = d.pop("labels", UNSET)
        labels: list[DatabaseLabelCreate] | Unset = UNSET
        if _labels is not UNSET:
            labels = []
            for labels_item_data in _labels:
                labels_item = DatabaseLabelCreate.from_dict(labels_item_data)

                labels.append(labels_item)

        _properties = d.pop("properties", UNSET)
        properties: DatabaseServicePropertiesRedis | Unset
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = DatabaseServicePropertiesRedis.from_dict(_properties)

        database_service_clone_redis = cls(
            hostname_prefix=hostname_prefix,
            plan=plan,
            plan_compute=plan_compute,
            plan_node_count=plan_node_count,
            plan_storage_gib=plan_storage_gib,
            plan_backups=plan_backups,
            title=title,
            clone_time=clone_time,
            backup_name=backup_name,
            set_service_uuid=set_service_uuid,
            zone=zone,
            termination_protection=termination_protection,
            maintenance=maintenance,
            networks=networks,
            labels=labels,
            properties=properties,
        )

        return database_service_clone_redis
