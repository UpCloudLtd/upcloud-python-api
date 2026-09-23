from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="TagError404Error")


@_attrs_define
class TagError404Error:
    """
    Attributes:
        error_code (Literal['TAG_NOT_FOUND']):
        error_message (str):
    """

    error_code: Literal["TAG_NOT_FOUND"]
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
        error_code = cast(Literal["TAG_NOT_FOUND"], d.pop("error_code"))
        if error_code != "TAG_NOT_FOUND":
            raise ValueError(f"error_code must match const 'TAG_NOT_FOUND', got '{error_code}'")

        error_message = d.pop("error_message")

        tag_error_404_error = cls(
            error_code=error_code,
            error_message=error_message,
        )

        return tag_error_404_error
