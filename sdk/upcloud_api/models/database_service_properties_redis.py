from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.database_service_properties_redis_redis_acl_channels_default import (
    DatabaseServicePropertiesRedisRedisAclChannelsDefault,
)
from ..models.database_service_properties_redis_redis_maxmemory_policy import (
    DatabaseServicePropertiesRedisRedisMaxmemoryPolicy,
)
from ..models.database_service_properties_redis_redis_persistence import DatabaseServicePropertiesRedisRedisPersistence
from ..models.database_service_properties_redis_redis_version import DatabaseServicePropertiesRedisRedisVersion
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_service_properties_redis_migration_type_0 import DatabaseServicePropertiesRedisMigrationType0


T = TypeVar("T", bound="DatabaseServicePropertiesRedis")


@_attrs_define
class DatabaseServicePropertiesRedis:
    """redis properties

    Attributes:
        automatic_utility_network_ip_filter (bool | Unset): Automatically allow connections from servers in the utility
            network within the same zone
        backup_hour (int | None | Unset):
        backup_minute (int | None | Unset):
        ip_filter (list[str] | Unset): Allow incoming connections from CIDR address block, e.g. '10.20.0.0/16'
        migration (DatabaseServicePropertiesRedisMigrationType0 | None | Unset):
        public_access (bool | Unset): Allow access to the service from the public Internet
        public_access_prometheus (bool | Unset): Allow access to Prometheus monitoring from the public Internet
        redis_acl_channels_default (DatabaseServicePropertiesRedisRedisAclChannelsDefault | Unset): Determines default
            pub/sub channels' ACL for new users if ACL is not supplied. When this option is not defined, all_channels is
            assumed to keep backward compatibility. This option doesn't affect Redis configuration acl-pubsub-default.
        redis_io_threads (int | Unset): Set Redis IO thread count. Changing this will cause a restart of the Redis
            service.
        redis_lfu_decay_time (int | Unset):
        redis_lfu_log_factor (int | Unset):
        redis_maxmemory_policy (DatabaseServicePropertiesRedisRedisMaxmemoryPolicy | Unset):
        redis_notify_keyspace_events (str | Unset):
        redis_number_of_databases (int | Unset): Set number of Redis databases. Changing this will cause a restart of
            the Redis service.
        redis_persistence (DatabaseServicePropertiesRedisRedisPersistence | Unset): When persistence is 'rdb', Redis
            does RDB dumps each 10 minutes if any key is changed. Also RDB dumps are done according to the backup schedule
            for backup purposes. When persistence is 'off', no RDB dumps or backups are done, so data can be lost at any
            moment if the service is restarted for any reason, or if the service is powered off. Also, the service can't be
            forked.
        redis_pubsub_client_output_buffer_limit (int | Unset): Set output buffer limit for pub / sub clients in MB. The
            value is the hard limit, the soft limit is 1/4 of the hard limit. When setting the limit, be mindful of the
            available memory in the selected service plan.
        redis_ssl (bool | Unset):
        redis_timeout (int | Unset):
        redis_version (DatabaseServicePropertiesRedisRedisVersion | Unset):
        service_log (bool | None | Unset): Store logs for the service so that they are available in the HTTP API and
            console.
    """

    automatic_utility_network_ip_filter: bool | Unset = UNSET
    backup_hour: int | None | Unset = UNSET
    backup_minute: int | None | Unset = UNSET
    ip_filter: list[str] | Unset = UNSET
    migration: DatabaseServicePropertiesRedisMigrationType0 | None | Unset = UNSET
    public_access: bool | Unset = UNSET
    public_access_prometheus: bool | Unset = UNSET
    redis_acl_channels_default: DatabaseServicePropertiesRedisRedisAclChannelsDefault | Unset = UNSET
    redis_io_threads: int | Unset = UNSET
    redis_lfu_decay_time: int | Unset = UNSET
    redis_lfu_log_factor: int | Unset = UNSET
    redis_maxmemory_policy: DatabaseServicePropertiesRedisRedisMaxmemoryPolicy | Unset = UNSET
    redis_notify_keyspace_events: str | Unset = UNSET
    redis_number_of_databases: int | Unset = UNSET
    redis_persistence: DatabaseServicePropertiesRedisRedisPersistence | Unset = UNSET
    redis_pubsub_client_output_buffer_limit: int | Unset = UNSET
    redis_ssl: bool | Unset = UNSET
    redis_timeout: int | Unset = UNSET
    redis_version: DatabaseServicePropertiesRedisRedisVersion | Unset = UNSET
    service_log: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.database_service_properties_redis_migration_type_0 import (
            DatabaseServicePropertiesRedisMigrationType0,  # noqa: PLC0415
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

        ip_filter: list[str] | Unset = UNSET
        if not isinstance(self.ip_filter, Unset):
            ip_filter = self.ip_filter

        migration: dict[str, Any] | None | Unset
        if isinstance(self.migration, Unset):
            migration = UNSET
        elif isinstance(self.migration, DatabaseServicePropertiesRedisMigrationType0):
            migration = self.migration.to_dict()
        else:
            migration = self.migration

        public_access = self.public_access

        public_access_prometheus = self.public_access_prometheus

        redis_acl_channels_default: str | Unset = UNSET
        if not isinstance(self.redis_acl_channels_default, Unset):
            redis_acl_channels_default = self.redis_acl_channels_default.value

        redis_io_threads = self.redis_io_threads

        redis_lfu_decay_time = self.redis_lfu_decay_time

        redis_lfu_log_factor = self.redis_lfu_log_factor

        redis_maxmemory_policy: str | Unset = UNSET
        if not isinstance(self.redis_maxmemory_policy, Unset):
            redis_maxmemory_policy = self.redis_maxmemory_policy.value

        redis_notify_keyspace_events = self.redis_notify_keyspace_events

        redis_number_of_databases = self.redis_number_of_databases

        redis_persistence: str | Unset = UNSET
        if not isinstance(self.redis_persistence, Unset):
            redis_persistence = self.redis_persistence.value

        redis_pubsub_client_output_buffer_limit = self.redis_pubsub_client_output_buffer_limit

        redis_ssl = self.redis_ssl

        redis_timeout = self.redis_timeout

        redis_version: str | Unset = UNSET
        if not isinstance(self.redis_version, Unset):
            redis_version = self.redis_version.value

        service_log: bool | None | Unset
        if isinstance(self.service_log, Unset):
            service_log = UNSET
        else:
            service_log = self.service_log

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if automatic_utility_network_ip_filter is not UNSET:
            field_dict["automatic_utility_network_ip_filter"] = automatic_utility_network_ip_filter
        if backup_hour is not UNSET:
            field_dict["backup_hour"] = backup_hour
        if backup_minute is not UNSET:
            field_dict["backup_minute"] = backup_minute
        if ip_filter is not UNSET:
            field_dict["ip_filter"] = ip_filter
        if migration is not UNSET:
            field_dict["migration"] = migration
        if public_access is not UNSET:
            field_dict["public_access"] = public_access
        if public_access_prometheus is not UNSET:
            field_dict["public_access_prometheus"] = public_access_prometheus
        if redis_acl_channels_default is not UNSET:
            field_dict["redis_acl_channels_default"] = redis_acl_channels_default
        if redis_io_threads is not UNSET:
            field_dict["redis_io_threads"] = redis_io_threads
        if redis_lfu_decay_time is not UNSET:
            field_dict["redis_lfu_decay_time"] = redis_lfu_decay_time
        if redis_lfu_log_factor is not UNSET:
            field_dict["redis_lfu_log_factor"] = redis_lfu_log_factor
        if redis_maxmemory_policy is not UNSET:
            field_dict["redis_maxmemory_policy"] = redis_maxmemory_policy
        if redis_notify_keyspace_events is not UNSET:
            field_dict["redis_notify_keyspace_events"] = redis_notify_keyspace_events
        if redis_number_of_databases is not UNSET:
            field_dict["redis_number_of_databases"] = redis_number_of_databases
        if redis_persistence is not UNSET:
            field_dict["redis_persistence"] = redis_persistence
        if redis_pubsub_client_output_buffer_limit is not UNSET:
            field_dict["redis_pubsub_client_output_buffer_limit"] = redis_pubsub_client_output_buffer_limit
        if redis_ssl is not UNSET:
            field_dict["redis_ssl"] = redis_ssl
        if redis_timeout is not UNSET:
            field_dict["redis_timeout"] = redis_timeout
        if redis_version is not UNSET:
            field_dict["redis_version"] = redis_version
        if service_log is not UNSET:
            field_dict["service_log"] = service_log

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_service_properties_redis_migration_type_0 import (
            DatabaseServicePropertiesRedisMigrationType0,  # noqa: PLC0415
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

        ip_filter = cast(list[str], d.pop("ip_filter", UNSET))

        def _parse_migration(data: object) -> DatabaseServicePropertiesRedisMigrationType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                migration_type_0 = DatabaseServicePropertiesRedisMigrationType0.from_dict(data)

                return migration_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatabaseServicePropertiesRedisMigrationType0 | None | Unset, data)

        migration = _parse_migration(d.pop("migration", UNSET))

        public_access = d.pop("public_access", UNSET)

        public_access_prometheus = d.pop("public_access_prometheus", UNSET)

        _redis_acl_channels_default = d.pop("redis_acl_channels_default", UNSET)
        redis_acl_channels_default: DatabaseServicePropertiesRedisRedisAclChannelsDefault | Unset
        if isinstance(_redis_acl_channels_default, Unset):
            redis_acl_channels_default = UNSET
        else:
            redis_acl_channels_default = DatabaseServicePropertiesRedisRedisAclChannelsDefault(
                _redis_acl_channels_default
            )

        redis_io_threads = d.pop("redis_io_threads", UNSET)

        redis_lfu_decay_time = d.pop("redis_lfu_decay_time", UNSET)

        redis_lfu_log_factor = d.pop("redis_lfu_log_factor", UNSET)

        _redis_maxmemory_policy = d.pop("redis_maxmemory_policy", UNSET)
        redis_maxmemory_policy: DatabaseServicePropertiesRedisRedisMaxmemoryPolicy | Unset
        if isinstance(_redis_maxmemory_policy, Unset):
            redis_maxmemory_policy = UNSET
        else:
            redis_maxmemory_policy = DatabaseServicePropertiesRedisRedisMaxmemoryPolicy(_redis_maxmemory_policy)

        redis_notify_keyspace_events = d.pop("redis_notify_keyspace_events", UNSET)

        redis_number_of_databases = d.pop("redis_number_of_databases", UNSET)

        _redis_persistence = d.pop("redis_persistence", UNSET)
        redis_persistence: DatabaseServicePropertiesRedisRedisPersistence | Unset
        if isinstance(_redis_persistence, Unset):
            redis_persistence = UNSET
        else:
            redis_persistence = DatabaseServicePropertiesRedisRedisPersistence(_redis_persistence)

        redis_pubsub_client_output_buffer_limit = d.pop("redis_pubsub_client_output_buffer_limit", UNSET)

        redis_ssl = d.pop("redis_ssl", UNSET)

        redis_timeout = d.pop("redis_timeout", UNSET)

        _redis_version = d.pop("redis_version", UNSET)
        redis_version: DatabaseServicePropertiesRedisRedisVersion | Unset
        if isinstance(_redis_version, Unset):
            redis_version = UNSET
        else:
            redis_version = DatabaseServicePropertiesRedisRedisVersion(_redis_version)

        def _parse_service_log(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        service_log = _parse_service_log(d.pop("service_log", UNSET))

        database_service_properties_redis = cls(
            automatic_utility_network_ip_filter=automatic_utility_network_ip_filter,
            backup_hour=backup_hour,
            backup_minute=backup_minute,
            ip_filter=ip_filter,
            migration=migration,
            public_access=public_access,
            public_access_prometheus=public_access_prometheus,
            redis_acl_channels_default=redis_acl_channels_default,
            redis_io_threads=redis_io_threads,
            redis_lfu_decay_time=redis_lfu_decay_time,
            redis_lfu_log_factor=redis_lfu_log_factor,
            redis_maxmemory_policy=redis_maxmemory_policy,
            redis_notify_keyspace_events=redis_notify_keyspace_events,
            redis_number_of_databases=redis_number_of_databases,
            redis_persistence=redis_persistence,
            redis_pubsub_client_output_buffer_limit=redis_pubsub_client_output_buffer_limit,
            redis_ssl=redis_ssl,
            redis_timeout=redis_timeout,
            redis_version=redis_version,
            service_log=service_log,
        )

        return database_service_properties_redis
