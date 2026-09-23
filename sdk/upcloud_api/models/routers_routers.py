from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.router_details import RouterDetails


T = TypeVar("T", bound="RoutersRouters")


@_attrs_define
class RoutersRouters:
    """
    Example:
        {'router': [{'attached_network_gateways': [], 'attached_networks': {'network': []}, 'labels': [], 'name':
            'Example router', 'static_routes': [], 'type': 'normal', 'uuid': '04c0df35-2658-4b0c-8ac7-962090f4e92a'}]}

    Attributes:
        router (list[RouterDetails]):
    """

    router: list[RouterDetails]

    def to_dict(self) -> dict[str, Any]:
        router = []
        for router_item_data in self.router:
            router_item = router_item_data.to_dict()
            router.append(router_item)

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
        router = []
        _router = d.pop("router")
        for router_item_data in _router:
            router_item = RouterDetails.from_dict(router_item_data)

            router.append(router_item)

        routers_routers = cls(
            router=router,
        )

        return routers_routers
