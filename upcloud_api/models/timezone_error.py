from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.timezone_error_error import TimezoneErrorError


T = TypeVar("T", bound="TimezoneError")


@_attrs_define
class TimezoneError:
    """A general error response indicating that the request could not be fulfilled due to a technical issue.

    Attributes:
        error (TimezoneErrorError):
    """

    error: TimezoneErrorError

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
        from ..models.timezone_error_error import TimezoneErrorError  # noqa: PLC0415

        d = dict(src_dict)
        error = TimezoneErrorError.from_dict(d.pop("error"))

        timezone_error = cls(
            error=error,
        )

        return timezone_error
