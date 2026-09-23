from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

T = TypeVar("T", bound="RouterDetailsAttachedNetworkGatewaysItem")


@_attrs_define
class RouterDetailsAttachedNetworkGatewaysItem:
    """
    Attributes:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
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

        router_details_attached_network_gateways_item = cls(
            uuid=uuid,
        )

        return router_details_attached_network_gateways_item
