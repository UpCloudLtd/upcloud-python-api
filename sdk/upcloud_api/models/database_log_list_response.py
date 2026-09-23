from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_log_entry_response import DatabaseLogEntryResponse


T = TypeVar("T", bound="DatabaseLogListResponse")


@_attrs_define
class DatabaseLogListResponse:
    """Schema representing a paginated list of log entries from UpCloud services.

    Attributes:
        first_log_offset (str | Unset): Offset of the first log entry in the list. Example: 123456.
        offset (str | Unset): Current offset for pagination. Example: 123460.
        logs (list[DatabaseLogEntryResponse] | Unset): Array of log entries from UpCloud services. Example:
            [{'hostname': 'upc-pg-1a2b3c4d5e', 'msg': 'UpCloud PostgreSQL backup completed successfully', 'time':
            '2024-06-12T14:23:00Z', 'service': 'upcloud-pg'}].
    """

    first_log_offset: str | Unset = UNSET
    offset: str | Unset = UNSET
    logs: list[DatabaseLogEntryResponse] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        first_log_offset = self.first_log_offset

        offset = self.offset

        logs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.logs, Unset):
            logs = []
            for logs_item_data in self.logs:
                logs_item = logs_item_data.to_dict()
                logs.append(logs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if first_log_offset is not UNSET:
            field_dict["first_log_offset"] = first_log_offset
        if offset is not UNSET:
            field_dict["offset"] = offset
        if logs is not UNSET:
            field_dict["logs"] = logs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_log_entry_response import DatabaseLogEntryResponse  # noqa: PLC0415

        d = dict(src_dict)
        first_log_offset = d.pop("first_log_offset", UNSET)

        offset = d.pop("offset", UNSET)

        _logs = d.pop("logs", UNSET)
        logs: list[DatabaseLogEntryResponse] | Unset = UNSET
        if _logs is not UNSET:
            logs = []
            for logs_item_data in _logs:
                logs_item = DatabaseLogEntryResponse.from_dict(logs_item_data)

                logs.append(logs_item)

        database_log_list_response = cls(
            first_log_offset=first_log_offset,
            offset=offset,
            logs=logs,
        )

        database_log_list_response.additional_properties = d
        return database_log_list_response

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
