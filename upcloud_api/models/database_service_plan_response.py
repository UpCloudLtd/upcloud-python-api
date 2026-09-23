from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_backup_config_open_search_response import DatabaseBackupConfigOpenSearchResponse
    from ..models.database_backup_config_response import DatabaseBackupConfigResponse
    from ..models.database_plan_components_response import DatabasePlanComponentsResponse
    from ..models.database_service_plan_response_zones import DatabaseServicePlanResponseZones


T = TypeVar("T", bound="DatabaseServicePlanResponse")


@_attrs_define
class DatabaseServicePlanResponse:
    """Schema definition for a service plan

    Attributes:
        backup_config (DatabaseBackupConfigResponse | Unset): General backup configuration schema
        backup_config_pg (DatabaseBackupConfigResponse | Unset): General backup configuration schema
        backup_config_mysql (DatabaseBackupConfigResponse | Unset): General backup configuration schema
        backup_config_redis (DatabaseBackupConfigResponse | Unset): General backup configuration schema
        backup_config_valkey (DatabaseBackupConfigResponse | Unset): General backup configuration schema
        backup_config_opensearch (DatabaseBackupConfigOpenSearchResponse | Unset): OpenSearch specific backup
            configuration response
        node_count (int | Unset): Number of nodes in the service plan Example: 10.
        zones (DatabaseServicePlanResponseZones | Unset):
        plan (str | Unset): Name of the service plan Example: 2x2xCPU-4GB-50G.
        core_number (int | Unset): Number of CPU cores per node Example: 2.
        storage_size (int | Unset): Storage size in MiB per node Example: 25600.
        memory_amount (int | Unset): Memory amount in MB per node Example: 4096.
        components (DatabasePlanComponentsResponse | Unset): Structured breakdown of a service plan into compute,
            storage and backups components. Sizes are expressed in GB to match plan naming; the classic MB/MiB fields on the
            plan object are unchanged.
    """

    backup_config: DatabaseBackupConfigResponse | Unset = UNSET
    backup_config_pg: DatabaseBackupConfigResponse | Unset = UNSET
    backup_config_mysql: DatabaseBackupConfigResponse | Unset = UNSET
    backup_config_redis: DatabaseBackupConfigResponse | Unset = UNSET
    backup_config_valkey: DatabaseBackupConfigResponse | Unset = UNSET
    backup_config_opensearch: DatabaseBackupConfigOpenSearchResponse | Unset = UNSET
    node_count: int | Unset = UNSET
    zones: DatabaseServicePlanResponseZones | Unset = UNSET
    plan: str | Unset = UNSET
    core_number: int | Unset = UNSET
    storage_size: int | Unset = UNSET
    memory_amount: int | Unset = UNSET
    components: DatabasePlanComponentsResponse | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backup_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.backup_config, Unset):
            backup_config = self.backup_config.to_dict()

        backup_config_pg: dict[str, Any] | Unset = UNSET
        if not isinstance(self.backup_config_pg, Unset):
            backup_config_pg = self.backup_config_pg.to_dict()

        backup_config_mysql: dict[str, Any] | Unset = UNSET
        if not isinstance(self.backup_config_mysql, Unset):
            backup_config_mysql = self.backup_config_mysql.to_dict()

        backup_config_redis: dict[str, Any] | Unset = UNSET
        if not isinstance(self.backup_config_redis, Unset):
            backup_config_redis = self.backup_config_redis.to_dict()

        backup_config_valkey: dict[str, Any] | Unset = UNSET
        if not isinstance(self.backup_config_valkey, Unset):
            backup_config_valkey = self.backup_config_valkey.to_dict()

        backup_config_opensearch: dict[str, Any] | Unset = UNSET
        if not isinstance(self.backup_config_opensearch, Unset):
            backup_config_opensearch = self.backup_config_opensearch.to_dict()

        node_count = self.node_count

        zones: dict[str, Any] | Unset = UNSET
        if not isinstance(self.zones, Unset):
            zones = self.zones.to_dict()

        plan = self.plan

        core_number = self.core_number

        storage_size = self.storage_size

        memory_amount = self.memory_amount

        components: dict[str, Any] | Unset = UNSET
        if not isinstance(self.components, Unset):
            components = self.components.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if backup_config is not UNSET:
            field_dict["backup_config"] = backup_config
        if backup_config_pg is not UNSET:
            field_dict["backup_config_pg"] = backup_config_pg
        if backup_config_mysql is not UNSET:
            field_dict["backup_config_mysql"] = backup_config_mysql
        if backup_config_redis is not UNSET:
            field_dict["backup_config_redis"] = backup_config_redis
        if backup_config_valkey is not UNSET:
            field_dict["backup_config_valkey"] = backup_config_valkey
        if backup_config_opensearch is not UNSET:
            field_dict["backup_config_opensearch"] = backup_config_opensearch
        if node_count is not UNSET:
            field_dict["node_count"] = node_count
        if zones is not UNSET:
            field_dict["zones"] = zones
        if plan is not UNSET:
            field_dict["plan"] = plan
        if core_number is not UNSET:
            field_dict["core_number"] = core_number
        if storage_size is not UNSET:
            field_dict["storage_size"] = storage_size
        if memory_amount is not UNSET:
            field_dict["memory_amount"] = memory_amount
        if components is not UNSET:
            field_dict["components"] = components

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_backup_config_open_search_response import (
            DatabaseBackupConfigOpenSearchResponse,  # noqa: PLC0415
        )
        from ..models.database_backup_config_response import DatabaseBackupConfigResponse  # noqa: PLC0415
        from ..models.database_plan_components_response import DatabasePlanComponentsResponse  # noqa: PLC0415
        from ..models.database_service_plan_response_zones import DatabaseServicePlanResponseZones  # noqa: PLC0415

        d = dict(src_dict)
        _backup_config = d.pop("backup_config", UNSET)
        backup_config: DatabaseBackupConfigResponse | Unset
        if isinstance(_backup_config, Unset):
            backup_config = UNSET
        else:
            backup_config = DatabaseBackupConfigResponse.from_dict(_backup_config)

        _backup_config_pg = d.pop("backup_config_pg", UNSET)
        backup_config_pg: DatabaseBackupConfigResponse | Unset
        if isinstance(_backup_config_pg, Unset):
            backup_config_pg = UNSET
        else:
            backup_config_pg = DatabaseBackupConfigResponse.from_dict(_backup_config_pg)

        _backup_config_mysql = d.pop("backup_config_mysql", UNSET)
        backup_config_mysql: DatabaseBackupConfigResponse | Unset
        if isinstance(_backup_config_mysql, Unset):
            backup_config_mysql = UNSET
        else:
            backup_config_mysql = DatabaseBackupConfigResponse.from_dict(_backup_config_mysql)

        _backup_config_redis = d.pop("backup_config_redis", UNSET)
        backup_config_redis: DatabaseBackupConfigResponse | Unset
        if isinstance(_backup_config_redis, Unset):
            backup_config_redis = UNSET
        else:
            backup_config_redis = DatabaseBackupConfigResponse.from_dict(_backup_config_redis)

        _backup_config_valkey = d.pop("backup_config_valkey", UNSET)
        backup_config_valkey: DatabaseBackupConfigResponse | Unset
        if isinstance(_backup_config_valkey, Unset):
            backup_config_valkey = UNSET
        else:
            backup_config_valkey = DatabaseBackupConfigResponse.from_dict(_backup_config_valkey)

        _backup_config_opensearch = d.pop("backup_config_opensearch", UNSET)
        backup_config_opensearch: DatabaseBackupConfigOpenSearchResponse | Unset
        if isinstance(_backup_config_opensearch, Unset):
            backup_config_opensearch = UNSET
        else:
            backup_config_opensearch = DatabaseBackupConfigOpenSearchResponse.from_dict(_backup_config_opensearch)

        node_count = d.pop("node_count", UNSET)

        _zones = d.pop("zones", UNSET)
        zones: DatabaseServicePlanResponseZones | Unset
        if isinstance(_zones, Unset):
            zones = UNSET
        else:
            zones = DatabaseServicePlanResponseZones.from_dict(_zones)

        plan = d.pop("plan", UNSET)

        core_number = d.pop("core_number", UNSET)

        storage_size = d.pop("storage_size", UNSET)

        memory_amount = d.pop("memory_amount", UNSET)

        _components = d.pop("components", UNSET)
        components: DatabasePlanComponentsResponse | Unset
        if isinstance(_components, Unset):
            components = UNSET
        else:
            components = DatabasePlanComponentsResponse.from_dict(_components)

        database_service_plan_response = cls(
            backup_config=backup_config,
            backup_config_pg=backup_config_pg,
            backup_config_mysql=backup_config_mysql,
            backup_config_redis=backup_config_redis,
            backup_config_valkey=backup_config_valkey,
            backup_config_opensearch=backup_config_opensearch,
            node_count=node_count,
            zones=zones,
            plan=plan,
            core_number=core_number,
            storage_size=storage_size,
            memory_amount=memory_amount,
            components=components,
        )

        database_service_plan_response.additional_properties = d
        return database_service_plan_response

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
