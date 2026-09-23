from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="PermissionErrorError")


@_attrs_define
class PermissionErrorError:
    """
    Attributes:
        error_code (str):
        error_message (str):
    """

    error_code: str
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
        error_code = d.pop("error_code")

        error_message = d.pop("error_message")

        permission_error_error = cls(
            error_code=error_code,
            error_message=error_message,
        )

        return permission_error_error
