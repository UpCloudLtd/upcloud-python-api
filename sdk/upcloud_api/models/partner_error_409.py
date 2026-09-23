from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.partner_error_409_error import PartnerError409Error


T = TypeVar("T", bound="PartnerError409")


@_attrs_define
class PartnerError409:
    """409 Conflict errors for partner account creation.

    Attributes:
        error (PartnerError409Error):
    """

    error: PartnerError409Error

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
        from ..models.partner_error_409_error import PartnerError409Error  # noqa: PLC0415

        d = dict(src_dict)
        error = PartnerError409Error.from_dict(d.pop("error"))

        partner_error_409 = cls(
            error=error,
        )

        return partner_error_409
