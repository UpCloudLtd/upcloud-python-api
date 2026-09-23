from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.account_create_ms_lma_signing_link_response_signing_status_state import (
    AccountCreateMsLmaSigningLinkResponseSigningStatusState,
)

T = TypeVar("T", bound="AccountCreateMsLmaSigningLinkResponseSigningStatus")


@_attrs_define
class AccountCreateMsLmaSigningLinkResponseSigningStatus:
    """
    Example:
        {'id': 'mslma_1234567890', 'initiated': '2026-07-29T11:00:00Z', 'signed_at': '2026-07-29T11:05:00Z',
            'signing_link': 'https://example.com/sign/mslma_1234567890', 'state': 'completed'}

    Attributes:
        id (str):
        initiated (datetime.datetime):
        signed_at (datetime.datetime):
        signing_link (str):
        state (AccountCreateMsLmaSigningLinkResponseSigningStatusState):
    """

    id: str
    initiated: datetime.datetime
    signed_at: datetime.datetime
    signing_link: str
    state: AccountCreateMsLmaSigningLinkResponseSigningStatusState
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        initiated = self.initiated.isoformat()

        signed_at = self.signed_at.isoformat()

        signing_link = self.signing_link

        state = self.state.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "initiated": initiated,
                "signed_at": signed_at,
                "signing_link": signing_link,
                "state": state,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        initiated = datetime.datetime.fromisoformat(d.pop("initiated"))

        signed_at = datetime.datetime.fromisoformat(d.pop("signed_at"))

        signing_link = d.pop("signing_link")

        state = AccountCreateMsLmaSigningLinkResponseSigningStatusState(d.pop("state"))

        account_create_ms_lma_signing_link_response_signing_status = cls(
            id=id,
            initiated=initiated,
            signed_at=signed_at,
            signing_link=signing_link,
            state=state,
        )

        account_create_ms_lma_signing_link_response_signing_status.additional_properties = d
        return account_create_ms_lma_signing_link_response_signing_status

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
