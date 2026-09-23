from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.database_service_properties_pg_backup_interval_hours_type_1 import (
    DatabaseServicePropertiesPgBackupIntervalHoursType1,
)
from ..models.database_service_properties_pg_backup_interval_hours_type_2_type_1 import (
    DatabaseServicePropertiesPgBackupIntervalHoursType2Type1,
)
from ..models.database_service_properties_pg_backup_interval_hours_type_3_type_1 import (
    DatabaseServicePropertiesPgBackupIntervalHoursType3Type1,
)
from ..models.database_service_properties_pg_default_toast_compression import (
    DatabaseServicePropertiesPgDefaultToastCompression,
)
from ..models.database_service_properties_pg_io_method import DatabaseServicePropertiesPgIoMethod
from ..models.database_service_properties_pg_log_error_verbosity import DatabaseServicePropertiesPgLogErrorVerbosity
from ..models.database_service_properties_pg_log_line_prefix import DatabaseServicePropertiesPgLogLinePrefix
from ..models.database_service_properties_pg_password_encryption import DatabaseServicePropertiesPgPasswordEncryption
from ..models.database_service_properties_pg_pg_stat_statements_track import (
    DatabaseServicePropertiesPgPgStatStatementsTrack,
)
from ..models.database_service_properties_pg_synchronous_commit import DatabaseServicePropertiesPgSynchronousCommit
from ..models.database_service_properties_pg_synchronous_replication import (
    DatabaseServicePropertiesPgSynchronousReplication,
)
from ..models.database_service_properties_pg_track_commit_timestamp import (
    DatabaseServicePropertiesPgTrackCommitTimestamp,
)
from ..models.database_service_properties_pg_track_functions import DatabaseServicePropertiesPgTrackFunctions
from ..models.database_service_properties_pg_track_io_timing import DatabaseServicePropertiesPgTrackIoTiming
from ..models.database_service_properties_pg_variant import DatabaseServicePropertiesPgVariant
from ..models.database_service_properties_pg_version import DatabaseServicePropertiesPgVersion
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_service_properties_pg_migration_type_0 import DatabaseServicePropertiesPgMigrationType0
    from ..models.database_service_properties_pg_pgaudit import DatabaseServicePropertiesPgPgaudit
    from ..models.database_service_properties_pg_pgbouncer import DatabaseServicePropertiesPgPgbouncer
    from ..models.database_service_properties_pg_pglookout import DatabaseServicePropertiesPgPglookout
    from ..models.database_service_properties_pg_timescaledb import DatabaseServicePropertiesPgTimescaledb


T = TypeVar("T", bound="DatabaseServicePropertiesPg")


@_attrs_define
class DatabaseServicePropertiesPg:
    """pg properties

    Attributes:
        admin_password (None | str | Unset):
        admin_username (None | str | Unset):
        automatic_utility_network_ip_filter (bool | Unset): Automatically allow connections from servers in the utility
            network within the same zone
        autovacuum_analyze_scale_factor (float | Unset): Specifies a fraction of the table size to add to
            autovacuum_analyze_threshold when deciding whether to trigger an ANALYZE (e.g. `0.2` for 20% of the table size).
            The default is `0.2`.
        autovacuum_analyze_threshold (int | Unset): Specifies the minimum number of inserted, updated or deleted tuples
            needed to trigger an ANALYZE in any one table. The default is `50`.
        autovacuum_freeze_max_age (int | Unset): Specifies the maximum age (in transactions) that a table's
            pg_class.relfrozenxid field can attain before a VACUUM operation is forced to prevent transaction ID wraparound
            within the table. The system launches autovacuum processes to prevent wraparound even when autovacuum is
            otherwise disabled. Changing this parameter causes a service restart.
        autovacuum_max_workers (int | Unset): Specifies the maximum number of autovacuum processes (other than the
            autovacuum launcher) that may be running at any one time. The default is `3`. Changing this parameter causes a
            service restart.
        autovacuum_naptime (int | Unset): Specifies the minimum delay between autovacuum runs on any given database. The
            delay is measured in seconds. The default is `60`.
        autovacuum_vacuum_cost_delay (int | Unset): Specifies the cost delay value that will be used in automatic VACUUM
            operations. If `-1` is specified, the regular vacuum_cost_delay value will be used. The default is `2` (upstream
            default).
        autovacuum_vacuum_cost_limit (int | Unset): Specifies the cost limit value that will be used in automatic VACUUM
            operations. If `-1` is specified, the regular vacuum_cost_limit value will be used. The default is `-1`
            (upstream default).
        autovacuum_vacuum_scale_factor (float | Unset): Specifies a fraction of the table size to add to
            autovacuum_vacuum_threshold when deciding whether to trigger a VACUUM (e.g. `0.2` for 20% of the table size).
            The default is `0.2`.
        autovacuum_vacuum_threshold (int | Unset): Specifies the minimum number of updated or deleted tuples needed to
            trigger a VACUUM in any one table. The default is `50`.
        backup_hour (int | None | Unset):
        backup_interval_hours (DatabaseServicePropertiesPgBackupIntervalHoursType1 |
            DatabaseServicePropertiesPgBackupIntervalHoursType2Type1 |
            DatabaseServicePropertiesPgBackupIntervalHoursType3Type1 | None | Unset): Interval in hours between automatic
            backups. Minimum value is 3 hours. Must be a divisor of 24 (3, 4, 6, 8, 12, 24).  (Applicable to ACU plans only)
        backup_minute (int | None | Unset):
        backup_retention_days (int | None | Unset): Number of days to retain automatic backups. Backups older than this
            value will be automatically deleted. (Applicable to ACU plans only)
        bgwriter_delay (int | Unset): Specifies the delay between activity rounds for the background writer in
            milliseconds. The default is `200`.
        bgwriter_flush_after (int | Unset): Whenever more than bgwriter_flush_after bytes have been written by the
            background writer, attempt to force the OS to issue these writes to the underlying storage. Specified in
            kilobytes. Setting of 0 disables forced writeback. The default is `512`.
        bgwriter_lru_maxpages (int | Unset): In each round, no more than this many buffers will be written by the
            background writer. Setting this to zero disables background writing. The default is `100`.
        bgwriter_lru_multiplier (float | Unset): The average recent need for new buffers is multiplied by
            bgwriter_lru_multiplier to arrive at an estimate of the number that will be needed during the next round, (up to
            bgwriter_lru_maxpages). 1.0 represents a “just in time” policy of writing exactly the number of buffers
            predicted to be needed. Larger values provide some cushion against spikes in demand, while smaller values
            intentionally leave writes to be done by server processes. The default is `2.0`.
        deadlock_timeout (int | Unset): This is the amount of time, in milliseconds, to wait on a lock before checking
            to see if there is a deadlock condition. The default is `1000` (upstream default).
        default_toast_compression (DatabaseServicePropertiesPgDefaultToastCompression | Unset): Specifies the default
            TOAST compression method for values of compressible columns. The default is `lz4`. Only available for PostgreSQL
            14+.
        enable_ha_replica_dns (bool | Unset): Creates a dedicated read-only DNS that automatically falls back to the
            primary if standby nodes are unavailable. It switches back when a standby recovers.
        idle_in_transaction_session_timeout (int | Unset): Time out sessions with open transactions after this number of
            milliseconds
        io_combine_limit (int | Unset): EXPERIMENTAL: Controls the largest I/O size in operations that combine I/O in
            8kB units. Version 17 and up only.
        io_max_combine_limit (int | Unset): EXPERIMENTAL: Controls the largest I/O size in operations that combine I/O
            in 8kB units, and silently limits the user-settable parameter io_combine_limit. Version 18 and up only. Changing
            this parameter causes a service restart.
        io_max_concurrency (int | Unset): EXPERIMENTAL: Controls the maximum number of I/O operations that one process
            can execute simultaneously. Version 18 and up only. Changing this parameter causes a service restart.
        io_method (DatabaseServicePropertiesPgIoMethod | Unset): EXPERIMENTAL: Controls the maximum number of I/O
            operations that one process can execute simultaneously. Version 18 and up only. Changing this parameter causes a
            service restart.
        io_workers (int | Unset): EXPERIMENTAL: Number of IO worker processes, for io_method=worker. Version 18 and up
            only.
        ip_filter (list[str] | Unset): Allow incoming connections from CIDR address block, e.g. '10.20.0.0/16'
        jit (bool | Unset): Controls system-wide use of Just-in-Time Compilation (JIT).
        log_autovacuum_min_duration (int | Unset): Causes each action executed by autovacuum to be logged if it ran for
            at least the specified number of milliseconds. Setting this to zero logs all autovacuum actions. Minus-one
            disables logging autovacuum actions. The default is `1000`.
        log_error_verbosity (DatabaseServicePropertiesPgLogErrorVerbosity | Unset): Controls the amount of detail
            written in the server log for each message that is logged.
        log_line_prefix (DatabaseServicePropertiesPgLogLinePrefix | Unset): Choose from one of the available log
            formats.
        log_min_duration_statement (int | Unset): Log statements that take more than this number of milliseconds to run,
            -1 disables
        log_temp_files (int | Unset): Log statements for each temporary file created larger than this number of
            kilobytes, -1 disables
        max_connections (int | Unset): Sets the PostgreSQL maximum number of concurrent connections to the database
            server. For services with a read replica, first increase the read replica's value. After the change is applied
            to the replica, you can increase the primary service's value. Changing this parameter causes a service restart.
        max_files_per_process (int | Unset): PostgreSQL maximum number of files that can be open per process. The
            default is `1000` (upstream default). Changing this parameter causes a service restart.
        max_locks_per_transaction (int | Unset): PostgreSQL maximum locks per transaction. Changing this parameter
            causes a service restart.
        max_logical_replication_workers (int | Unset): PostgreSQL maximum logical replication workers (taken from the
            pool defined by max_worker_processes). The default is `4` (upstream default). Changing this parameter causes a
            service restart.
        max_parallel_workers (int | Unset): Sets the maximum number of workers that the system can support for parallel
            queries. The default is `8` (upstream default).
        max_parallel_workers_per_gather (int | Unset): Sets the maximum number of workers that can be started by a
            single Gather or Gather Merge node. The default is `2` (upstream default).
        max_pred_locks_per_transaction (int | Unset): PostgreSQL maximum predicate locks per transaction. The default is
            `64` (upstream default). Changing this parameter causes a service restart.
        max_prepared_transactions (int | Unset): PostgreSQL maximum prepared transactions. The default is `0`. Changing
            this parameter causes a service restart.
        max_replication_slots (int | Unset): PostgreSQL maximum replication slots. The default is `20`. Changing this
            parameter causes a service restart.
        max_slot_wal_keep_size (int | Unset): PostgreSQL maximum WAL size (MB) reserved for replication slots. If `-1`
            is specified, replication slots may retain an unlimited amount of WAL files. The default is `-1` (upstream
            default). wal_keep_size minimum WAL size setting takes precedence over this.
        max_stack_depth (int | Unset): Maximum depth of the stack in bytes. The default is `2097152` (upstream default).
        max_standby_archive_delay (int | Unset): Max standby archive delay in milliseconds. The default is `30000`
            (upstream default).
        max_standby_streaming_delay (int | Unset): Max standby streaming delay in milliseconds. The default is `30000`
            (upstream default).
        max_sync_workers_per_subscription (int | Unset): Maximum number of synchronization workers per subscription. The
            default is `2`.
        max_wal_senders (int | Unset): PostgreSQL maximum WAL senders. The default is `20`. Changing this parameter
            causes a service restart.
        max_worker_processes (int | Unset): Sets the maximum number of background processes that the system can support.
            The default is `8`. Changing this parameter causes a service restart.
        migration (DatabaseServicePropertiesPgMigrationType0 | None | Unset):
        node_count (int | Unset):
        password_encryption (DatabaseServicePropertiesPgPasswordEncryption | Unset): Chooses the algorithm for
            encrypting passwords.
        pg_partman_bgw_interval (int | Unset): Sets the time interval in seconds to run pg_partman's scheduled tasks.
            The default is `3600`.
        pg_partman_bgw_role (str | Unset): Controls which role to use for pg_partman's scheduled background tasks.
        pg_stat_monitor_enable (bool | Unset): Enable the pg_stat_monitor extension. Changing this parameter causes a
            service restart. When this extension is enabled, pg_stat_statements results for utility commands are unreliable
        pg_stat_monitor_pgsm_enable_query_plan (bool | Unset): Enables or disables query plan monitoring. Only available
            for PostgreSQL 13+.
        pg_stat_monitor_pgsm_max_buckets (int | Unset): Sets the maximum number of buckets. Changing this parameter
            causes a service restart. Only available for PostgreSQL 13+.
        pg_stat_statements_track (DatabaseServicePropertiesPgPgStatStatementsTrack | Unset): Controls which statements
            are counted. Specify top to track top-level statements (those issued directly by clients), all to also track
            nested statements (such as statements invoked within functions), or none to disable statement statistics
            collection. The default is `top`.
        pgaudit (DatabaseServicePropertiesPgPgaudit | Unset): System-wide settings for the pgaudit extension.
        pgbouncer (DatabaseServicePropertiesPgPgbouncer | Unset): System-wide settings for pgbouncer.
        pglookout (DatabaseServicePropertiesPgPglookout | Unset): System-wide settings for pglookout.
        public_access (bool | Unset): Allow access to the service from the public Internet
        public_access_prometheus (bool | Unset): Allow access to Prometheus metrics from the public Internet
        service_log (bool | None | Unset): Store logs for the service so that they are available in the HTTP API and
            console.
        shared_buffers_percentage (float | Unset): Percentage of total RAM that the database server uses for shared
            memory buffers. Valid range is 20-60 (float), which corresponds to 20% - 60%. This setting adjusts the
            shared_buffers configuration value. Changing this parameter causes a service restart.
        synchronous_commit (DatabaseServicePropertiesPgSynchronousCommit | Unset): Sets the current transaction's
            synchronization level. The default is `off`. This setting takes precedence over `synchronous_replication`.
        synchronous_replication (DatabaseServicePropertiesPgSynchronousReplication | Unset): This setting is deprecated.
            Use synchronous_commit instead. Any change to this setting will automatically update synchronous_commit. Setting
            the value to quorum changes synchronous_commit to remote_write, while setting it to off changes
            synchronous_commit to off.
        temp_file_limit (int | Unset): PostgreSQL temporary file limit in KiB, -1 for unlimited
        timescaledb (DatabaseServicePropertiesPgTimescaledb | Unset): System-wide settings for the timescaledb extension
        timezone (str | Unset): PostgreSQL service timezone
        track_activity_query_size (int | Unset): Specifies the number of bytes reserved to track the currently executing
            command for each active session. Changing this parameter causes a service restart.
        track_commit_timestamp (DatabaseServicePropertiesPgTrackCommitTimestamp | Unset): Record commit time of
            transactions. Changing this parameter causes a service restart.
        track_functions (DatabaseServicePropertiesPgTrackFunctions | Unset): Enables tracking of function call counts
            and time used.
        track_io_timing (DatabaseServicePropertiesPgTrackIoTiming | Unset): Enables timing of database I/O calls. The
            default is `off`. When on, it will repeatedly query the operating system for the current time, which may cause
            significant overhead on some platforms.
        variant (DatabaseServicePropertiesPgVariant | Unset):
        version (DatabaseServicePropertiesPgVersion | Unset):
        wal_sender_timeout (Any | Unset): Terminate replication connections that are inactive for longer than this
            amount of time, in milliseconds. Setting this value to zero disables the timeout.
        wal_writer_delay (int | Unset): WAL flush interval in milliseconds. The default is `200`. Setting this parameter
            to a lower value may negatively impact performance.
        work_mem (int | Unset): Sets the maximum amount of memory to be used by a query operation (such as a sort or
            hash table) before writing to temporary disk files, in MB. The default is 1MB + 0.075% of total RAM (up to
            32MB).
    """

    admin_password: None | str | Unset = UNSET
    admin_username: None | str | Unset = UNSET
    automatic_utility_network_ip_filter: bool | Unset = UNSET
    autovacuum_analyze_scale_factor: float | Unset = UNSET
    autovacuum_analyze_threshold: int | Unset = UNSET
    autovacuum_freeze_max_age: int | Unset = UNSET
    autovacuum_max_workers: int | Unset = UNSET
    autovacuum_naptime: int | Unset = UNSET
    autovacuum_vacuum_cost_delay: int | Unset = UNSET
    autovacuum_vacuum_cost_limit: int | Unset = UNSET
    autovacuum_vacuum_scale_factor: float | Unset = UNSET
    autovacuum_vacuum_threshold: int | Unset = UNSET
    backup_hour: int | None | Unset = UNSET
    backup_interval_hours: (
        DatabaseServicePropertiesPgBackupIntervalHoursType1
        | DatabaseServicePropertiesPgBackupIntervalHoursType2Type1
        | DatabaseServicePropertiesPgBackupIntervalHoursType3Type1
        | None
        | Unset
    ) = UNSET
    backup_minute: int | None | Unset = UNSET
    backup_retention_days: int | None | Unset = UNSET
    bgwriter_delay: int | Unset = UNSET
    bgwriter_flush_after: int | Unset = UNSET
    bgwriter_lru_maxpages: int | Unset = UNSET
    bgwriter_lru_multiplier: float | Unset = UNSET
    deadlock_timeout: int | Unset = UNSET
    default_toast_compression: DatabaseServicePropertiesPgDefaultToastCompression | Unset = UNSET
    enable_ha_replica_dns: bool | Unset = UNSET
    idle_in_transaction_session_timeout: int | Unset = UNSET
    io_combine_limit: int | Unset = UNSET
    io_max_combine_limit: int | Unset = UNSET
    io_max_concurrency: int | Unset = UNSET
    io_method: DatabaseServicePropertiesPgIoMethod | Unset = UNSET
    io_workers: int | Unset = UNSET
    ip_filter: list[str] | Unset = UNSET
    jit: bool | Unset = UNSET
    log_autovacuum_min_duration: int | Unset = UNSET
    log_error_verbosity: DatabaseServicePropertiesPgLogErrorVerbosity | Unset = UNSET
    log_line_prefix: DatabaseServicePropertiesPgLogLinePrefix | Unset = UNSET
    log_min_duration_statement: int | Unset = UNSET
    log_temp_files: int | Unset = UNSET
    max_connections: int | Unset = UNSET
    max_files_per_process: int | Unset = UNSET
    max_locks_per_transaction: int | Unset = UNSET
    max_logical_replication_workers: int | Unset = UNSET
    max_parallel_workers: int | Unset = UNSET
    max_parallel_workers_per_gather: int | Unset = UNSET
    max_pred_locks_per_transaction: int | Unset = UNSET
    max_prepared_transactions: int | Unset = UNSET
    max_replication_slots: int | Unset = UNSET
    max_slot_wal_keep_size: int | Unset = UNSET
    max_stack_depth: int | Unset = UNSET
    max_standby_archive_delay: int | Unset = UNSET
    max_standby_streaming_delay: int | Unset = UNSET
    max_sync_workers_per_subscription: int | Unset = UNSET
    max_wal_senders: int | Unset = UNSET
    max_worker_processes: int | Unset = UNSET
    migration: DatabaseServicePropertiesPgMigrationType0 | None | Unset = UNSET
    node_count: int | Unset = UNSET
    password_encryption: DatabaseServicePropertiesPgPasswordEncryption | Unset = UNSET
    pg_partman_bgw_interval: int | Unset = UNSET
    pg_partman_bgw_role: str | Unset = UNSET
    pg_stat_monitor_enable: bool | Unset = UNSET
    pg_stat_monitor_pgsm_enable_query_plan: bool | Unset = UNSET
    pg_stat_monitor_pgsm_max_buckets: int | Unset = UNSET
    pg_stat_statements_track: DatabaseServicePropertiesPgPgStatStatementsTrack | Unset = UNSET
    pgaudit: DatabaseServicePropertiesPgPgaudit | Unset = UNSET
    pgbouncer: DatabaseServicePropertiesPgPgbouncer | Unset = UNSET
    pglookout: DatabaseServicePropertiesPgPglookout | Unset = UNSET
    public_access: bool | Unset = UNSET
    public_access_prometheus: bool | Unset = UNSET
    service_log: bool | None | Unset = UNSET
    shared_buffers_percentage: float | Unset = UNSET
    synchronous_commit: DatabaseServicePropertiesPgSynchronousCommit | Unset = UNSET
    synchronous_replication: DatabaseServicePropertiesPgSynchronousReplication | Unset = UNSET
    temp_file_limit: int | Unset = UNSET
    timescaledb: DatabaseServicePropertiesPgTimescaledb | Unset = UNSET
    timezone: str | Unset = UNSET
    track_activity_query_size: int | Unset = UNSET
    track_commit_timestamp: DatabaseServicePropertiesPgTrackCommitTimestamp | Unset = UNSET
    track_functions: DatabaseServicePropertiesPgTrackFunctions | Unset = UNSET
    track_io_timing: DatabaseServicePropertiesPgTrackIoTiming | Unset = UNSET
    variant: DatabaseServicePropertiesPgVariant | Unset = UNSET
    version: DatabaseServicePropertiesPgVersion | Unset = UNSET
    wal_sender_timeout: Any | Unset = UNSET
    wal_writer_delay: int | Unset = UNSET
    work_mem: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.database_service_properties_pg_migration_type_0 import (
            DatabaseServicePropertiesPgMigrationType0,  # noqa: PLC0415
        )

        admin_password: None | str | Unset
        if isinstance(self.admin_password, Unset):
            admin_password = UNSET
        else:
            admin_password = self.admin_password

        admin_username: None | str | Unset
        if isinstance(self.admin_username, Unset):
            admin_username = UNSET
        else:
            admin_username = self.admin_username

        automatic_utility_network_ip_filter = self.automatic_utility_network_ip_filter

        autovacuum_analyze_scale_factor = self.autovacuum_analyze_scale_factor

        autovacuum_analyze_threshold = self.autovacuum_analyze_threshold

        autovacuum_freeze_max_age = self.autovacuum_freeze_max_age

        autovacuum_max_workers = self.autovacuum_max_workers

        autovacuum_naptime = self.autovacuum_naptime

        autovacuum_vacuum_cost_delay = self.autovacuum_vacuum_cost_delay

        autovacuum_vacuum_cost_limit = self.autovacuum_vacuum_cost_limit

        autovacuum_vacuum_scale_factor = self.autovacuum_vacuum_scale_factor

        autovacuum_vacuum_threshold = self.autovacuum_vacuum_threshold

        backup_hour: int | None | Unset
        if isinstance(self.backup_hour, Unset):
            backup_hour = UNSET
        else:
            backup_hour = self.backup_hour

        backup_interval_hours: int | None | Unset
        if isinstance(self.backup_interval_hours, Unset):
            backup_interval_hours = UNSET
        elif isinstance(self.backup_interval_hours, DatabaseServicePropertiesPgBackupIntervalHoursType1):
            backup_interval_hours = self.backup_interval_hours.value
        elif isinstance(self.backup_interval_hours, DatabaseServicePropertiesPgBackupIntervalHoursType2Type1):
            backup_interval_hours = self.backup_interval_hours.value
        elif isinstance(self.backup_interval_hours, DatabaseServicePropertiesPgBackupIntervalHoursType3Type1):
            backup_interval_hours = self.backup_interval_hours.value
        else:
            backup_interval_hours = self.backup_interval_hours

        backup_minute: int | None | Unset
        if isinstance(self.backup_minute, Unset):
            backup_minute = UNSET
        else:
            backup_minute = self.backup_minute

        backup_retention_days: int | None | Unset
        if isinstance(self.backup_retention_days, Unset):
            backup_retention_days = UNSET
        else:
            backup_retention_days = self.backup_retention_days

        bgwriter_delay = self.bgwriter_delay

        bgwriter_flush_after = self.bgwriter_flush_after

        bgwriter_lru_maxpages = self.bgwriter_lru_maxpages

        bgwriter_lru_multiplier = self.bgwriter_lru_multiplier

        deadlock_timeout = self.deadlock_timeout

        default_toast_compression: str | Unset = UNSET
        if not isinstance(self.default_toast_compression, Unset):
            default_toast_compression = self.default_toast_compression.value

        enable_ha_replica_dns = self.enable_ha_replica_dns

        idle_in_transaction_session_timeout = self.idle_in_transaction_session_timeout

        io_combine_limit = self.io_combine_limit

        io_max_combine_limit = self.io_max_combine_limit

        io_max_concurrency = self.io_max_concurrency

        io_method: str | Unset = UNSET
        if not isinstance(self.io_method, Unset):
            io_method = self.io_method.value

        io_workers = self.io_workers

        ip_filter: list[str] | Unset = UNSET
        if not isinstance(self.ip_filter, Unset):
            ip_filter = self.ip_filter

        jit = self.jit

        log_autovacuum_min_duration = self.log_autovacuum_min_duration

        log_error_verbosity: str | Unset = UNSET
        if not isinstance(self.log_error_verbosity, Unset):
            log_error_verbosity = self.log_error_verbosity.value

        log_line_prefix: str | Unset = UNSET
        if not isinstance(self.log_line_prefix, Unset):
            log_line_prefix = self.log_line_prefix.value

        log_min_duration_statement = self.log_min_duration_statement

        log_temp_files = self.log_temp_files

        max_connections = self.max_connections

        max_files_per_process = self.max_files_per_process

        max_locks_per_transaction = self.max_locks_per_transaction

        max_logical_replication_workers = self.max_logical_replication_workers

        max_parallel_workers = self.max_parallel_workers

        max_parallel_workers_per_gather = self.max_parallel_workers_per_gather

        max_pred_locks_per_transaction = self.max_pred_locks_per_transaction

        max_prepared_transactions = self.max_prepared_transactions

        max_replication_slots = self.max_replication_slots

        max_slot_wal_keep_size = self.max_slot_wal_keep_size

        max_stack_depth = self.max_stack_depth

        max_standby_archive_delay = self.max_standby_archive_delay

        max_standby_streaming_delay = self.max_standby_streaming_delay

        max_sync_workers_per_subscription = self.max_sync_workers_per_subscription

        max_wal_senders = self.max_wal_senders

        max_worker_processes = self.max_worker_processes

        migration: dict[str, Any] | None | Unset
        if isinstance(self.migration, Unset):
            migration = UNSET
        elif isinstance(self.migration, DatabaseServicePropertiesPgMigrationType0):
            migration = self.migration.to_dict()
        else:
            migration = self.migration

        node_count = self.node_count

        password_encryption: str | Unset = UNSET
        if not isinstance(self.password_encryption, Unset):
            password_encryption = self.password_encryption.value

        pg_partman_bgw_interval = self.pg_partman_bgw_interval

        pg_partman_bgw_role = self.pg_partman_bgw_role

        pg_stat_monitor_enable = self.pg_stat_monitor_enable

        pg_stat_monitor_pgsm_enable_query_plan = self.pg_stat_monitor_pgsm_enable_query_plan

        pg_stat_monitor_pgsm_max_buckets = self.pg_stat_monitor_pgsm_max_buckets

        pg_stat_statements_track: str | Unset = UNSET
        if not isinstance(self.pg_stat_statements_track, Unset):
            pg_stat_statements_track = self.pg_stat_statements_track.value

        pgaudit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pgaudit, Unset):
            pgaudit = self.pgaudit.to_dict()

        pgbouncer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pgbouncer, Unset):
            pgbouncer = self.pgbouncer.to_dict()

        pglookout: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pglookout, Unset):
            pglookout = self.pglookout.to_dict()

        public_access = self.public_access

        public_access_prometheus = self.public_access_prometheus

        service_log: bool | None | Unset
        if isinstance(self.service_log, Unset):
            service_log = UNSET
        else:
            service_log = self.service_log

        shared_buffers_percentage = self.shared_buffers_percentage

        synchronous_commit: str | Unset = UNSET
        if not isinstance(self.synchronous_commit, Unset):
            synchronous_commit = self.synchronous_commit.value

        synchronous_replication: str | Unset = UNSET
        if not isinstance(self.synchronous_replication, Unset):
            synchronous_replication = self.synchronous_replication.value

        temp_file_limit = self.temp_file_limit

        timescaledb: dict[str, Any] | Unset = UNSET
        if not isinstance(self.timescaledb, Unset):
            timescaledb = self.timescaledb.to_dict()

        timezone = self.timezone

        track_activity_query_size = self.track_activity_query_size

        track_commit_timestamp: str | Unset = UNSET
        if not isinstance(self.track_commit_timestamp, Unset):
            track_commit_timestamp = self.track_commit_timestamp.value

        track_functions: str | Unset = UNSET
        if not isinstance(self.track_functions, Unset):
            track_functions = self.track_functions.value

        track_io_timing: str | Unset = UNSET
        if not isinstance(self.track_io_timing, Unset):
            track_io_timing = self.track_io_timing.value

        variant: str | Unset = UNSET
        if not isinstance(self.variant, Unset):
            variant = self.variant.value

        version: str | Unset = UNSET
        if not isinstance(self.version, Unset):
            version = self.version.value

        wal_sender_timeout: Any | Unset
        if isinstance(self.wal_sender_timeout, Unset):
            wal_sender_timeout = UNSET
        else:
            wal_sender_timeout = self.wal_sender_timeout

        wal_writer_delay = self.wal_writer_delay

        work_mem = self.work_mem

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if admin_password is not UNSET:
            field_dict["admin_password"] = admin_password
        if admin_username is not UNSET:
            field_dict["admin_username"] = admin_username
        if automatic_utility_network_ip_filter is not UNSET:
            field_dict["automatic_utility_network_ip_filter"] = automatic_utility_network_ip_filter
        if autovacuum_analyze_scale_factor is not UNSET:
            field_dict["autovacuum_analyze_scale_factor"] = autovacuum_analyze_scale_factor
        if autovacuum_analyze_threshold is not UNSET:
            field_dict["autovacuum_analyze_threshold"] = autovacuum_analyze_threshold
        if autovacuum_freeze_max_age is not UNSET:
            field_dict["autovacuum_freeze_max_age"] = autovacuum_freeze_max_age
        if autovacuum_max_workers is not UNSET:
            field_dict["autovacuum_max_workers"] = autovacuum_max_workers
        if autovacuum_naptime is not UNSET:
            field_dict["autovacuum_naptime"] = autovacuum_naptime
        if autovacuum_vacuum_cost_delay is not UNSET:
            field_dict["autovacuum_vacuum_cost_delay"] = autovacuum_vacuum_cost_delay
        if autovacuum_vacuum_cost_limit is not UNSET:
            field_dict["autovacuum_vacuum_cost_limit"] = autovacuum_vacuum_cost_limit
        if autovacuum_vacuum_scale_factor is not UNSET:
            field_dict["autovacuum_vacuum_scale_factor"] = autovacuum_vacuum_scale_factor
        if autovacuum_vacuum_threshold is not UNSET:
            field_dict["autovacuum_vacuum_threshold"] = autovacuum_vacuum_threshold
        if backup_hour is not UNSET:
            field_dict["backup_hour"] = backup_hour
        if backup_interval_hours is not UNSET:
            field_dict["backup_interval_hours"] = backup_interval_hours
        if backup_minute is not UNSET:
            field_dict["backup_minute"] = backup_minute
        if backup_retention_days is not UNSET:
            field_dict["backup_retention_days"] = backup_retention_days
        if bgwriter_delay is not UNSET:
            field_dict["bgwriter_delay"] = bgwriter_delay
        if bgwriter_flush_after is not UNSET:
            field_dict["bgwriter_flush_after"] = bgwriter_flush_after
        if bgwriter_lru_maxpages is not UNSET:
            field_dict["bgwriter_lru_maxpages"] = bgwriter_lru_maxpages
        if bgwriter_lru_multiplier is not UNSET:
            field_dict["bgwriter_lru_multiplier"] = bgwriter_lru_multiplier
        if deadlock_timeout is not UNSET:
            field_dict["deadlock_timeout"] = deadlock_timeout
        if default_toast_compression is not UNSET:
            field_dict["default_toast_compression"] = default_toast_compression
        if enable_ha_replica_dns is not UNSET:
            field_dict["enable_ha_replica_dns"] = enable_ha_replica_dns
        if idle_in_transaction_session_timeout is not UNSET:
            field_dict["idle_in_transaction_session_timeout"] = idle_in_transaction_session_timeout
        if io_combine_limit is not UNSET:
            field_dict["io_combine_limit"] = io_combine_limit
        if io_max_combine_limit is not UNSET:
            field_dict["io_max_combine_limit"] = io_max_combine_limit
        if io_max_concurrency is not UNSET:
            field_dict["io_max_concurrency"] = io_max_concurrency
        if io_method is not UNSET:
            field_dict["io_method"] = io_method
        if io_workers is not UNSET:
            field_dict["io_workers"] = io_workers
        if ip_filter is not UNSET:
            field_dict["ip_filter"] = ip_filter
        if jit is not UNSET:
            field_dict["jit"] = jit
        if log_autovacuum_min_duration is not UNSET:
            field_dict["log_autovacuum_min_duration"] = log_autovacuum_min_duration
        if log_error_verbosity is not UNSET:
            field_dict["log_error_verbosity"] = log_error_verbosity
        if log_line_prefix is not UNSET:
            field_dict["log_line_prefix"] = log_line_prefix
        if log_min_duration_statement is not UNSET:
            field_dict["log_min_duration_statement"] = log_min_duration_statement
        if log_temp_files is not UNSET:
            field_dict["log_temp_files"] = log_temp_files
        if max_connections is not UNSET:
            field_dict["max_connections"] = max_connections
        if max_files_per_process is not UNSET:
            field_dict["max_files_per_process"] = max_files_per_process
        if max_locks_per_transaction is not UNSET:
            field_dict["max_locks_per_transaction"] = max_locks_per_transaction
        if max_logical_replication_workers is not UNSET:
            field_dict["max_logical_replication_workers"] = max_logical_replication_workers
        if max_parallel_workers is not UNSET:
            field_dict["max_parallel_workers"] = max_parallel_workers
        if max_parallel_workers_per_gather is not UNSET:
            field_dict["max_parallel_workers_per_gather"] = max_parallel_workers_per_gather
        if max_pred_locks_per_transaction is not UNSET:
            field_dict["max_pred_locks_per_transaction"] = max_pred_locks_per_transaction
        if max_prepared_transactions is not UNSET:
            field_dict["max_prepared_transactions"] = max_prepared_transactions
        if max_replication_slots is not UNSET:
            field_dict["max_replication_slots"] = max_replication_slots
        if max_slot_wal_keep_size is not UNSET:
            field_dict["max_slot_wal_keep_size"] = max_slot_wal_keep_size
        if max_stack_depth is not UNSET:
            field_dict["max_stack_depth"] = max_stack_depth
        if max_standby_archive_delay is not UNSET:
            field_dict["max_standby_archive_delay"] = max_standby_archive_delay
        if max_standby_streaming_delay is not UNSET:
            field_dict["max_standby_streaming_delay"] = max_standby_streaming_delay
        if max_sync_workers_per_subscription is not UNSET:
            field_dict["max_sync_workers_per_subscription"] = max_sync_workers_per_subscription
        if max_wal_senders is not UNSET:
            field_dict["max_wal_senders"] = max_wal_senders
        if max_worker_processes is not UNSET:
            field_dict["max_worker_processes"] = max_worker_processes
        if migration is not UNSET:
            field_dict["migration"] = migration
        if node_count is not UNSET:
            field_dict["node_count"] = node_count
        if password_encryption is not UNSET:
            field_dict["password_encryption"] = password_encryption
        if pg_partman_bgw_interval is not UNSET:
            field_dict["pg_partman_bgw_interval"] = pg_partman_bgw_interval
        if pg_partman_bgw_role is not UNSET:
            field_dict["pg_partman_bgw_role"] = pg_partman_bgw_role
        if pg_stat_monitor_enable is not UNSET:
            field_dict["pg_stat_monitor_enable"] = pg_stat_monitor_enable
        if pg_stat_monitor_pgsm_enable_query_plan is not UNSET:
            field_dict["pg_stat_monitor_pgsm_enable_query_plan"] = pg_stat_monitor_pgsm_enable_query_plan
        if pg_stat_monitor_pgsm_max_buckets is not UNSET:
            field_dict["pg_stat_monitor_pgsm_max_buckets"] = pg_stat_monitor_pgsm_max_buckets
        if pg_stat_statements_track is not UNSET:
            field_dict["pg_stat_statements_track"] = pg_stat_statements_track
        if pgaudit is not UNSET:
            field_dict["pgaudit"] = pgaudit
        if pgbouncer is not UNSET:
            field_dict["pgbouncer"] = pgbouncer
        if pglookout is not UNSET:
            field_dict["pglookout"] = pglookout
        if public_access is not UNSET:
            field_dict["public_access"] = public_access
        if public_access_prometheus is not UNSET:
            field_dict["public_access_prometheus"] = public_access_prometheus
        if service_log is not UNSET:
            field_dict["service_log"] = service_log
        if shared_buffers_percentage is not UNSET:
            field_dict["shared_buffers_percentage"] = shared_buffers_percentage
        if synchronous_commit is not UNSET:
            field_dict["synchronous_commit"] = synchronous_commit
        if synchronous_replication is not UNSET:
            field_dict["synchronous_replication"] = synchronous_replication
        if temp_file_limit is not UNSET:
            field_dict["temp_file_limit"] = temp_file_limit
        if timescaledb is not UNSET:
            field_dict["timescaledb"] = timescaledb
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if track_activity_query_size is not UNSET:
            field_dict["track_activity_query_size"] = track_activity_query_size
        if track_commit_timestamp is not UNSET:
            field_dict["track_commit_timestamp"] = track_commit_timestamp
        if track_functions is not UNSET:
            field_dict["track_functions"] = track_functions
        if track_io_timing is not UNSET:
            field_dict["track_io_timing"] = track_io_timing
        if variant is not UNSET:
            field_dict["variant"] = variant
        if version is not UNSET:
            field_dict["version"] = version
        if wal_sender_timeout is not UNSET:
            field_dict["wal_sender_timeout"] = wal_sender_timeout
        if wal_writer_delay is not UNSET:
            field_dict["wal_writer_delay"] = wal_writer_delay
        if work_mem is not UNSET:
            field_dict["work_mem"] = work_mem

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_service_properties_pg_migration_type_0 import (
            DatabaseServicePropertiesPgMigrationType0,  # noqa: PLC0415
        )
        from ..models.database_service_properties_pg_pgaudit import DatabaseServicePropertiesPgPgaudit  # noqa: PLC0415
        from ..models.database_service_properties_pg_pgbouncer import (
            DatabaseServicePropertiesPgPgbouncer,  # noqa: PLC0415
        )
        from ..models.database_service_properties_pg_pglookout import (
            DatabaseServicePropertiesPgPglookout,  # noqa: PLC0415
        )
        from ..models.database_service_properties_pg_timescaledb import (
            DatabaseServicePropertiesPgTimescaledb,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_admin_password(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        admin_password = _parse_admin_password(d.pop("admin_password", UNSET))

        def _parse_admin_username(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        admin_username = _parse_admin_username(d.pop("admin_username", UNSET))

        automatic_utility_network_ip_filter = d.pop("automatic_utility_network_ip_filter", UNSET)

        autovacuum_analyze_scale_factor = d.pop("autovacuum_analyze_scale_factor", UNSET)

        autovacuum_analyze_threshold = d.pop("autovacuum_analyze_threshold", UNSET)

        autovacuum_freeze_max_age = d.pop("autovacuum_freeze_max_age", UNSET)

        autovacuum_max_workers = d.pop("autovacuum_max_workers", UNSET)

        autovacuum_naptime = d.pop("autovacuum_naptime", UNSET)

        autovacuum_vacuum_cost_delay = d.pop("autovacuum_vacuum_cost_delay", UNSET)

        autovacuum_vacuum_cost_limit = d.pop("autovacuum_vacuum_cost_limit", UNSET)

        autovacuum_vacuum_scale_factor = d.pop("autovacuum_vacuum_scale_factor", UNSET)

        autovacuum_vacuum_threshold = d.pop("autovacuum_vacuum_threshold", UNSET)

        def _parse_backup_hour(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        backup_hour = _parse_backup_hour(d.pop("backup_hour", UNSET))

        def _parse_backup_interval_hours(
            data: object,
        ) -> (
            DatabaseServicePropertiesPgBackupIntervalHoursType1
            | DatabaseServicePropertiesPgBackupIntervalHoursType2Type1
            | DatabaseServicePropertiesPgBackupIntervalHoursType3Type1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, int):
                    raise TypeError()
                backup_interval_hours_type_1 = DatabaseServicePropertiesPgBackupIntervalHoursType1(data)

                return backup_interval_hours_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                backup_interval_hours_type_2_type_1 = DatabaseServicePropertiesPgBackupIntervalHoursType2Type1(data)

                return backup_interval_hours_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                backup_interval_hours_type_3_type_1 = DatabaseServicePropertiesPgBackupIntervalHoursType3Type1(data)

                return backup_interval_hours_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                DatabaseServicePropertiesPgBackupIntervalHoursType1
                | DatabaseServicePropertiesPgBackupIntervalHoursType2Type1
                | DatabaseServicePropertiesPgBackupIntervalHoursType3Type1
                | None
                | Unset,
                data,
            )

        backup_interval_hours = _parse_backup_interval_hours(d.pop("backup_interval_hours", UNSET))

        def _parse_backup_minute(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        backup_minute = _parse_backup_minute(d.pop("backup_minute", UNSET))

        def _parse_backup_retention_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        backup_retention_days = _parse_backup_retention_days(d.pop("backup_retention_days", UNSET))

        bgwriter_delay = d.pop("bgwriter_delay", UNSET)

        bgwriter_flush_after = d.pop("bgwriter_flush_after", UNSET)

        bgwriter_lru_maxpages = d.pop("bgwriter_lru_maxpages", UNSET)

        bgwriter_lru_multiplier = d.pop("bgwriter_lru_multiplier", UNSET)

        deadlock_timeout = d.pop("deadlock_timeout", UNSET)

        _default_toast_compression = d.pop("default_toast_compression", UNSET)
        default_toast_compression: DatabaseServicePropertiesPgDefaultToastCompression | Unset
        if isinstance(_default_toast_compression, Unset):
            default_toast_compression = UNSET
        else:
            default_toast_compression = DatabaseServicePropertiesPgDefaultToastCompression(_default_toast_compression)

        enable_ha_replica_dns = d.pop("enable_ha_replica_dns", UNSET)

        idle_in_transaction_session_timeout = d.pop("idle_in_transaction_session_timeout", UNSET)

        io_combine_limit = d.pop("io_combine_limit", UNSET)

        io_max_combine_limit = d.pop("io_max_combine_limit", UNSET)

        io_max_concurrency = d.pop("io_max_concurrency", UNSET)

        _io_method = d.pop("io_method", UNSET)
        io_method: DatabaseServicePropertiesPgIoMethod | Unset
        if isinstance(_io_method, Unset):
            io_method = UNSET
        else:
            io_method = DatabaseServicePropertiesPgIoMethod(_io_method)

        io_workers = d.pop("io_workers", UNSET)

        ip_filter = cast(list[str], d.pop("ip_filter", UNSET))

        jit = d.pop("jit", UNSET)

        log_autovacuum_min_duration = d.pop("log_autovacuum_min_duration", UNSET)

        _log_error_verbosity = d.pop("log_error_verbosity", UNSET)
        log_error_verbosity: DatabaseServicePropertiesPgLogErrorVerbosity | Unset
        if isinstance(_log_error_verbosity, Unset):
            log_error_verbosity = UNSET
        else:
            log_error_verbosity = DatabaseServicePropertiesPgLogErrorVerbosity(_log_error_verbosity)

        _log_line_prefix = d.pop("log_line_prefix", UNSET)
        log_line_prefix: DatabaseServicePropertiesPgLogLinePrefix | Unset
        if isinstance(_log_line_prefix, Unset):
            log_line_prefix = UNSET
        else:
            log_line_prefix = DatabaseServicePropertiesPgLogLinePrefix(_log_line_prefix)

        log_min_duration_statement = d.pop("log_min_duration_statement", UNSET)

        log_temp_files = d.pop("log_temp_files", UNSET)

        max_connections = d.pop("max_connections", UNSET)

        max_files_per_process = d.pop("max_files_per_process", UNSET)

        max_locks_per_transaction = d.pop("max_locks_per_transaction", UNSET)

        max_logical_replication_workers = d.pop("max_logical_replication_workers", UNSET)

        max_parallel_workers = d.pop("max_parallel_workers", UNSET)

        max_parallel_workers_per_gather = d.pop("max_parallel_workers_per_gather", UNSET)

        max_pred_locks_per_transaction = d.pop("max_pred_locks_per_transaction", UNSET)

        max_prepared_transactions = d.pop("max_prepared_transactions", UNSET)

        max_replication_slots = d.pop("max_replication_slots", UNSET)

        max_slot_wal_keep_size = d.pop("max_slot_wal_keep_size", UNSET)

        max_stack_depth = d.pop("max_stack_depth", UNSET)

        max_standby_archive_delay = d.pop("max_standby_archive_delay", UNSET)

        max_standby_streaming_delay = d.pop("max_standby_streaming_delay", UNSET)

        max_sync_workers_per_subscription = d.pop("max_sync_workers_per_subscription", UNSET)

        max_wal_senders = d.pop("max_wal_senders", UNSET)

        max_worker_processes = d.pop("max_worker_processes", UNSET)

        def _parse_migration(data: object) -> DatabaseServicePropertiesPgMigrationType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                migration_type_0 = DatabaseServicePropertiesPgMigrationType0.from_dict(data)

                return migration_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatabaseServicePropertiesPgMigrationType0 | None | Unset, data)

        migration = _parse_migration(d.pop("migration", UNSET))

        node_count = d.pop("node_count", UNSET)

        _password_encryption = d.pop("password_encryption", UNSET)
        password_encryption: DatabaseServicePropertiesPgPasswordEncryption | Unset
        if isinstance(_password_encryption, Unset):
            password_encryption = UNSET
        else:
            password_encryption = DatabaseServicePropertiesPgPasswordEncryption(_password_encryption)

        pg_partman_bgw_interval = d.pop("pg_partman_bgw_interval", UNSET)

        pg_partman_bgw_role = d.pop("pg_partman_bgw_role", UNSET)

        pg_stat_monitor_enable = d.pop("pg_stat_monitor_enable", UNSET)

        pg_stat_monitor_pgsm_enable_query_plan = d.pop("pg_stat_monitor_pgsm_enable_query_plan", UNSET)

        pg_stat_monitor_pgsm_max_buckets = d.pop("pg_stat_monitor_pgsm_max_buckets", UNSET)

        _pg_stat_statements_track = d.pop("pg_stat_statements_track", UNSET)
        pg_stat_statements_track: DatabaseServicePropertiesPgPgStatStatementsTrack | Unset
        if isinstance(_pg_stat_statements_track, Unset):
            pg_stat_statements_track = UNSET
        else:
            pg_stat_statements_track = DatabaseServicePropertiesPgPgStatStatementsTrack(_pg_stat_statements_track)

        _pgaudit = d.pop("pgaudit", UNSET)
        pgaudit: DatabaseServicePropertiesPgPgaudit | Unset
        if isinstance(_pgaudit, Unset):
            pgaudit = UNSET
        else:
            pgaudit = DatabaseServicePropertiesPgPgaudit.from_dict(_pgaudit)

        _pgbouncer = d.pop("pgbouncer", UNSET)
        pgbouncer: DatabaseServicePropertiesPgPgbouncer | Unset
        if isinstance(_pgbouncer, Unset):
            pgbouncer = UNSET
        else:
            pgbouncer = DatabaseServicePropertiesPgPgbouncer.from_dict(_pgbouncer)

        _pglookout = d.pop("pglookout", UNSET)
        pglookout: DatabaseServicePropertiesPgPglookout | Unset
        if isinstance(_pglookout, Unset):
            pglookout = UNSET
        else:
            pglookout = DatabaseServicePropertiesPgPglookout.from_dict(_pglookout)

        public_access = d.pop("public_access", UNSET)

        public_access_prometheus = d.pop("public_access_prometheus", UNSET)

        def _parse_service_log(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        service_log = _parse_service_log(d.pop("service_log", UNSET))

        shared_buffers_percentage = d.pop("shared_buffers_percentage", UNSET)

        _synchronous_commit = d.pop("synchronous_commit", UNSET)
        synchronous_commit: DatabaseServicePropertiesPgSynchronousCommit | Unset
        if isinstance(_synchronous_commit, Unset):
            synchronous_commit = UNSET
        else:
            synchronous_commit = DatabaseServicePropertiesPgSynchronousCommit(_synchronous_commit)

        _synchronous_replication = d.pop("synchronous_replication", UNSET)
        synchronous_replication: DatabaseServicePropertiesPgSynchronousReplication | Unset
        if isinstance(_synchronous_replication, Unset):
            synchronous_replication = UNSET
        else:
            synchronous_replication = DatabaseServicePropertiesPgSynchronousReplication(_synchronous_replication)

        temp_file_limit = d.pop("temp_file_limit", UNSET)

        _timescaledb = d.pop("timescaledb", UNSET)
        timescaledb: DatabaseServicePropertiesPgTimescaledb | Unset
        if isinstance(_timescaledb, Unset):
            timescaledb = UNSET
        else:
            timescaledb = DatabaseServicePropertiesPgTimescaledb.from_dict(_timescaledb)

        timezone = d.pop("timezone", UNSET)

        track_activity_query_size = d.pop("track_activity_query_size", UNSET)

        _track_commit_timestamp = d.pop("track_commit_timestamp", UNSET)
        track_commit_timestamp: DatabaseServicePropertiesPgTrackCommitTimestamp | Unset
        if isinstance(_track_commit_timestamp, Unset):
            track_commit_timestamp = UNSET
        else:
            track_commit_timestamp = DatabaseServicePropertiesPgTrackCommitTimestamp(_track_commit_timestamp)

        _track_functions = d.pop("track_functions", UNSET)
        track_functions: DatabaseServicePropertiesPgTrackFunctions | Unset
        if isinstance(_track_functions, Unset):
            track_functions = UNSET
        else:
            track_functions = DatabaseServicePropertiesPgTrackFunctions(_track_functions)

        _track_io_timing = d.pop("track_io_timing", UNSET)
        track_io_timing: DatabaseServicePropertiesPgTrackIoTiming | Unset
        if isinstance(_track_io_timing, Unset):
            track_io_timing = UNSET
        else:
            track_io_timing = DatabaseServicePropertiesPgTrackIoTiming(_track_io_timing)

        _variant = d.pop("variant", UNSET)
        variant: DatabaseServicePropertiesPgVariant | Unset
        if isinstance(_variant, Unset):
            variant = UNSET
        else:
            variant = DatabaseServicePropertiesPgVariant(_variant)

        _version = d.pop("version", UNSET)
        version: DatabaseServicePropertiesPgVersion | Unset
        if isinstance(_version, Unset):
            version = UNSET
        else:
            version = DatabaseServicePropertiesPgVersion(_version)

        def _parse_wal_sender_timeout(data: object) -> Any | Unset:
            if isinstance(data, Unset):
                return data
            return cast(Any | Unset, data)

        wal_sender_timeout = _parse_wal_sender_timeout(d.pop("wal_sender_timeout", UNSET))

        wal_writer_delay = d.pop("wal_writer_delay", UNSET)

        work_mem = d.pop("work_mem", UNSET)

        database_service_properties_pg = cls(
            admin_password=admin_password,
            admin_username=admin_username,
            automatic_utility_network_ip_filter=automatic_utility_network_ip_filter,
            autovacuum_analyze_scale_factor=autovacuum_analyze_scale_factor,
            autovacuum_analyze_threshold=autovacuum_analyze_threshold,
            autovacuum_freeze_max_age=autovacuum_freeze_max_age,
            autovacuum_max_workers=autovacuum_max_workers,
            autovacuum_naptime=autovacuum_naptime,
            autovacuum_vacuum_cost_delay=autovacuum_vacuum_cost_delay,
            autovacuum_vacuum_cost_limit=autovacuum_vacuum_cost_limit,
            autovacuum_vacuum_scale_factor=autovacuum_vacuum_scale_factor,
            autovacuum_vacuum_threshold=autovacuum_vacuum_threshold,
            backup_hour=backup_hour,
            backup_interval_hours=backup_interval_hours,
            backup_minute=backup_minute,
            backup_retention_days=backup_retention_days,
            bgwriter_delay=bgwriter_delay,
            bgwriter_flush_after=bgwriter_flush_after,
            bgwriter_lru_maxpages=bgwriter_lru_maxpages,
            bgwriter_lru_multiplier=bgwriter_lru_multiplier,
            deadlock_timeout=deadlock_timeout,
            default_toast_compression=default_toast_compression,
            enable_ha_replica_dns=enable_ha_replica_dns,
            idle_in_transaction_session_timeout=idle_in_transaction_session_timeout,
            io_combine_limit=io_combine_limit,
            io_max_combine_limit=io_max_combine_limit,
            io_max_concurrency=io_max_concurrency,
            io_method=io_method,
            io_workers=io_workers,
            ip_filter=ip_filter,
            jit=jit,
            log_autovacuum_min_duration=log_autovacuum_min_duration,
            log_error_verbosity=log_error_verbosity,
            log_line_prefix=log_line_prefix,
            log_min_duration_statement=log_min_duration_statement,
            log_temp_files=log_temp_files,
            max_connections=max_connections,
            max_files_per_process=max_files_per_process,
            max_locks_per_transaction=max_locks_per_transaction,
            max_logical_replication_workers=max_logical_replication_workers,
            max_parallel_workers=max_parallel_workers,
            max_parallel_workers_per_gather=max_parallel_workers_per_gather,
            max_pred_locks_per_transaction=max_pred_locks_per_transaction,
            max_prepared_transactions=max_prepared_transactions,
            max_replication_slots=max_replication_slots,
            max_slot_wal_keep_size=max_slot_wal_keep_size,
            max_stack_depth=max_stack_depth,
            max_standby_archive_delay=max_standby_archive_delay,
            max_standby_streaming_delay=max_standby_streaming_delay,
            max_sync_workers_per_subscription=max_sync_workers_per_subscription,
            max_wal_senders=max_wal_senders,
            max_worker_processes=max_worker_processes,
            migration=migration,
            node_count=node_count,
            password_encryption=password_encryption,
            pg_partman_bgw_interval=pg_partman_bgw_interval,
            pg_partman_bgw_role=pg_partman_bgw_role,
            pg_stat_monitor_enable=pg_stat_monitor_enable,
            pg_stat_monitor_pgsm_enable_query_plan=pg_stat_monitor_pgsm_enable_query_plan,
            pg_stat_monitor_pgsm_max_buckets=pg_stat_monitor_pgsm_max_buckets,
            pg_stat_statements_track=pg_stat_statements_track,
            pgaudit=pgaudit,
            pgbouncer=pgbouncer,
            pglookout=pglookout,
            public_access=public_access,
            public_access_prometheus=public_access_prometheus,
            service_log=service_log,
            shared_buffers_percentage=shared_buffers_percentage,
            synchronous_commit=synchronous_commit,
            synchronous_replication=synchronous_replication,
            temp_file_limit=temp_file_limit,
            timescaledb=timescaledb,
            timezone=timezone,
            track_activity_query_size=track_activity_query_size,
            track_commit_timestamp=track_commit_timestamp,
            track_functions=track_functions,
            track_io_timing=track_io_timing,
            variant=variant,
            version=version,
            wal_sender_timeout=wal_sender_timeout,
            wal_writer_delay=wal_writer_delay,
            work_mem=work_mem,
        )

        return database_service_properties_pg
