from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.account_resource_network_usage_type import AccountResourceNetworkUsageType

T = TypeVar("T", bound="AccountResourceNetworkUsageStatsStatItem")


@_attrs_define
class AccountResourceNetworkUsageStatsStatItem:
    """
    Attributes:
        resource_id (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        service (AccountResourceNetworkUsageType): Network usage type for resource
        zone (str): Zone identifier
        start_time (datetime.datetime): Datetime in RFC 3339 format
        sent_bytes (int | None):
    """

    resource_id: UUID
    service: AccountResourceNetworkUsageType
    zone: str
    start_time: datetime.datetime
    sent_bytes: int | None

    def to_dict(self) -> dict[str, Any]:
        resource_id = str(self.resource_id)

        service = self.service.value

        zone = self.zone

        start_time = self.start_time.isoformat()

        sent_bytes: int | None
        sent_bytes = self.sent_bytes

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "resource_id": resource_id,
                "service": service,
                "zone": zone,
                "start_time": start_time,
                "sent_bytes": sent_bytes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        resource_id = UUID(d.pop("resource_id"))

        service = AccountResourceNetworkUsageType(d.pop("service"))

        zone = d.pop("zone")

        start_time = datetime.datetime.fromisoformat(d.pop("start_time"))

        def _parse_sent_bytes(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        sent_bytes = _parse_sent_bytes(d.pop("sent_bytes"))

        account_resource_network_usage_stats_stat_item = cls(
            resource_id=resource_id,
            service=service,
            zone=zone,
            start_time=start_time,
            sent_bytes=sent_bytes,
        )

        return account_resource_network_usage_stats_stat_item
