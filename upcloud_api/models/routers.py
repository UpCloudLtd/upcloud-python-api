from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.routers_routers import RoutersRouters


T = TypeVar("T", bound="Routers")


@_attrs_define
class Routers:
    """A list of routers

    Example:
        {'routers': {'router': [{'attached_network_gateways': [], 'attached_networks': {'network': []}, 'labels': [],
            'name': 'Example router', 'static_routes': [], 'type': 'normal', 'uuid':
            '04c0df35-2658-4b0c-8ac7-962090f4e92a'}]}}

    Attributes:
        routers (RoutersRouters):  Example: {'router': [{'attached_network_gateways': [], 'attached_networks':
            {'network': []}, 'labels': [], 'name': 'Example router', 'static_routes': [], 'type': 'normal', 'uuid':
            '04c0df35-2658-4b0c-8ac7-962090f4e92a'}]}.
    """

    routers: RoutersRouters

    def to_dict(self) -> dict[str, Any]:
        routers = self.routers.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "routers": routers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.routers_routers import RoutersRouters  # noqa: PLC0415

        d = dict(src_dict)
        routers = RoutersRouters.from_dict(d.pop("routers"))

        routers = cls(
            routers=routers,
        )

        return routers
