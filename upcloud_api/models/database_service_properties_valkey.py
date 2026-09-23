from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.database_service_properties_valkey_valkey_acl_channels_default import (
    DatabaseServicePropertiesValkeyValkeyAclChannelsDefault,
)
from ..models.database_service_properties_valkey_valkey_maxmemory_policy import (
    DatabaseServicePropertiesValkeyValkeyMaxmemoryPolicy,
)
from ..models.database_service_properties_valkey_valkey_persistence import (
    DatabaseServicePropertiesValkeyValkeyPersistence,
)
from ..models.database_service_properties_valkey_valkey_version import DatabaseServicePropertiesValkeyValkeyVersion
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_service_properties_valkey_migration_type_0 import (
        DatabaseServicePropertiesValkeyMigrationType0,
    )


T = TypeVar("T", bound="DatabaseServicePropertiesValkey")


@_attrs_define
class DatabaseServicePropertiesValkey:
    """valkey properties

    Attributes:
        automatic_utility_network_ip_filter (bool | Unset): Automatically allow connections from servers in the utility
            network within the same zone
        backup_hour (int | None | Unset):
        backup_minute (int | None | Unset):
        frequent_snapshots (bool | Unset): When enabled, Valkey will create frequent local RDB snapshots. When disabled,
            Valkey will only take RDB snapshots when a backup is created, based on the backup schedule. This setting is
            ignored when `valkey_persistence` is set to `off`.
        ip_filter (list[str] | Unset): Allow incoming connections from CIDR address block, e.g. '10.20.0.0/16'
        migration (DatabaseServicePropertiesValkeyMigrationType0 | None | Unset):
        public_access (bool | Unset): Allow access to the service from the public Internet
        public_access_prometheus (bool | Unset): Allow access to Prometheus metrics from the public Internet
        service_log (bool | None | Unset): Store logs for the service so that they are available in the HTTP API and
            console.
        valkey_acl_channels_default (DatabaseServicePropertiesValkeyValkeyAclChannelsDefault | Unset): Determines
            default pub/sub channels' ACL for new users if ACL is not supplied. When this option is not defined,
            all_channels is assumed to keep backward compatibility. This option doesn't affect Valkey configuration acl-
            pubsub-default.
        valkey_active_expire_effort (int | Unset): Valkey reclaims expired keys both when accessed and in the
            background. The background process scans for expired keys to free memory. Increasing the active-expire-effort
            setting (default 1, max 10) uses more CPU to reclaim expired keys faster, reducing memory usage but potentially
            increasing latency.
        valkey_activedefrag (bool | Unset): Enable active memory defragmentation. When enabled, Valkey relocates objects
            off sparsely-used memory pages to reduce fragmentation and return memory to the operating system.
            Defragmentation runs on the main thread and consumes CPU, so it may increase latency under load.
        valkey_io_threads (int | Unset): Set Valkey IO thread count. Changing this will cause a restart of the Valkey
            service.
        valkey_lfu_decay_time (int | Unset):
        valkey_lfu_log_factor (int | Unset):
        valkey_maxmemory_policy (DatabaseServicePropertiesValkeyValkeyMaxmemoryPolicy | Unset):
        valkey_notify_keyspace_events (str | Unset):
        valkey_number_of_databases (int | Unset): Set number of Valkey databases. Changing this will cause a restart of
            the Valkey service.
        valkey_persistence (DatabaseServicePropertiesValkeyValkeyPersistence | Unset): When persistence is 'rdb', Valkey
            does RDB dumps each 10 minutes if any key is changed. Also RDB dumps are done according to backup schedule for
            backup purposes. When persistence is 'off', no RDB dumps and backups are done, so data can be lost at any moment
            if service is restarted for any reason, or if service is powered off. Also service can't be forked.
        valkey_pubsub_client_output_buffer_limit (int | Unset): Set output buffer limit for pub / sub clients in MB. The
            value is the hard limit, the soft limit is 1/4 of the hard limit. When setting the limit, be mindful of the
            available memory in the selected service plan.
        valkey_ssl (bool | Unset):
        valkey_timeout (int | Unset):
        valkey_version (DatabaseServicePropertiesValkeyValkeyVersion | Unset):
    """

    automatic_utility_network_ip_filter: bool | Unset = UNSET
    backup_hour: int | None | Unset = UNSET
    backup_minute: int | None | Unset = UNSET
    frequent_snapshots: bool | Unset = UNSET
    ip_filter: list[str] | Unset = UNSET
    migration: DatabaseServicePropertiesValkeyMigrationType0 | None | Unset = UNSET
    public_access: bool | Unset = UNSET
    public_access_prometheus: bool | Unset = UNSET
    service_log: bool | None | Unset = UNSET
    valkey_acl_channels_default: DatabaseServicePropertiesValkeyValkeyAclChannelsDefault | Unset = UNSET
    valkey_active_expire_effort: int | Unset = UNSET
    valkey_activedefrag: bool | Unset = UNSET
    valkey_io_threads: int | Unset = UNSET
    valkey_lfu_decay_time: int | Unset = UNSET
    valkey_lfu_log_factor: int | Unset = UNSET
    valkey_maxmemory_policy: DatabaseServicePropertiesValkeyValkeyMaxmemoryPolicy | Unset = UNSET
    valkey_notify_keyspace_events: str | Unset = UNSET
    valkey_number_of_databases: int | Unset = UNSET
    valkey_persistence: DatabaseServicePropertiesValkeyValkeyPersistence | Unset = UNSET
    valkey_pubsub_client_output_buffer_limit: int | Unset = UNSET
    valkey_ssl: bool | Unset = UNSET
    valkey_timeout: int | Unset = UNSET
    valkey_version: DatabaseServicePropertiesValkeyValkeyVersion | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.database_service_properties_valkey_migration_type_0 import (
            DatabaseServicePropertiesValkeyMigrationType0,  # noqa: PLC0415
        )

        automatic_utility_network_ip_filter = self.automatic_utility_network_ip_filter

        backup_hour: int | None | Unset
        if isinstance(self.backup_hour, Unset):
            backup_hour = UNSET
        else:
            backup_hour = self.backup_hour

        backup_minute: int | None | Unset
        if isinstance(self.backup_minute, Unset):
            backup_minute = UNSET
        else:
            backup_minute = self.backup_minute

        frequent_snapshots = self.frequent_snapshots

        ip_filter: list[str] | Unset = UNSET
        if not isinstance(self.ip_filter, Unset):
            ip_filter = self.ip_filter

        migration: dict[str, Any] | None | Unset
        if isinstance(self.migration, Unset):
            migration = UNSET
        elif isinstance(self.migration, DatabaseServicePropertiesValkeyMigrationType0):
            migration = self.migration.to_dict()
        else:
            migration = self.migration

        public_access = self.public_access

        public_access_prometheus = self.public_access_prometheus

        service_log: bool | None | Unset
        if isinstance(self.service_log, Unset):
            service_log = UNSET
        else:
            service_log = self.service_log

        valkey_acl_channels_default: str | Unset = UNSET
        if not isinstance(self.valkey_acl_channels_default, Unset):
            valkey_acl_channels_default = self.valkey_acl_channels_default.value

        valkey_active_expire_effort = self.valkey_active_expire_effort

        valkey_activedefrag = self.valkey_activedefrag

        valkey_io_threads = self.valkey_io_threads

        valkey_lfu_decay_time = self.valkey_lfu_decay_time

        valkey_lfu_log_factor = self.valkey_lfu_log_factor

        valkey_maxmemory_policy: str | Unset = UNSET
        if not isinstance(self.valkey_maxmemory_policy, Unset):
            valkey_maxmemory_policy = self.valkey_maxmemory_policy.value

        valkey_notify_keyspace_events = self.valkey_notify_keyspace_events

        valkey_number_of_databases = self.valkey_number_of_databases

        valkey_persistence: str | Unset = UNSET
        if not isinstance(self.valkey_persistence, Unset):
            valkey_persistence = self.valkey_persistence.value

        valkey_pubsub_client_output_buffer_limit = self.valkey_pubsub_client_output_buffer_limit

        valkey_ssl = self.valkey_ssl

        valkey_timeout = self.valkey_timeout

        valkey_version: str | Unset = UNSET
        if not isinstance(self.valkey_version, Unset):
            valkey_version = self.valkey_version.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if automatic_utility_network_ip_filter is not UNSET:
            field_dict["automatic_utility_network_ip_filter"] = automatic_utility_network_ip_filter
        if backup_hour is not UNSET:
            field_dict["backup_hour"] = backup_hour
        if backup_minute is not UNSET:
            field_dict["backup_minute"] = backup_minute
        if frequent_snapshots is not UNSET:
            field_dict["frequent_snapshots"] = frequent_snapshots
        if ip_filter is not UNSET:
            field_dict["ip_filter"] = ip_filter
        if migration is not UNSET:
            field_dict["migration"] = migration
        if public_access is not UNSET:
            field_dict["public_access"] = public_access
        if public_access_prometheus is not UNSET:
            field_dict["public_access_prometheus"] = public_access_prometheus
        if service_log is not UNSET:
            field_dict["service_log"] = service_log
        if valkey_acl_channels_default is not UNSET:
            field_dict["valkey_acl_channels_default"] = valkey_acl_channels_default
        if valkey_active_expire_effort is not UNSET:
            field_dict["valkey_active_expire_effort"] = valkey_active_expire_effort
        if valkey_activedefrag is not UNSET:
            field_dict["valkey_activedefrag"] = valkey_activedefrag
        if valkey_io_threads is not UNSET:
            field_dict["valkey_io_threads"] = valkey_io_threads
        if valkey_lfu_decay_time is not UNSET:
            field_dict["valkey_lfu_decay_time"] = valkey_lfu_decay_time
        if valkey_lfu_log_factor is not UNSET:
            field_dict["valkey_lfu_log_factor"] = valkey_lfu_log_factor
        if valkey_maxmemory_policy is not UNSET:
            field_dict["valkey_maxmemory_policy"] = valkey_maxmemory_policy
        if valkey_notify_keyspace_events is not UNSET:
            field_dict["valkey_notify_keyspace_events"] = valkey_notify_keyspace_events
        if valkey_number_of_databases is not UNSET:
            field_dict["valkey_number_of_databases"] = valkey_number_of_databases
        if valkey_persistence is not UNSET:
            field_dict["valkey_persistence"] = valkey_persistence
        if valkey_pubsub_client_output_buffer_limit is not UNSET:
            field_dict["valkey_pubsub_client_output_buffer_limit"] = valkey_pubsub_client_output_buffer_limit
        if valkey_ssl is not UNSET:
            field_dict["valkey_ssl"] = valkey_ssl
        if valkey_timeout is not UNSET:
            field_dict["valkey_timeout"] = valkey_timeout
        if valkey_version is not UNSET:
            field_dict["valkey_version"] = valkey_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_service_properties_valkey_migration_type_0 import (
            DatabaseServicePropertiesValkeyMigrationType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        automatic_utility_network_ip_filter = d.pop("automatic_utility_network_ip_filter", UNSET)

        def _parse_backup_hour(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        backup_hour = _parse_backup_hour(d.pop("backup_hour", UNSET))

        def _parse_backup_minute(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        backup_minute = _parse_backup_minute(d.pop("backup_minute", UNSET))

        frequent_snapshots = d.pop("frequent_snapshots", UNSET)

        ip_filter = cast(list[str], d.pop("ip_filter", UNSET))

        def _parse_migration(data: object) -> DatabaseServicePropertiesValkeyMigrationType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                migration_type_0 = DatabaseServicePropertiesValkeyMigrationType0.from_dict(data)

                return migration_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatabaseServicePropertiesValkeyMigrationType0 | None | Unset, data)

        migration = _parse_migration(d.pop("migration", UNSET))

        public_access = d.pop("public_access", UNSET)

        public_access_prometheus = d.pop("public_access_prometheus", UNSET)

        def _parse_service_log(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        service_log = _parse_service_log(d.pop("service_log", UNSET))

        _valkey_acl_channels_default = d.pop("valkey_acl_channels_default", UNSET)
        valkey_acl_channels_default: DatabaseServicePropertiesValkeyValkeyAclChannelsDefault | Unset
        if isinstance(_valkey_acl_channels_default, Unset):
            valkey_acl_channels_default = UNSET
        else:
            valkey_acl_channels_default = DatabaseServicePropertiesValkeyValkeyAclChannelsDefault(
                _valkey_acl_channels_default
            )

        valkey_active_expire_effort = d.pop("valkey_active_expire_effort", UNSET)

        valkey_activedefrag = d.pop("valkey_activedefrag", UNSET)

        valkey_io_threads = d.pop("valkey_io_threads", UNSET)

        valkey_lfu_decay_time = d.pop("valkey_lfu_decay_time", UNSET)

        valkey_lfu_log_factor = d.pop("valkey_lfu_log_factor", UNSET)

        _valkey_maxmemory_policy = d.pop("valkey_maxmemory_policy", UNSET)
        valkey_maxmemory_policy: DatabaseServicePropertiesValkeyValkeyMaxmemoryPolicy | Unset
        if isinstance(_valkey_maxmemory_policy, Unset):
            valkey_maxmemory_policy = UNSET
        else:
            valkey_maxmemory_policy = DatabaseServicePropertiesValkeyValkeyMaxmemoryPolicy(_valkey_maxmemory_policy)

        valkey_notify_keyspace_events = d.pop("valkey_notify_keyspace_events", UNSET)

        valkey_number_of_databases = d.pop("valkey_number_of_databases", UNSET)

        _valkey_persistence = d.pop("valkey_persistence", UNSET)
        valkey_persistence: DatabaseServicePropertiesValkeyValkeyPersistence | Unset
        if isinstance(_valkey_persistence, Unset):
            valkey_persistence = UNSET
        else:
            valkey_persistence = DatabaseServicePropertiesValkeyValkeyPersistence(_valkey_persistence)

        valkey_pubsub_client_output_buffer_limit = d.pop("valkey_pubsub_client_output_buffer_limit", UNSET)

        valkey_ssl = d.pop("valkey_ssl", UNSET)

        valkey_timeout = d.pop("valkey_timeout", UNSET)

        _valkey_version = d.pop("valkey_version", UNSET)
        valkey_version: DatabaseServicePropertiesValkeyValkeyVersion | Unset
        if isinstance(_valkey_version, Unset):
            valkey_version = UNSET
        else:
            valkey_version = DatabaseServicePropertiesValkeyValkeyVersion(_valkey_version)

        database_service_properties_valkey = cls(
            automatic_utility_network_ip_filter=automatic_utility_network_ip_filter,
            backup_hour=backup_hour,
            backup_minute=backup_minute,
            frequent_snapshots=frequent_snapshots,
            ip_filter=ip_filter,
            migration=migration,
            public_access=public_access,
            public_access_prometheus=public_access_prometheus,
            service_log=service_log,
            valkey_acl_channels_default=valkey_acl_channels_default,
            valkey_active_expire_effort=valkey_active_expire_effort,
            valkey_activedefrag=valkey_activedefrag,
            valkey_io_threads=valkey_io_threads,
            valkey_lfu_decay_time=valkey_lfu_decay_time,
            valkey_lfu_log_factor=valkey_lfu_log_factor,
            valkey_maxmemory_policy=valkey_maxmemory_policy,
            valkey_notify_keyspace_events=valkey_notify_keyspace_events,
            valkey_number_of_databases=valkey_number_of_databases,
            valkey_persistence=valkey_persistence,
            valkey_pubsub_client_output_buffer_limit=valkey_pubsub_client_output_buffer_limit,
            valkey_ssl=valkey_ssl,
            valkey_timeout=valkey_timeout,
            valkey_version=valkey_version,
        )

        return database_service_properties_valkey
