from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="GatewayAddressDetailsResponse")


@_attrs_define
class GatewayAddressDetailsResponse:
    """Response schema for gateway address details.

    Attributes:
        name (str | Unset): Name of the address
        address (str | Unset): VPN address
        provisioned_by (str | Unset): Provisioner of the address
    """

    name: str | Unset = UNSET
    address: str | Unset = UNSET
    provisioned_by: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        address = self.address

        provisioned_by = self.provisioned_by

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if address is not UNSET:
            field_dict["address"] = address
        if provisioned_by is not UNSET:
            field_dict["provisioned_by"] = provisioned_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        address = d.pop("address", UNSET)

        provisioned_by = d.pop("provisioned_by", UNSET)

        gateway_address_details_response = cls(
            name=name,
            address=address,
            provisioned_by=provisioned_by,
        )

        return gateway_address_details_response
