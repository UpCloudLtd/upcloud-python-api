from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.router_create_router_static_routes_item_nexthop_type_1 import (
    RouterCreateRouterStaticRoutesItemNexthopType1,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RouterCreateRouterStaticRoutesItem")


@_attrs_define
class RouterCreateRouterStaticRoutesItem:
    """
    Attributes:
        nexthop (RouterCreateRouterStaticRoutesItemNexthopType1 | str):
        route (str): IP CIDR
        name (str | Unset):
    """

    nexthop: RouterCreateRouterStaticRoutesItemNexthopType1 | str
    route: str
    name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        nexthop: str
        if isinstance(self.nexthop, RouterCreateRouterStaticRoutesItemNexthopType1):
            nexthop = self.nexthop.value
        else:
            nexthop = self.nexthop

        route = self.route

        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "nexthop": nexthop,
                "route": route,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_nexthop(data: object) -> RouterCreateRouterStaticRoutesItemNexthopType1 | str:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                nexthop_type_1 = RouterCreateRouterStaticRoutesItemNexthopType1(data)

                return nexthop_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(RouterCreateRouterStaticRoutesItemNexthopType1 | str, data)

        nexthop = _parse_nexthop(d.pop("nexthop"))

        route = d.pop("route")

        name = d.pop("name", UNSET)

        router_create_router_static_routes_item = cls(
            nexthop=nexthop,
            route=route,
            name=name,
        )

        return router_create_router_static_routes_item
