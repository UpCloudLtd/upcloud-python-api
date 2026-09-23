from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.database_service_properties_opensearch_elasticsearch_version import (
    DatabaseServicePropertiesOpensearchElasticsearchVersion,
)
from ..models.database_service_properties_opensearch_version import DatabaseServicePropertiesOpensearchVersion
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_service_properties_opensearch_auth_failure_listeners import (
        DatabaseServicePropertiesOpensearchAuthFailureListeners,
    )
    from ..models.database_service_properties_opensearch_cluster_remote_store import (
        DatabaseServicePropertiesOpensearchClusterRemoteStore,
    )
    from ..models.database_service_properties_opensearch_cluster_search_request_slowlog import (
        DatabaseServicePropertiesOpensearchClusterSearchRequestSlowlog,
    )
    from ..models.database_service_properties_opensearch_custom_keystores_item import (
        DatabaseServicePropertiesOpensearchCustomKeystoresItem,
    )
    from ..models.database_service_properties_opensearch_custom_repos_item import (
        DatabaseServicePropertiesOpensearchCustomReposItem,
    )
    from ..models.database_service_properties_opensearch_disk_watermarks import (
        DatabaseServicePropertiesOpensearchDiskWatermarks,
    )
    from ..models.database_service_properties_opensearch_glob_pattern_and_number_of_indexes_matching_that_pattern_to_be_kept import (
        DatabaseServicePropertiesOpensearchGlobPatternAndNumberOfIndexesMatchingThatPatternToBeKept,
    )
    from ..models.database_service_properties_opensearch_index_rollup import (
        DatabaseServicePropertiesOpensearchIndexRollup,
    )
    from ..models.database_service_properties_opensearch_index_template import (
        DatabaseServicePropertiesOpensearchIndexTemplate,
    )
    from ..models.database_service_properties_opensearch_jwt import DatabaseServicePropertiesOpensearchJwt
    from ..models.database_service_properties_opensearch_openid import DatabaseServicePropertiesOpensearchOpenid
    from ..models.database_service_properties_opensearch_opensearch_dashboards import (
        DatabaseServicePropertiesOpensearchOpensearchDashboards,
    )
    from ..models.database_service_properties_opensearch_remote_store import (
        DatabaseServicePropertiesOpensearchRemoteStore,
    )
    from ..models.database_service_properties_opensearch_saml import DatabaseServicePropertiesOpensearchSaml
    from ..models.database_service_properties_opensearch_search_backpressure import (
        DatabaseServicePropertiesOpensearchSearchBackpressure,
    )
    from ..models.database_service_properties_opensearch_search_insights_top_queries import (
        DatabaseServicePropertiesOpensearchSearchInsightsTopQueries,
    )
    from ..models.database_service_properties_opensearch_segrep import DatabaseServicePropertiesOpensearchSegrep
    from ..models.database_service_properties_opensearch_shard_indexing_pressure import (
        DatabaseServicePropertiesOpensearchShardIndexingPressure,
    )


T = TypeVar("T", bound="DatabaseServicePropertiesOpensearch")


@_attrs_define
class DatabaseServicePropertiesOpensearch:
    """opensearch properties

    Attributes:
        action_auto_create_index_enabled (bool | Unset): Explicitly allow or block automatic creation of indices.
            Defaults to true
        action_destructive_requires_name (bool | None | Unset):
        auth_failure_listeners (DatabaseServicePropertiesOpensearchAuthFailureListeners | Unset):
        automatic_utility_network_ip_filter (bool | Unset): Automatically allow connections from servers in the utility
            network within the same zone
        cluster_filecache_remote_data_ratio (float | int | None | Unset): Defines a limit of how much total remote data
            can be referenced as a ratio of the size of the disk reserved for the file cache. This is designed to be a
            safeguard to prevent oversubscribing a cluster. Defaults to 0.
        cluster_max_shards_per_node (int | Unset): Controls the number of shards allowed in the cluster per data node
        cluster_remote_store (DatabaseServicePropertiesOpensearchClusterRemoteStore | Unset):
        cluster_routing_allocation_balance_prefer_primary (bool | Unset): When set to true, OpenSearch attempts to
            evenly distribute the primary shards between the cluster nodes. Enabling this setting does not always guarantee
            an equal number of primary shards on each node, especially in the event of a failover. Changing this setting to
            false after it was set to true does not invoke redistribution of primary shards. Default is false.
        cluster_routing_allocation_node_concurrent_recoveries (int | Unset): How many concurrent incoming/outgoing shard
            recoveries (normally replicas) are allowed to happen on a node. Defaults to node cpu count * 2.
        cluster_search_request_slowlog (DatabaseServicePropertiesOpensearchClusterSearchRequestSlowlog | Unset):
        custom_domain (None | str | Unset): Serve the web frontend using a custom CNAME pointing to the UpCloud DNS
            name. When you set a custom domain for a service deployed in a VPC, the service certificate is only created for
            the public-* hostname and the custom domain.
        custom_keystores (list[DatabaseServicePropertiesOpensearchCustomKeystoresItem] | Unset): Allow to register
            custom keystores in OpenSearch
        custom_repos (list[DatabaseServicePropertiesOpensearchCustomReposItem] | Unset): Allow to register object
            storage repositories in OpenSearch
        disk_watermarks (DatabaseServicePropertiesOpensearchDiskWatermarks | Unset):
        elasticsearch_version (DatabaseServicePropertiesOpensearchElasticsearchVersion | Unset):
        email_sender_name (str | Unset): This should be identical to the Sender name defined in Opensearch dashboards
        email_sender_password (str | Unset): Sender password for Opensearch alerts to authenticate with SMTP server
        email_sender_username (str | Unset):
        enable_remote_backed_storage (bool | Unset):
        enable_searchable_snapshots (bool | Unset):
        enable_security_audit (bool | Unset):
        enable_snapshot_api (bool | Unset): Enable/Disable snapshot API for custom repositories, this requires security
            management to be enabled
        http_max_content_length (int | Unset): Maximum content length for HTTP requests to the OpenSearch HTTP API, in
            bytes.
        http_max_header_size (int | Unset): The max size of allowed headers, in bytes
        http_max_initial_line_length (int | Unset): The max length of an HTTP URL, in bytes
        index_patterns
            (list[DatabaseServicePropertiesOpensearchGlobPatternAndNumberOfIndexesMatchingThatPatternToBeKept] | Unset):
        index_rollup (DatabaseServicePropertiesOpensearchIndexRollup | Unset):
        index_template (DatabaseServicePropertiesOpensearchIndexTemplate | Unset):
        indices_fielddata_cache_size (int | None | Unset): Relative amount. Maximum amount of heap memory used for field
            data cache. This is an expert setting; decreasing the value too much will increase overhead of loading field
            data; too much memory used for field data cache will decrease amount of heap available for other operations.
        indices_memory_index_buffer_size (int | Unset): Percentage value. Default is 10%. Total amount of heap used for
            indexing buffer, before writing segments to disk. This is an expert setting. Too low value will slow down
            indexing; too high value will increase indexing performance but causes performance issues for query performance.
        indices_memory_max_index_buffer_size (int | Unset): Absolute value. Default is unbound. Doesn't work without
            indices.memory.index_buffer_size. Maximum amount of heap used for query cache, an absolute
            indices.memory.index_buffer_size maximum hard limit.
        indices_memory_min_index_buffer_size (int | Unset): Absolute value. Default is 48mb. Doesn't work without
            indices.memory.index_buffer_size. Minimum amount of heap used for query cache, an absolute
            indices.memory.index_buffer_size minimal hard limit.
        indices_queries_cache_size (int | Unset): Percentage value. Default is 10%. Maximum amount of heap used for
            query cache. This is an expert setting. Too low value will decrease query performance and increase performance
            for other operations; too high value will cause issues with other OpenSearch functionality.
        indices_query_bool_max_clause_count (int | Unset): Maximum number of clauses Lucene BooleanQuery can have. The
            default value (1024) is relatively high, and increasing it may cause performance issues. Investigate other
            approaches first before increasing this value.
        indices_recovery_max_bytes_per_sec (int | Unset): Limits total inbound and outbound recovery traffic for each
            node. Applies to both peer recoveries as well as snapshot recoveries (i.e., restores from a snapshot). Defaults
            to 40mb
        indices_recovery_max_concurrent_file_chunks (int | Unset): Number of file chunks sent in parallel for each
            recovery. Defaults to 2.
        ip_filter (list[str] | Unset): Allow incoming connections from CIDR address block, e.g. '10.20.0.0/16'
        ism_enabled (bool | Unset):
        ism_history_enabled (bool | Unset):
        ism_history_max_age (int | Unset):
        ism_history_max_docs (int | Unset):
        ism_history_rollover_check_period (int | Unset):
        ism_history_rollover_retention_period (int | Unset):
        jwt (DatabaseServicePropertiesOpensearchJwt | Unset):
        keep_index_refresh_interval (bool | Unset): UpCloud automation resets index.refresh_interval to default value
            for every index to be sure that indices are always visible to search. If it doesn't fit your case, you can
            disable this by setting up this flag to true.
        knn_memory_circuit_breaker_enabled (bool | Unset): Enable or disable KNN memory circuit breaker. Defaults to
            true.
        knn_memory_circuit_breaker_limit (int | Unset): Maximum amount of memory in percentage that can be used for the
            KNN index. Defaults to 50% of the JVM heap size. 0 is used to set it to null which can be used to invalidate
            caches.
        ml_commons_model_access_control_enabled (bool | Unset): Enable or disable model access control for ML Commons.
            When enabled, access to ML models is controlled by security permissions. Defaults to false.
        ml_commons_native_memory_threshold (int | Unset): Native memory threshold percentage for ML Commons. Controls
            the maximum percentage of native memory that can be used by ML Commons operations. Defaults to 90%.
        ml_commons_only_run_on_ml_node (bool | Unset): Enable or disable running ML Commons tasks only on ML nodes. When
            enabled, ML tasks will only execute on nodes designated as ML nodes. Defaults to true.
        node_search_cache_size (None | str | Unset): Defines a limit of how much total remote data can be referenced as
            a ratio of the size of the disk reserved for the file cache. This is designed to be a safeguard to prevent
            oversubscribing a cluster. Defaults to 5gb. Requires restarting all OpenSearch nodes.
        openid (DatabaseServicePropertiesOpensearchOpenid | Unset):
        opensearch_dashboards (DatabaseServicePropertiesOpensearchOpensearchDashboards | Unset):
        override_main_response_version (bool | Unset): Compatibility mode sets OpenSearch to report its version as 7.10
            so clients continue to work. Default is false. Deprecated and ignored for service version 3.3 and higher.
        plugins_alerting_filter_by_backend_roles (bool | Unset): Enable or disable filtering of alerting by backend
            roles. Requires Security plugin. Defaults to false
        public_access (bool | Unset): Allow access to the service from the public Internet
        public_access_prometheus (bool | Unset): Allow access to Prometheus metrics from the public Internet
        reindex_remote_whitelist (list[None | str] | None | Unset): Whitelisted addresses for reindexing. Changing this
            value will cause all OpenSearch instances to restart.
        remote_store (DatabaseServicePropertiesOpensearchRemoteStore | Unset):
        saml (DatabaseServicePropertiesOpensearchSaml | Unset):
        script_max_compilations_rate (str | Unset): Script compilation circuit breaker limits the number of inline
            script compilations within a period of time. Default is use-context
        search_backpressure (DatabaseServicePropertiesOpensearchSearchBackpressure | Unset):
        search_insights_top_queries (DatabaseServicePropertiesOpensearchSearchInsightsTopQueries | Unset):
        search_max_buckets (int | None | Unset): Maximum number of aggregation buckets allowed in a single response.
            OpenSearch default value is used when this is not defined.
        segrep (DatabaseServicePropertiesOpensearchSegrep | Unset):
        service_log (bool | None | Unset): Store logs for the service so that they are available in the HTTP API and
            console.
        shard_indexing_pressure (DatabaseServicePropertiesOpensearchShardIndexingPressure | Unset):
        thread_pool_analyze_queue_size (int | Unset): Size for the thread pool queue. See documentation for exact
            details.
        thread_pool_analyze_size (int | Unset): Size for the thread pool. See documentation for exact details. Do note
            this may have maximum value depending on CPU count - value is automatically lowered if set to higher than
            maximum value.
        thread_pool_force_merge_size (int | Unset): Size for the thread pool. See documentation for exact details. Do
            note this may have maximum value depending on CPU count - value is automatically lowered if set to higher than
            maximum value.
        thread_pool_get_queue_size (int | Unset): Size for the thread pool queue. See documentation for exact details.
        thread_pool_get_size (int | Unset): Size for the thread pool. See documentation for exact details. Do note this
            may have maximum value depending on CPU count - value is automatically lowered if set to higher than maximum
            value.
        thread_pool_search_queue_size (int | Unset): Size for the thread pool queue. See documentation for exact
            details.
        thread_pool_search_size (int | Unset): Size for the thread pool. See documentation for exact details. Do note
            this may have maximum value depending on CPU count - value is automatically lowered if set to higher than
            maximum value.
        thread_pool_search_throttled_queue_size (int | Unset): Size for the thread pool queue. See documentation for
            exact details.
        thread_pool_search_throttled_size (int | Unset): Size for the thread pool. See documentation for exact details.
            Do note this may have maximum value depending on CPU count - value is automatically lowered if set to higher
            than maximum value.
        thread_pool_write_queue_size (int | Unset): Size for the thread pool queue. See documentation for exact details.
        thread_pool_write_size (int | Unset): Size for the thread pool. See documentation for exact details. Do note
            this may have maximum value depending on CPU count - value is automatically lowered if set to higher than
            maximum value.
        version (DatabaseServicePropertiesOpensearchVersion | Unset):
    """

    action_auto_create_index_enabled: bool | Unset = UNSET
    action_destructive_requires_name: bool | None | Unset = UNSET
    auth_failure_listeners: DatabaseServicePropertiesOpensearchAuthFailureListeners | Unset = UNSET
    automatic_utility_network_ip_filter: bool | Unset = UNSET
    cluster_filecache_remote_data_ratio: float | int | None | Unset = UNSET
    cluster_max_shards_per_node: int | Unset = UNSET
    cluster_remote_store: DatabaseServicePropertiesOpensearchClusterRemoteStore | Unset = UNSET
    cluster_routing_allocation_balance_prefer_primary: bool | Unset = UNSET
    cluster_routing_allocation_node_concurrent_recoveries: int | Unset = UNSET
    cluster_search_request_slowlog: DatabaseServicePropertiesOpensearchClusterSearchRequestSlowlog | Unset = UNSET
    custom_domain: None | str | Unset = UNSET
    custom_keystores: list[DatabaseServicePropertiesOpensearchCustomKeystoresItem] | Unset = UNSET
    custom_repos: list[DatabaseServicePropertiesOpensearchCustomReposItem] | Unset = UNSET
    disk_watermarks: DatabaseServicePropertiesOpensearchDiskWatermarks | Unset = UNSET
    elasticsearch_version: DatabaseServicePropertiesOpensearchElasticsearchVersion | Unset = UNSET
    email_sender_name: str | Unset = UNSET
    email_sender_password: str | Unset = UNSET
    email_sender_username: str | Unset = UNSET
    enable_remote_backed_storage: bool | Unset = UNSET
    enable_searchable_snapshots: bool | Unset = UNSET
    enable_security_audit: bool | Unset = UNSET
    enable_snapshot_api: bool | Unset = UNSET
    http_max_content_length: int | Unset = UNSET
    http_max_header_size: int | Unset = UNSET
    http_max_initial_line_length: int | Unset = UNSET
    index_patterns: (
        list[DatabaseServicePropertiesOpensearchGlobPatternAndNumberOfIndexesMatchingThatPatternToBeKept] | Unset
    ) = UNSET
    index_rollup: DatabaseServicePropertiesOpensearchIndexRollup | Unset = UNSET
    index_template: DatabaseServicePropertiesOpensearchIndexTemplate | Unset = UNSET
    indices_fielddata_cache_size: int | None | Unset = UNSET
    indices_memory_index_buffer_size: int | Unset = UNSET
    indices_memory_max_index_buffer_size: int | Unset = UNSET
    indices_memory_min_index_buffer_size: int | Unset = UNSET
    indices_queries_cache_size: int | Unset = UNSET
    indices_query_bool_max_clause_count: int | Unset = UNSET
    indices_recovery_max_bytes_per_sec: int | Unset = UNSET
    indices_recovery_max_concurrent_file_chunks: int | Unset = UNSET
    ip_filter: list[str] | Unset = UNSET
    ism_enabled: bool | Unset = UNSET
    ism_history_enabled: bool | Unset = UNSET
    ism_history_max_age: int | Unset = UNSET
    ism_history_max_docs: int | Unset = UNSET
    ism_history_rollover_check_period: int | Unset = UNSET
    ism_history_rollover_retention_period: int | Unset = UNSET
    jwt: DatabaseServicePropertiesOpensearchJwt | Unset = UNSET
    keep_index_refresh_interval: bool | Unset = UNSET
    knn_memory_circuit_breaker_enabled: bool | Unset = UNSET
    knn_memory_circuit_breaker_limit: int | Unset = UNSET
    ml_commons_model_access_control_enabled: bool | Unset = UNSET
    ml_commons_native_memory_threshold: int | Unset = UNSET
    ml_commons_only_run_on_ml_node: bool | Unset = UNSET
    node_search_cache_size: None | str | Unset = UNSET
    openid: DatabaseServicePropertiesOpensearchOpenid | Unset = UNSET
    opensearch_dashboards: DatabaseServicePropertiesOpensearchOpensearchDashboards | Unset = UNSET
    override_main_response_version: bool | Unset = UNSET
    plugins_alerting_filter_by_backend_roles: bool | Unset = UNSET
    public_access: bool | Unset = UNSET
    public_access_prometheus: bool | Unset = UNSET
    reindex_remote_whitelist: list[None | str] | None | Unset = UNSET
    remote_store: DatabaseServicePropertiesOpensearchRemoteStore | Unset = UNSET
    saml: DatabaseServicePropertiesOpensearchSaml | Unset = UNSET
    script_max_compilations_rate: str | Unset = UNSET
    search_backpressure: DatabaseServicePropertiesOpensearchSearchBackpressure | Unset = UNSET
    search_insights_top_queries: DatabaseServicePropertiesOpensearchSearchInsightsTopQueries | Unset = UNSET
    search_max_buckets: int | None | Unset = UNSET
    segrep: DatabaseServicePropertiesOpensearchSegrep | Unset = UNSET
    service_log: bool | None | Unset = UNSET
    shard_indexing_pressure: DatabaseServicePropertiesOpensearchShardIndexingPressure | Unset = UNSET
    thread_pool_analyze_queue_size: int | Unset = UNSET
    thread_pool_analyze_size: int | Unset = UNSET
    thread_pool_force_merge_size: int | Unset = UNSET
    thread_pool_get_queue_size: int | Unset = UNSET
    thread_pool_get_size: int | Unset = UNSET
    thread_pool_search_queue_size: int | Unset = UNSET
    thread_pool_search_size: int | Unset = UNSET
    thread_pool_search_throttled_queue_size: int | Unset = UNSET
    thread_pool_search_throttled_size: int | Unset = UNSET
    thread_pool_write_queue_size: int | Unset = UNSET
    thread_pool_write_size: int | Unset = UNSET
    version: DatabaseServicePropertiesOpensearchVersion | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        action_auto_create_index_enabled = self.action_auto_create_index_enabled

        action_destructive_requires_name: bool | None | Unset
        if isinstance(self.action_destructive_requires_name, Unset):
            action_destructive_requires_name = UNSET
        else:
            action_destructive_requires_name = self.action_destructive_requires_name

        auth_failure_listeners: dict[str, Any] | Unset = UNSET
        if not isinstance(self.auth_failure_listeners, Unset):
            auth_failure_listeners = self.auth_failure_listeners.to_dict()

        automatic_utility_network_ip_filter = self.automatic_utility_network_ip_filter

        cluster_filecache_remote_data_ratio: float | int | None | Unset
        if isinstance(self.cluster_filecache_remote_data_ratio, Unset):
            cluster_filecache_remote_data_ratio = UNSET
        else:
            cluster_filecache_remote_data_ratio = self.cluster_filecache_remote_data_ratio

        cluster_max_shards_per_node = self.cluster_max_shards_per_node

        cluster_remote_store: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cluster_remote_store, Unset):
            cluster_remote_store = self.cluster_remote_store.to_dict()

        cluster_routing_allocation_balance_prefer_primary = self.cluster_routing_allocation_balance_prefer_primary

        cluster_routing_allocation_node_concurrent_recoveries = (
            self.cluster_routing_allocation_node_concurrent_recoveries
        )

        cluster_search_request_slowlog: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cluster_search_request_slowlog, Unset):
            cluster_search_request_slowlog = self.cluster_search_request_slowlog.to_dict()

        custom_domain: None | str | Unset
        if isinstance(self.custom_domain, Unset):
            custom_domain = UNSET
        else:
            custom_domain = self.custom_domain

        custom_keystores: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.custom_keystores, Unset):
            custom_keystores = []
            for custom_keystores_item_data in self.custom_keystores:
                custom_keystores_item = custom_keystores_item_data.to_dict()
                custom_keystores.append(custom_keystores_item)

        custom_repos: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.custom_repos, Unset):
            custom_repos = []
            for custom_repos_item_data in self.custom_repos:
                custom_repos_item = custom_repos_item_data.to_dict()
                custom_repos.append(custom_repos_item)

        disk_watermarks: dict[str, Any] | Unset = UNSET
        if not isinstance(self.disk_watermarks, Unset):
            disk_watermarks = self.disk_watermarks.to_dict()

        elasticsearch_version: str | Unset = UNSET
        if not isinstance(self.elasticsearch_version, Unset):
            elasticsearch_version = self.elasticsearch_version.value

        email_sender_name = self.email_sender_name

        email_sender_password = self.email_sender_password

        email_sender_username = self.email_sender_username

        enable_remote_backed_storage = self.enable_remote_backed_storage

        enable_searchable_snapshots = self.enable_searchable_snapshots

        enable_security_audit = self.enable_security_audit

        enable_snapshot_api = self.enable_snapshot_api

        http_max_content_length = self.http_max_content_length

        http_max_header_size = self.http_max_header_size

        http_max_initial_line_length = self.http_max_initial_line_length

        index_patterns: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.index_patterns, Unset):
            index_patterns = []
            for index_patterns_item_data in self.index_patterns:
                index_patterns_item = index_patterns_item_data.to_dict()
                index_patterns.append(index_patterns_item)

        index_rollup: dict[str, Any] | Unset = UNSET
        if not isinstance(self.index_rollup, Unset):
            index_rollup = self.index_rollup.to_dict()

        index_template: dict[str, Any] | Unset = UNSET
        if not isinstance(self.index_template, Unset):
            index_template = self.index_template.to_dict()

        indices_fielddata_cache_size: int | None | Unset
        if isinstance(self.indices_fielddata_cache_size, Unset):
            indices_fielddata_cache_size = UNSET
        else:
            indices_fielddata_cache_size = self.indices_fielddata_cache_size

        indices_memory_index_buffer_size = self.indices_memory_index_buffer_size

        indices_memory_max_index_buffer_size = self.indices_memory_max_index_buffer_size

        indices_memory_min_index_buffer_size = self.indices_memory_min_index_buffer_size

        indices_queries_cache_size = self.indices_queries_cache_size

        indices_query_bool_max_clause_count = self.indices_query_bool_max_clause_count

        indices_recovery_max_bytes_per_sec = self.indices_recovery_max_bytes_per_sec

        indices_recovery_max_concurrent_file_chunks = self.indices_recovery_max_concurrent_file_chunks

        ip_filter: list[str] | Unset = UNSET
        if not isinstance(self.ip_filter, Unset):
            ip_filter = self.ip_filter

        ism_enabled = self.ism_enabled

        ism_history_enabled = self.ism_history_enabled

        ism_history_max_age = self.ism_history_max_age

        ism_history_max_docs = self.ism_history_max_docs

        ism_history_rollover_check_period = self.ism_history_rollover_check_period

        ism_history_rollover_retention_period = self.ism_history_rollover_retention_period

        jwt: dict[str, Any] | Unset = UNSET
        if not isinstance(self.jwt, Unset):
            jwt = self.jwt.to_dict()

        keep_index_refresh_interval = self.keep_index_refresh_interval

        knn_memory_circuit_breaker_enabled = self.knn_memory_circuit_breaker_enabled

        knn_memory_circuit_breaker_limit = self.knn_memory_circuit_breaker_limit

        ml_commons_model_access_control_enabled = self.ml_commons_model_access_control_enabled

        ml_commons_native_memory_threshold = self.ml_commons_native_memory_threshold

        ml_commons_only_run_on_ml_node = self.ml_commons_only_run_on_ml_node

        node_search_cache_size: None | str | Unset
        if isinstance(self.node_search_cache_size, Unset):
            node_search_cache_size = UNSET
        else:
            node_search_cache_size = self.node_search_cache_size

        openid: dict[str, Any] | Unset = UNSET
        if not isinstance(self.openid, Unset):
            openid = self.openid.to_dict()

        opensearch_dashboards: dict[str, Any] | Unset = UNSET
        if not isinstance(self.opensearch_dashboards, Unset):
            opensearch_dashboards = self.opensearch_dashboards.to_dict()

        override_main_response_version = self.override_main_response_version

        plugins_alerting_filter_by_backend_roles = self.plugins_alerting_filter_by_backend_roles

        public_access = self.public_access

        public_access_prometheus = self.public_access_prometheus

        reindex_remote_whitelist: list[None | str] | None | Unset
        if isinstance(self.reindex_remote_whitelist, Unset):
            reindex_remote_whitelist = UNSET
        elif isinstance(self.reindex_remote_whitelist, list):
            reindex_remote_whitelist = []
            for reindex_remote_whitelist_type_0_item_data in self.reindex_remote_whitelist:
                reindex_remote_whitelist_type_0_item: None | str
                reindex_remote_whitelist_type_0_item = reindex_remote_whitelist_type_0_item_data
                reindex_remote_whitelist.append(reindex_remote_whitelist_type_0_item)

        else:
            reindex_remote_whitelist = self.reindex_remote_whitelist

        remote_store: dict[str, Any] | Unset = UNSET
        if not isinstance(self.remote_store, Unset):
            remote_store = self.remote_store.to_dict()

        saml: dict[str, Any] | Unset = UNSET
        if not isinstance(self.saml, Unset):
            saml = self.saml.to_dict()

        script_max_compilations_rate = self.script_max_compilations_rate

        search_backpressure: dict[str, Any] | Unset = UNSET
        if not isinstance(self.search_backpressure, Unset):
            search_backpressure = self.search_backpressure.to_dict()

        search_insights_top_queries: dict[str, Any] | Unset = UNSET
        if not isinstance(self.search_insights_top_queries, Unset):
            search_insights_top_queries = self.search_insights_top_queries.to_dict()

        search_max_buckets: int | None | Unset
        if isinstance(self.search_max_buckets, Unset):
            search_max_buckets = UNSET
        else:
            search_max_buckets = self.search_max_buckets

        segrep: dict[str, Any] | Unset = UNSET
        if not isinstance(self.segrep, Unset):
            segrep = self.segrep.to_dict()

        service_log: bool | None | Unset
        if isinstance(self.service_log, Unset):
            service_log = UNSET
        else:
            service_log = self.service_log

        shard_indexing_pressure: dict[str, Any] | Unset = UNSET
        if not isinstance(self.shard_indexing_pressure, Unset):
            shard_indexing_pressure = self.shard_indexing_pressure.to_dict()

        thread_pool_analyze_queue_size = self.thread_pool_analyze_queue_size

        thread_pool_analyze_size = self.thread_pool_analyze_size

        thread_pool_force_merge_size = self.thread_pool_force_merge_size

        thread_pool_get_queue_size = self.thread_pool_get_queue_size

        thread_pool_get_size = self.thread_pool_get_size

        thread_pool_search_queue_size = self.thread_pool_search_queue_size

        thread_pool_search_size = self.thread_pool_search_size

        thread_pool_search_throttled_queue_size = self.thread_pool_search_throttled_queue_size

        thread_pool_search_throttled_size = self.thread_pool_search_throttled_size

        thread_pool_write_queue_size = self.thread_pool_write_queue_size

        thread_pool_write_size = self.thread_pool_write_size

        version: str | Unset = UNSET
        if not isinstance(self.version, Unset):
            version = self.version.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if action_auto_create_index_enabled is not UNSET:
            field_dict["action_auto_create_index_enabled"] = action_auto_create_index_enabled
        if action_destructive_requires_name is not UNSET:
            field_dict["action_destructive_requires_name"] = action_destructive_requires_name
        if auth_failure_listeners is not UNSET:
            field_dict["auth_failure_listeners"] = auth_failure_listeners
        if automatic_utility_network_ip_filter is not UNSET:
            field_dict["automatic_utility_network_ip_filter"] = automatic_utility_network_ip_filter
        if cluster_filecache_remote_data_ratio is not UNSET:
            field_dict["cluster_filecache_remote_data_ratio"] = cluster_filecache_remote_data_ratio
        if cluster_max_shards_per_node is not UNSET:
            field_dict["cluster_max_shards_per_node"] = cluster_max_shards_per_node
        if cluster_remote_store is not UNSET:
            field_dict["cluster_remote_store"] = cluster_remote_store
        if cluster_routing_allocation_balance_prefer_primary is not UNSET:
            field_dict["cluster_routing_allocation_balance_prefer_primary"] = (
                cluster_routing_allocation_balance_prefer_primary
            )
        if cluster_routing_allocation_node_concurrent_recoveries is not UNSET:
            field_dict["cluster_routing_allocation_node_concurrent_recoveries"] = (
                cluster_routing_allocation_node_concurrent_recoveries
            )
        if cluster_search_request_slowlog is not UNSET:
            field_dict["cluster_search_request_slowlog"] = cluster_search_request_slowlog
        if custom_domain is not UNSET:
            field_dict["custom_domain"] = custom_domain
        if custom_keystores is not UNSET:
            field_dict["custom_keystores"] = custom_keystores
        if custom_repos is not UNSET:
            field_dict["custom_repos"] = custom_repos
        if disk_watermarks is not UNSET:
            field_dict["disk_watermarks"] = disk_watermarks
        if elasticsearch_version is not UNSET:
            field_dict["elasticsearch_version"] = elasticsearch_version
        if email_sender_name is not UNSET:
            field_dict["email_sender_name"] = email_sender_name
        if email_sender_password is not UNSET:
            field_dict["email_sender_password"] = email_sender_password
        if email_sender_username is not UNSET:
            field_dict["email_sender_username"] = email_sender_username
        if enable_remote_backed_storage is not UNSET:
            field_dict["enable_remote_backed_storage"] = enable_remote_backed_storage
        if enable_searchable_snapshots is not UNSET:
            field_dict["enable_searchable_snapshots"] = enable_searchable_snapshots
        if enable_security_audit is not UNSET:
            field_dict["enable_security_audit"] = enable_security_audit
        if enable_snapshot_api is not UNSET:
            field_dict["enable_snapshot_api"] = enable_snapshot_api
        if http_max_content_length is not UNSET:
            field_dict["http_max_content_length"] = http_max_content_length
        if http_max_header_size is not UNSET:
            field_dict["http_max_header_size"] = http_max_header_size
        if http_max_initial_line_length is not UNSET:
            field_dict["http_max_initial_line_length"] = http_max_initial_line_length
        if index_patterns is not UNSET:
            field_dict["index_patterns"] = index_patterns
        if index_rollup is not UNSET:
            field_dict["index_rollup"] = index_rollup
        if index_template is not UNSET:
            field_dict["index_template"] = index_template
        if indices_fielddata_cache_size is not UNSET:
            field_dict["indices_fielddata_cache_size"] = indices_fielddata_cache_size
        if indices_memory_index_buffer_size is not UNSET:
            field_dict["indices_memory_index_buffer_size"] = indices_memory_index_buffer_size
        if indices_memory_max_index_buffer_size is not UNSET:
            field_dict["indices_memory_max_index_buffer_size"] = indices_memory_max_index_buffer_size
        if indices_memory_min_index_buffer_size is not UNSET:
            field_dict["indices_memory_min_index_buffer_size"] = indices_memory_min_index_buffer_size
        if indices_queries_cache_size is not UNSET:
            field_dict["indices_queries_cache_size"] = indices_queries_cache_size
        if indices_query_bool_max_clause_count is not UNSET:
            field_dict["indices_query_bool_max_clause_count"] = indices_query_bool_max_clause_count
        if indices_recovery_max_bytes_per_sec is not UNSET:
            field_dict["indices_recovery_max_bytes_per_sec"] = indices_recovery_max_bytes_per_sec
        if indices_recovery_max_concurrent_file_chunks is not UNSET:
            field_dict["indices_recovery_max_concurrent_file_chunks"] = indices_recovery_max_concurrent_file_chunks
        if ip_filter is not UNSET:
            field_dict["ip_filter"] = ip_filter
        if ism_enabled is not UNSET:
            field_dict["ism_enabled"] = ism_enabled
        if ism_history_enabled is not UNSET:
            field_dict["ism_history_enabled"] = ism_history_enabled
        if ism_history_max_age is not UNSET:
            field_dict["ism_history_max_age"] = ism_history_max_age
        if ism_history_max_docs is not UNSET:
            field_dict["ism_history_max_docs"] = ism_history_max_docs
        if ism_history_rollover_check_period is not UNSET:
            field_dict["ism_history_rollover_check_period"] = ism_history_rollover_check_period
        if ism_history_rollover_retention_period is not UNSET:
            field_dict["ism_history_rollover_retention_period"] = ism_history_rollover_retention_period
        if jwt is not UNSET:
            field_dict["jwt"] = jwt
        if keep_index_refresh_interval is not UNSET:
            field_dict["keep_index_refresh_interval"] = keep_index_refresh_interval
        if knn_memory_circuit_breaker_enabled is not UNSET:
            field_dict["knn_memory_circuit_breaker_enabled"] = knn_memory_circuit_breaker_enabled
        if knn_memory_circuit_breaker_limit is not UNSET:
            field_dict["knn_memory_circuit_breaker_limit"] = knn_memory_circuit_breaker_limit
        if ml_commons_model_access_control_enabled is not UNSET:
            field_dict["ml_commons_model_access_control_enabled"] = ml_commons_model_access_control_enabled
        if ml_commons_native_memory_threshold is not UNSET:
            field_dict["ml_commons_native_memory_threshold"] = ml_commons_native_memory_threshold
        if ml_commons_only_run_on_ml_node is not UNSET:
            field_dict["ml_commons_only_run_on_ml_node"] = ml_commons_only_run_on_ml_node
        if node_search_cache_size is not UNSET:
            field_dict["node_search_cache_size"] = node_search_cache_size
        if openid is not UNSET:
            field_dict["openid"] = openid
        if opensearch_dashboards is not UNSET:
            field_dict["opensearch_dashboards"] = opensearch_dashboards
        if override_main_response_version is not UNSET:
            field_dict["override_main_response_version"] = override_main_response_version
        if plugins_alerting_filter_by_backend_roles is not UNSET:
            field_dict["plugins_alerting_filter_by_backend_roles"] = plugins_alerting_filter_by_backend_roles
        if public_access is not UNSET:
            field_dict["public_access"] = public_access
        if public_access_prometheus is not UNSET:
            field_dict["public_access_prometheus"] = public_access_prometheus
        if reindex_remote_whitelist is not UNSET:
            field_dict["reindex_remote_whitelist"] = reindex_remote_whitelist
        if remote_store is not UNSET:
            field_dict["remote_store"] = remote_store
        if saml is not UNSET:
            field_dict["saml"] = saml
        if script_max_compilations_rate is not UNSET:
            field_dict["script_max_compilations_rate"] = script_max_compilations_rate
        if search_backpressure is not UNSET:
            field_dict["search_backpressure"] = search_backpressure
        if search_insights_top_queries is not UNSET:
            field_dict["search_insights_top_queries"] = search_insights_top_queries
        if search_max_buckets is not UNSET:
            field_dict["search_max_buckets"] = search_max_buckets
        if segrep is not UNSET:
            field_dict["segrep"] = segrep
        if service_log is not UNSET:
            field_dict["service_log"] = service_log
        if shard_indexing_pressure is not UNSET:
            field_dict["shard_indexing_pressure"] = shard_indexing_pressure
        if thread_pool_analyze_queue_size is not UNSET:
            field_dict["thread_pool_analyze_queue_size"] = thread_pool_analyze_queue_size
        if thread_pool_analyze_size is not UNSET:
            field_dict["thread_pool_analyze_size"] = thread_pool_analyze_size
        if thread_pool_force_merge_size is not UNSET:
            field_dict["thread_pool_force_merge_size"] = thread_pool_force_merge_size
        if thread_pool_get_queue_size is not UNSET:
            field_dict["thread_pool_get_queue_size"] = thread_pool_get_queue_size
        if thread_pool_get_size is not UNSET:
            field_dict["thread_pool_get_size"] = thread_pool_get_size
        if thread_pool_search_queue_size is not UNSET:
            field_dict["thread_pool_search_queue_size"] = thread_pool_search_queue_size
        if thread_pool_search_size is not UNSET:
            field_dict["thread_pool_search_size"] = thread_pool_search_size
        if thread_pool_search_throttled_queue_size is not UNSET:
            field_dict["thread_pool_search_throttled_queue_size"] = thread_pool_search_throttled_queue_size
        if thread_pool_search_throttled_size is not UNSET:
            field_dict["thread_pool_search_throttled_size"] = thread_pool_search_throttled_size
        if thread_pool_write_queue_size is not UNSET:
            field_dict["thread_pool_write_queue_size"] = thread_pool_write_queue_size
        if thread_pool_write_size is not UNSET:
            field_dict["thread_pool_write_size"] = thread_pool_write_size
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_service_properties_opensearch_auth_failure_listeners import (
            DatabaseServicePropertiesOpensearchAuthFailureListeners,  # noqa: PLC0415
        )
        from ..models.database_service_properties_opensearch_cluster_remote_store import (
            DatabaseServicePropertiesOpensearchClusterRemoteStore,  # noqa: PLC0415
        )
        from ..models.database_service_properties_opensearch_cluster_search_request_slowlog import (
            DatabaseServicePropertiesOpensearchClusterSearchRequestSlowlog,  # noqa: PLC0415
        )
        from ..models.database_service_properties_opensearch_custom_keystores_item import (
            DatabaseServicePropertiesOpensearchCustomKeystoresItem,  # noqa: PLC0415
        )
        from ..models.database_service_properties_opensearch_custom_repos_item import (
            DatabaseServicePropertiesOpensearchCustomReposItem,  # noqa: PLC0415
        )
        from ..models.database_service_properties_opensearch_disk_watermarks import (
            DatabaseServicePropertiesOpensearchDiskWatermarks,  # noqa: PLC0415
        )
        from ..models.database_service_properties_opensearch_glob_pattern_and_number_of_indexes_matching_that_pattern_to_be_kept import (
            DatabaseServicePropertiesOpensearchGlobPatternAndNumberOfIndexesMatchingThatPatternToBeKept,  # noqa: PLC0415
        )
        from ..models.database_service_properties_opensearch_index_rollup import (
            DatabaseServicePropertiesOpensearchIndexRollup,  # noqa: PLC0415
        )
        from ..models.database_service_properties_opensearch_index_template import (
            DatabaseServicePropertiesOpensearchIndexTemplate,  # noqa: PLC0415
        )
        from ..models.database_service_properties_opensearch_jwt import (
            DatabaseServicePropertiesOpensearchJwt,  # noqa: PLC0415
        )
        from ..models.database_service_properties_opensearch_openid import (
            DatabaseServicePropertiesOpensearchOpenid,  # noqa: PLC0415
        )
        from ..models.database_service_properties_opensearch_opensearch_dashboards import (
            DatabaseServicePropertiesOpensearchOpensearchDashboards,  # noqa: PLC0415
        )
        from ..models.database_service_properties_opensearch_remote_store import (
            DatabaseServicePropertiesOpensearchRemoteStore,  # noqa: PLC0415
        )
        from ..models.database_service_properties_opensearch_saml import (
            DatabaseServicePropertiesOpensearchSaml,  # noqa: PLC0415
        )
        from ..models.database_service_properties_opensearch_search_backpressure import (
            DatabaseServicePropertiesOpensearchSearchBackpressure,  # noqa: PLC0415
        )
        from ..models.database_service_properties_opensearch_search_insights_top_queries import (
            DatabaseServicePropertiesOpensearchSearchInsightsTopQueries,  # noqa: PLC0415
        )
        from ..models.database_service_properties_opensearch_segrep import (
            DatabaseServicePropertiesOpensearchSegrep,  # noqa: PLC0415
        )
        from ..models.database_service_properties_opensearch_shard_indexing_pressure import (
            DatabaseServicePropertiesOpensearchShardIndexingPressure,  # noqa: PLC0415
        )

        d = dict(src_dict)
        action_auto_create_index_enabled = d.pop("action_auto_create_index_enabled", UNSET)

        def _parse_action_destructive_requires_name(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        action_destructive_requires_name = _parse_action_destructive_requires_name(
            d.pop("action_destructive_requires_name", UNSET)
        )

        _auth_failure_listeners = d.pop("auth_failure_listeners", UNSET)
        auth_failure_listeners: DatabaseServicePropertiesOpensearchAuthFailureListeners | Unset
        if isinstance(_auth_failure_listeners, Unset):
            auth_failure_listeners = UNSET
        else:
            auth_failure_listeners = DatabaseServicePropertiesOpensearchAuthFailureListeners.from_dict(
                _auth_failure_listeners
            )

        automatic_utility_network_ip_filter = d.pop("automatic_utility_network_ip_filter", UNSET)

        def _parse_cluster_filecache_remote_data_ratio(data: object) -> float | int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | int | None | Unset, data)

        cluster_filecache_remote_data_ratio = _parse_cluster_filecache_remote_data_ratio(
            d.pop("cluster_filecache_remote_data_ratio", UNSET)
        )

        cluster_max_shards_per_node = d.pop("cluster_max_shards_per_node", UNSET)

        _cluster_remote_store = d.pop("cluster_remote_store", UNSET)
        cluster_remote_store: DatabaseServicePropertiesOpensearchClusterRemoteStore | Unset
        if isinstance(_cluster_remote_store, Unset):
            cluster_remote_store = UNSET
        else:
            cluster_remote_store = DatabaseServicePropertiesOpensearchClusterRemoteStore.from_dict(
                _cluster_remote_store
            )

        cluster_routing_allocation_balance_prefer_primary = d.pop(
            "cluster_routing_allocation_balance_prefer_primary", UNSET
        )

        cluster_routing_allocation_node_concurrent_recoveries = d.pop(
            "cluster_routing_allocation_node_concurrent_recoveries", UNSET
        )

        _cluster_search_request_slowlog = d.pop("cluster_search_request_slowlog", UNSET)
        cluster_search_request_slowlog: DatabaseServicePropertiesOpensearchClusterSearchRequestSlowlog | Unset
        if isinstance(_cluster_search_request_slowlog, Unset):
            cluster_search_request_slowlog = UNSET
        else:
            cluster_search_request_slowlog = DatabaseServicePropertiesOpensearchClusterSearchRequestSlowlog.from_dict(
                _cluster_search_request_slowlog
            )

        def _parse_custom_domain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        custom_domain = _parse_custom_domain(d.pop("custom_domain", UNSET))

        _custom_keystores = d.pop("custom_keystores", UNSET)
        custom_keystores: list[DatabaseServicePropertiesOpensearchCustomKeystoresItem] | Unset = UNSET
        if _custom_keystores is not UNSET:
            custom_keystores = []
            for custom_keystores_item_data in _custom_keystores:
                custom_keystores_item = DatabaseServicePropertiesOpensearchCustomKeystoresItem.from_dict(
                    custom_keystores_item_data
                )

                custom_keystores.append(custom_keystores_item)

        _custom_repos = d.pop("custom_repos", UNSET)
        custom_repos: list[DatabaseServicePropertiesOpensearchCustomReposItem] | Unset = UNSET
        if _custom_repos is not UNSET:
            custom_repos = []
            for custom_repos_item_data in _custom_repos:
                custom_repos_item = DatabaseServicePropertiesOpensearchCustomReposItem.from_dict(custom_repos_item_data)

                custom_repos.append(custom_repos_item)

        _disk_watermarks = d.pop("disk_watermarks", UNSET)
        disk_watermarks: DatabaseServicePropertiesOpensearchDiskWatermarks | Unset
        if isinstance(_disk_watermarks, Unset):
            disk_watermarks = UNSET
        else:
            disk_watermarks = DatabaseServicePropertiesOpensearchDiskWatermarks.from_dict(_disk_watermarks)

        _elasticsearch_version = d.pop("elasticsearch_version", UNSET)
        elasticsearch_version: DatabaseServicePropertiesOpensearchElasticsearchVersion | Unset
        if isinstance(_elasticsearch_version, Unset):
            elasticsearch_version = UNSET
        else:
            elasticsearch_version = DatabaseServicePropertiesOpensearchElasticsearchVersion(_elasticsearch_version)

        email_sender_name = d.pop("email_sender_name", UNSET)

        email_sender_password = d.pop("email_sender_password", UNSET)

        email_sender_username = d.pop("email_sender_username", UNSET)

        enable_remote_backed_storage = d.pop("enable_remote_backed_storage", UNSET)

        enable_searchable_snapshots = d.pop("enable_searchable_snapshots", UNSET)

        enable_security_audit = d.pop("enable_security_audit", UNSET)

        enable_snapshot_api = d.pop("enable_snapshot_api", UNSET)

        http_max_content_length = d.pop("http_max_content_length", UNSET)

        http_max_header_size = d.pop("http_max_header_size", UNSET)

        http_max_initial_line_length = d.pop("http_max_initial_line_length", UNSET)

        _index_patterns = d.pop("index_patterns", UNSET)
        index_patterns: (
            list[DatabaseServicePropertiesOpensearchGlobPatternAndNumberOfIndexesMatchingThatPatternToBeKept] | Unset
        ) = UNSET
        if _index_patterns is not UNSET:
            index_patterns = []
            for index_patterns_item_data in _index_patterns:
                index_patterns_item = DatabaseServicePropertiesOpensearchGlobPatternAndNumberOfIndexesMatchingThatPatternToBeKept.from_dict(
                    index_patterns_item_data
                )

                index_patterns.append(index_patterns_item)

        _index_rollup = d.pop("index_rollup", UNSET)
        index_rollup: DatabaseServicePropertiesOpensearchIndexRollup | Unset
        if isinstance(_index_rollup, Unset):
            index_rollup = UNSET
        else:
            index_rollup = DatabaseServicePropertiesOpensearchIndexRollup.from_dict(_index_rollup)

        _index_template = d.pop("index_template", UNSET)
        index_template: DatabaseServicePropertiesOpensearchIndexTemplate | Unset
        if isinstance(_index_template, Unset):
            index_template = UNSET
        else:
            index_template = DatabaseServicePropertiesOpensearchIndexTemplate.from_dict(_index_template)

        def _parse_indices_fielddata_cache_size(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        indices_fielddata_cache_size = _parse_indices_fielddata_cache_size(d.pop("indices_fielddata_cache_size", UNSET))

        indices_memory_index_buffer_size = d.pop("indices_memory_index_buffer_size", UNSET)

        indices_memory_max_index_buffer_size = d.pop("indices_memory_max_index_buffer_size", UNSET)

        indices_memory_min_index_buffer_size = d.pop("indices_memory_min_index_buffer_size", UNSET)

        indices_queries_cache_size = d.pop("indices_queries_cache_size", UNSET)

        indices_query_bool_max_clause_count = d.pop("indices_query_bool_max_clause_count", UNSET)

        indices_recovery_max_bytes_per_sec = d.pop("indices_recovery_max_bytes_per_sec", UNSET)

        indices_recovery_max_concurrent_file_chunks = d.pop("indices_recovery_max_concurrent_file_chunks", UNSET)

        ip_filter = cast(list[str], d.pop("ip_filter", UNSET))

        ism_enabled = d.pop("ism_enabled", UNSET)

        ism_history_enabled = d.pop("ism_history_enabled", UNSET)

        ism_history_max_age = d.pop("ism_history_max_age", UNSET)

        ism_history_max_docs = d.pop("ism_history_max_docs", UNSET)

        ism_history_rollover_check_period = d.pop("ism_history_rollover_check_period", UNSET)

        ism_history_rollover_retention_period = d.pop("ism_history_rollover_retention_period", UNSET)

        _jwt = d.pop("jwt", UNSET)
        jwt: DatabaseServicePropertiesOpensearchJwt | Unset
        if isinstance(_jwt, Unset):
            jwt = UNSET
        else:
            jwt = DatabaseServicePropertiesOpensearchJwt.from_dict(_jwt)

        keep_index_refresh_interval = d.pop("keep_index_refresh_interval", UNSET)

        knn_memory_circuit_breaker_enabled = d.pop("knn_memory_circuit_breaker_enabled", UNSET)

        knn_memory_circuit_breaker_limit = d.pop("knn_memory_circuit_breaker_limit", UNSET)

        ml_commons_model_access_control_enabled = d.pop("ml_commons_model_access_control_enabled", UNSET)

        ml_commons_native_memory_threshold = d.pop("ml_commons_native_memory_threshold", UNSET)

        ml_commons_only_run_on_ml_node = d.pop("ml_commons_only_run_on_ml_node", UNSET)

        def _parse_node_search_cache_size(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        node_search_cache_size = _parse_node_search_cache_size(d.pop("node_search_cache_size", UNSET))

        _openid = d.pop("openid", UNSET)
        openid: DatabaseServicePropertiesOpensearchOpenid | Unset
        if isinstance(_openid, Unset):
            openid = UNSET
        else:
            openid = DatabaseServicePropertiesOpensearchOpenid.from_dict(_openid)

        _opensearch_dashboards = d.pop("opensearch_dashboards", UNSET)
        opensearch_dashboards: DatabaseServicePropertiesOpensearchOpensearchDashboards | Unset
        if isinstance(_opensearch_dashboards, Unset):
            opensearch_dashboards = UNSET
        else:
            opensearch_dashboards = DatabaseServicePropertiesOpensearchOpensearchDashboards.from_dict(
                _opensearch_dashboards
            )

        override_main_response_version = d.pop("override_main_response_version", UNSET)

        plugins_alerting_filter_by_backend_roles = d.pop("plugins_alerting_filter_by_backend_roles", UNSET)

        public_access = d.pop("public_access", UNSET)

        public_access_prometheus = d.pop("public_access_prometheus", UNSET)

        def _parse_reindex_remote_whitelist(data: object) -> list[None | str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                reindex_remote_whitelist_type_0 = []
                _reindex_remote_whitelist_type_0 = data
                for reindex_remote_whitelist_type_0_item_data in _reindex_remote_whitelist_type_0:

                    def _parse_reindex_remote_whitelist_type_0_item(data: object) -> None | str:
                        if data is None:
                            return data
                        return cast(None | str, data)

                    reindex_remote_whitelist_type_0_item = _parse_reindex_remote_whitelist_type_0_item(
                        reindex_remote_whitelist_type_0_item_data
                    )

                    reindex_remote_whitelist_type_0.append(reindex_remote_whitelist_type_0_item)

                return reindex_remote_whitelist_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[None | str] | None | Unset, data)

        reindex_remote_whitelist = _parse_reindex_remote_whitelist(d.pop("reindex_remote_whitelist", UNSET))

        _remote_store = d.pop("remote_store", UNSET)
        remote_store: DatabaseServicePropertiesOpensearchRemoteStore | Unset
        if isinstance(_remote_store, Unset):
            remote_store = UNSET
        else:
            remote_store = DatabaseServicePropertiesOpensearchRemoteStore.from_dict(_remote_store)

        _saml = d.pop("saml", UNSET)
        saml: DatabaseServicePropertiesOpensearchSaml | Unset
        if isinstance(_saml, Unset):
            saml = UNSET
        else:
            saml = DatabaseServicePropertiesOpensearchSaml.from_dict(_saml)

        script_max_compilations_rate = d.pop("script_max_compilations_rate", UNSET)

        _search_backpressure = d.pop("search_backpressure", UNSET)
        search_backpressure: DatabaseServicePropertiesOpensearchSearchBackpressure | Unset
        if isinstance(_search_backpressure, Unset):
            search_backpressure = UNSET
        else:
            search_backpressure = DatabaseServicePropertiesOpensearchSearchBackpressure.from_dict(_search_backpressure)

        _search_insights_top_queries = d.pop("search_insights_top_queries", UNSET)
        search_insights_top_queries: DatabaseServicePropertiesOpensearchSearchInsightsTopQueries | Unset
        if isinstance(_search_insights_top_queries, Unset):
            search_insights_top_queries = UNSET
        else:
            search_insights_top_queries = DatabaseServicePropertiesOpensearchSearchInsightsTopQueries.from_dict(
                _search_insights_top_queries
            )

        def _parse_search_max_buckets(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        search_max_buckets = _parse_search_max_buckets(d.pop("search_max_buckets", UNSET))

        _segrep = d.pop("segrep", UNSET)
        segrep: DatabaseServicePropertiesOpensearchSegrep | Unset
        if isinstance(_segrep, Unset):
            segrep = UNSET
        else:
            segrep = DatabaseServicePropertiesOpensearchSegrep.from_dict(_segrep)

        def _parse_service_log(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        service_log = _parse_service_log(d.pop("service_log", UNSET))

        _shard_indexing_pressure = d.pop("shard_indexing_pressure", UNSET)
        shard_indexing_pressure: DatabaseServicePropertiesOpensearchShardIndexingPressure | Unset
        if isinstance(_shard_indexing_pressure, Unset):
            shard_indexing_pressure = UNSET
        else:
            shard_indexing_pressure = DatabaseServicePropertiesOpensearchShardIndexingPressure.from_dict(
                _shard_indexing_pressure
            )

        thread_pool_analyze_queue_size = d.pop("thread_pool_analyze_queue_size", UNSET)

        thread_pool_analyze_size = d.pop("thread_pool_analyze_size", UNSET)

        thread_pool_force_merge_size = d.pop("thread_pool_force_merge_size", UNSET)

        thread_pool_get_queue_size = d.pop("thread_pool_get_queue_size", UNSET)

        thread_pool_get_size = d.pop("thread_pool_get_size", UNSET)

        thread_pool_search_queue_size = d.pop("thread_pool_search_queue_size", UNSET)

        thread_pool_search_size = d.pop("thread_pool_search_size", UNSET)

        thread_pool_search_throttled_queue_size = d.pop("thread_pool_search_throttled_queue_size", UNSET)

        thread_pool_search_throttled_size = d.pop("thread_pool_search_throttled_size", UNSET)

        thread_pool_write_queue_size = d.pop("thread_pool_write_queue_size", UNSET)

        thread_pool_write_size = d.pop("thread_pool_write_size", UNSET)

        _version = d.pop("version", UNSET)
        version: DatabaseServicePropertiesOpensearchVersion | Unset
        if isinstance(_version, Unset):
            version = UNSET
        else:
            version = DatabaseServicePropertiesOpensearchVersion(_version)

        database_service_properties_opensearch = cls(
            action_auto_create_index_enabled=action_auto_create_index_enabled,
            action_destructive_requires_name=action_destructive_requires_name,
            auth_failure_listeners=auth_failure_listeners,
            automatic_utility_network_ip_filter=automatic_utility_network_ip_filter,
            cluster_filecache_remote_data_ratio=cluster_filecache_remote_data_ratio,
            cluster_max_shards_per_node=cluster_max_shards_per_node,
            cluster_remote_store=cluster_remote_store,
            cluster_routing_allocation_balance_prefer_primary=cluster_routing_allocation_balance_prefer_primary,
            cluster_routing_allocation_node_concurrent_recoveries=cluster_routing_allocation_node_concurrent_recoveries,
            cluster_search_request_slowlog=cluster_search_request_slowlog,
            custom_domain=custom_domain,
            custom_keystores=custom_keystores,
            custom_repos=custom_repos,
            disk_watermarks=disk_watermarks,
            elasticsearch_version=elasticsearch_version,
            email_sender_name=email_sender_name,
            email_sender_password=email_sender_password,
            email_sender_username=email_sender_username,
            enable_remote_backed_storage=enable_remote_backed_storage,
            enable_searchable_snapshots=enable_searchable_snapshots,
            enable_security_audit=enable_security_audit,
            enable_snapshot_api=enable_snapshot_api,
            http_max_content_length=http_max_content_length,
            http_max_header_size=http_max_header_size,
            http_max_initial_line_length=http_max_initial_line_length,
            index_patterns=index_patterns,
            index_rollup=index_rollup,
            index_template=index_template,
            indices_fielddata_cache_size=indices_fielddata_cache_size,
            indices_memory_index_buffer_size=indices_memory_index_buffer_size,
            indices_memory_max_index_buffer_size=indices_memory_max_index_buffer_size,
            indices_memory_min_index_buffer_size=indices_memory_min_index_buffer_size,
            indices_queries_cache_size=indices_queries_cache_size,
            indices_query_bool_max_clause_count=indices_query_bool_max_clause_count,
            indices_recovery_max_bytes_per_sec=indices_recovery_max_bytes_per_sec,
            indices_recovery_max_concurrent_file_chunks=indices_recovery_max_concurrent_file_chunks,
            ip_filter=ip_filter,
            ism_enabled=ism_enabled,
            ism_history_enabled=ism_history_enabled,
            ism_history_max_age=ism_history_max_age,
            ism_history_max_docs=ism_history_max_docs,
            ism_history_rollover_check_period=ism_history_rollover_check_period,
            ism_history_rollover_retention_period=ism_history_rollover_retention_period,
            jwt=jwt,
            keep_index_refresh_interval=keep_index_refresh_interval,
            knn_memory_circuit_breaker_enabled=knn_memory_circuit_breaker_enabled,
            knn_memory_circuit_breaker_limit=knn_memory_circuit_breaker_limit,
            ml_commons_model_access_control_enabled=ml_commons_model_access_control_enabled,
            ml_commons_native_memory_threshold=ml_commons_native_memory_threshold,
            ml_commons_only_run_on_ml_node=ml_commons_only_run_on_ml_node,
            node_search_cache_size=node_search_cache_size,
            openid=openid,
            opensearch_dashboards=opensearch_dashboards,
            override_main_response_version=override_main_response_version,
            plugins_alerting_filter_by_backend_roles=plugins_alerting_filter_by_backend_roles,
            public_access=public_access,
            public_access_prometheus=public_access_prometheus,
            reindex_remote_whitelist=reindex_remote_whitelist,
            remote_store=remote_store,
            saml=saml,
            script_max_compilations_rate=script_max_compilations_rate,
            search_backpressure=search_backpressure,
            search_insights_top_queries=search_insights_top_queries,
            search_max_buckets=search_max_buckets,
            segrep=segrep,
            service_log=service_log,
            shard_indexing_pressure=shard_indexing_pressure,
            thread_pool_analyze_queue_size=thread_pool_analyze_queue_size,
            thread_pool_analyze_size=thread_pool_analyze_size,
            thread_pool_force_merge_size=thread_pool_force_merge_size,
            thread_pool_get_queue_size=thread_pool_get_queue_size,
            thread_pool_get_size=thread_pool_get_size,
            thread_pool_search_queue_size=thread_pool_search_queue_size,
            thread_pool_search_size=thread_pool_search_size,
            thread_pool_search_throttled_queue_size=thread_pool_search_throttled_queue_size,
            thread_pool_search_throttled_size=thread_pool_search_throttled_size,
            thread_pool_write_queue_size=thread_pool_write_queue_size,
            thread_pool_write_size=thread_pool_write_size,
            version=version,
        )

        return database_service_properties_opensearch
