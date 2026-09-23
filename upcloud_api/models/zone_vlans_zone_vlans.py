from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.zone_vlans_zone_vlans_vlan_item import ZoneVlansZoneVlansVlanItem


T = TypeVar("T", bound="ZoneVlansZoneVlans")


@_attrs_define
class ZoneVlansZoneVlans:
    """
    Example:
        {'vlan': [{'id': 100, 'access': 'public', 'description': 'default public vlan', 'default': 1}]}

    Attributes:
        vlan (list[ZoneVlansZoneVlansVlanItem]):  Example: [{'id': 100, 'access': 'public', 'description': 'default
            public vlan', 'default': 1}].
    """

    vlan: list[ZoneVlansZoneVlansVlanItem]

    def to_dict(self) -> dict[str, Any]:
        vlan = []
        for vlan_item_data in self.vlan:
            vlan_item = vlan_item_data.to_dict()
            vlan.append(vlan_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "vlan": vlan,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.zone_vlans_zone_vlans_vlan_item import ZoneVlansZoneVlansVlanItem  # noqa: PLC0415

        d = dict(src_dict)
        vlan = []
        _vlan = d.pop("vlan")
        for vlan_item_data in _vlan:
            vlan_item = ZoneVlansZoneVlansVlanItem.from_dict(vlan_item_data)

            vlan.append(vlan_item)

        zone_vlans_zone_vlans = cls(
            vlan=vlan,
        )

        return zone_vlans_zone_vlans
