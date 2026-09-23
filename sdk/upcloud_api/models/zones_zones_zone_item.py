from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.zone_boolean_yesno import ZoneBooleanYesno

T = TypeVar("T", bound="ZonesZonesZoneItem")


@_attrs_define
class ZonesZonesZoneItem:
    """
    Attributes:
        description (str):
        id (str): Zone identifier
        public (ZoneBooleanYesno): Boolean value represented as yes/no Example: yes.
    """

    description: str
    id: str
    public: ZoneBooleanYesno

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        id = self.id

        public = self.public.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "description": description,
                "id": id,
                "public": public,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description")

        id = d.pop("id")

        public = ZoneBooleanYesno(d.pop("public"))

        zones_zones_zone_item = cls(
            description=description,
            id=id,
            public=public,
        )

        return zones_zones_zone_item
