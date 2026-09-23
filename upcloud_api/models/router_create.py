from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.router_create_router import RouterCreateRouter


T = TypeVar("T", bound="RouterCreate")


@_attrs_define
class RouterCreate:
    """Request schema for creating a router

    Example:
        {'router': {'name': 'Example router', 'static_routes': [{'name': 'static-route-0', 'nexthop': '192.168.1.1',
            'route': '0.0.0.0/0'}]}}

    Attributes:
        router (RouterCreateRouter):  Example: {'name': 'Example router', 'static_routes': [{'name': 'static-route-0',
            'nexthop': '192.168.1.1', 'route': '0.0.0.0/0'}]}.
    """

    router: RouterCreateRouter

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
        from ..models.router_create_router import RouterCreateRouter  # noqa: PLC0415

        d = dict(src_dict)
        router = RouterCreateRouter.from_dict(d.pop("router"))

        router_create = cls(
            router=router,
        )

        return router_create
