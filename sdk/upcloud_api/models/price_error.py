from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.price_error_error import PriceErrorError


T = TypeVar("T", bound="PriceError")


@_attrs_define
class PriceError:
    """A general error response indicating that the request could not be fulfilled due to a technical issue.

    Attributes:
        error (PriceErrorError):
    """

    error: PriceErrorError

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
        from ..models.price_error_error import PriceErrorError  # noqa: PLC0415

        d = dict(src_dict)
        error = PriceErrorError.from_dict(d.pop("error"))

        price_error = cls(
            error=error,
        )

        return price_error
