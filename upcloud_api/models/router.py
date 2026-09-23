from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.router_details import RouterDetails


T = TypeVar("T", bound="Router")


@_attrs_define
class Router:
    """Schema for a single router

    Attributes:
        router (RouterDetails): Router describes a virtual router that can route between SDN networks Example:
            {'attached_network_gateways': [], 'attached_networks': {'network': [{'uuid':
            '03804f7f-828a-4610-867f-9d62cf9fc14f'}]}, 'name': 'Example router', 'static_routes': [{'name': 'static-
            route-0', 'nexthop': '192.168.1.1', 'route': '0.0.0.0/0', 'type': 'user'}], 'labels': [], 'type': 'normal',
            'uuid': '0414e0d7-4436-4037-9dd8-6eaf47dce599'}.
    """

    router: RouterDetails

    def to_dict(self) -> dict[str, Any]:
        router = self.router.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "router": router,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.router_details import RouterDetails  # noqa: PLC0415

        d = dict(src_dict)
        router = RouterDetails.from_dict(d.pop("router"))

        router = cls(
            router=router,
        )

        return router
