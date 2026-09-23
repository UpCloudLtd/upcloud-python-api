from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.router_create_router_static_routes_item import RouterCreateRouterStaticRoutesItem
    from ..models.router_label import RouterLabel


T = TypeVar("T", bound="RouterCreateRouter")


@_attrs_define
class RouterCreateRouter:
    """
    Example:
        {'name': 'Example router', 'static_routes': [{'name': 'static-route-0', 'nexthop': '192.168.1.1', 'route':
            '0.0.0.0/0'}]}

    Attributes:
        name (str):  Example: Example router.
        static_routes (list[RouterCreateRouterStaticRoutesItem] | Unset): Static routes that will be added to the
            routing table of the SDN router Example: [{'name': 'static-route-0', 'nexthop': '192.168.1.1', 'route':
            '0.0.0.0/0'}].
        labels (list[RouterLabel] | Unset):
    """

    name: str
    static_routes: list[RouterCreateRouterStaticRoutesItem] | Unset = UNSET
    labels: list[RouterLabel] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        static_routes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.static_routes, Unset):
            static_routes = []
            for static_routes_item_data in self.static_routes:
                static_routes_item = static_routes_item_data.to_dict()
                static_routes.append(static_routes_item)

        labels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()
                labels.append(labels_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )
        if static_routes is not UNSET:
            field_dict["static_routes"] = static_routes
        if labels is not UNSET:
            field_dict["labels"] = labels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.router_create_router_static_routes_item import RouterCreateRouterStaticRoutesItem  # noqa: PLC0415
        from ..models.router_label import RouterLabel  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        _static_routes = d.pop("static_routes", UNSET)
        static_routes: list[RouterCreateRouterStaticRoutesItem] | Unset = UNSET
        if _static_routes is not UNSET:
            static_routes = []
            for static_routes_item_data in _static_routes:
                static_routes_item = RouterCreateRouterStaticRoutesItem.from_dict(static_routes_item_data)

                static_routes.append(static_routes_item)

        _labels = d.pop("labels", UNSET)
        labels: list[RouterLabel] | Unset = UNSET
        if _labels is not UNSET:
            labels = []
            for labels_item_data in _labels:
                labels_item = RouterLabel.from_dict(labels_item_data)

                labels.append(labels_item)

        router_create_router = cls(
            name=name,
            static_routes=static_routes,
            labels=labels,
        )

        return router_create_router
