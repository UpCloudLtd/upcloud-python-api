from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_create_ms_lma_signing_link_response_signing_status import (
        AccountCreateMsLmaSigningLinkResponseSigningStatus,
    )


T = TypeVar("T", bound="AccountCreateMsLmaSigningLinkResponse")


@_attrs_define
class AccountCreateMsLmaSigningLinkResponse:
    """Response schema for Microsoft LMA signing link creation.

    Example:
        {'signing_status': {'id': 'mslma_1234567890', 'initiated': '2026-07-29T11:00:00Z', 'signed_at':
            '2026-07-29T11:05:00Z', 'signing_link': 'https://example.com/sign/mslma_1234567890', 'state': 'completed'}}

    Attributes:
        signing_status (AccountCreateMsLmaSigningLinkResponseSigningStatus | Unset):  Example: {'id':
            'mslma_1234567890', 'initiated': '2026-07-29T11:00:00Z', 'signed_at': '2026-07-29T11:05:00Z', 'signing_link':
            'https://example.com/sign/mslma_1234567890', 'state': 'completed'}.
    """

    signing_status: AccountCreateMsLmaSigningLinkResponseSigningStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        signing_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.signing_status, Unset):
            signing_status = self.signing_status.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if signing_status is not UNSET:
            field_dict["signing_status"] = signing_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_create_ms_lma_signing_link_response_signing_status import (
            AccountCreateMsLmaSigningLinkResponseSigningStatus,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _signing_status = d.pop("signing_status", UNSET)
        signing_status: AccountCreateMsLmaSigningLinkResponseSigningStatus | Unset
        if isinstance(_signing_status, Unset):
            signing_status = UNSET
        else:
            signing_status = AccountCreateMsLmaSigningLinkResponseSigningStatus.from_dict(_signing_status)

        account_create_ms_lma_signing_link_response = cls(
            signing_status=signing_status,
        )

        account_create_ms_lma_signing_link_response.additional_properties = d
        return account_create_ms_lma_signing_link_response

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
