from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseMigrationStatusDetailsResponse")


@_attrs_define
class DatabaseMigrationStatusDetailsResponse:
    """Schema for migration status details response.

    Attributes:
        error (str | Unset): Error message if any Example: some error occurred.
        dbname (str | Unset): Name of the database Example: defaultdb.
        method (str | Unset): Migration method used Example: replication.
        status (str | Unset): Current status of the migration Example: syncing.
    """

    error: str | Unset = UNSET
    dbname: str | Unset = UNSET
    method: str | Unset = UNSET
    status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error = self.error

        dbname = self.dbname

        method = self.method

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error is not UNSET:
            field_dict["error"] = error
        if dbname is not UNSET:
            field_dict["dbname"] = dbname
        if method is not UNSET:
            field_dict["method"] = method
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        error = d.pop("error", UNSET)

        dbname = d.pop("dbname", UNSET)

        method = d.pop("method", UNSET)

        status = d.pop("status", UNSET)

        database_migration_status_details_response = cls(
            error=error,
            dbname=dbname,
            method=method,
            status=status,
        )

        database_migration_status_details_response.additional_properties = d
        return database_migration_status_details_response

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
