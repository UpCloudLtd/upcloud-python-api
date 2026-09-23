from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.device_error_error import DeviceErrorError


T = TypeVar("T", bound="DeviceError")


@_attrs_define
class DeviceError:
    """A general error response indicating that the request could not be fulfilled due to a technical issue.

    Attributes:
        error (DeviceErrorError):
    """

    error: DeviceErrorError

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
        from ..models.device_error_error import DeviceErrorError  # noqa: PLC0415

        d = dict(src_dict)
        error = DeviceErrorError.from_dict(d.pop("error"))

        device_error = cls(
            error=error,
        )

        return device_error
