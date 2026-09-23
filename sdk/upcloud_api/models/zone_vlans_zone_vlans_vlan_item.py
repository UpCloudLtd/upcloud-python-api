from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.zone_boolean_01 import ZoneBoolean01

T = TypeVar("T", bound="ZoneVlansZoneVlansVlanItem")


@_attrs_define
class ZoneVlansZoneVlansVlanItem:
    """
    Attributes:
        id (int):
        access (str):
        description (str):
        default (ZoneBoolean01): Schema for boolean-like values encoded as 0 or 1.
    """

    id: int
    access: str
    description: str
    default: ZoneBoolean01

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        access = self.access

        description = self.description

        default = self.default.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "access": access,
                "description": description,
                "default": default,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        access = d.pop("access")

        description = d.pop("description")

        default = ZoneBoolean01(d.pop("default"))

        zone_vlans_zone_vlans_vlan_item = cls(
            id=id,
            access=access,
            description=description,
            default=default,
        )

        return zone_vlans_zone_vlans_vlan_item
