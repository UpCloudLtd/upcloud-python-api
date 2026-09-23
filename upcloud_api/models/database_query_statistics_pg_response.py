from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseQueryStatisticsPgResponse")


@_attrs_define
class DatabaseQueryStatisticsPgResponse:
    """Schema for PostgreSQL query statistics response.

    Attributes:
        blk_read_time (int | Unset): Time spent reading data blocks, in milliseconds. Example: 120.
        blk_write_time (int | Unset): Time spent writing data blocks, in milliseconds. Example: 45.
        calls (int | Unset): Number of times the query was executed. Example: 10.
        database_name (str | Unset): Name of the database. Example: mydb.
        local_blks_dirtied (int | Unset): Number of local blocks dirtied. Example: 2.
        local_blks_hit (int | Unset): Number of local block cache hits. Example: 100.
        local_blks_read (int | Unset): Number of local blocks read. Example: 5.
        local_blks_written (int | Unset): Number of local blocks written. Example: 3.
        max_time (int | Unset): Maximum execution time, in milliseconds. Example: 300.
        mean_time (int | Unset): Mean execution time, in milliseconds. Example: 150.
        min_time (int | Unset): Minimum execution time, in milliseconds. Example: 100.
        query (str | Unset): The SQL query text. Example: SELECT * FROM users WHERE id = 1.
        rows (int | Unset): Total number of rows returned or affected. Example: 20.
        shared_blks_dirtied (int | Unset): Number of shared blocks dirtied. Example: 4.
        shared_blks_hit (int | Unset): Number of shared block cache hits. Example: 200.
        shared_blks_read (int | Unset): Number of shared blocks read. Example: 8.
        shared_blks_written (int | Unset): Number of shared blocks written. Example: 6.
        stddev_time (int | Unset): Standard deviation of execution time, in milliseconds. Example: 20.
        temp_blks_read (int | Unset): Number of temporary blocks read. Example: 1.
        temp_blks_written (int | Unset): Number of temporary blocks written. Example: 1.
        total_time (int | Unset): Total execution time, in milliseconds. Example: 1500.
        user_name (str | Unset): Name of the user who executed the query. Example: postgres.
    """

    blk_read_time: int | Unset = UNSET
    blk_write_time: int | Unset = UNSET
    calls: int | Unset = UNSET
    database_name: str | Unset = UNSET
    local_blks_dirtied: int | Unset = UNSET
    local_blks_hit: int | Unset = UNSET
    local_blks_read: int | Unset = UNSET
    local_blks_written: int | Unset = UNSET
    max_time: int | Unset = UNSET
    mean_time: int | Unset = UNSET
    min_time: int | Unset = UNSET
    query: str | Unset = UNSET
    rows: int | Unset = UNSET
    shared_blks_dirtied: int | Unset = UNSET
    shared_blks_hit: int | Unset = UNSET
    shared_blks_read: int | Unset = UNSET
    shared_blks_written: int | Unset = UNSET
    stddev_time: int | Unset = UNSET
    temp_blks_read: int | Unset = UNSET
    temp_blks_written: int | Unset = UNSET
    total_time: int | Unset = UNSET
    user_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        blk_read_time = self.blk_read_time

        blk_write_time = self.blk_write_time

        calls = self.calls

        database_name = self.database_name

        local_blks_dirtied = self.local_blks_dirtied

        local_blks_hit = self.local_blks_hit

        local_blks_read = self.local_blks_read

        local_blks_written = self.local_blks_written

        max_time = self.max_time

        mean_time = self.mean_time

        min_time = self.min_time

        query = self.query

        rows = self.rows

        shared_blks_dirtied = self.shared_blks_dirtied

        shared_blks_hit = self.shared_blks_hit

        shared_blks_read = self.shared_blks_read

        shared_blks_written = self.shared_blks_written

        stddev_time = self.stddev_time

        temp_blks_read = self.temp_blks_read

        temp_blks_written = self.temp_blks_written

        total_time = self.total_time

        user_name = self.user_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if blk_read_time is not UNSET:
            field_dict["blk_read_time"] = blk_read_time
        if blk_write_time is not UNSET:
            field_dict["blk_write_time"] = blk_write_time
        if calls is not UNSET:
            field_dict["calls"] = calls
        if database_name is not UNSET:
            field_dict["database_name"] = database_name
        if local_blks_dirtied is not UNSET:
            field_dict["local_blks_dirtied"] = local_blks_dirtied
        if local_blks_hit is not UNSET:
            field_dict["local_blks_hit"] = local_blks_hit
        if local_blks_read is not UNSET:
            field_dict["local_blks_read"] = local_blks_read
        if local_blks_written is not UNSET:
            field_dict["local_blks_written"] = local_blks_written
        if max_time is not UNSET:
            field_dict["max_time"] = max_time
        if mean_time is not UNSET:
            field_dict["mean_time"] = mean_time
        if min_time is not UNSET:
            field_dict["min_time"] = min_time
        if query is not UNSET:
            field_dict["query"] = query
        if rows is not UNSET:
            field_dict["rows"] = rows
        if shared_blks_dirtied is not UNSET:
            field_dict["shared_blks_dirtied"] = shared_blks_dirtied
        if shared_blks_hit is not UNSET:
            field_dict["shared_blks_hit"] = shared_blks_hit
        if shared_blks_read is not UNSET:
            field_dict["shared_blks_read"] = shared_blks_read
        if shared_blks_written is not UNSET:
            field_dict["shared_blks_written"] = shared_blks_written
        if stddev_time is not UNSET:
            field_dict["stddev_time"] = stddev_time
        if temp_blks_read is not UNSET:
            field_dict["temp_blks_read"] = temp_blks_read
        if temp_blks_written is not UNSET:
            field_dict["temp_blks_written"] = temp_blks_written
        if total_time is not UNSET:
            field_dict["total_time"] = total_time
        if user_name is not UNSET:
            field_dict["user_name"] = user_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        blk_read_time = d.pop("blk_read_time", UNSET)

        blk_write_time = d.pop("blk_write_time", UNSET)

        calls = d.pop("calls", UNSET)

        database_name = d.pop("database_name", UNSET)

        local_blks_dirtied = d.pop("local_blks_dirtied", UNSET)

        local_blks_hit = d.pop("local_blks_hit", UNSET)

        local_blks_read = d.pop("local_blks_read", UNSET)

        local_blks_written = d.pop("local_blks_written", UNSET)

        max_time = d.pop("max_time", UNSET)

        mean_time = d.pop("mean_time", UNSET)

        min_time = d.pop("min_time", UNSET)

        query = d.pop("query", UNSET)

        rows = d.pop("rows", UNSET)

        shared_blks_dirtied = d.pop("shared_blks_dirtied", UNSET)

        shared_blks_hit = d.pop("shared_blks_hit", UNSET)

        shared_blks_read = d.pop("shared_blks_read", UNSET)

        shared_blks_written = d.pop("shared_blks_written", UNSET)

        stddev_time = d.pop("stddev_time", UNSET)

        temp_blks_read = d.pop("temp_blks_read", UNSET)

        temp_blks_written = d.pop("temp_blks_written", UNSET)

        total_time = d.pop("total_time", UNSET)

        user_name = d.pop("user_name", UNSET)

        database_query_statistics_pg_response = cls(
            blk_read_time=blk_read_time,
            blk_write_time=blk_write_time,
            calls=calls,
            database_name=database_name,
            local_blks_dirtied=local_blks_dirtied,
            local_blks_hit=local_blks_hit,
            local_blks_read=local_blks_read,
            local_blks_written=local_blks_written,
            max_time=max_time,
            mean_time=mean_time,
            min_time=min_time,
            query=query,
            rows=rows,
            shared_blks_dirtied=shared_blks_dirtied,
            shared_blks_hit=shared_blks_hit,
            shared_blks_read=shared_blks_read,
            shared_blks_written=shared_blks_written,
            stddev_time=stddev_time,
            temp_blks_read=temp_blks_read,
            temp_blks_written=temp_blks_written,
            total_time=total_time,
            user_name=user_name,
        )

        database_query_statistics_pg_response.additional_properties = d
        return database_query_statistics_pg_response

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
