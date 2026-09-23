from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ObjectStorage2MetricsSeriesListResponseItem")


@_attrs_define
class ObjectStorage2MetricsSeriesListResponseItem:
    """
    Attributes:
        bytes_created (int | Unset):
        bytes_deleted (int | Unset):
        bytes_received (int | Unset):
        bytes_total (int | Unset):
        bytes_transmitted (int | Unset):
        end_at (datetime.datetime | Unset):
        objects_created (int | Unset):
        objects_deleted (int | Unset):
        objects_total (int | Unset):
        start_at (datetime.datetime | Unset):
    """

    bytes_created: int | Unset = UNSET
    bytes_deleted: int | Unset = UNSET
    bytes_received: int | Unset = UNSET
    bytes_total: int | Unset = UNSET
    bytes_transmitted: int | Unset = UNSET
    end_at: datetime.datetime | Unset = UNSET
    objects_created: int | Unset = UNSET
    objects_deleted: int | Unset = UNSET
    objects_total: int | Unset = UNSET
    start_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bytes_created = self.bytes_created

        bytes_deleted = self.bytes_deleted

        bytes_received = self.bytes_received

        bytes_total = self.bytes_total

        bytes_transmitted = self.bytes_transmitted

        end_at: str | Unset = UNSET
        if not isinstance(self.end_at, Unset):
            end_at = self.end_at.isoformat()

        objects_created = self.objects_created

        objects_deleted = self.objects_deleted

        objects_total = self.objects_total

        start_at: str | Unset = UNSET
        if not isinstance(self.start_at, Unset):
            start_at = self.start_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bytes_created is not UNSET:
            field_dict["bytes_created"] = bytes_created
        if bytes_deleted is not UNSET:
            field_dict["bytes_deleted"] = bytes_deleted
        if bytes_received is not UNSET:
            field_dict["bytes_received"] = bytes_received
        if bytes_total is not UNSET:
            field_dict["bytes_total"] = bytes_total
        if bytes_transmitted is not UNSET:
            field_dict["bytes_transmitted"] = bytes_transmitted
        if end_at is not UNSET:
            field_dict["end_at"] = end_at
        if objects_created is not UNSET:
            field_dict["objects_created"] = objects_created
        if objects_deleted is not UNSET:
            field_dict["objects_deleted"] = objects_deleted
        if objects_total is not UNSET:
            field_dict["objects_total"] = objects_total
        if start_at is not UNSET:
            field_dict["start_at"] = start_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bytes_created = d.pop("bytes_created", UNSET)

        bytes_deleted = d.pop("bytes_deleted", UNSET)

        bytes_received = d.pop("bytes_received", UNSET)

        bytes_total = d.pop("bytes_total", UNSET)

        bytes_transmitted = d.pop("bytes_transmitted", UNSET)

        _end_at = d.pop("end_at", UNSET)
        end_at: datetime.datetime | Unset
        if isinstance(_end_at, Unset):
            end_at = UNSET
        else:
            end_at = datetime.datetime.fromisoformat(_end_at)

        objects_created = d.pop("objects_created", UNSET)

        objects_deleted = d.pop("objects_deleted", UNSET)

        objects_total = d.pop("objects_total", UNSET)

        _start_at = d.pop("start_at", UNSET)
        start_at: datetime.datetime | Unset
        if isinstance(_start_at, Unset):
            start_at = UNSET
        else:
            start_at = datetime.datetime.fromisoformat(_start_at)

        object_storage_2_metrics_series_list_response_item = cls(
            bytes_created=bytes_created,
            bytes_deleted=bytes_deleted,
            bytes_received=bytes_received,
            bytes_total=bytes_total,
            bytes_transmitted=bytes_transmitted,
            end_at=end_at,
            objects_created=objects_created,
            objects_deleted=objects_deleted,
            objects_total=objects_total,
            start_at=start_at,
        )

        object_storage_2_metrics_series_list_response_item.additional_properties = d
        return object_storage_2_metrics_series_list_response_item

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
