from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.account_details import AccountDetails


T = TypeVar("T", bound="Account")


@_attrs_define
class Account:
    """Response schema containing account details.

    Example:
        {'account': {'username': 'apiuser01', 'credits': 25.5, 'resource_limits': {'managed_databases': 5,
            'network_peerings': 20, 'file_storages': 10, 'managed_kubernetes': 5, 'tags': 200, 'cores': 64,
            'cloud_server_dev_1xcpu_1gb_10gb_plans': 0, 'cloud_server_dev_1xcpu_1gb_plans': 0, 'storage_hdd': 10240,
            'networks': 100, 'network_gateways_essentials': 20, 'network_gateways': 20, 'storage_ssd': 20480,
            'load_balancers_essentials': 20, 'load_balancers': 20, 'gpus': 8, 'detached_interfaces': 100,
            'detached_floating_ips': 50, 'managed_object_storages': 50, 'memory': 524288, 'ntp_excess_gib': 100,
            'public_ipv4': 64, 'public_ipv6': 64, 'routers': 20, 'storage_maxiops': 10240, 'storage_standard': 20480,
            'storage_total': 40960}}}

    Attributes:
        account (AccountDetails): Detailed account information and limits. Example: {'username': 'apiuser01', 'credits':
            25.5, 'resource_limits': {'managed_databases': 5, 'network_peerings': 20, 'file_storages': 10,
            'managed_kubernetes': 5, 'tags': 200, 'cores': 64, 'cloud_server_dev_1xcpu_1gb_10gb_plans': 0,
            'cloud_server_dev_1xcpu_1gb_plans': 0, 'storage_hdd': 10240, 'networks': 100, 'network_gateways_essentials': 20,
            'network_gateways': 20, 'storage_ssd': 20480, 'load_balancers_essentials': 20, 'load_balancers': 20, 'gpus': 8,
            'detached_interfaces': 100, 'detached_floating_ips': 50, 'managed_object_storages': 50, 'memory': 524288,
            'ntp_excess_gib': 100, 'public_ipv4': 64, 'public_ipv6': 64, 'routers': 20, 'storage_maxiops': 10240,
            'storage_standard': 20480, 'storage_total': 40960}}.
    """

    account: AccountDetails

    def to_dict(self) -> dict[str, Any]:
        account = self.account.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "account": account,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_details import AccountDetails  # noqa: PLC0415

        d = dict(src_dict)
        account = AccountDetails.from_dict(d.pop("account"))

        account = cls(
            account=account,
        )

        return account
