from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.account_boolean_01 import AccountBoolean01
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_resource_limits import AccountResourceLimits


T = TypeVar("T", bound="AccountDetails")


@_attrs_define
class AccountDetails:
    """Detailed account information and limits.

    Example:
        {'username': 'apiuser01', 'credits': 25.5, 'resource_limits': {'managed_databases': 5, 'network_peerings': 20,
            'file_storages': 10, 'managed_kubernetes': 5, 'tags': 200, 'cores': 64, 'cloud_server_dev_1xcpu_1gb_10gb_plans':
            0, 'cloud_server_dev_1xcpu_1gb_plans': 0, 'storage_hdd': 10240, 'networks': 100, 'network_gateways_essentials':
            20, 'network_gateways': 20, 'storage_ssd': 20480, 'load_balancers_essentials': 20, 'load_balancers': 20, 'gpus':
            8, 'detached_interfaces': 100, 'detached_floating_ips': 50, 'managed_object_storages': 50, 'memory': 524288,
            'ntp_excess_gib': 100, 'public_ipv4': 64, 'public_ipv6': 64, 'routers': 20, 'storage_maxiops': 10240,
            'storage_standard': 20480, 'storage_total': 40960}}

    Attributes:
        resource_limits (AccountResourceLimits): Per-resource quota limits for an account.
        username (str): Username for an account.
        credits_ (float | Unset): Current account credit balance.
        trial_mode (AccountBoolean01 | Unset): Schema for boolean-like values encoded as 0 or 1.
    """

    resource_limits: AccountResourceLimits
    username: str
    credits_: float | Unset = UNSET
    trial_mode: AccountBoolean01 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource_limits = self.resource_limits.to_dict()

        username = self.username

        credits_ = self.credits_

        trial_mode: int | Unset = UNSET
        if not isinstance(self.trial_mode, Unset):
            trial_mode = self.trial_mode.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resource_limits": resource_limits,
                "username": username,
            }
        )
        if credits_ is not UNSET:
            field_dict["credits"] = credits_
        if trial_mode is not UNSET:
            field_dict["trial_mode"] = trial_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_resource_limits import AccountResourceLimits  # noqa: PLC0415

        d = dict(src_dict)
        resource_limits = AccountResourceLimits.from_dict(d.pop("resource_limits"))

        username = d.pop("username")

        credits_ = d.pop("credits", UNSET)

        _trial_mode = d.pop("trial_mode", UNSET)
        trial_mode: AccountBoolean01 | Unset
        if isinstance(_trial_mode, Unset):
            trial_mode = UNSET
        else:
            trial_mode = AccountBoolean01(_trial_mode)

        account_details = cls(
            resource_limits=resource_limits,
            username=username,
            credits_=credits_,
            trial_mode=trial_mode,
        )

        account_details.additional_properties = d
        return account_details

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
