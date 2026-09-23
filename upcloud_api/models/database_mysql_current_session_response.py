from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseMysqlCurrentSessionResponse")


@_attrs_define
class DatabaseMysqlCurrentSessionResponse:
    """Schema for the current session of a MySQL service.

    Attributes:
        application_name (str | Unset): Name of the application that is connected to this service. Example: my-app.
        client_addr (str | Unset): IP address of the client connected to this service. Example: 198.51.100.23.
        datname (str | Unset): Name of the database this service is connected to. Example: defaultdb.
        id (str | Unset): Process ID of this service. Example: 3159.
        query (str | Unset): Text of this service's most recent query. If state is active this shows the currently
            executing query; otherwise an empty string. Example: SELECT 1.
        query_duration (int | Unset): The active query’s current duration, serialized as nanoseconds. Example:
            125000000.
        state (str | Unset): Current overall state of this service. Allowed values include: active (executing a query)
            and idle (waiting for a new client command). Example: active.
        usename (str | Unset): Name of the user logged into this service. Example: appuser.
    """

    application_name: str | Unset = UNSET
    client_addr: str | Unset = UNSET
    datname: str | Unset = UNSET
    id: str | Unset = UNSET
    query: str | Unset = UNSET
    query_duration: int | Unset = UNSET
    state: str | Unset = UNSET
    usename: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        application_name = self.application_name

        client_addr = self.client_addr

        datname = self.datname

        id = self.id

        query = self.query

        query_duration = self.query_duration

        state = self.state

        usename = self.usename

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if application_name is not UNSET:
            field_dict["application_name"] = application_name
        if client_addr is not UNSET:
            field_dict["client_addr"] = client_addr
        if datname is not UNSET:
            field_dict["datname"] = datname
        if id is not UNSET:
            field_dict["id"] = id
        if query is not UNSET:
            field_dict["query"] = query
        if query_duration is not UNSET:
            field_dict["query_duration"] = query_duration
        if state is not UNSET:
            field_dict["state"] = state
        if usename is not UNSET:
            field_dict["usename"] = usename

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        application_name = d.pop("application_name", UNSET)

        client_addr = d.pop("client_addr", UNSET)

        datname = d.pop("datname", UNSET)

        id = d.pop("id", UNSET)

        query = d.pop("query", UNSET)

        query_duration = d.pop("query_duration", UNSET)

        state = d.pop("state", UNSET)

        usename = d.pop("usename", UNSET)

        database_mysql_current_session_response = cls(
            application_name=application_name,
            client_addr=client_addr,
            datname=datname,
            id=id,
            query=query,
            query_duration=query_duration,
            state=state,
            usename=usename,
        )

        database_mysql_current_session_response.additional_properties = d
        return database_mysql_current_session_response

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
