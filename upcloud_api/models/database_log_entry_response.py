from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseLogEntryResponse")


@_attrs_define
class DatabaseLogEntryResponse:
    """Schema representing a log entry from an UpCloud service.

    Attributes:
        hostname (str | Unset): The name of the UpCloud service host where the log entry originated. Example: api-doc-
            hostname.
        msg (str | Unset): The log message content. Example: [10-1]
            pid=3328089,user=postgres,db=defaultdb,app=[unknown],client=[local] LOG:  connection authorized: user=postgres
            database=defaultdb.
        time (datetime.datetime | Unset): Timestamp of the log entry. Example: 2022-01-21T13:07:23.687241Z.
        service (str | Unset): Name of the UpCloud service that generated the log entry. Example: postgresql-13.service.
    """

    hostname: str | Unset = UNSET
    msg: str | Unset = UNSET
    time: datetime.datetime | Unset = UNSET
    service: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hostname = self.hostname

        msg = self.msg

        time: str | Unset = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.isoformat()

        service = self.service

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if msg is not UNSET:
            field_dict["msg"] = msg
        if time is not UNSET:
            field_dict["time"] = time
        if service is not UNSET:
            field_dict["service"] = service

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hostname = d.pop("hostname", UNSET)

        msg = d.pop("msg", UNSET)

        _time = d.pop("time", UNSET)
        time: datetime.datetime | Unset
        if isinstance(_time, Unset):
            time = UNSET
        else:
            time = datetime.datetime.fromisoformat(_time)

        service = d.pop("service", UNSET)

        database_log_entry_response = cls(
            hostname=hostname,
            msg=msg,
            time=time,
            service=service,
        )

        database_log_entry_response.additional_properties = d
        return database_log_entry_response

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
