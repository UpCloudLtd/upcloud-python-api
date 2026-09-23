from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gateway_ipsec_ike_sa_metrics_details_response import GatewayIpsecIkeSaMetricsDetailsResponse


T = TypeVar("T", bound="GatewayIpsecMetricsDetailsResponse")


@_attrs_define
class GatewayIpsecMetricsDetailsResponse:
    """Response schema for IPsec IKE SA metrics details.

    Attributes:
        ike_sas (list[GatewayIpsecIkeSaMetricsDetailsResponse] | None | Unset): List of IKE SAs
    """

    ike_sas: list[GatewayIpsecIkeSaMetricsDetailsResponse] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ike_sas: list[dict[str, Any]] | None | Unset
        if isinstance(self.ike_sas, Unset):
            ike_sas = UNSET
        elif isinstance(self.ike_sas, list):
            ike_sas = []
            for ike_sas_type_0_item_data in self.ike_sas:
                ike_sas_type_0_item = ike_sas_type_0_item_data.to_dict()
                ike_sas.append(ike_sas_type_0_item)

        else:
            ike_sas = self.ike_sas

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ike_sas is not UNSET:
            field_dict["ike_sas"] = ike_sas

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gateway_ipsec_ike_sa_metrics_details_response import (
            GatewayIpsecIkeSaMetricsDetailsResponse,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_ike_sas(data: object) -> list[GatewayIpsecIkeSaMetricsDetailsResponse] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ike_sas_type_0 = []
                _ike_sas_type_0 = data
                for ike_sas_type_0_item_data in _ike_sas_type_0:
                    ike_sas_type_0_item = GatewayIpsecIkeSaMetricsDetailsResponse.from_dict(ike_sas_type_0_item_data)

                    ike_sas_type_0.append(ike_sas_type_0_item)

                return ike_sas_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GatewayIpsecIkeSaMetricsDetailsResponse] | None | Unset, data)

        ike_sas = _parse_ike_sas(d.pop("ike_sas", UNSET))

        gateway_ipsec_metrics_details_response = cls(
            ike_sas=ike_sas,
        )

        gateway_ipsec_metrics_details_response.additional_properties = d
        return gateway_ipsec_metrics_details_response

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
