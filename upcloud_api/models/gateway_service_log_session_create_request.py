from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.gateway_service_log_session_types import GatewayServiceLogSessionTypes

T = TypeVar("T", bound="GatewayServiceLogSessionCreateRequest")


@_attrs_define
class GatewayServiceLogSessionCreateRequest:
    """Request to create a new log session for a service.

    Attributes:
        session_type (GatewayServiceLogSessionTypes): Service log session types
    """

    session_type: GatewayServiceLogSessionTypes

    def to_dict(self) -> dict[str, Any]:
        session_type = self.session_type.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "session_type": session_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        session_type = GatewayServiceLogSessionTypes(d.pop("session_type"))

        gateway_service_log_session_create_request = cls(
            session_type=session_type,
        )

        return gateway_service_log_session_create_request
