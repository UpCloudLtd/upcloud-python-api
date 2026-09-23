from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.partner_error_403_error import PartnerError403Error


T = TypeVar("T", bound="PartnerError403")


@_attrs_define
class PartnerError403:
    """403 Forbidden errors for partner account creation.

    Attributes:
        error (PartnerError403Error):
    """

    error: PartnerError403Error

    def to_dict(self) -> dict[str, Any]:
        error = self.error.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "error": error,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.partner_error_403_error import PartnerError403Error  # noqa: PLC0415

        d = dict(src_dict)
        error = PartnerError403Error.from_dict(d.pop("error"))

        partner_error_403 = cls(
            error=error,
        )

        return partner_error_403
