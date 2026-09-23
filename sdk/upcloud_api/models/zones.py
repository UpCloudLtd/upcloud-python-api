from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.zones_zones import ZonesZones


T = TypeVar("T", bound="Zones")


@_attrs_define
class Zones:
    """Zones schema

    Example:
        {'zones': {'zone': [{'id': 'de-fra1', 'description': 'Germany, Frankfurt', 'public': 'yes'}, {'id': 'fi-hel2',
            'description': 'Finland, Helsinki', 'public': 'no'}]}}

    Attributes:
        zones (ZonesZones):  Example: {'zone': [{'id': 'de-fra1', 'description': 'Germany, Frankfurt', 'public':
            'yes'}]}.
    """

    zones: ZonesZones

    def to_dict(self) -> dict[str, Any]:
        zones = self.zones.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "zones": zones,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.zones_zones import ZonesZones  # noqa: PLC0415

        d = dict(src_dict)
        zones = ZonesZones.from_dict(d.pop("zones"))

        zones = cls(
            zones=zones,
        )

        return zones
