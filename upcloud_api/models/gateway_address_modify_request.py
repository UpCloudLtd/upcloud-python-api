from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="GatewayAddressModifyRequest")


@_attrs_define
class GatewayAddressModifyRequest:
    """Gateway service address modify request

    Attributes:
        address (str): Floating IP address to assign to the service address.
    """

    address: str

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "address": address,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        address = d.pop("address")

        gateway_address_modify_request = cls(
            address=address,
        )

        return gateway_address_modify_request
