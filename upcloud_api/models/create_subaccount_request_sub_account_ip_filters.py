from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="CreateSubaccountRequestSubAccountIpFilters")


@_attrs_define
class CreateSubaccountRequestSubAccountIpFilters:
    """
    Attributes:
        ip_filter (list[str]):
    """

    ip_filter: list[str]

    def to_dict(self) -> dict[str, Any]:
        ip_filter = self.ip_filter

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "ip_filter": ip_filter,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ip_filter = cast(list[str], d.pop("ip_filter"))

        create_subaccount_request_sub_account_ip_filters = cls(
            ip_filter=ip_filter,
        )

        return create_subaccount_request_sub_account_ip_filters
