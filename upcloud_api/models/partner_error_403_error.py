from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="PartnerError403Error")


@_attrs_define
class PartnerError403Error:
    """
    Attributes:
        error_code (Literal['ACCOUNT_CREATION_LIMIT_REACHED']):
        error_message (str):
    """

    error_code: Literal["ACCOUNT_CREATION_LIMIT_REACHED"]
    error_message: str

    def to_dict(self) -> dict[str, Any]:
        error_code = self.error_code

        error_message = self.error_message

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "error_code": error_code,
                "error_message": error_message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        error_code = cast(Literal["ACCOUNT_CREATION_LIMIT_REACHED"], d.pop("error_code"))
        if error_code != "ACCOUNT_CREATION_LIMIT_REACHED":
            raise ValueError(f"error_code must match const 'ACCOUNT_CREATION_LIMIT_REACHED', got '{error_code}'")

        error_message = d.pop("error_message")

        partner_error_403_error = cls(
            error_code=error_code,
            error_message=error_message,
        )

        return partner_error_403_error
