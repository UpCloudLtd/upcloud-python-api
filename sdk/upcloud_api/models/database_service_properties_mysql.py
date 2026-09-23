from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.database_service_properties_mysql_internal_tmp_mem_storage_engine import (
    DatabaseServicePropertiesMysqlInternalTmpMemStorageEngine,
)
from ..models.database_service_properties_mysql_log_output import DatabaseServicePropertiesMysqlLogOutput
from ..models.database_service_properties_mysql_lower_case_table_names import (
    DatabaseServicePropertiesMysqlLowerCaseTableNames,
)
from ..models.database_service_properties_mysql_version import DatabaseServicePropertiesMysqlVersion
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_service_properties_mysql_migration_type_0 import DatabaseServicePropertiesMysqlMigrationType0
    from ..models.database_service_properties_mysql_mysql_incremental_backup import (
        DatabaseServicePropertiesMysqlMysqlIncrementalBackup,
    )


T = TypeVar("T", bound="DatabaseServicePropertiesMysql")


@_attrs_define
class DatabaseServicePropertiesMysql:
    """mysql properties

    Attributes:
        admin_password (None | str | Unset):
        admin_username (None | str | Unset):
        automatic_sp_privileges (bool | Unset): When enabled, the server automatically grants the EXECUTE and ALTER
            ROUTINE privileges to the creator of a stored routine and drops them when the routine is dropped.
        automatic_utility_network_ip_filter (bool | Unset): Automatically allow connections from servers in the utility
            network within the same zone
        backup_hour (int | Unset):
        backup_minute (int | Unset):
        binlog_retention_period (int | Unset): Warning: reducing this value can make a large batch of binary logs
            eligible for purge at once. Depending on the volume, this can sometimes stall the MySQL commit path and block
            writes until the purge completes. To stay on the safe side, prefer lowering the value gradually in small
            decrements during a low-traffic window rather than dropping it drastically in one step.
        connect_timeout (int | Unset): The number of seconds that the mysqld server waits for a connect packet before
            responding with Bad handshake
        default_time_zone (str | Unset): Default server time zone as an offset from UTC (from -12:00 to +12:00), a time
            zone name, or 'SYSTEM' to use the MySQL server default.
        div_precision_increment (int | Unset): Number of digits by which to increase the scale of the result of division
            operations performed with the / operator. Default is 4.
        end_markers_in_json (bool | Unset): Whether optimizer JSON output such as EXPLAIN FORMAT=JSON adds end markers
            that repeat a structure's key near its closing bracket, making large JSON structures easier to read.
        eq_range_index_dive_limit (int | Unset): The number of equality ranges in a query at or above which the
            optimizer switches from index dives to index statistics when estimating the number of qualifying rows. 0 means
            always use index dives. Default is 200.
        group_concat_max_len (int | Unset): The maximum permitted result length in bytes for the GROUP_CONCAT()
            function.
        information_schema_stats_expiry (int | Unset): The time, in seconds, before cached statistics expire
        innodb_adaptive_hash_index (bool | Unset): Whether InnoDB adaptive hash indexing is enabled. The optimal setting
            is workload-dependent: it speeds up lookups for some workloads but its internal latch can become a contention
            point under high concurrency, in which case disabling it can improve throughput.
        innodb_change_buffer_max_size (int | Unset): Maximum size for the InnoDB change buffer, as a percentage of the
            total size of the buffer pool. Default is 25
        innodb_flush_neighbors (int | Unset): Specifies whether flushing a page from the InnoDB buffer pool also flushes
            other dirty pages in the same extent (default is 1): 0 - dirty pages in the same extent are not flushed, 1 -
            flush contiguous dirty pages in the same extent, 2 - flush dirty pages in the same extent
        innodb_ft_enable_stopword (bool | Unset): Whether stopword processing is applied when creating or rebuilding an
            InnoDB FULLTEXT index. Enabled by default.
        innodb_ft_max_token_size (int | Unset): Maximum length of words that are stored in an InnoDB FULLTEXT index.
            Changing this parameter will lead to a restart of the MySQL service.
        innodb_ft_min_token_size (int | Unset): Minimum length of words that are stored in an InnoDB FULLTEXT index.
            Changing this parameter will lead to a restart of the MySQL service.
        innodb_ft_num_word_optimize (int | Unset): Number of words processed during each OPTIMIZE TABLE operation on an
            InnoDB FULLTEXT index. Default is 2000.
        innodb_ft_result_cache_limit (int | Unset): Maximum memory in bytes used per query for the InnoDB FULLTEXT
            search query result cache. UpCloud sizes this automatically based on the service plan's memory; setting a value
            overrides the calculated default.
        innodb_ft_server_stopword_table (None | str | Unset): This option is used to specify your own InnoDB FULLTEXT
            index stopword list for all InnoDB tables.
        innodb_ft_user_stopword_table (None | str | Unset): This option is used to specify your own InnoDB FULLTEXT
            index stopword list for specific InnoDB tables.
        innodb_io_capacity (int | Unset): The number of I/O operations per second (IOPS) available to InnoDB background
            tasks, such as flushing pages from the buffer pool and merging data from the change buffer. Set this to a value
            appropriate for the underlying storage; it must not exceed innodb_io_capacity_max.
        innodb_io_capacity_max (int | Unset): The maximum number of I/O operations per second (IOPS) that InnoDB
            background tasks may perform when flushing falls behind. Defaults to twice innodb_io_capacity (minimum 2000).
            This must be greater than or equal to innodb_io_capacity.
        innodb_lock_wait_timeout (int | Unset): The length of time in seconds an InnoDB transaction waits for a row lock
            before giving up. Default is 120.
        innodb_log_buffer_size (int | Unset): The size in bytes of the buffer that InnoDB uses to write to the log files
            on disk.
        innodb_online_alter_log_max_size (int | Unset): The upper limit in bytes on the size of the temporary log files
            used during online DDL operations for InnoDB tables.
        innodb_optimize_fulltext_only (bool | Unset): When enabled, OPTIMIZE TABLE on InnoDB tables only updates the
            FULLTEXT index instead of rebuilding the table. Intended to be enabled temporarily during FULLTEXT index
            maintenance and disabled afterwards; while enabled, OPTIMIZE TABLE does not reclaim table space.
        innodb_print_all_deadlocks (bool | Unset): When enabled, information about all deadlocks in InnoDB user
            transactions is recorded in the error log. Disabled by default.
        innodb_read_io_threads (int | Unset): The number of I/O threads for read operations in InnoDB. Default is 4.
            Changing this parameter will lead to a restart of the MySQL service.
        innodb_rollback_on_timeout (bool | Unset): When enabled a transaction timeout causes InnoDB to abort and roll
            back the entire transaction. Changing this parameter will lead to a restart of the MySQL service.
        innodb_thread_concurrency (int | Unset): Defines the maximum number of threads permitted inside of InnoDB.
            Default is 0 (infinite concurrency - no limit)
        innodb_write_io_threads (int | Unset): The number of I/O threads for write operations in InnoDB. Default is 4.
            Changing this parameter will lead to a restart of the MySQL service.
        interactive_timeout (int | Unset): The number of seconds the server waits for activity on an interactive
            connection before closing it.
        internal_tmp_mem_storage_engine (DatabaseServicePropertiesMysqlInternalTmpMemStorageEngine | Unset): The storage
            engine for in-memory internal temporary tables.
        ip_filter (list[str] | Unset): Allow incoming connections from CIDR address block, e.g. '10.20.0.0/16'
        log_output (DatabaseServicePropertiesMysqlLogOutput | Unset): The slow log output destination when
            slow_query_log is ON. To enable MySQL AI Insights, choose INSIGHTS. To use MySQL AI Insights and the
            mysql.slow_log table at the same time, choose INSIGHTS,TABLE. To only use the mysql.slow_log table, choose
            TABLE. To silence slow logs, choose NONE.
        long_query_time (float | Unset): The slow_query_logs work as SQL statements that take more than long_query_time
            seconds to execute.
        lower_case_table_names (DatabaseServicePropertiesMysqlLowerCaseTableNames | Unset): Sets how table and database
            names are stored and compared. 0 = case-sensitive (default), 1 = names stored lowercase, comparisons are case-
            insensitive. This option can only be set when creating the service and cannot be changed later. See
            https://dev.mysql.com/doc/refman/8.0/en/identifier-case-sensitivity.html for details.
        max_allowed_packet (int | Unset): Size of the largest message in bytes that can be received by the server.
            Default is 67108864 (64M)
        max_execution_time (int | Unset): Execution timeout in milliseconds for read-only top-level SELECT statements. 0
            (the default) means no timeout.
        max_heap_table_size (int | Unset): Limits the size of internal in-memory tables. Also set tmp_table_size.
            Default is 16777216 (16M)
        max_seeks_for_key (int | Unset): Limit on the assumed maximum number of index seeks when looking up rows based
            on a key. Lowering this value causes the optimizer to prefer index lookups over table scans.
        migration (DatabaseServicePropertiesMysqlMigrationType0 | None | Unset):
        mysql_incremental_backup (DatabaseServicePropertiesMysqlMysqlIncrementalBackup | Unset):
        net_buffer_length (int | Unset): Start sizes of connection buffer and result buffer. Default is 16384 (16K).
            Changing this parameter will lead to a restart of the MySQL service.
        net_read_timeout (int | Unset): The number of seconds to wait for more data from a connection before aborting
            the read.
        net_write_timeout (int | Unset): The number of seconds to wait for a block to be written to a connection before
            aborting the write.
        optimizer_prune_level (int | Unset): Controls the heuristics applied during query optimization to prune less-
            promising partial plans from the optimizer search space. 0 disables heuristics (exhaustive search); 1 prunes
            plans based on the number of rows retrieved.
        optimizer_search_depth (int | Unset): Maximum depth of search performed by the query optimizer when choosing a
            join order. Larger values produce better plans for joins over many tables but take longer to compile; 0 lets the
            optimizer choose the depth automatically.
        optimizer_switch (str | Unset): Comma-separated list of optimizer flag assignments in the form
            flag=on|off|default, or the single value 'default' to reset all flags. Flags not listed keep their current
            values. Controls query optimizer behaviors such as index merge, hash join and semijoin strategies.
        performance_schema_events_statements_history_size (int | None | Unset): The number of rows per thread in the
            events_statements_history table. Changing this parameter will lead to a restart of the MySQL service.
        public_access (bool | Unset): Allow access to the service from the public Internet
        public_access_prometheus (bool | Unset): Allow access to Prometheus metrics from the public Internet
        relay_log_space_limit (int | Unset): The maximum amount of space in bytes to use for all relay logs while
            replicating from an external migration source. When the limit is reached, the replication I/O thread stops
            fetching relay log events until the SQL thread has caught up. Raise this to give a large migration a bigger
            relay-log budget; ensure the service disk is sized accordingly. The setting applies only on the node replicating
            from the external source; standby nodes always use the UpCloud-managed default (the smaller of 5 GiB and 30% of
            the service disk), which is also used when this option is left unset. Changing this parameter will lead to a
            restart of the MySQL service.
        service_log (bool | None | Unset): Store logs for the service so that they are available in the HTTP API and
            console.
        slow_query_log (bool | Unset): Slow query log enables capturing of slow queries. Setting slow_query_log to false
            also truncates the mysql.slow_log table.
        sort_buffer_size (int | Unset): Sort buffer size in bytes for ORDER BY optimization. Default is 262144 (256K)
        sql_mode (str | Unset): Global SQL mode. Set to empty to use MySQL server defaults. When creating a new service
            and not setting this field UpCloud default SQL mode (strict, SQL standard compliant) will be assigned.
        sql_require_primary_key (bool | Unset): Require primary key to be defined for new tables or old tables modified
            with ALTER TABLE and fail if missing. It is recommended to always have primary keys because various
            functionality may break if any large table is missing them.
        tmp_table_size (int | Unset): Limits the size of internal in-memory tables. Also set max_heap_table_size.
            Default is 16777216 (16M)
        version (DatabaseServicePropertiesMysqlVersion | Unset):
        wait_timeout (int | Unset): The number of seconds the server waits for activity on a noninteractive connection
            before closing it.
        windowing_use_high_precision (bool | Unset): Whether window functions are computed to high precision. Disabling
            this trades exactness for speed in window function evaluation.
    """

    admin_password: None | str | Unset = UNSET
    admin_username: None | str | Unset = UNSET
    automatic_sp_privileges: bool | Unset = UNSET
    automatic_utility_network_ip_filter: bool | Unset = UNSET
    backup_hour: int | Unset = UNSET
    backup_minute: int | Unset = UNSET
    binlog_retention_period: int | Unset = UNSET
    connect_timeout: int | Unset = UNSET
    default_time_zone: str | Unset = UNSET
    div_precision_increment: int | Unset = UNSET
    end_markers_in_json: bool | Unset = UNSET
    eq_range_index_dive_limit: int | Unset = UNSET
    group_concat_max_len: int | Unset = UNSET
    information_schema_stats_expiry: int | Unset = UNSET
    innodb_adaptive_hash_index: bool | Unset = UNSET
    innodb_change_buffer_max_size: int | Unset = UNSET
    innodb_flush_neighbors: int | Unset = UNSET
    innodb_ft_enable_stopword: bool | Unset = UNSET
    innodb_ft_max_token_size: int | Unset = UNSET
    innodb_ft_min_token_size: int | Unset = UNSET
    innodb_ft_num_word_optimize: int | Unset = UNSET
    innodb_ft_result_cache_limit: int | Unset = UNSET
    innodb_ft_server_stopword_table: None | str | Unset = UNSET
    innodb_ft_user_stopword_table: None | str | Unset = UNSET
    innodb_io_capacity: int | Unset = UNSET
    innodb_io_capacity_max: int | Unset = UNSET
    innodb_lock_wait_timeout: int | Unset = UNSET
    innodb_log_buffer_size: int | Unset = UNSET
    innodb_online_alter_log_max_size: int | Unset = UNSET
    innodb_optimize_fulltext_only: bool | Unset = UNSET
    innodb_print_all_deadlocks: bool | Unset = UNSET
    innodb_read_io_threads: int | Unset = UNSET
    innodb_rollback_on_timeout: bool | Unset = UNSET
    innodb_thread_concurrency: int | Unset = UNSET
    innodb_write_io_threads: int | Unset = UNSET
    interactive_timeout: int | Unset = UNSET
    internal_tmp_mem_storage_engine: DatabaseServicePropertiesMysqlInternalTmpMemStorageEngine | Unset = UNSET
    ip_filter: list[str] | Unset = UNSET
    log_output: DatabaseServicePropertiesMysqlLogOutput | Unset = UNSET
    long_query_time: float | Unset = UNSET
    lower_case_table_names: DatabaseServicePropertiesMysqlLowerCaseTableNames | Unset = UNSET
    max_allowed_packet: int | Unset = UNSET
    max_execution_time: int | Unset = UNSET
    max_heap_table_size: int | Unset = UNSET
    max_seeks_for_key: int | Unset = UNSET
    migration: DatabaseServicePropertiesMysqlMigrationType0 | None | Unset = UNSET
    mysql_incremental_backup: DatabaseServicePropertiesMysqlMysqlIncrementalBackup | Unset = UNSET
    net_buffer_length: int | Unset = UNSET
    net_read_timeout: int | Unset = UNSET
    net_write_timeout: int | Unset = UNSET
    optimizer_prune_level: int | Unset = UNSET
    optimizer_search_depth: int | Unset = UNSET
    optimizer_switch: str | Unset = UNSET
    performance_schema_events_statements_history_size: int | None | Unset = UNSET
    public_access: bool | Unset = UNSET
    public_access_prometheus: bool | Unset = UNSET
    relay_log_space_limit: int | Unset = UNSET
    service_log: bool | None | Unset = UNSET
    slow_query_log: bool | Unset = UNSET
    sort_buffer_size: int | Unset = UNSET
    sql_mode: str | Unset = UNSET
    sql_require_primary_key: bool | Unset = UNSET
    tmp_table_size: int | Unset = UNSET
    version: DatabaseServicePropertiesMysqlVersion | Unset = UNSET
    wait_timeout: int | Unset = UNSET
    windowing_use_high_precision: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.database_service_properties_mysql_migration_type_0 import (
            DatabaseServicePropertiesMysqlMigrationType0,  # noqa: PLC0415
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

        automatic_sp_privileges = self.automatic_sp_privileges

        automatic_utility_network_ip_filter = self.automatic_utility_network_ip_filter

        backup_hour = self.backup_hour

        backup_minute = self.backup_minute

        binlog_retention_period = self.binlog_retention_period

        connect_timeout = self.connect_timeout

        default_time_zone = self.default_time_zone

        div_precision_increment = self.div_precision_increment

        end_markers_in_json = self.end_markers_in_json

        eq_range_index_dive_limit = self.eq_range_index_dive_limit

        group_concat_max_len = self.group_concat_max_len

        information_schema_stats_expiry = self.information_schema_stats_expiry

        innodb_adaptive_hash_index = self.innodb_adaptive_hash_index

        innodb_change_buffer_max_size = self.innodb_change_buffer_max_size

        innodb_flush_neighbors = self.innodb_flush_neighbors

        innodb_ft_enable_stopword = self.innodb_ft_enable_stopword

        innodb_ft_max_token_size = self.innodb_ft_max_token_size

        innodb_ft_min_token_size = self.innodb_ft_min_token_size

        innodb_ft_num_word_optimize = self.innodb_ft_num_word_optimize

        innodb_ft_result_cache_limit = self.innodb_ft_result_cache_limit

        innodb_ft_server_stopword_table: None | str | Unset
        if isinstance(self.innodb_ft_server_stopword_table, Unset):
            innodb_ft_server_stopword_table = UNSET
        else:
            innodb_ft_server_stopword_table = self.innodb_ft_server_stopword_table

        innodb_ft_user_stopword_table: None | str | Unset
        if isinstance(self.innodb_ft_user_stopword_table, Unset):
            innodb_ft_user_stopword_table = UNSET
        else:
            innodb_ft_user_stopword_table = self.innodb_ft_user_stopword_table

        innodb_io_capacity = self.innodb_io_capacity

        innodb_io_capacity_max = self.innodb_io_capacity_max

        innodb_lock_wait_timeout = self.innodb_lock_wait_timeout

        innodb_log_buffer_size = self.innodb_log_buffer_size

        innodb_online_alter_log_max_size = self.innodb_online_alter_log_max_size

        innodb_optimize_fulltext_only = self.innodb_optimize_fulltext_only

        innodb_print_all_deadlocks = self.innodb_print_all_deadlocks

        innodb_read_io_threads = self.innodb_read_io_threads

        innodb_rollback_on_timeout = self.innodb_rollback_on_timeout

        innodb_thread_concurrency = self.innodb_thread_concurrency

        innodb_write_io_threads = self.innodb_write_io_threads

        interactive_timeout = self.interactive_timeout

        internal_tmp_mem_storage_engine: str | Unset = UNSET
        if not isinstance(self.internal_tmp_mem_storage_engine, Unset):
            internal_tmp_mem_storage_engine = self.internal_tmp_mem_storage_engine.value

        ip_filter: list[str] | Unset = UNSET
        if not isinstance(self.ip_filter, Unset):
            ip_filter = self.ip_filter

        log_output: str | Unset = UNSET
        if not isinstance(self.log_output, Unset):
            log_output = self.log_output.value

        long_query_time = self.long_query_time

        lower_case_table_names: int | Unset = UNSET
        if not isinstance(self.lower_case_table_names, Unset):
            lower_case_table_names = self.lower_case_table_names.value

        max_allowed_packet = self.max_allowed_packet

        max_execution_time = self.max_execution_time

        max_heap_table_size = self.max_heap_table_size

        max_seeks_for_key = self.max_seeks_for_key

        migration: dict[str, Any] | None | Unset
        if isinstance(self.migration, Unset):
            migration = UNSET
        elif isinstance(self.migration, DatabaseServicePropertiesMysqlMigrationType0):
            migration = self.migration.to_dict()
        else:
            migration = self.migration

        mysql_incremental_backup: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mysql_incremental_backup, Unset):
            mysql_incremental_backup = self.mysql_incremental_backup.to_dict()

        net_buffer_length = self.net_buffer_length

        net_read_timeout = self.net_read_timeout

        net_write_timeout = self.net_write_timeout

        optimizer_prune_level = self.optimizer_prune_level

        optimizer_search_depth = self.optimizer_search_depth

        optimizer_switch = self.optimizer_switch

        performance_schema_events_statements_history_size: int | None | Unset
        if isinstance(self.performance_schema_events_statements_history_size, Unset):
            performance_schema_events_statements_history_size = UNSET
        else:
            performance_schema_events_statements_history_size = self.performance_schema_events_statements_history_size

        public_access = self.public_access

        public_access_prometheus = self.public_access_prometheus

        relay_log_space_limit = self.relay_log_space_limit

        service_log: bool | None | Unset
        if isinstance(self.service_log, Unset):
            service_log = UNSET
        else:
            service_log = self.service_log

        slow_query_log = self.slow_query_log

        sort_buffer_size = self.sort_buffer_size

        sql_mode = self.sql_mode

        sql_require_primary_key = self.sql_require_primary_key

        tmp_table_size = self.tmp_table_size

        version: str | Unset = UNSET
        if not isinstance(self.version, Unset):
            version = self.version.value

        wait_timeout = self.wait_timeout

        windowing_use_high_precision = self.windowing_use_high_precision

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if admin_password is not UNSET:
            field_dict["admin_password"] = admin_password
        if admin_username is not UNSET:
            field_dict["admin_username"] = admin_username
        if automatic_sp_privileges is not UNSET:
            field_dict["automatic_sp_privileges"] = automatic_sp_privileges
        if automatic_utility_network_ip_filter is not UNSET:
            field_dict["automatic_utility_network_ip_filter"] = automatic_utility_network_ip_filter
        if backup_hour is not UNSET:
            field_dict["backup_hour"] = backup_hour
        if backup_minute is not UNSET:
            field_dict["backup_minute"] = backup_minute
        if binlog_retention_period is not UNSET:
            field_dict["binlog_retention_period"] = binlog_retention_period
        if connect_timeout is not UNSET:
            field_dict["connect_timeout"] = connect_timeout
        if default_time_zone is not UNSET:
            field_dict["default_time_zone"] = default_time_zone
        if div_precision_increment is not UNSET:
            field_dict["div_precision_increment"] = div_precision_increment
        if end_markers_in_json is not UNSET:
            field_dict["end_markers_in_json"] = end_markers_in_json
        if eq_range_index_dive_limit is not UNSET:
            field_dict["eq_range_index_dive_limit"] = eq_range_index_dive_limit
        if group_concat_max_len is not UNSET:
            field_dict["group_concat_max_len"] = group_concat_max_len
        if information_schema_stats_expiry is not UNSET:
            field_dict["information_schema_stats_expiry"] = information_schema_stats_expiry
        if innodb_adaptive_hash_index is not UNSET:
            field_dict["innodb_adaptive_hash_index"] = innodb_adaptive_hash_index
        if innodb_change_buffer_max_size is not UNSET:
            field_dict["innodb_change_buffer_max_size"] = innodb_change_buffer_max_size
        if innodb_flush_neighbors is not UNSET:
            field_dict["innodb_flush_neighbors"] = innodb_flush_neighbors
        if innodb_ft_enable_stopword is not UNSET:
            field_dict["innodb_ft_enable_stopword"] = innodb_ft_enable_stopword
        if innodb_ft_max_token_size is not UNSET:
            field_dict["innodb_ft_max_token_size"] = innodb_ft_max_token_size
        if innodb_ft_min_token_size is not UNSET:
            field_dict["innodb_ft_min_token_size"] = innodb_ft_min_token_size
        if innodb_ft_num_word_optimize is not UNSET:
            field_dict["innodb_ft_num_word_optimize"] = innodb_ft_num_word_optimize
        if innodb_ft_result_cache_limit is not UNSET:
            field_dict["innodb_ft_result_cache_limit"] = innodb_ft_result_cache_limit
        if innodb_ft_server_stopword_table is not UNSET:
            field_dict["innodb_ft_server_stopword_table"] = innodb_ft_server_stopword_table
        if innodb_ft_user_stopword_table is not UNSET:
            field_dict["innodb_ft_user_stopword_table"] = innodb_ft_user_stopword_table
        if innodb_io_capacity is not UNSET:
            field_dict["innodb_io_capacity"] = innodb_io_capacity
        if innodb_io_capacity_max is not UNSET:
            field_dict["innodb_io_capacity_max"] = innodb_io_capacity_max
        if innodb_lock_wait_timeout is not UNSET:
            field_dict["innodb_lock_wait_timeout"] = innodb_lock_wait_timeout
        if innodb_log_buffer_size is not UNSET:
            field_dict["innodb_log_buffer_size"] = innodb_log_buffer_size
        if innodb_online_alter_log_max_size is not UNSET:
            field_dict["innodb_online_alter_log_max_size"] = innodb_online_alter_log_max_size
        if innodb_optimize_fulltext_only is not UNSET:
            field_dict["innodb_optimize_fulltext_only"] = innodb_optimize_fulltext_only
        if innodb_print_all_deadlocks is not UNSET:
            field_dict["innodb_print_all_deadlocks"] = innodb_print_all_deadlocks
        if innodb_read_io_threads is not UNSET:
            field_dict["innodb_read_io_threads"] = innodb_read_io_threads
        if innodb_rollback_on_timeout is not UNSET:
            field_dict["innodb_rollback_on_timeout"] = innodb_rollback_on_timeout
        if innodb_thread_concurrency is not UNSET:
            field_dict["innodb_thread_concurrency"] = innodb_thread_concurrency
        if innodb_write_io_threads is not UNSET:
            field_dict["innodb_write_io_threads"] = innodb_write_io_threads
        if interactive_timeout is not UNSET:
            field_dict["interactive_timeout"] = interactive_timeout
        if internal_tmp_mem_storage_engine is not UNSET:
            field_dict["internal_tmp_mem_storage_engine"] = internal_tmp_mem_storage_engine
        if ip_filter is not UNSET:
            field_dict["ip_filter"] = ip_filter
        if log_output is not UNSET:
            field_dict["log_output"] = log_output
        if long_query_time is not UNSET:
            field_dict["long_query_time"] = long_query_time
        if lower_case_table_names is not UNSET:
            field_dict["lower_case_table_names"] = lower_case_table_names
        if max_allowed_packet is not UNSET:
            field_dict["max_allowed_packet"] = max_allowed_packet
        if max_execution_time is not UNSET:
            field_dict["max_execution_time"] = max_execution_time
        if max_heap_table_size is not UNSET:
            field_dict["max_heap_table_size"] = max_heap_table_size
        if max_seeks_for_key is not UNSET:
            field_dict["max_seeks_for_key"] = max_seeks_for_key
        if migration is not UNSET:
            field_dict["migration"] = migration
        if mysql_incremental_backup is not UNSET:
            field_dict["mysql_incremental_backup"] = mysql_incremental_backup
        if net_buffer_length is not UNSET:
            field_dict["net_buffer_length"] = net_buffer_length
        if net_read_timeout is not UNSET:
            field_dict["net_read_timeout"] = net_read_timeout
        if net_write_timeout is not UNSET:
            field_dict["net_write_timeout"] = net_write_timeout
        if optimizer_prune_level is not UNSET:
            field_dict["optimizer_prune_level"] = optimizer_prune_level
        if optimizer_search_depth is not UNSET:
            field_dict["optimizer_search_depth"] = optimizer_search_depth
        if optimizer_switch is not UNSET:
            field_dict["optimizer_switch"] = optimizer_switch
        if performance_schema_events_statements_history_size is not UNSET:
            field_dict["performance_schema_events_statements_history_size"] = (
                performance_schema_events_statements_history_size
            )
        if public_access is not UNSET:
            field_dict["public_access"] = public_access
        if public_access_prometheus is not UNSET:
            field_dict["public_access_prometheus"] = public_access_prometheus
        if relay_log_space_limit is not UNSET:
            field_dict["relay_log_space_limit"] = relay_log_space_limit
        if service_log is not UNSET:
            field_dict["service_log"] = service_log
        if slow_query_log is not UNSET:
            field_dict["slow_query_log"] = slow_query_log
        if sort_buffer_size is not UNSET:
            field_dict["sort_buffer_size"] = sort_buffer_size
        if sql_mode is not UNSET:
            field_dict["sql_mode"] = sql_mode
        if sql_require_primary_key is not UNSET:
            field_dict["sql_require_primary_key"] = sql_require_primary_key
        if tmp_table_size is not UNSET:
            field_dict["tmp_table_size"] = tmp_table_size
        if version is not UNSET:
            field_dict["version"] = version
        if wait_timeout is not UNSET:
            field_dict["wait_timeout"] = wait_timeout
        if windowing_use_high_precision is not UNSET:
            field_dict["windowing_use_high_precision"] = windowing_use_high_precision

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_service_properties_mysql_migration_type_0 import (
            DatabaseServicePropertiesMysqlMigrationType0,  # noqa: PLC0415
        )
        from ..models.database_service_properties_mysql_mysql_incremental_backup import (
            DatabaseServicePropertiesMysqlMysqlIncrementalBackup,  # noqa: PLC0415
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

        automatic_sp_privileges = d.pop("automatic_sp_privileges", UNSET)

        automatic_utility_network_ip_filter = d.pop("automatic_utility_network_ip_filter", UNSET)

        backup_hour = d.pop("backup_hour", UNSET)

        backup_minute = d.pop("backup_minute", UNSET)

        binlog_retention_period = d.pop("binlog_retention_period", UNSET)

        connect_timeout = d.pop("connect_timeout", UNSET)

        default_time_zone = d.pop("default_time_zone", UNSET)

        div_precision_increment = d.pop("div_precision_increment", UNSET)

        end_markers_in_json = d.pop("end_markers_in_json", UNSET)

        eq_range_index_dive_limit = d.pop("eq_range_index_dive_limit", UNSET)

        group_concat_max_len = d.pop("group_concat_max_len", UNSET)

        information_schema_stats_expiry = d.pop("information_schema_stats_expiry", UNSET)

        innodb_adaptive_hash_index = d.pop("innodb_adaptive_hash_index", UNSET)

        innodb_change_buffer_max_size = d.pop("innodb_change_buffer_max_size", UNSET)

        innodb_flush_neighbors = d.pop("innodb_flush_neighbors", UNSET)

        innodb_ft_enable_stopword = d.pop("innodb_ft_enable_stopword", UNSET)

        innodb_ft_max_token_size = d.pop("innodb_ft_max_token_size", UNSET)

        innodb_ft_min_token_size = d.pop("innodb_ft_min_token_size", UNSET)

        innodb_ft_num_word_optimize = d.pop("innodb_ft_num_word_optimize", UNSET)

        innodb_ft_result_cache_limit = d.pop("innodb_ft_result_cache_limit", UNSET)

        def _parse_innodb_ft_server_stopword_table(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        innodb_ft_server_stopword_table = _parse_innodb_ft_server_stopword_table(
            d.pop("innodb_ft_server_stopword_table", UNSET)
        )

        def _parse_innodb_ft_user_stopword_table(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        innodb_ft_user_stopword_table = _parse_innodb_ft_user_stopword_table(
            d.pop("innodb_ft_user_stopword_table", UNSET)
        )

        innodb_io_capacity = d.pop("innodb_io_capacity", UNSET)

        innodb_io_capacity_max = d.pop("innodb_io_capacity_max", UNSET)

        innodb_lock_wait_timeout = d.pop("innodb_lock_wait_timeout", UNSET)

        innodb_log_buffer_size = d.pop("innodb_log_buffer_size", UNSET)

        innodb_online_alter_log_max_size = d.pop("innodb_online_alter_log_max_size", UNSET)

        innodb_optimize_fulltext_only = d.pop("innodb_optimize_fulltext_only", UNSET)

        innodb_print_all_deadlocks = d.pop("innodb_print_all_deadlocks", UNSET)

        innodb_read_io_threads = d.pop("innodb_read_io_threads", UNSET)

        innodb_rollback_on_timeout = d.pop("innodb_rollback_on_timeout", UNSET)

        innodb_thread_concurrency = d.pop("innodb_thread_concurrency", UNSET)

        innodb_write_io_threads = d.pop("innodb_write_io_threads", UNSET)

        interactive_timeout = d.pop("interactive_timeout", UNSET)

        _internal_tmp_mem_storage_engine = d.pop("internal_tmp_mem_storage_engine", UNSET)
        internal_tmp_mem_storage_engine: DatabaseServicePropertiesMysqlInternalTmpMemStorageEngine | Unset
        if isinstance(_internal_tmp_mem_storage_engine, Unset):
            internal_tmp_mem_storage_engine = UNSET
        else:
            internal_tmp_mem_storage_engine = DatabaseServicePropertiesMysqlInternalTmpMemStorageEngine(
                _internal_tmp_mem_storage_engine
            )

        ip_filter = cast(list[str], d.pop("ip_filter", UNSET))

        _log_output = d.pop("log_output", UNSET)
        log_output: DatabaseServicePropertiesMysqlLogOutput | Unset
        if isinstance(_log_output, Unset):
            log_output = UNSET
        else:
            log_output = DatabaseServicePropertiesMysqlLogOutput(_log_output)

        long_query_time = d.pop("long_query_time", UNSET)

        _lower_case_table_names = d.pop("lower_case_table_names", UNSET)
        lower_case_table_names: DatabaseServicePropertiesMysqlLowerCaseTableNames | Unset
        if isinstance(_lower_case_table_names, Unset):
            lower_case_table_names = UNSET
        else:
            lower_case_table_names = DatabaseServicePropertiesMysqlLowerCaseTableNames(_lower_case_table_names)

        max_allowed_packet = d.pop("max_allowed_packet", UNSET)

        max_execution_time = d.pop("max_execution_time", UNSET)

        max_heap_table_size = d.pop("max_heap_table_size", UNSET)

        max_seeks_for_key = d.pop("max_seeks_for_key", UNSET)

        def _parse_migration(data: object) -> DatabaseServicePropertiesMysqlMigrationType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                migration_type_0 = DatabaseServicePropertiesMysqlMigrationType0.from_dict(data)

                return migration_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatabaseServicePropertiesMysqlMigrationType0 | None | Unset, data)

        migration = _parse_migration(d.pop("migration", UNSET))

        _mysql_incremental_backup = d.pop("mysql_incremental_backup", UNSET)
        mysql_incremental_backup: DatabaseServicePropertiesMysqlMysqlIncrementalBackup | Unset
        if isinstance(_mysql_incremental_backup, Unset):
            mysql_incremental_backup = UNSET
        else:
            mysql_incremental_backup = DatabaseServicePropertiesMysqlMysqlIncrementalBackup.from_dict(
                _mysql_incremental_backup
            )

        net_buffer_length = d.pop("net_buffer_length", UNSET)

        net_read_timeout = d.pop("net_read_timeout", UNSET)

        net_write_timeout = d.pop("net_write_timeout", UNSET)

        optimizer_prune_level = d.pop("optimizer_prune_level", UNSET)

        optimizer_search_depth = d.pop("optimizer_search_depth", UNSET)

        optimizer_switch = d.pop("optimizer_switch", UNSET)

        def _parse_performance_schema_events_statements_history_size(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        performance_schema_events_statements_history_size = _parse_performance_schema_events_statements_history_size(
            d.pop("performance_schema_events_statements_history_size", UNSET)
        )

        public_access = d.pop("public_access", UNSET)

        public_access_prometheus = d.pop("public_access_prometheus", UNSET)

        relay_log_space_limit = d.pop("relay_log_space_limit", UNSET)

        def _parse_service_log(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        service_log = _parse_service_log(d.pop("service_log", UNSET))

        slow_query_log = d.pop("slow_query_log", UNSET)

        sort_buffer_size = d.pop("sort_buffer_size", UNSET)

        sql_mode = d.pop("sql_mode", UNSET)

        sql_require_primary_key = d.pop("sql_require_primary_key", UNSET)

        tmp_table_size = d.pop("tmp_table_size", UNSET)

        _version = d.pop("version", UNSET)
        version: DatabaseServicePropertiesMysqlVersion | Unset
        if isinstance(_version, Unset):
            version = UNSET
        else:
            version = DatabaseServicePropertiesMysqlVersion(_version)

        wait_timeout = d.pop("wait_timeout", UNSET)

        windowing_use_high_precision = d.pop("windowing_use_high_precision", UNSET)

        database_service_properties_mysql = cls(
            admin_password=admin_password,
            admin_username=admin_username,
            automatic_sp_privileges=automatic_sp_privileges,
            automatic_utility_network_ip_filter=automatic_utility_network_ip_filter,
            backup_hour=backup_hour,
            backup_minute=backup_minute,
            binlog_retention_period=binlog_retention_period,
            connect_timeout=connect_timeout,
            default_time_zone=default_time_zone,
            div_precision_increment=div_precision_increment,
            end_markers_in_json=end_markers_in_json,
            eq_range_index_dive_limit=eq_range_index_dive_limit,
            group_concat_max_len=group_concat_max_len,
            information_schema_stats_expiry=information_schema_stats_expiry,
            innodb_adaptive_hash_index=innodb_adaptive_hash_index,
            innodb_change_buffer_max_size=innodb_change_buffer_max_size,
            innodb_flush_neighbors=innodb_flush_neighbors,
            innodb_ft_enable_stopword=innodb_ft_enable_stopword,
            innodb_ft_max_token_size=innodb_ft_max_token_size,
            innodb_ft_min_token_size=innodb_ft_min_token_size,
            innodb_ft_num_word_optimize=innodb_ft_num_word_optimize,
            innodb_ft_result_cache_limit=innodb_ft_result_cache_limit,
            innodb_ft_server_stopword_table=innodb_ft_server_stopword_table,
            innodb_ft_user_stopword_table=innodb_ft_user_stopword_table,
            innodb_io_capacity=innodb_io_capacity,
            innodb_io_capacity_max=innodb_io_capacity_max,
            innodb_lock_wait_timeout=innodb_lock_wait_timeout,
            innodb_log_buffer_size=innodb_log_buffer_size,
            innodb_online_alter_log_max_size=innodb_online_alter_log_max_size,
            innodb_optimize_fulltext_only=innodb_optimize_fulltext_only,
            innodb_print_all_deadlocks=innodb_print_all_deadlocks,
            innodb_read_io_threads=innodb_read_io_threads,
            innodb_rollback_on_timeout=innodb_rollback_on_timeout,
            innodb_thread_concurrency=innodb_thread_concurrency,
            innodb_write_io_threads=innodb_write_io_threads,
            interactive_timeout=interactive_timeout,
            internal_tmp_mem_storage_engine=internal_tmp_mem_storage_engine,
            ip_filter=ip_filter,
            log_output=log_output,
            long_query_time=long_query_time,
            lower_case_table_names=lower_case_table_names,
            max_allowed_packet=max_allowed_packet,
            max_execution_time=max_execution_time,
            max_heap_table_size=max_heap_table_size,
            max_seeks_for_key=max_seeks_for_key,
            migration=migration,
            mysql_incremental_backup=mysql_incremental_backup,
            net_buffer_length=net_buffer_length,
            net_read_timeout=net_read_timeout,
            net_write_timeout=net_write_timeout,
            optimizer_prune_level=optimizer_prune_level,
            optimizer_search_depth=optimizer_search_depth,
            optimizer_switch=optimizer_switch,
            performance_schema_events_statements_history_size=performance_schema_events_statements_history_size,
            public_access=public_access,
            public_access_prometheus=public_access_prometheus,
            relay_log_space_limit=relay_log_space_limit,
            service_log=service_log,
            slow_query_log=slow_query_log,
            sort_buffer_size=sort_buffer_size,
            sql_mode=sql_mode,
            sql_require_primary_key=sql_require_primary_key,
            tmp_table_size=tmp_table_size,
            version=version,
            wait_timeout=wait_timeout,
            windowing_use_high_precision=windowing_use_high_precision,
        )

        return database_service_properties_mysql
