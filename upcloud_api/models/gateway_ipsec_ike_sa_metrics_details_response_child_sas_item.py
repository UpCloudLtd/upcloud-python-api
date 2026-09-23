from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gateway_ipsec_ike_sa_metrics_details_response_child_sas_item_state import (
    GatewayIpsecIkeSaMetricsDetailsResponseChildSasItemState,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GatewayIpsecIkeSaMetricsDetailsResponseChildSasItem")


@_attrs_define
class GatewayIpsecIkeSaMetricsDetailsResponseChildSasItem:
    """
    Attributes:
        name (str | Unset): Name of the child SA
        tunnel_id (int | Unset):
        unique_id (str | Unset): Unique ID of the child SA
        state (GatewayIpsecIkeSaMetricsDetailsResponseChildSasItemState | Unset): Operational state of the child SA
        spi_in (str | Unset):
        spi_out (str | Unset):
        bytes_in (int | Unset):
        bytes_out (int | Unset):
        packets_in (int | Unset):
        packets_out (int | Unset):
        rekey_time (int | Unset):
        life_time (int | Unset):
        install_time (int | Unset):
        local_traffic_selector (list[str] | Unset):
        remote_traffic_selector (list[str] | Unset):
        created_at (datetime.datetime | Unset): Timestamp of when the child SA was created.
        updated_at (datetime.datetime | Unset): Timestamp of when the child SA was last updated.
    """

    name: str | Unset = UNSET
    tunnel_id: int | Unset = UNSET
    unique_id: str | Unset = UNSET
    state: GatewayIpsecIkeSaMetricsDetailsResponseChildSasItemState | Unset = UNSET
    spi_in: str | Unset = UNSET
    spi_out: str | Unset = UNSET
    bytes_in: int | Unset = UNSET
    bytes_out: int | Unset = UNSET
    packets_in: int | Unset = UNSET
    packets_out: int | Unset = UNSET
    rekey_time: int | Unset = UNSET
    life_time: int | Unset = UNSET
    install_time: int | Unset = UNSET
    local_traffic_selector: list[str] | Unset = UNSET
    remote_traffic_selector: list[str] | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        tunnel_id = self.tunnel_id

        unique_id = self.unique_id

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        spi_in = self.spi_in

        spi_out = self.spi_out

        bytes_in = self.bytes_in

        bytes_out = self.bytes_out

        packets_in = self.packets_in

        packets_out = self.packets_out

        rekey_time = self.rekey_time

        life_time = self.life_time

        install_time = self.install_time

        local_traffic_selector: list[str] | Unset = UNSET
        if not isinstance(self.local_traffic_selector, Unset):
            local_traffic_selector = self.local_traffic_selector

        remote_traffic_selector: list[str] | Unset = UNSET
        if not isinstance(self.remote_traffic_selector, Unset):
            remote_traffic_selector = self.remote_traffic_selector

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if tunnel_id is not UNSET:
            field_dict["tunnel_id"] = tunnel_id
        if unique_id is not UNSET:
            field_dict["unique_id"] = unique_id
        if state is not UNSET:
            field_dict["state"] = state
        if spi_in is not UNSET:
            field_dict["spi_in"] = spi_in
        if spi_out is not UNSET:
            field_dict["spi_out"] = spi_out
        if bytes_in is not UNSET:
            field_dict["bytes_in"] = bytes_in
        if bytes_out is not UNSET:
            field_dict["bytes_out"] = bytes_out
        if packets_in is not UNSET:
            field_dict["packets_in"] = packets_in
        if packets_out is not UNSET:
            field_dict["packets_out"] = packets_out
        if rekey_time is not UNSET:
            field_dict["rekey_time"] = rekey_time
        if life_time is not UNSET:
            field_dict["life_time"] = life_time
        if install_time is not UNSET:
            field_dict["install_time"] = install_time
        if local_traffic_selector is not UNSET:
            field_dict["local_traffic_selector"] = local_traffic_selector
        if remote_traffic_selector is not UNSET:
            field_dict["remote_traffic_selector"] = remote_traffic_selector
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        tunnel_id = d.pop("tunnel_id", UNSET)

        unique_id = d.pop("unique_id", UNSET)

        _state = d.pop("state", UNSET)
        state: GatewayIpsecIkeSaMetricsDetailsResponseChildSasItemState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = GatewayIpsecIkeSaMetricsDetailsResponseChildSasItemState(_state)

        spi_in = d.pop("spi_in", UNSET)

        spi_out = d.pop("spi_out", UNSET)

        bytes_in = d.pop("bytes_in", UNSET)

        bytes_out = d.pop("bytes_out", UNSET)

        packets_in = d.pop("packets_in", UNSET)

        packets_out = d.pop("packets_out", UNSET)

        rekey_time = d.pop("rekey_time", UNSET)

        life_time = d.pop("life_time", UNSET)

        install_time = d.pop("install_time", UNSET)

        local_traffic_selector = cast(list[str], d.pop("local_traffic_selector", UNSET))

        remote_traffic_selector = cast(list[str], d.pop("remote_traffic_selector", UNSET))

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)

        gateway_ipsec_ike_sa_metrics_details_response_child_sas_item = cls(
            name=name,
            tunnel_id=tunnel_id,
            unique_id=unique_id,
            state=state,
            spi_in=spi_in,
            spi_out=spi_out,
            bytes_in=bytes_in,
            bytes_out=bytes_out,
            packets_in=packets_in,
            packets_out=packets_out,
            rekey_time=rekey_time,
            life_time=life_time,
            install_time=install_time,
            local_traffic_selector=local_traffic_selector,
            remote_traffic_selector=remote_traffic_selector,
            created_at=created_at,
            updated_at=updated_at,
        )

        gateway_ipsec_ike_sa_metrics_details_response_child_sas_item.additional_properties = d
        return gateway_ipsec_ike_sa_metrics_details_response_child_sas_item

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
