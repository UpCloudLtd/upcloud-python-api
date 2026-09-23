from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.gateway_service_configured_status import GatewayServiceConfiguredStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gateway_label_create_request import GatewayLabelCreateRequest


T = TypeVar("T", bound="GatewayServiceReplaceRequest")


@_attrs_define
class GatewayServiceReplaceRequest:
    """Request to replace a gateway service

    Attributes:
        name (str): Name of the service
        configured_status (GatewayServiceConfiguredStatus): Service configured status
        plan (str | Unset): Plan
        connections (Any | Unset): Service connections
        labels (list[GatewayLabelCreateRequest] | Unset): Labels
        automatic_tunnel_internal_ip_allocation (bool | Unset): Allocate and use tunnel internal IPs automatically
    """

    name: str
    configured_status: GatewayServiceConfiguredStatus
    plan: str | Unset = UNSET
    connections: Any | Unset = UNSET
    labels: list[GatewayLabelCreateRequest] | Unset = UNSET
    automatic_tunnel_internal_ip_allocation: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        configured_status = self.configured_status.value

        plan = self.plan

        connections = self.connections

        labels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()
                labels.append(labels_item)

        automatic_tunnel_internal_ip_allocation = self.automatic_tunnel_internal_ip_allocation

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "configured_status": configured_status,
            }
        )
        if plan is not UNSET:
            field_dict["plan"] = plan
        if connections is not UNSET:
            field_dict["connections"] = connections
        if labels is not UNSET:
            field_dict["labels"] = labels
        if automatic_tunnel_internal_ip_allocation is not UNSET:
            field_dict["automatic_tunnel_internal_ip_allocation"] = automatic_tunnel_internal_ip_allocation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gateway_label_create_request import GatewayLabelCreateRequest  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        configured_status = GatewayServiceConfiguredStatus(d.pop("configured_status"))

        plan = d.pop("plan", UNSET)

        connections = d.pop("connections", UNSET)

        _labels = d.pop("labels", UNSET)
        labels: list[GatewayLabelCreateRequest] | Unset = UNSET
        if _labels is not UNSET:
            labels = []
            for labels_item_data in _labels:
                labels_item = GatewayLabelCreateRequest.from_dict(labels_item_data)

                labels.append(labels_item)

        automatic_tunnel_internal_ip_allocation = d.pop("automatic_tunnel_internal_ip_allocation", UNSET)

        gateway_service_replace_request = cls(
            name=name,
            configured_status=configured_status,
            plan=plan,
            connections=connections,
            labels=labels,
            automatic_tunnel_internal_ip_allocation=automatic_tunnel_internal_ip_allocation,
        )

        return gateway_service_replace_request
