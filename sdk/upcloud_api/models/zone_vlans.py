from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.zone_vlans_zone_vlans import ZoneVlansZoneVlans


T = TypeVar("T", bound="ZoneVlans")


@_attrs_define
class ZoneVlans:
    """Schema for zone VLANs

    Example:
        {'zone_vlans': {'vlan': [{'id': 100, 'access': 'public', 'description': 'default public vlan', 'default': 1}]}}

    Attributes:
        zone_vlans (ZoneVlansZoneVlans):  Example: {'vlan': [{'id': 100, 'access': 'public', 'description': 'default
            public vlan', 'default': 1}]}.
    """

    zone_vlans: ZoneVlansZoneVlans

    def to_dict(self) -> dict[str, Any]:
        zone_vlans = self.zone_vlans.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "zone_vlans": zone_vlans,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.zone_vlans_zone_vlans import ZoneVlansZoneVlans  # noqa: PLC0415

        d = dict(src_dict)
        zone_vlans = ZoneVlansZoneVlans.from_dict(d.pop("zone_vlans"))

        zone_vlans = cls(
            zone_vlans=zone_vlans,
        )

        return zone_vlans
