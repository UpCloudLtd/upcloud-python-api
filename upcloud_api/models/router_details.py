from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.router_type import RouterType

if TYPE_CHECKING:
    from ..models.router_details_attached_network_gateways_item import RouterDetailsAttachedNetworkGatewaysItem
    from ..models.router_details_attached_networks import RouterDetailsAttachedNetworks
    from ..models.router_label import RouterLabel
    from ..models.router_route_nexthop import RouterRouteNexthop


T = TypeVar("T", bound="RouterDetails")


@_attrs_define
class RouterDetails:
    """Router describes a virtual router that can route between SDN networks

    Example:
        {'attached_network_gateways': [], 'attached_networks': {'network': [{'uuid':
            '03804f7f-828a-4610-867f-9d62cf9fc14f'}]}, 'name': 'Example router', 'static_routes': [{'name': 'static-
            route-0', 'nexthop': '192.168.1.1', 'route': '0.0.0.0/0', 'type': 'user'}], 'labels': [], 'type': 'normal',
            'uuid': '0414e0d7-4436-4037-9dd8-6eaf47dce599'}

    Attributes:
        attached_network_gateways (list[RouterDetailsAttachedNetworkGatewaysItem]): Gateways of the networks attached to
            the router.
        attached_networks (RouterDetailsAttachedNetworks): Networks attached to the router. Example: {'network':
            [{'uuid': '03804f7f-828a-4610-867f-9d62cf9fc14f'}]}.
        labels (list[RouterLabel]):
        name (str):  Example: Example router.
        static_routes (list[RouterRouteNexthop]):  Example: [{'name': 'static-route-0', 'nexthop': '192.168.1.1',
            'route': '0.0.0.0/0', 'type': 'user'}].
        type_ (RouterType): Type of the router. Example: normal.
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
    """

    attached_network_gateways: list[RouterDetailsAttachedNetworkGatewaysItem]
    attached_networks: RouterDetailsAttachedNetworks
    labels: list[RouterLabel]
    name: str
    static_routes: list[RouterRouteNexthop]
    type_: RouterType
    uuid: UUID

    def to_dict(self) -> dict[str, Any]:
        attached_network_gateways = []
        for attached_network_gateways_item_data in self.attached_network_gateways:
            attached_network_gateways_item = attached_network_gateways_item_data.to_dict()
            attached_network_gateways.append(attached_network_gateways_item)

        attached_networks = self.attached_networks.to_dict()

        labels = []
        for labels_item_data in self.labels:
            labels_item = labels_item_data.to_dict()
            labels.append(labels_item)

        name = self.name

        static_routes = []
        for static_routes_item_data in self.static_routes:
            static_routes_item = static_routes_item_data.to_dict()
            static_routes.append(static_routes_item)

        type_ = self.type_.value

        uuid = str(self.uuid)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "attached_network_gateways": attached_network_gateways,
                "attached_networks": attached_networks,
                "labels": labels,
                "name": name,
                "static_routes": static_routes,
                "type": type_,
                "uuid": uuid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.router_details_attached_network_gateways_item import (
            RouterDetailsAttachedNetworkGatewaysItem,  # noqa: PLC0415
        )
        from ..models.router_details_attached_networks import RouterDetailsAttachedNetworks  # noqa: PLC0415
        from ..models.router_label import RouterLabel  # noqa: PLC0415
        from ..models.router_route_nexthop import RouterRouteNexthop  # noqa: PLC0415

        d = dict(src_dict)
        attached_network_gateways = []
        _attached_network_gateways = d.pop("attached_network_gateways")
        for attached_network_gateways_item_data in _attached_network_gateways:
            attached_network_gateways_item = RouterDetailsAttachedNetworkGatewaysItem.from_dict(
                attached_network_gateways_item_data
            )

            attached_network_gateways.append(attached_network_gateways_item)

        attached_networks = RouterDetailsAttachedNetworks.from_dict(d.pop("attached_networks"))

        labels = []
        _labels = d.pop("labels")
        for labels_item_data in _labels:
            labels_item = RouterLabel.from_dict(labels_item_data)

            labels.append(labels_item)

        name = d.pop("name")

        static_routes = []
        _static_routes = d.pop("static_routes")
        for static_routes_item_data in _static_routes:
            static_routes_item = RouterRouteNexthop.from_dict(static_routes_item_data)

            static_routes.append(static_routes_item)

        type_ = RouterType(d.pop("type"))

        uuid = UUID(d.pop("uuid"))

        router_details = cls(
            attached_network_gateways=attached_network_gateways,
            attached_networks=attached_networks,
            labels=labels,
            name=name,
            static_routes=static_routes,
            type_=type_,
            uuid=uuid,
        )

        return router_details
