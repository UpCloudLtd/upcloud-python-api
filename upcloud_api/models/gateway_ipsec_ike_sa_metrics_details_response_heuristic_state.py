from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GatewayIpsecIkeSaMetricsDetailsResponseHeuristicState")


@_attrs_define
class GatewayIpsecIkeSaMetricsDetailsResponseHeuristicState:
    """Heuristic state of the IKE SA

    Attributes:
        tunnel_up (bool | Unset):
        tunnel_healthy (bool | Unset):
        last_down_message (str | Unset):
        updated_at (datetime.datetime | Unset): Timestamp of when the heuristic state was last updated.
        last_down_message_updated_at (datetime.datetime | Unset): Timestamp of when the last down message was updated.
        up_events (int | Unset): Number of times the IKE SA has transitioned to up state
        down_events (int | Unset): Number of times the IKE SA has transitioned to down state
        log_message_bad_events (int | Unset): Number of times the IKE SA has logged a bad message
    """

    tunnel_up: bool | Unset = UNSET
    tunnel_healthy: bool | Unset = UNSET
    last_down_message: str | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    last_down_message_updated_at: datetime.datetime | Unset = UNSET
    up_events: int | Unset = UNSET
    down_events: int | Unset = UNSET
    log_message_bad_events: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tunnel_up = self.tunnel_up

        tunnel_healthy = self.tunnel_healthy

        last_down_message = self.last_down_message

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        last_down_message_updated_at: str | Unset = UNSET
        if not isinstance(self.last_down_message_updated_at, Unset):
            last_down_message_updated_at = self.last_down_message_updated_at.isoformat()

        up_events = self.up_events

        down_events = self.down_events

        log_message_bad_events = self.log_message_bad_events

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tunnel_up is not UNSET:
            field_dict["tunnel_up"] = tunnel_up
        if tunnel_healthy is not UNSET:
            field_dict["tunnel_healthy"] = tunnel_healthy
        if last_down_message is not UNSET:
            field_dict["last_down_message"] = last_down_message
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if last_down_message_updated_at is not UNSET:
            field_dict["last_down_message_updated_at"] = last_down_message_updated_at
        if up_events is not UNSET:
            field_dict["up_events"] = up_events
        if down_events is not UNSET:
            field_dict["down_events"] = down_events
        if log_message_bad_events is not UNSET:
            field_dict["log_message_bad_events"] = log_message_bad_events

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tunnel_up = d.pop("tunnel_up", UNSET)

        tunnel_healthy = d.pop("tunnel_healthy", UNSET)

        last_down_message = d.pop("last_down_message", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)

        _last_down_message_updated_at = d.pop("last_down_message_updated_at", UNSET)
        last_down_message_updated_at: datetime.datetime | Unset
        if isinstance(_last_down_message_updated_at, Unset):
            last_down_message_updated_at = UNSET
        else:
            last_down_message_updated_at = datetime.datetime.fromisoformat(_last_down_message_updated_at)

        up_events = d.pop("up_events", UNSET)

        down_events = d.pop("down_events", UNSET)

        log_message_bad_events = d.pop("log_message_bad_events", UNSET)

        gateway_ipsec_ike_sa_metrics_details_response_heuristic_state = cls(
            tunnel_up=tunnel_up,
            tunnel_healthy=tunnel_healthy,
            last_down_message=last_down_message,
            updated_at=updated_at,
            last_down_message_updated_at=last_down_message_updated_at,
            up_events=up_events,
            down_events=down_events,
            log_message_bad_events=log_message_bad_events,
        )

        gateway_ipsec_ike_sa_metrics_details_response_heuristic_state.additional_properties = d
        return gateway_ipsec_ike_sa_metrics_details_response_heuristic_state

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
