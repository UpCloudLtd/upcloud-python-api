from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.router_route_nexthop_nexthop_type_1 import RouterRouteNexthopNexthopType1
from ..models.router_static_route_type import RouterStaticRouteType

T = TypeVar("T", bound="RouterRouteNexthop")


@_attrs_define
class RouterRouteNexthop:
    """Static route with nexthop information.

    Attributes:
        name (str):
        nexthop (RouterRouteNexthopNexthopType1 | str):
        route (str): IP CIDR
        type_ (RouterStaticRouteType): Type of static route. Example: user.
    """

    name: str
    nexthop: RouterRouteNexthopNexthopType1 | str
    route: str
    type_: RouterStaticRouteType

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        nexthop: str
        if isinstance(self.nexthop, RouterRouteNexthopNexthopType1):
            nexthop = self.nexthop.value
        else:
            nexthop = self.nexthop

        route = self.route

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "nexthop": nexthop,
                "route": route,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_nexthop(data: object) -> RouterRouteNexthopNexthopType1 | str:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                nexthop_type_1 = RouterRouteNexthopNexthopType1(data)

                return nexthop_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(RouterRouteNexthopNexthopType1 | str, data)

        nexthop = _parse_nexthop(d.pop("nexthop"))

        route = d.pop("route")

        type_ = RouterStaticRouteType(d.pop("type"))

        router_route_nexthop = cls(
            name=name,
            nexthop=nexthop,
            route=route,
            type_=type_,
        )

        return router_route_nexthop
