from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="RelocateServer")


@_attrs_define
class RelocateServer:
    """Relocate Cloud Server request

    Example:
        {'zone': 'fi-hel2'}

    Attributes:
        zone (str): Zone identifier
    """

    zone: str

    def to_dict(self) -> dict[str, Any]:
        zone = self.zone

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "zone": zone,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        zone = d.pop("zone")

        relocate_server = cls(
            zone=zone,
        )

        return relocate_server
