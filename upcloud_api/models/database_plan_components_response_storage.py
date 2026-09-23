from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabasePlanComponentsResponseStorage")


@_attrs_define
class DatabasePlanComponentsResponseStorage:
    """Storage included in the plan. Omitted for service types without persistent storage.

    Attributes:
        included_gib (int | Unset): Storage included in the plan per node, in GB. Omitted for tiered (rdb.*) plans,
            which present storage as a single total_gib. Example: 100.
        dynamic_storage_supported (bool | Unset): Whether the storage total can be adjusted on top of the plan's
            included storage. Example: True.
        additional_gib (int | Unset): Extra dynamic storage configured on the service, in GB. Only present on legacy
            (non-tiered) service responses; tiered plans present total_gib instead. Example: 40.
        total_gib (int | Unset): Total storage, in GB. For tiered (rdb.*) plans this is the single storage number: the
            plan's base storage in the catalog, or the chosen total (included plus dynamic) on a service response. Omitted
            for legacy catalog plans. Example: 140.
    """

    included_gib: int | Unset = UNSET
    dynamic_storage_supported: bool | Unset = UNSET
    additional_gib: int | Unset = UNSET
    total_gib: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        included_gib = self.included_gib

        dynamic_storage_supported = self.dynamic_storage_supported

        additional_gib = self.additional_gib

        total_gib = self.total_gib

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if included_gib is not UNSET:
            field_dict["included_gib"] = included_gib
        if dynamic_storage_supported is not UNSET:
            field_dict["dynamic_storage_supported"] = dynamic_storage_supported
        if additional_gib is not UNSET:
            field_dict["additional_gib"] = additional_gib
        if total_gib is not UNSET:
            field_dict["total_gib"] = total_gib

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        included_gib = d.pop("included_gib", UNSET)

        dynamic_storage_supported = d.pop("dynamic_storage_supported", UNSET)

        additional_gib = d.pop("additional_gib", UNSET)

        total_gib = d.pop("total_gib", UNSET)

        database_plan_components_response_storage = cls(
            included_gib=included_gib,
            dynamic_storage_supported=dynamic_storage_supported,
            additional_gib=additional_gib,
            total_gib=total_gib,
        )

        database_plan_components_response_storage.additional_properties = d
        return database_plan_components_response_storage

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
