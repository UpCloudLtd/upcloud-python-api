from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.partner_create_account_contact_details import PartnerCreateAccountContactDetails


T = TypeVar("T", bound="PartnerCreateAccount")


@_attrs_define
class PartnerCreateAccount:
    """Request payload for creating a partner-managed account.

    Attributes:
        username (str):
        password (str):
        contact_details (PartnerCreateAccountContactDetails | Unset):
    """

    username: str
    password: str
    contact_details: PartnerCreateAccountContactDetails | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        password = self.password

        contact_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.contact_details, Unset):
            contact_details = self.contact_details.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "username": username,
                "password": password,
            }
        )
        if contact_details is not UNSET:
            field_dict["contact_details"] = contact_details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.partner_create_account_contact_details import PartnerCreateAccountContactDetails  # noqa: PLC0415

        d = dict(src_dict)
        username = d.pop("username")

        password = d.pop("password")

        _contact_details = d.pop("contact_details", UNSET)
        contact_details: PartnerCreateAccountContactDetails | Unset
        if isinstance(_contact_details, Unset):
            contact_details = UNSET
        else:
            contact_details = PartnerCreateAccountContactDetails.from_dict(_contact_details)

        partner_create_account = cls(
            username=username,
            password=password,
            contact_details=contact_details,
        )

        partner_create_account.additional_properties = d
        return partner_create_account

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
