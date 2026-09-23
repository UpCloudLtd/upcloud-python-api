from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PartnerAccount")


@_attrs_define
class PartnerAccount:
    """Partner-managed account details.

    Attributes:
        username (str):
        address (str | Unset):
        city (str | Unset):
        company (str | Unset):
        country (str | Unset):
        email (str | Unset):
        first_name (str | Unset):
        last_name (str | Unset):
        phone (str | Unset):
        postal_code (str | Unset):
        state (str | Unset):
        vat_number (str | Unset):
    """

    username: str
    address: str | Unset = UNSET
    city: str | Unset = UNSET
    company: str | Unset = UNSET
    country: str | Unset = UNSET
    email: str | Unset = UNSET
    first_name: str | Unset = UNSET
    last_name: str | Unset = UNSET
    phone: str | Unset = UNSET
    postal_code: str | Unset = UNSET
    state: str | Unset = UNSET
    vat_number: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        address = self.address

        city = self.city

        company = self.company

        country = self.country

        email = self.email

        first_name = self.first_name

        last_name = self.last_name

        phone = self.phone

        postal_code = self.postal_code

        state = self.state

        vat_number = self.vat_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "username": username,
            }
        )
        if address is not UNSET:
            field_dict["address"] = address
        if city is not UNSET:
            field_dict["city"] = city
        if company is not UNSET:
            field_dict["company"] = company
        if country is not UNSET:
            field_dict["country"] = country
        if email is not UNSET:
            field_dict["email"] = email
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if phone is not UNSET:
            field_dict["phone"] = phone
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
        username = d.pop("username")

        address = d.pop("address", UNSET)

        city = d.pop("city", UNSET)

        company = d.pop("company", UNSET)

        country = d.pop("country", UNSET)

        email = d.pop("email", UNSET)

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        phone = d.pop("phone", UNSET)

        postal_code = d.pop("postal_code", UNSET)

        state = d.pop("state", UNSET)

        vat_number = d.pop("vat_number", UNSET)

        partner_account = cls(
            username=username,
            address=address,
            city=city,
            company=company,
            country=country,
            email=email,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            postal_code=postal_code,
            state=state,
            vat_number=vat_number,
        )

        partner_account.additional_properties = d
        return partner_account

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
