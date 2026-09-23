from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.router_modify_router import RouterModifyRouter


T = TypeVar("T", bound="RouterModify")


@_attrs_define
class RouterModify:
    """Request schema for modifying a router

    Example:
        {'router': {'name': 'Example router', 'labels': [{'key': 'service', 'value': 'postgres cluster connectivity'}],
            'static_routes': []}}

    Attributes:
        router (RouterModifyRouter):  Example: {'name': 'Example router', 'static_routes': [{'name': 'static-route-0',
            'nexthop': '192.168.1.1', 'route': '0.0.0.0/0'}]}.
    """

    router: RouterModifyRouter

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
        from ..models.router_modify_router import RouterModifyRouter  # noqa: PLC0415

        d = dict(src_dict)
        router = RouterModifyRouter.from_dict(d.pop("router"))

        router_modify = cls(
            router=router,
        )

        return router_modify
