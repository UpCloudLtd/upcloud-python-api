from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gateway_ipsec_metrics_details_response import GatewayIpsecMetricsDetailsResponse
    from ..models.gateway_metrics_details_response import GatewayMetricsDetailsResponse


T = TypeVar("T", bound="GatewayServiceMetricsResponse")


@_attrs_define
class GatewayServiceMetricsResponse:
    """Response schema for service metrics.

    Attributes:
        gateways (list[GatewayMetricsDetailsResponse] | Unset):
        ipsec_metrics (GatewayIpsecMetricsDetailsResponse | Unset): Response schema for IPsec IKE SA metrics details.
    """

    gateways: list[GatewayMetricsDetailsResponse] | Unset = UNSET
    ipsec_metrics: GatewayIpsecMetricsDetailsResponse | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gateways: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.gateways, Unset):
            gateways = []
            for gateways_item_data in self.gateways:
                gateways_item = gateways_item_data.to_dict()
                gateways.append(gateways_item)

        ipsec_metrics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ipsec_metrics, Unset):
            ipsec_metrics = self.ipsec_metrics.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gateways is not UNSET:
            field_dict["gateways"] = gateways
        if ipsec_metrics is not UNSET:
            field_dict["ipsec_metrics"] = ipsec_metrics

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gateway_ipsec_metrics_details_response import GatewayIpsecMetricsDetailsResponse  # noqa: PLC0415
        from ..models.gateway_metrics_details_response import GatewayMetricsDetailsResponse  # noqa: PLC0415

        d = dict(src_dict)
        _gateways = d.pop("gateways", UNSET)
        gateways: list[GatewayMetricsDetailsResponse] | Unset = UNSET
        if _gateways is not UNSET:
            gateways = []
            for gateways_item_data in _gateways:
                gateways_item = GatewayMetricsDetailsResponse.from_dict(gateways_item_data)

                gateways.append(gateways_item)

        _ipsec_metrics = d.pop("ipsec_metrics", UNSET)
        ipsec_metrics: GatewayIpsecMetricsDetailsResponse | Unset
        if isinstance(_ipsec_metrics, Unset):
            ipsec_metrics = UNSET
        else:
            ipsec_metrics = GatewayIpsecMetricsDetailsResponse.from_dict(_ipsec_metrics)

        gateway_service_metrics_response = cls(
            gateways=gateways,
            ipsec_metrics=ipsec_metrics,
        )

        gateway_service_metrics_response.additional_properties = d
        return gateway_service_metrics_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
