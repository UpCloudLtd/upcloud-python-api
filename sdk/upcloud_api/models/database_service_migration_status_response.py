from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_migration_status_details_response import DatabaseMigrationStatusDetailsResponse


T = TypeVar("T", bound="DatabaseServiceMigrationStatusResponse")


@_attrs_define
class DatabaseServiceMigrationStatusResponse:
    """Response schema for service migration status

    Attributes:
        error (str | Unset): Error message if any Example: some error occurred.
        method (str | Unset): Migration method used Example: replication.
        seconds_behind_master (int | Unset): Seconds behind master Example: 10.
        source_active (bool | Unset): Is source active Example: True.
        status (str | Unset): Current status of the migration Example: syncing.
        databases (list[DatabaseMigrationStatusDetailsResponse] | Unset):
    """

    error: str | Unset = UNSET
    method: str | Unset = UNSET
    seconds_behind_master: int | Unset = UNSET
    source_active: bool | Unset = UNSET
    status: str | Unset = UNSET
    databases: list[DatabaseMigrationStatusDetailsResponse] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error = self.error

        method = self.method

        seconds_behind_master = self.seconds_behind_master

        source_active = self.source_active

        status = self.status

        databases: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.databases, Unset):
            databases = []
            for databases_item_data in self.databases:
                databases_item = databases_item_data.to_dict()
                databases.append(databases_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error is not UNSET:
            field_dict["error"] = error
        if method is not UNSET:
            field_dict["method"] = method
        if seconds_behind_master is not UNSET:
            field_dict["seconds_behind_master"] = seconds_behind_master
        if source_active is not UNSET:
            field_dict["source_active"] = source_active
        if status is not UNSET:
            field_dict["status"] = status
        if databases is not UNSET:
            field_dict["databases"] = databases

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_migration_status_details_response import (
            DatabaseMigrationStatusDetailsResponse,  # noqa: PLC0415
        )

        d = dict(src_dict)
        error = d.pop("error", UNSET)

        method = d.pop("method", UNSET)

        seconds_behind_master = d.pop("seconds_behind_master", UNSET)

        source_active = d.pop("source_active", UNSET)

        status = d.pop("status", UNSET)

        _databases = d.pop("databases", UNSET)
        databases: list[DatabaseMigrationStatusDetailsResponse] | Unset = UNSET
        if _databases is not UNSET:
            databases = []
            for databases_item_data in _databases:
                databases_item = DatabaseMigrationStatusDetailsResponse.from_dict(databases_item_data)

                databases.append(databases_item)

        database_service_migration_status_response = cls(
            error=error,
            method=method,
            seconds_behind_master=seconds_behind_master,
            source_active=source_active,
            status=status,
            databases=databases,
        )

        database_service_migration_status_response.additional_properties = d
        return database_service_migration_status_response

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
