from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

T = TypeVar("T", bound="GatewayServiceLogSessionDetailsResponse")


@_attrs_define
class GatewayServiceLogSessionDetailsResponse:
    """Response schema for details of a service log session.

    Attributes:
        session_id (UUID): The unique identifier for the resource.
        token (UUID): The unique identifier for the resource.
    """

    session_id: UUID
    token: UUID

    def to_dict(self) -> dict[str, Any]:
        session_id = str(self.session_id)

        token = str(self.token)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "session_id": session_id,
                "token": token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        session_id = UUID(d.pop("session_id"))

        token = UUID(d.pop("token"))

        gateway_service_log_session_details_response = cls(
            session_id=session_id,
            token=token,
        )

        return gateway_service_log_session_details_response
