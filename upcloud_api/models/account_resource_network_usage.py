from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.account_resource_network_usage_stats import AccountResourceNetworkUsageStats


T = TypeVar("T", bound="AccountResourceNetworkUsage")


@_attrs_define
class AccountResourceNetworkUsage:
    """Network usage statistics grouped by resource.

    Example:
        {'stats': {'stat': [{'resource_id': '00777436-a6f8-43af-9daf-89e8e6833a7a', 'sent_bytes': 10094, 'service':
            'server_public', 'start_time': '2020-09-07T00:00:00Z', 'zone': 'de-fra1'}, {'resource_id':
            '00777436-a6f8-43af-9daf-89e8e6833a7a', 'sent_bytes': 35174050, 'service': 'server_public', 'start_time':
            '2020-09-08T00:00:00Z', 'zone': 'de-fra1'}, {'resource_id': '00777436-a6f8-43af-9daf-89e8e6833a7a',
            'sent_bytes': 32790622, 'service': 'server_public', 'start_time': '2020-09-09T00:00:00Z', 'zone': 'de-fra1'}]}}

    Attributes:
        stats (AccountResourceNetworkUsageStats):
    """

    stats: AccountResourceNetworkUsageStats

    def to_dict(self) -> dict[str, Any]:
        stats = self.stats.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "stats": stats,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_resource_network_usage_stats import AccountResourceNetworkUsageStats  # noqa: PLC0415

        d = dict(src_dict)
        stats = AccountResourceNetworkUsageStats.from_dict(d.pop("stats"))

        account_resource_network_usage = cls(
            stats=stats,
        )

        return account_resource_network_usage
