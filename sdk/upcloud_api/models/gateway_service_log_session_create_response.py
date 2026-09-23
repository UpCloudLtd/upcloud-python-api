from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.gateway_service_log_session_details_response import GatewayServiceLogSessionDetailsResponse


T = TypeVar("T", bound="GatewayServiceLogSessionCreateResponse")


@_attrs_define
class GatewayServiceLogSessionCreateResponse:
    """Response schema for service log session creation.

    Attributes:
        sessions (list[GatewayServiceLogSessionDetailsResponse]): List of service sessions created.
    """

    sessions: list[GatewayServiceLogSessionDetailsResponse]

    def to_dict(self) -> dict[str, Any]:
        sessions = []
        for sessions_item_data in self.sessions:
            sessions_item = sessions_item_data.to_dict()
            sessions.append(sessions_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "sessions": sessions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gateway_service_log_session_details_response import (
            GatewayServiceLogSessionDetailsResponse,  # noqa: PLC0415
        )

        d = dict(src_dict)
        sessions = []
        _sessions = d.pop("sessions")
        for sessions_item_data in _sessions:
            sessions_item = GatewayServiceLogSessionDetailsResponse.from_dict(sessions_item_data)

            sessions.append(sessions_item)

        gateway_service_log_session_create_response = cls(
            sessions=sessions,
        )

        return gateway_service_log_session_create_response
