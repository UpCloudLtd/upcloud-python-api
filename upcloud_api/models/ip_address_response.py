from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.ip_address_details import IpAddressDetails


T = TypeVar("T", bound="IpAddressResponse")


@_attrs_define
class IpAddressResponse:
    """Request schema for IP address operations

    Attributes:
        ip_address (IpAddressDetails): Details of an IP address
    """

    ip_address: IpAddressDetails

    def to_dict(self) -> dict[str, Any]:
        ip_address = self.ip_address.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "ip_address": ip_address,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ip_address_details import IpAddressDetails  # noqa: PLC0415

        d = dict(src_dict)
        ip_address = IpAddressDetails.from_dict(d.pop("ip_address"))

        ip_address_response = cls(
            ip_address=ip_address,
        )

        return ip_address_response
