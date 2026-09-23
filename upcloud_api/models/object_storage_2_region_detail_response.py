from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.object_storage_2_region_detail_response_zones_item import ObjectStorage2RegionDetailResponseZonesItem


T = TypeVar("T", bound="ObjectStorage2RegionDetailResponse")


@_attrs_define
class ObjectStorage2RegionDetailResponse:
    """Response schema for detailed information about a specific region.

    Attributes:
        name (str | Unset):  Example: europe-1.
        primary_zone (str | Unset):  Example: fi-hel1.
        zones (list[ObjectStorage2RegionDetailResponseZonesItem] | Unset):
    """

    name: str | Unset = UNSET
    primary_zone: str | Unset = UNSET
    zones: list[ObjectStorage2RegionDetailResponseZonesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        primary_zone = self.primary_zone

        zones: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.zones, Unset):
            zones = []
            for zones_item_data in self.zones:
                zones_item = zones_item_data.to_dict()
                zones.append(zones_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if primary_zone is not UNSET:
            field_dict["primary_zone"] = primary_zone
        if zones is not UNSET:
            field_dict["zones"] = zones

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.object_storage_2_region_detail_response_zones_item import (
            ObjectStorage2RegionDetailResponseZonesItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        primary_zone = d.pop("primary_zone", UNSET)

        _zones = d.pop("zones", UNSET)
        zones: list[ObjectStorage2RegionDetailResponseZonesItem] | Unset = UNSET
        if _zones is not UNSET:
            zones = []
            for zones_item_data in _zones:
                zones_item = ObjectStorage2RegionDetailResponseZonesItem.from_dict(zones_item_data)

                zones.append(zones_item)

        object_storage_2_region_detail_response = cls(
            name=name,
            primary_zone=primary_zone,
            zones=zones,
        )

        object_storage_2_region_detail_response.additional_properties = d
        return object_storage_2_region_detail_response

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
