from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseQueryStatisticsMysqlResponse")


@_attrs_define
class DatabaseQueryStatisticsMysqlResponse:
    """Schema for MySQL query statistics response.

    Attributes:
        avg_timer_wait (int | Unset): Average wait time for the query. Example: 12345.
        count_star (int | Unset): Total number of times the query was executed. Example: 100.
        digest (str | Unset): Query digest hash. Example: abc123def456.
        digest_text (str | Unset): Normalized query text. Example: SELECT * FROM users WHERE id = ?.
        first_seen (datetime.datetime | Unset): Timestamp when the query was first seen. Example: 2024-06-01T12:00:00Z.
        last_seen (datetime.datetime | Unset): Timestamp when the query was last seen. Example: 2024-06-10T15:30:00Z.
        max_timer_wait (int | Unset): Maximum wait time for the query. Example: 54321.
        min_timer_wait (int | Unset): Minimum wait time for the query. Example: 100.
        quantile_95 (int | Unset): 95th percentile wait time. Example: 20000.
        quantile_99 (int | Unset): 99th percentile wait time. Example: 30000.
        quantile_999 (int | Unset): 99.9th percentile wait time. Example: 40000.
        query_sample_seen (datetime.datetime | Unset): Timestamp when the sample query was seen. Example:
            2024-06-05T10:00:00Z.
        query_sample_text (str | Unset): Sample query text. Example: SELECT * FROM users WHERE id = 1.
        query_sample_timer_wait (int | Unset): Wait time for the sample query. Example: 15000.
        schema_name (str | Unset): Name of the database schema. Example: my_database.
        sum_created_tmp_disk_tables (int | Unset): Total number of temporary disk tables created. Example: 2.
        sum_created_tmp_tables (int | Unset): Total number of temporary tables created. Example: 5.
        sum_errors (int | Unset): Total number of errors encountered. Example: 0.
        sum_lock_time (int | Unset): Total lock time for the query. Example: 1000.
        sum_no_good_index_used (int | Unset): Total number of times no good index was used. Example: 1.
        sum_no_index_used (int | Unset): Total number of times no index was used. Example: 3.
        sum_rows_affected (int | Unset): Total number of rows affected. Example: 10.
        sum_rows_examined (int | Unset): Total number of rows examined. Example: 1000.
        sum_rows_sent (int | Unset): Total number of rows sent. Example: 500.
        sum_select_full_join (int | Unset): Total number of full joins performed. Example: 0.
        sum_select_full_range_join (int | Unset): Total number of full range joins performed. Example: 0.
        sum_select_range (int | Unset): Total number of range selects performed. Example: 2.
        sum_select_range_check (int | Unset): Total number of range checks performed. Example: 0.
        sum_select_scan (int | Unset): Total number of select scans performed. Example: 4.
        sum_sort_merge_passes (int | Unset): Total number of sort merge passes. Example: 1.
        sum_sort_range (int | Unset): Total number of sort range operations. Example: 2.
        sum_sort_rows (int | Unset): Total number of rows sorted. Example: 100.
        sum_sort_scan (int | Unset): Total number of sort scans performed. Example: 3.
        sum_timer_wait (int | Unset): Total wait time for the query. Example: 20000.
        sum_warnings (int | Unset): Total number of warnings generated. Example: 0.
    """

    avg_timer_wait: int | Unset = UNSET
    count_star: int | Unset = UNSET
    digest: str | Unset = UNSET
    digest_text: str | Unset = UNSET
    first_seen: datetime.datetime | Unset = UNSET
    last_seen: datetime.datetime | Unset = UNSET
    max_timer_wait: int | Unset = UNSET
    min_timer_wait: int | Unset = UNSET
    quantile_95: int | Unset = UNSET
    quantile_99: int | Unset = UNSET
    quantile_999: int | Unset = UNSET
    query_sample_seen: datetime.datetime | Unset = UNSET
    query_sample_text: str | Unset = UNSET
    query_sample_timer_wait: int | Unset = UNSET
    schema_name: str | Unset = UNSET
    sum_created_tmp_disk_tables: int | Unset = UNSET
    sum_created_tmp_tables: int | Unset = UNSET
    sum_errors: int | Unset = UNSET
    sum_lock_time: int | Unset = UNSET
    sum_no_good_index_used: int | Unset = UNSET
    sum_no_index_used: int | Unset = UNSET
    sum_rows_affected: int | Unset = UNSET
    sum_rows_examined: int | Unset = UNSET
    sum_rows_sent: int | Unset = UNSET
    sum_select_full_join: int | Unset = UNSET
    sum_select_full_range_join: int | Unset = UNSET
    sum_select_range: int | Unset = UNSET
    sum_select_range_check: int | Unset = UNSET
    sum_select_scan: int | Unset = UNSET
    sum_sort_merge_passes: int | Unset = UNSET
    sum_sort_range: int | Unset = UNSET
    sum_sort_rows: int | Unset = UNSET
    sum_sort_scan: int | Unset = UNSET
    sum_timer_wait: int | Unset = UNSET
    sum_warnings: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avg_timer_wait = self.avg_timer_wait

        count_star = self.count_star

        digest = self.digest

        digest_text = self.digest_text

        first_seen: str | Unset = UNSET
        if not isinstance(self.first_seen, Unset):
            first_seen = self.first_seen.isoformat()

        last_seen: str | Unset = UNSET
        if not isinstance(self.last_seen, Unset):
            last_seen = self.last_seen.isoformat()

        max_timer_wait = self.max_timer_wait

        min_timer_wait = self.min_timer_wait

        quantile_95 = self.quantile_95

        quantile_99 = self.quantile_99

        quantile_999 = self.quantile_999

        query_sample_seen: str | Unset = UNSET
        if not isinstance(self.query_sample_seen, Unset):
            query_sample_seen = self.query_sample_seen.isoformat()

        query_sample_text = self.query_sample_text

        query_sample_timer_wait = self.query_sample_timer_wait

        schema_name = self.schema_name

        sum_created_tmp_disk_tables = self.sum_created_tmp_disk_tables

        sum_created_tmp_tables = self.sum_created_tmp_tables

        sum_errors = self.sum_errors

        sum_lock_time = self.sum_lock_time

        sum_no_good_index_used = self.sum_no_good_index_used

        sum_no_index_used = self.sum_no_index_used

        sum_rows_affected = self.sum_rows_affected

        sum_rows_examined = self.sum_rows_examined

        sum_rows_sent = self.sum_rows_sent

        sum_select_full_join = self.sum_select_full_join

        sum_select_full_range_join = self.sum_select_full_range_join

        sum_select_range = self.sum_select_range

        sum_select_range_check = self.sum_select_range_check

        sum_select_scan = self.sum_select_scan

        sum_sort_merge_passes = self.sum_sort_merge_passes

        sum_sort_range = self.sum_sort_range

        sum_sort_rows = self.sum_sort_rows

        sum_sort_scan = self.sum_sort_scan

        sum_timer_wait = self.sum_timer_wait

        sum_warnings = self.sum_warnings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avg_timer_wait is not UNSET:
            field_dict["avg_timer_wait"] = avg_timer_wait
        if count_star is not UNSET:
            field_dict["count_star"] = count_star
        if digest is not UNSET:
            field_dict["digest"] = digest
        if digest_text is not UNSET:
            field_dict["digest_text"] = digest_text
        if first_seen is not UNSET:
            field_dict["first_seen"] = first_seen
        if last_seen is not UNSET:
            field_dict["last_seen"] = last_seen
        if max_timer_wait is not UNSET:
            field_dict["max_timer_wait"] = max_timer_wait
        if min_timer_wait is not UNSET:
            field_dict["min_timer_wait"] = min_timer_wait
        if quantile_95 is not UNSET:
            field_dict["quantile_95"] = quantile_95
        if quantile_99 is not UNSET:
            field_dict["quantile_99"] = quantile_99
        if quantile_999 is not UNSET:
            field_dict["quantile_999"] = quantile_999
        if query_sample_seen is not UNSET:
            field_dict["query_sample_seen"] = query_sample_seen
        if query_sample_text is not UNSET:
            field_dict["query_sample_text"] = query_sample_text
        if query_sample_timer_wait is not UNSET:
            field_dict["query_sample_timer_wait"] = query_sample_timer_wait
        if schema_name is not UNSET:
            field_dict["schema_name"] = schema_name
        if sum_created_tmp_disk_tables is not UNSET:
            field_dict["sum_created_tmp_disk_tables"] = sum_created_tmp_disk_tables
        if sum_created_tmp_tables is not UNSET:
            field_dict["sum_created_tmp_tables"] = sum_created_tmp_tables
        if sum_errors is not UNSET:
            field_dict["sum_errors"] = sum_errors
        if sum_lock_time is not UNSET:
            field_dict["sum_lock_time"] = sum_lock_time
        if sum_no_good_index_used is not UNSET:
            field_dict["sum_no_good_index_used"] = sum_no_good_index_used
        if sum_no_index_used is not UNSET:
            field_dict["sum_no_index_used"] = sum_no_index_used
        if sum_rows_affected is not UNSET:
            field_dict["sum_rows_affected"] = sum_rows_affected
        if sum_rows_examined is not UNSET:
            field_dict["sum_rows_examined"] = sum_rows_examined
        if sum_rows_sent is not UNSET:
            field_dict["sum_rows_sent"] = sum_rows_sent
        if sum_select_full_join is not UNSET:
            field_dict["sum_select_full_join"] = sum_select_full_join
        if sum_select_full_range_join is not UNSET:
            field_dict["sum_select_full_range_join"] = sum_select_full_range_join
        if sum_select_range is not UNSET:
            field_dict["sum_select_range"] = sum_select_range
        if sum_select_range_check is not UNSET:
            field_dict["sum_select_range_check"] = sum_select_range_check
        if sum_select_scan is not UNSET:
            field_dict["sum_select_scan"] = sum_select_scan
        if sum_sort_merge_passes is not UNSET:
            field_dict["sum_sort_merge_passes"] = sum_sort_merge_passes
        if sum_sort_range is not UNSET:
            field_dict["sum_sort_range"] = sum_sort_range
        if sum_sort_rows is not UNSET:
            field_dict["sum_sort_rows"] = sum_sort_rows
        if sum_sort_scan is not UNSET:
            field_dict["sum_sort_scan"] = sum_sort_scan
        if sum_timer_wait is not UNSET:
            field_dict["sum_timer_wait"] = sum_timer_wait
        if sum_warnings is not UNSET:
            field_dict["sum_warnings"] = sum_warnings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        avg_timer_wait = d.pop("avg_timer_wait", UNSET)

        count_star = d.pop("count_star", UNSET)

        digest = d.pop("digest", UNSET)

        digest_text = d.pop("digest_text", UNSET)

        _first_seen = d.pop("first_seen", UNSET)
        first_seen: datetime.datetime | Unset
        if isinstance(_first_seen, Unset):
            first_seen = UNSET
        else:
            first_seen = datetime.datetime.fromisoformat(_first_seen)

        _last_seen = d.pop("last_seen", UNSET)
        last_seen: datetime.datetime | Unset
        if isinstance(_last_seen, Unset):
            last_seen = UNSET
        else:
            last_seen = datetime.datetime.fromisoformat(_last_seen)

        max_timer_wait = d.pop("max_timer_wait", UNSET)

        min_timer_wait = d.pop("min_timer_wait", UNSET)

        quantile_95 = d.pop("quantile_95", UNSET)

        quantile_99 = d.pop("quantile_99", UNSET)

        quantile_999 = d.pop("quantile_999", UNSET)

        _query_sample_seen = d.pop("query_sample_seen", UNSET)
        query_sample_seen: datetime.datetime | Unset
        if isinstance(_query_sample_seen, Unset):
            query_sample_seen = UNSET
        else:
            query_sample_seen = datetime.datetime.fromisoformat(_query_sample_seen)

        query_sample_text = d.pop("query_sample_text", UNSET)

        query_sample_timer_wait = d.pop("query_sample_timer_wait", UNSET)

        schema_name = d.pop("schema_name", UNSET)

        sum_created_tmp_disk_tables = d.pop("sum_created_tmp_disk_tables", UNSET)

        sum_created_tmp_tables = d.pop("sum_created_tmp_tables", UNSET)

        sum_errors = d.pop("sum_errors", UNSET)

        sum_lock_time = d.pop("sum_lock_time", UNSET)

        sum_no_good_index_used = d.pop("sum_no_good_index_used", UNSET)

        sum_no_index_used = d.pop("sum_no_index_used", UNSET)

        sum_rows_affected = d.pop("sum_rows_affected", UNSET)

        sum_rows_examined = d.pop("sum_rows_examined", UNSET)

        sum_rows_sent = d.pop("sum_rows_sent", UNSET)

        sum_select_full_join = d.pop("sum_select_full_join", UNSET)

        sum_select_full_range_join = d.pop("sum_select_full_range_join", UNSET)

        sum_select_range = d.pop("sum_select_range", UNSET)

        sum_select_range_check = d.pop("sum_select_range_check", UNSET)

        sum_select_scan = d.pop("sum_select_scan", UNSET)

        sum_sort_merge_passes = d.pop("sum_sort_merge_passes", UNSET)

        sum_sort_range = d.pop("sum_sort_range", UNSET)

        sum_sort_rows = d.pop("sum_sort_rows", UNSET)

        sum_sort_scan = d.pop("sum_sort_scan", UNSET)

        sum_timer_wait = d.pop("sum_timer_wait", UNSET)

        sum_warnings = d.pop("sum_warnings", UNSET)

        database_query_statistics_mysql_response = cls(
            avg_timer_wait=avg_timer_wait,
            count_star=count_star,
            digest=digest,
            digest_text=digest_text,
            first_seen=first_seen,
            last_seen=last_seen,
            max_timer_wait=max_timer_wait,
            min_timer_wait=min_timer_wait,
            quantile_95=quantile_95,
            quantile_99=quantile_99,
            quantile_999=quantile_999,
            query_sample_seen=query_sample_seen,
            query_sample_text=query_sample_text,
            query_sample_timer_wait=query_sample_timer_wait,
            schema_name=schema_name,
            sum_created_tmp_disk_tables=sum_created_tmp_disk_tables,
            sum_created_tmp_tables=sum_created_tmp_tables,
            sum_errors=sum_errors,
            sum_lock_time=sum_lock_time,
            sum_no_good_index_used=sum_no_good_index_used,
            sum_no_index_used=sum_no_index_used,
            sum_rows_affected=sum_rows_affected,
            sum_rows_examined=sum_rows_examined,
            sum_rows_sent=sum_rows_sent,
            sum_select_full_join=sum_select_full_join,
            sum_select_full_range_join=sum_select_full_range_join,
            sum_select_range=sum_select_range,
            sum_select_range_check=sum_select_range_check,
            sum_select_scan=sum_select_scan,
            sum_sort_merge_passes=sum_sort_merge_passes,
            sum_sort_range=sum_sort_range,
            sum_sort_rows=sum_sort_rows,
            sum_sort_scan=sum_sort_scan,
            sum_timer_wait=sum_timer_wait,
            sum_warnings=sum_warnings,
        )

        database_query_statistics_mysql_response.additional_properties = d
        return database_query_statistics_mysql_response

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
