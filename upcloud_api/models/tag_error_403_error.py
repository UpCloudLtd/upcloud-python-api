from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="TagError403Error")


@_attrs_define
class TagError403Error:
    """
    Attributes:
        error_code (Literal['TAG_FORBIDDEN']):
        error_message (str):
    """

    error_code: Literal["TAG_FORBIDDEN"]
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
        error_code = cast(Literal["TAG_FORBIDDEN"], d.pop("error_code"))
        if error_code != "TAG_FORBIDDEN":
            raise ValueError(f"error_code must match const 'TAG_FORBIDDEN', got '{error_code}'")

        error_message = d.pop("error_message")

        tag_error_403_error = cls(
            error_code=error_code,
            error_message=error_message,
        )

        return tag_error_403_error
