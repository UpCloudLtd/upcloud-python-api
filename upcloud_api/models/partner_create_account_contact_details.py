from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PartnerCreateAccountContactDetails")


@_attrs_define
class PartnerCreateAccountContactDetails:
    """
    Attributes:
        country (str):
        email (str):
        first_name (str):
        last_name (str):
        phone (str):
        address (str | Unset):
        city (str | Unset):
        company (str | Unset):
        postal_code (str | Unset):
        state (str | Unset): State or province, if applicable. Required for some countries.
        vat_number (str | Unset):
    """

    country: str
    email: str
    first_name: str
    last_name: str
    phone: str
    address: str | Unset = UNSET
    city: str | Unset = UNSET
    company: str | Unset = UNSET
    postal_code: str | Unset = UNSET
    state: str | Unset = UNSET
    vat_number: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        country = self.country

        email = self.email

        first_name = self.first_name

        last_name = self.last_name

        phone = self.phone

        address = self.address

        city = self.city

        company = self.company

        postal_code = self.postal_code

        state = self.state

        vat_number = self.vat_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "country": country,
                "email": email,
                "first_name": first_name,
                "last_name": last_name,
                "phone": phone,
            }
        )
        if address is not UNSET:
            field_dict["address"] = address
        if city is not UNSET:
            field_dict["city"] = city
        if company is not UNSET:
            field_dict["company"] = company
        if postal_code is not UNSET:
            field_dict["postal_code"] = postal_code
        if state is not UNSET:
            field_dict["state"] = state
        if vat_number is not UNSET:
            field_dict["vat_number"] = vat_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        country = d.pop("country")

        email = d.pop("email")

        first_name = d.pop("first_name")

        last_name = d.pop("last_name")

        phone = d.pop("phone")

        address = d.pop("address", UNSET)

        city = d.pop("city", UNSET)

        company = d.pop("company", UNSET)

        postal_code = d.pop("postal_code", UNSET)

        state = d.pop("state", UNSET)

        vat_number = d.pop("vat_number", UNSET)

        partner_create_account_contact_details = cls(
            country=country,
            email=email,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            address=address,
            city=city,
            company=company,
            postal_code=postal_code,
            state=state,
            vat_number=vat_number,
        )

        partner_create_account_contact_details.additional_properties = d
        return partner_create_account_contact_details

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
