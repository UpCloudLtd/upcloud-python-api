from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.database_versions_response_item_service_type import DatabaseVersionsResponseItemServiceType
from ..models.database_versions_response_item_state import DatabaseVersionsResponseItemState
from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseVersionsResponseItem")


@_attrs_define
class DatabaseVersionsResponseItem:
    """
    Attributes:
        major_version (str): The major version of the service Example: 16.
        service_type (DatabaseVersionsResponseItemServiceType): The type of service (e.g., mysql, pg, opensearch,
            valkey) Example: pg.
        state (DatabaseVersionsResponseItemState): The availability state of the version Example: available.
        end_of_life_time (datetime.datetime | None | Unset): The date when this version reaches end of life Example:
            2028-11-09T00:00:00Z.
        availability_end_time (datetime.datetime | None | Unset): The date when this version will no longer be available
            for new services Example: 2028-05-09T00:00:00Z.
        availability_start_time (datetime.datetime | None | Unset): The date when this version became available Example:
            2024-01-08T00:00:00Z.
        termination_time (datetime.datetime | None | Unset): The date when services running this version will be
            terminated Example: 2028-11-09T00:00:00Z.
        upgrade_to_service_type (datetime.datetime | None | Unset): The service type to upgrade to when this version
            reaches end of life Example: 2028-11-09T00:00:00Z.
        upgrade_to_version (None | str | Unset): The version to upgrade to when this version reaches end of life
            Example: 2.
        upstream_end_of_life_time (datetime.datetime | None | Unset): The upstream end of life date for this version
            Example: 2028-11-09T00:00:00Z.
    """

    major_version: str
    service_type: DatabaseVersionsResponseItemServiceType
    state: DatabaseVersionsResponseItemState
    end_of_life_time: datetime.datetime | None | Unset = UNSET
    availability_end_time: datetime.datetime | None | Unset = UNSET
    availability_start_time: datetime.datetime | None | Unset = UNSET
    termination_time: datetime.datetime | None | Unset = UNSET
    upgrade_to_service_type: datetime.datetime | None | Unset = UNSET
    upgrade_to_version: None | str | Unset = UNSET
    upstream_end_of_life_time: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        major_version = self.major_version

        service_type = self.service_type.value

        state = self.state.value

        end_of_life_time: None | str | Unset
        if isinstance(self.end_of_life_time, Unset):
            end_of_life_time = UNSET
        elif isinstance(self.end_of_life_time, datetime.datetime):
            end_of_life_time = self.end_of_life_time.isoformat()
        else:
            end_of_life_time = self.end_of_life_time

        availability_end_time: None | str | Unset
        if isinstance(self.availability_end_time, Unset):
            availability_end_time = UNSET
        elif isinstance(self.availability_end_time, datetime.datetime):
            availability_end_time = self.availability_end_time.isoformat()
        else:
            availability_end_time = self.availability_end_time

        availability_start_time: None | str | Unset
        if isinstance(self.availability_start_time, Unset):
            availability_start_time = UNSET
        elif isinstance(self.availability_start_time, datetime.datetime):
            availability_start_time = self.availability_start_time.isoformat()
        else:
            availability_start_time = self.availability_start_time

        termination_time: None | str | Unset
        if isinstance(self.termination_time, Unset):
            termination_time = UNSET
        elif isinstance(self.termination_time, datetime.datetime):
            termination_time = self.termination_time.isoformat()
        else:
            termination_time = self.termination_time

        upgrade_to_service_type: None | str | Unset
        if isinstance(self.upgrade_to_service_type, Unset):
            upgrade_to_service_type = UNSET
        elif isinstance(self.upgrade_to_service_type, datetime.datetime):
            upgrade_to_service_type = self.upgrade_to_service_type.isoformat()
        else:
            upgrade_to_service_type = self.upgrade_to_service_type

        upgrade_to_version: None | str | Unset
        if isinstance(self.upgrade_to_version, Unset):
            upgrade_to_version = UNSET
        else:
            upgrade_to_version = self.upgrade_to_version

        upstream_end_of_life_time: None | str | Unset
        if isinstance(self.upstream_end_of_life_time, Unset):
            upstream_end_of_life_time = UNSET
        elif isinstance(self.upstream_end_of_life_time, datetime.datetime):
            upstream_end_of_life_time = self.upstream_end_of_life_time.isoformat()
        else:
            upstream_end_of_life_time = self.upstream_end_of_life_time

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "major_version": major_version,
                "service_type": service_type,
                "state": state,
            }
        )
        if end_of_life_time is not UNSET:
            field_dict["end_of_life_time"] = end_of_life_time
        if availability_end_time is not UNSET:
            field_dict["availability_end_time"] = availability_end_time
        if availability_start_time is not UNSET:
            field_dict["availability_start_time"] = availability_start_time
        if termination_time is not UNSET:
            field_dict["termination_time"] = termination_time
        if upgrade_to_service_type is not UNSET:
            field_dict["upgrade_to_service_type"] = upgrade_to_service_type
        if upgrade_to_version is not UNSET:
            field_dict["upgrade_to_version"] = upgrade_to_version
        if upstream_end_of_life_time is not UNSET:
            field_dict["upstream_end_of_life_time"] = upstream_end_of_life_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        major_version = d.pop("major_version")

        service_type = DatabaseVersionsResponseItemServiceType(d.pop("service_type"))

        state = DatabaseVersionsResponseItemState(d.pop("state"))

        def _parse_end_of_life_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_of_life_time_type_0 = datetime.datetime.fromisoformat(data)

                return end_of_life_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        end_of_life_time = _parse_end_of_life_time(d.pop("end_of_life_time", UNSET))

        def _parse_availability_end_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                availability_end_time_type_0 = datetime.datetime.fromisoformat(data)

                return availability_end_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        availability_end_time = _parse_availability_end_time(d.pop("availability_end_time", UNSET))

        def _parse_availability_start_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                availability_start_time_type_0 = datetime.datetime.fromisoformat(data)

                return availability_start_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        availability_start_time = _parse_availability_start_time(d.pop("availability_start_time", UNSET))

        def _parse_termination_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                termination_time_type_0 = datetime.datetime.fromisoformat(data)

                return termination_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        termination_time = _parse_termination_time(d.pop("termination_time", UNSET))

        def _parse_upgrade_to_service_type(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                upgrade_to_service_type_type_0 = datetime.datetime.fromisoformat(data)

                return upgrade_to_service_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        upgrade_to_service_type = _parse_upgrade_to_service_type(d.pop("upgrade_to_service_type", UNSET))

        def _parse_upgrade_to_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        upgrade_to_version = _parse_upgrade_to_version(d.pop("upgrade_to_version", UNSET))

        def _parse_upstream_end_of_life_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                upstream_end_of_life_time_type_0 = datetime.datetime.fromisoformat(data)

                return upstream_end_of_life_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        upstream_end_of_life_time = _parse_upstream_end_of_life_time(d.pop("upstream_end_of_life_time", UNSET))

        database_versions_response_item = cls(
            major_version=major_version,
            service_type=service_type,
            state=state,
            end_of_life_time=end_of_life_time,
            availability_end_time=availability_end_time,
            availability_start_time=availability_start_time,
            termination_time=termination_time,
            upgrade_to_service_type=upgrade_to_service_type,
            upgrade_to_version=upgrade_to_version,
            upstream_end_of_life_time=upstream_end_of_life_time,
        )

        return database_versions_response_item
