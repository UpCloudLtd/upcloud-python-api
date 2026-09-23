from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseIndexResponse")


@_attrs_define
class DatabaseIndexResponse:
    """Schema representing the details of an index.

    Attributes:
        create_time (datetime.datetime | Unset): Creation time of the index. Example: 2023-05-11T13:24:10.623Z.
        docs (int | Unset): Number of documents in the index. Example: 1.
        health (str | Unset): Health status of the index. Example: green.
        index_name (str | Unset): Name of the index. Example: .kibana_1.
        number_of_replicas (int | Unset): Number of replicas for the index. Example: 1.
        number_of_shards (int | Unset): Number of shards for the index. Example: 1.
        read_only_allow_delete (bool | Unset): Indicates if the index is read-only and allows deletion. Example: False.
        size (int | Unset): Size of the index in bytes. Example: 5313.
        status (str | Unset): Status of the index. Example: open.
    """

    create_time: datetime.datetime | Unset = UNSET
    docs: int | Unset = UNSET
    health: str | Unset = UNSET
    index_name: str | Unset = UNSET
    number_of_replicas: int | Unset = UNSET
    number_of_shards: int | Unset = UNSET
    read_only_allow_delete: bool | Unset = UNSET
    size: int | Unset = UNSET
    status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        create_time: str | Unset = UNSET
        if not isinstance(self.create_time, Unset):
            create_time = self.create_time.isoformat()

        docs = self.docs

        health = self.health

        index_name = self.index_name

        number_of_replicas = self.number_of_replicas

        number_of_shards = self.number_of_shards

        read_only_allow_delete = self.read_only_allow_delete

        size = self.size

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if create_time is not UNSET:
            field_dict["create_time"] = create_time
        if docs is not UNSET:
            field_dict["docs"] = docs
        if health is not UNSET:
            field_dict["health"] = health
        if index_name is not UNSET:
            field_dict["index_name"] = index_name
        if number_of_replicas is not UNSET:
            field_dict["number_of_replicas"] = number_of_replicas
        if number_of_shards is not UNSET:
            field_dict["number_of_shards"] = number_of_shards
        if read_only_allow_delete is not UNSET:
            field_dict["read_only_allow_delete"] = read_only_allow_delete
        if size is not UNSET:
            field_dict["size"] = size
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _create_time = d.pop("create_time", UNSET)
        create_time: datetime.datetime | Unset
        if isinstance(_create_time, Unset):
            create_time = UNSET
        else:
            create_time = datetime.datetime.fromisoformat(_create_time)

        docs = d.pop("docs", UNSET)

        health = d.pop("health", UNSET)

        index_name = d.pop("index_name", UNSET)

        number_of_replicas = d.pop("number_of_replicas", UNSET)

        number_of_shards = d.pop("number_of_shards", UNSET)

        read_only_allow_delete = d.pop("read_only_allow_delete", UNSET)

        size = d.pop("size", UNSET)

        status = d.pop("status", UNSET)

        database_index_response = cls(
            create_time=create_time,
            docs=docs,
            health=health,
            index_name=index_name,
            number_of_replicas=number_of_replicas,
            number_of_shards=number_of_shards,
            read_only_allow_delete=read_only_allow_delete,
            size=size,
            status=status,
        )

        database_index_response.additional_properties = d
        return database_index_response

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
