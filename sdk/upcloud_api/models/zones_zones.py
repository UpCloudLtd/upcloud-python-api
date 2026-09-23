from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.zones_zones_zone_item import ZonesZonesZoneItem


T = TypeVar("T", bound="ZonesZones")


@_attrs_define
class ZonesZones:
    """
    Example:
        {'zone': [{'id': 'de-fra1', 'description': 'Germany, Frankfurt', 'public': 'yes'}]}

    Attributes:
        zone (list[ZonesZonesZoneItem]):  Example: [{'id': 'de-fra1', 'description': 'Germany, Frankfurt', 'public':
            'yes'}].
    """

    zone: list[ZonesZonesZoneItem]

    def to_dict(self) -> dict[str, Any]:
        zone = []
        for zone_item_data in self.zone:
            zone_item = zone_item_data.to_dict()
            zone.append(zone_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "zone": zone,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.zones_zones_zone_item import ZonesZonesZoneItem  # noqa: PLC0415

        d = dict(src_dict)
        zone = []
        _zone = d.pop("zone")
        for zone_item_data in _zone:
            zone_item = ZonesZonesZoneItem.from_dict(zone_item_data)

            zone.append(zone_item)

        zones_zones = cls(
            zone=zone,
        )

        return zones_zones
