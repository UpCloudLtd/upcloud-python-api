from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseServicePropertiesOpensearchIndexRollup")


@_attrs_define
class DatabaseServicePropertiesOpensearchIndexRollup:
    """
    Attributes:
        rollup_dashboards_enabled (bool | Unset): Whether rollups are enabled in OpenSearch Dashboards. Defaults to
            true.
        rollup_enabled (bool | Unset): Whether the rollup plugin is enabled. Defaults to true.
        rollup_search_backoff_count (int | Unset): How many retries the plugin should attempt for failed rollup jobs.
            Defaults to 5.
        rollup_search_backoff_millis (int | Unset): The backoff time between retries for failed rollup jobs. Defaults to
            1000ms.
        rollup_search_search_all_jobs (bool | Unset): Whether OpenSearch should return all jobs that match all specified
            search terms. If disabled, OpenSearch returns just one, as opposed to all, of the jobs that matches the search
            terms. Defaults to false.
    """

    rollup_dashboards_enabled: bool | Unset = UNSET
    rollup_enabled: bool | Unset = UNSET
    rollup_search_backoff_count: int | Unset = UNSET
    rollup_search_backoff_millis: int | Unset = UNSET
    rollup_search_search_all_jobs: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        rollup_dashboards_enabled = self.rollup_dashboards_enabled

        rollup_enabled = self.rollup_enabled

        rollup_search_backoff_count = self.rollup_search_backoff_count

        rollup_search_backoff_millis = self.rollup_search_backoff_millis

        rollup_search_search_all_jobs = self.rollup_search_search_all_jobs

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if rollup_dashboards_enabled is not UNSET:
            field_dict["rollup_dashboards_enabled"] = rollup_dashboards_enabled
        if rollup_enabled is not UNSET:
            field_dict["rollup_enabled"] = rollup_enabled
        if rollup_search_backoff_count is not UNSET:
            field_dict["rollup_search_backoff_count"] = rollup_search_backoff_count
        if rollup_search_backoff_millis is not UNSET:
            field_dict["rollup_search_backoff_millis"] = rollup_search_backoff_millis
        if rollup_search_search_all_jobs is not UNSET:
            field_dict["rollup_search_search_all_jobs"] = rollup_search_search_all_jobs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rollup_dashboards_enabled = d.pop("rollup_dashboards_enabled", UNSET)

        rollup_enabled = d.pop("rollup_enabled", UNSET)

        rollup_search_backoff_count = d.pop("rollup_search_backoff_count", UNSET)

        rollup_search_backoff_millis = d.pop("rollup_search_backoff_millis", UNSET)

        rollup_search_search_all_jobs = d.pop("rollup_search_search_all_jobs", UNSET)

        database_service_properties_opensearch_index_rollup = cls(
            rollup_dashboards_enabled=rollup_dashboards_enabled,
            rollup_enabled=rollup_enabled,
            rollup_search_backoff_count=rollup_search_backoff_count,
            rollup_search_backoff_millis=rollup_search_backoff_millis,
            rollup_search_search_all_jobs=rollup_search_search_all_jobs,
        )

        return database_service_properties_opensearch_index_rollup
