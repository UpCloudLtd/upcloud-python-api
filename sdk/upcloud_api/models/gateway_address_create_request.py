from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="GatewayAddressCreateRequest")


@_attrs_define
class GatewayAddressCreateRequest:
    """Gateway address

    Attributes:
        name (str): Name of the address
        address (str | Unset): Floating IP address
    """

    name: str
    address: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        address = self.address

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )
        if address is not UNSET:
            field_dict["address"] = address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        address = d.pop("address", UNSET)

        gateway_address_create_request = cls(
            name=name,
            address=address,
        )

        return gateway_address_create_request
