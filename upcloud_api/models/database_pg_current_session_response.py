from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabasePgCurrentSessionResponse")


@_attrs_define
class DatabasePgCurrentSessionResponse:
    """Schema for PostgreSQL current session response.

    Attributes:
        application_name (str | Unset): Name of the application that is connected to this service. Example: client
            1.5.14.
        backend_start (datetime.datetime | Unset): Time when this process was started (when the client connected).
            Example: 2025-09-21T12:34:56Z.
        backend_type (str | Unset): Type of current service (e.g., client backend). Example: client backend.
        backend_xid (int | Unset): Top-level transaction identifier of this service, if any. Example: 742.
        backend_xmin (int | Unset): The current service's xmin horizon. Example: 731.
        client_addr (str | Unset): IP address of the connected client. Example: 198.51.100.42.
        client_hostname (str | Unset): Hostname of the connected client (reverse DNS of client_addr). Example: app-
            host.example.internal.
        client_port (int | Unset): TCP port number used by the client, or -1 if a Unix socket is used. Example: 52344.
        datid (int | Unset): OID of the database this service is connected to. Example: 16384.
        datname (str | Unset): Name of the database this service is connected to. Example: defaultdb.
        id (str | Unset): Process ID of this service. Example: 3328089.
        query (str | Unset): Most recent query. If state is active, this is the currently executing query. Example:
            SELECT name, setting FROM pg_settings WHERE source = $1.
        query_duration (str | Unset): The active query's current duration (as a string). Example: 00:00:01.234.
        query_start (datetime.datetime | Unset): Time when the currently active (or last) query started. Example:
            2025-09-21T12:35:10Z.
        state (str | Unset): Overall state of this service (e.g., 'active' or 'idle'). Example: active.
        state_change (datetime.datetime | Unset): Time when the state was last changed. Example: 2025-09-21T12:35:10Z.
        usename (str | Unset): Name of the user logged into this service. Example: upadmin.
        usesysid (int | Unset): OID of the user logged into this service. Example: 10.
        wait_event (str | Unset): Wait event name if the service is currently waiting. Example: ClientRead.
        wait_event_type (str | Unset): Type of event for which the service is waiting (if any). Example: Client.
        xact_start (datetime.datetime | Unset): Time when the current transaction started. Example:
            2025-09-21T12:35:05Z.
    """

    application_name: str | Unset = UNSET
    backend_start: datetime.datetime | Unset = UNSET
    backend_type: str | Unset = UNSET
    backend_xid: int | Unset = UNSET
    backend_xmin: int | Unset = UNSET
    client_addr: str | Unset = UNSET
    client_hostname: str | Unset = UNSET
    client_port: int | Unset = UNSET
    datid: int | Unset = UNSET
    datname: str | Unset = UNSET
    id: str | Unset = UNSET
    query: str | Unset = UNSET
    query_duration: str | Unset = UNSET
    query_start: datetime.datetime | Unset = UNSET
    state: str | Unset = UNSET
    state_change: datetime.datetime | Unset = UNSET
    usename: str | Unset = UNSET
    usesysid: int | Unset = UNSET
    wait_event: str | Unset = UNSET
    wait_event_type: str | Unset = UNSET
    xact_start: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        application_name = self.application_name

        backend_start: str | Unset = UNSET
        if not isinstance(self.backend_start, Unset):
            backend_start = self.backend_start.isoformat()

        backend_type = self.backend_type

        backend_xid = self.backend_xid

        backend_xmin = self.backend_xmin

        client_addr = self.client_addr

        client_hostname = self.client_hostname

        client_port = self.client_port

        datid = self.datid

        datname = self.datname

        id = self.id

        query = self.query

        query_duration = self.query_duration

        query_start: str | Unset = UNSET
        if not isinstance(self.query_start, Unset):
            query_start = self.query_start.isoformat()

        state = self.state

        state_change: str | Unset = UNSET
        if not isinstance(self.state_change, Unset):
            state_change = self.state_change.isoformat()

        usename = self.usename

        usesysid = self.usesysid

        wait_event = self.wait_event

        wait_event_type = self.wait_event_type

        xact_start: str | Unset = UNSET
        if not isinstance(self.xact_start, Unset):
            xact_start = self.xact_start.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if application_name is not UNSET:
            field_dict["application_name"] = application_name
        if backend_start is not UNSET:
            field_dict["backend_start"] = backend_start
        if backend_type is not UNSET:
            field_dict["backend_type"] = backend_type
        if backend_xid is not UNSET:
            field_dict["backend_xid"] = backend_xid
        if backend_xmin is not UNSET:
            field_dict["backend_xmin"] = backend_xmin
        if client_addr is not UNSET:
            field_dict["client_addr"] = client_addr
        if client_hostname is not UNSET:
            field_dict["client_hostname"] = client_hostname
        if client_port is not UNSET:
            field_dict["client_port"] = client_port
        if datid is not UNSET:
            field_dict["datid"] = datid
        if datname is not UNSET:
            field_dict["datname"] = datname
        if id is not UNSET:
            field_dict["id"] = id
        if query is not UNSET:
            field_dict["query"] = query
        if query_duration is not UNSET:
            field_dict["query_duration"] = query_duration
        if query_start is not UNSET:
            field_dict["query_start"] = query_start
        if state is not UNSET:
            field_dict["state"] = state
        if state_change is not UNSET:
            field_dict["state_change"] = state_change
        if usename is not UNSET:
            field_dict["usename"] = usename
        if usesysid is not UNSET:
            field_dict["usesysid"] = usesysid
        if wait_event is not UNSET:
            field_dict["wait_event"] = wait_event
        if wait_event_type is not UNSET:
            field_dict["wait_event_type"] = wait_event_type
        if xact_start is not UNSET:
            field_dict["xact_start"] = xact_start

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        application_name = d.pop("application_name", UNSET)

        _backend_start = d.pop("backend_start", UNSET)
        backend_start: datetime.datetime | Unset
        if isinstance(_backend_start, Unset):
            backend_start = UNSET
        else:
            backend_start = datetime.datetime.fromisoformat(_backend_start)

        backend_type = d.pop("backend_type", UNSET)

        backend_xid = d.pop("backend_xid", UNSET)

        backend_xmin = d.pop("backend_xmin", UNSET)

        client_addr = d.pop("client_addr", UNSET)

        client_hostname = d.pop("client_hostname", UNSET)

        client_port = d.pop("client_port", UNSET)

        datid = d.pop("datid", UNSET)

        datname = d.pop("datname", UNSET)

        id = d.pop("id", UNSET)

        query = d.pop("query", UNSET)

        query_duration = d.pop("query_duration", UNSET)

        _query_start = d.pop("query_start", UNSET)
        query_start: datetime.datetime | Unset
        if isinstance(_query_start, Unset):
            query_start = UNSET
        else:
            query_start = datetime.datetime.fromisoformat(_query_start)

        state = d.pop("state", UNSET)

        _state_change = d.pop("state_change", UNSET)
        state_change: datetime.datetime | Unset
        if isinstance(_state_change, Unset):
            state_change = UNSET
        else:
            state_change = datetime.datetime.fromisoformat(_state_change)

        usename = d.pop("usename", UNSET)

        usesysid = d.pop("usesysid", UNSET)

        wait_event = d.pop("wait_event", UNSET)

        wait_event_type = d.pop("wait_event_type", UNSET)

        _xact_start = d.pop("xact_start", UNSET)
        xact_start: datetime.datetime | Unset
        if isinstance(_xact_start, Unset):
            xact_start = UNSET
        else:
            xact_start = datetime.datetime.fromisoformat(_xact_start)

        database_pg_current_session_response = cls(
            application_name=application_name,
            backend_start=backend_start,
            backend_type=backend_type,
            backend_xid=backend_xid,
            backend_xmin=backend_xmin,
            client_addr=client_addr,
            client_hostname=client_hostname,
            client_port=client_port,
            datid=datid,
            datname=datname,
            id=id,
            query=query,
            query_duration=query_duration,
            query_start=query_start,
            state=state,
            state_change=state_change,
            usename=usename,
            usesysid=usesysid,
            wait_event=wait_event,
            wait_event_type=wait_event_type,
            xact_start=xact_start,
        )

        database_pg_current_session_response.additional_properties = d
        return database_pg_current_session_response

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
