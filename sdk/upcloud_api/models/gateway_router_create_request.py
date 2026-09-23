from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

T = TypeVar("T", bound="GatewayRouterCreateRequest")


@_attrs_define
class GatewayRouterCreateRequest:
    """Network gateway router

    Attributes:
        uuid (UUID): The unique identifier for the resource.
    """

    uuid: UUID

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "uuid": uuid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        gateway_router_create_request = cls(
            uuid=uuid,
        )

        return gateway_router_create_request
