from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_service_task_base_response_result_codes_item import (
        DatabaseServiceTaskBaseResponseResultCodesItem,
    )


T = TypeVar("T", bound="DatabaseServiceTaskDetailsResponse")


@_attrs_define
class DatabaseServiceTaskDetailsResponse:
    """Response schema for retrieving detailed information about a specific service task, including result codes and
    success status.

        Attributes:
            create_time (datetime.datetime | Unset): The time when the service task was created Example:
                2022-10-04T12:21:42Z.
            result (str | Unset): A human-readable summary of the task result. Example: ok *Clusters are compatible*.
            result_codes (list[DatabaseServiceTaskBaseResponseResultCodesItem] | Unset): Optional list of result codes as
                key-value maps
            ignore_dbs (str | Unset): Optional list of databases to ignore
            operation (str | Unset): The operation being performed Example: mysql_migration_check.
            success (bool | Unset): Indicates whether the task completed successfully. Example: True.
            method (str | Unset): Optional method used for the operation Example: Replication.
            source_pg_version (str | Unset): Optional source PostgreSQL version Example: 13.
            target_pg_version (str | Unset): Optional target PostgreSQL version Example: 14.
            id (UUID | Unset): Optional identifier for the task Example: 9b39f10d-e356-437b-b907-d6d5574721b2.
    """

    create_time: datetime.datetime | Unset = UNSET
    result: str | Unset = UNSET
    result_codes: list[DatabaseServiceTaskBaseResponseResultCodesItem] | Unset = UNSET
    ignore_dbs: str | Unset = UNSET
    operation: str | Unset = UNSET
    success: bool | Unset = UNSET
    method: str | Unset = UNSET
    source_pg_version: str | Unset = UNSET
    target_pg_version: str | Unset = UNSET
    id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        create_time: str | Unset = UNSET
        if not isinstance(self.create_time, Unset):
            create_time = self.create_time.isoformat()

        result = self.result

        result_codes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.result_codes, Unset):
            result_codes = []
            for result_codes_item_data in self.result_codes:
                result_codes_item = result_codes_item_data.to_dict()
                result_codes.append(result_codes_item)

        ignore_dbs = self.ignore_dbs

        operation = self.operation

        success = self.success

        method = self.method

        source_pg_version = self.source_pg_version

        target_pg_version = self.target_pg_version

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if create_time is not UNSET:
            field_dict["create_time"] = create_time
        if result is not UNSET:
            field_dict["result"] = result
        if result_codes is not UNSET:
            field_dict["result_codes"] = result_codes
        if ignore_dbs is not UNSET:
            field_dict["ignore_dbs"] = ignore_dbs
        if operation is not UNSET:
            field_dict["operation"] = operation
        if success is not UNSET:
            field_dict["success"] = success
        if method is not UNSET:
            field_dict["method"] = method
        if source_pg_version is not UNSET:
            field_dict["source_pg_version"] = source_pg_version
        if target_pg_version is not UNSET:
            field_dict["target_pg_version"] = target_pg_version
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_service_task_base_response_result_codes_item import (
            DatabaseServiceTaskBaseResponseResultCodesItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _create_time = d.pop("create_time", UNSET)
        create_time: datetime.datetime | Unset
        if isinstance(_create_time, Unset):
            create_time = UNSET
        else:
            create_time = datetime.datetime.fromisoformat(_create_time)

        result = d.pop("result", UNSET)

        _result_codes = d.pop("result_codes", UNSET)
        result_codes: list[DatabaseServiceTaskBaseResponseResultCodesItem] | Unset = UNSET
        if _result_codes is not UNSET:
            result_codes = []
            for result_codes_item_data in _result_codes:
                result_codes_item = DatabaseServiceTaskBaseResponseResultCodesItem.from_dict(result_codes_item_data)

                result_codes.append(result_codes_item)

        ignore_dbs = d.pop("ignore_dbs", UNSET)

        operation = d.pop("operation", UNSET)

        success = d.pop("success", UNSET)

        method = d.pop("method", UNSET)

        source_pg_version = d.pop("source_pg_version", UNSET)

        target_pg_version = d.pop("target_pg_version", UNSET)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        database_service_task_details_response = cls(
            create_time=create_time,
            result=result,
            result_codes=result_codes,
            ignore_dbs=ignore_dbs,
            operation=operation,
            success=success,
            method=method,
            source_pg_version=source_pg_version,
            target_pg_version=target_pg_version,
            id=id,
        )

        database_service_task_details_response.additional_properties = d
        return database_service_task_details_response

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
