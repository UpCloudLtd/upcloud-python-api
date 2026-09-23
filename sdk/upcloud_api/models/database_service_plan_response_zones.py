from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_zone_info_response import DatabaseZoneInfoResponse


T = TypeVar("T", bound="DatabaseServicePlanResponseZones")


@_attrs_define
class DatabaseServicePlanResponseZones:
    """
    Attributes:
        zone (list[DatabaseZoneInfoResponse] | Unset):
    """

    zone: list[DatabaseZoneInfoResponse] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        zone: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.zone, Unset):
            zone = []
            for zone_item_data in self.zone:
                zone_item = zone_item_data.to_dict()
                zone.append(zone_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if zone is not UNSET:
            field_dict["zone"] = zone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_zone_info_response import DatabaseZoneInfoResponse  # noqa: PLC0415

        d = dict(src_dict)
        _zone = d.pop("zone", UNSET)
        zone: list[DatabaseZoneInfoResponse] | Unset = UNSET
        if _zone is not UNSET:
            zone = []
            for zone_item_data in _zone:
                zone_item = DatabaseZoneInfoResponse.from_dict(zone_item_data)

                zone.append(zone_item)

        database_service_plan_response_zones = cls(
            zone=zone,
        )

        database_service_plan_response_zones.additional_properties = d
        return database_service_plan_response_zones

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
