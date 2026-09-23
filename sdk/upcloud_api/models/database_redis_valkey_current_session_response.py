from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseRedisValkeyCurrentSessionResponse")


@_attrs_define
class DatabaseRedisValkeyCurrentSessionResponse:
    """Schema for Redis Valkey current session response.

    Attributes:
        active_channel_subscriptions (int | Unset): Number of active channel subscriptions. Example: 2.
        active_database (int | Unset): Current database ID. Example: 0.
        active_pattern_matching_channel_subscriptions (int | Unset): Number of pattern matching subscriptions. Example:
            1.
        application_name (str | Unset): Name of the application that is connected to this service. Example: my-app.
        client_addr (str | Unset): IP address of the client connected to this service. Example:
            [fff0:fff0:fff0:fff0:0:fff0:fff0:fff0]:39956.
        connection_age (int | Unset): Total duration of the connection in nanoseconds. Example: 2079483000000000.
        connection_idle (int | Unset): Idle time of the connection in nanoseconds. Example: 3000000000.
        flags (list[str] | Unset): List of flags describing the client connection. Example: ['N', 'U'].
        flags_raw (str | Unset): Client connection flags (raw string). Example: NU.
        id (int | Unset): Process ID of this session. Example: 15.
        multi_exec_commands (int | Unset): Number of commands in a MULTI/EXEC context. Example: -1.
        output_buffer (int | Unset): Output buffer length. Example: 0.
        output_buffer_memory (int | Unset): Output buffer memory usage. Example: 0.
        output_list_length (int | Unset): Output list length (replies queued when buffer is full). Example: 0.
        query (str | Unset): The last executed command. Example: info.
        query_buffer (int | Unset): Query buffer length (0 means no query pending). Example: 0.
        query_buffer_free (int | Unset): Free space of the query buffer (0 means the buffer is full). Example: 0.
    """

    active_channel_subscriptions: int | Unset = UNSET
    active_database: int | Unset = UNSET
    active_pattern_matching_channel_subscriptions: int | Unset = UNSET
    application_name: str | Unset = UNSET
    client_addr: str | Unset = UNSET
    connection_age: int | Unset = UNSET
    connection_idle: int | Unset = UNSET
    flags: list[str] | Unset = UNSET
    flags_raw: str | Unset = UNSET
    id: int | Unset = UNSET
    multi_exec_commands: int | Unset = UNSET
    output_buffer: int | Unset = UNSET
    output_buffer_memory: int | Unset = UNSET
    output_list_length: int | Unset = UNSET
    query: str | Unset = UNSET
    query_buffer: int | Unset = UNSET
    query_buffer_free: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active_channel_subscriptions = self.active_channel_subscriptions

        active_database = self.active_database

        active_pattern_matching_channel_subscriptions = self.active_pattern_matching_channel_subscriptions

        application_name = self.application_name

        client_addr = self.client_addr

        connection_age = self.connection_age

        connection_idle = self.connection_idle

        flags: list[str] | Unset = UNSET
        if not isinstance(self.flags, Unset):
            flags = self.flags

        flags_raw = self.flags_raw

        id = self.id

        multi_exec_commands = self.multi_exec_commands

        output_buffer = self.output_buffer

        output_buffer_memory = self.output_buffer_memory

        output_list_length = self.output_list_length

        query = self.query

        query_buffer = self.query_buffer

        query_buffer_free = self.query_buffer_free

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active_channel_subscriptions is not UNSET:
            field_dict["active_channel_subscriptions"] = active_channel_subscriptions
        if active_database is not UNSET:
            field_dict["active_database"] = active_database
        if active_pattern_matching_channel_subscriptions is not UNSET:
            field_dict["active_pattern_matching_channel_subscriptions"] = active_pattern_matching_channel_subscriptions
        if application_name is not UNSET:
            field_dict["application_name"] = application_name
        if client_addr is not UNSET:
            field_dict["client_addr"] = client_addr
        if connection_age is not UNSET:
            field_dict["connection_age"] = connection_age
        if connection_idle is not UNSET:
            field_dict["connection_idle"] = connection_idle
        if flags is not UNSET:
            field_dict["flags"] = flags
        if flags_raw is not UNSET:
            field_dict["flags_raw"] = flags_raw
        if id is not UNSET:
            field_dict["id"] = id
        if multi_exec_commands is not UNSET:
            field_dict["multi_exec_commands"] = multi_exec_commands
        if output_buffer is not UNSET:
            field_dict["output_buffer"] = output_buffer
        if output_buffer_memory is not UNSET:
            field_dict["output_buffer_memory"] = output_buffer_memory
        if output_list_length is not UNSET:
            field_dict["output_list_length"] = output_list_length
        if query is not UNSET:
            field_dict["query"] = query
        if query_buffer is not UNSET:
            field_dict["query_buffer"] = query_buffer
        if query_buffer_free is not UNSET:
            field_dict["query_buffer_free"] = query_buffer_free

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        active_channel_subscriptions = d.pop("active_channel_subscriptions", UNSET)

        active_database = d.pop("active_database", UNSET)

        active_pattern_matching_channel_subscriptions = d.pop("active_pattern_matching_channel_subscriptions", UNSET)

        application_name = d.pop("application_name", UNSET)

        client_addr = d.pop("client_addr", UNSET)

        connection_age = d.pop("connection_age", UNSET)

        connection_idle = d.pop("connection_idle", UNSET)

        flags = cast(list[str], d.pop("flags", UNSET))

        flags_raw = d.pop("flags_raw", UNSET)

        id = d.pop("id", UNSET)

        multi_exec_commands = d.pop("multi_exec_commands", UNSET)

        output_buffer = d.pop("output_buffer", UNSET)

        output_buffer_memory = d.pop("output_buffer_memory", UNSET)

        output_list_length = d.pop("output_list_length", UNSET)

        query = d.pop("query", UNSET)

        query_buffer = d.pop("query_buffer", UNSET)

        query_buffer_free = d.pop("query_buffer_free", UNSET)

        database_redis_valkey_current_session_response = cls(
            active_channel_subscriptions=active_channel_subscriptions,
            active_database=active_database,
            active_pattern_matching_channel_subscriptions=active_pattern_matching_channel_subscriptions,
            application_name=application_name,
            client_addr=client_addr,
            connection_age=connection_age,
            connection_idle=connection_idle,
            flags=flags,
            flags_raw=flags_raw,
            id=id,
            multi_exec_commands=multi_exec_commands,
            output_buffer=output_buffer,
            output_buffer_memory=output_buffer_memory,
            output_list_length=output_list_length,
            query=query,
            query_buffer=query_buffer,
            query_buffer_free=query_buffer_free,
        )

        database_redis_valkey_current_session_response.additional_properties = d
        return database_redis_valkey_current_session_response

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
