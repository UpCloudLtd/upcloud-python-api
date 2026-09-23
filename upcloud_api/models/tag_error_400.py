from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.tag_error_400_error import TagError400Error


T = TypeVar("T", bound="TagError400")


@_attrs_define
class TagError400:
    """400 Bad Request errors for tag operations.

    Attributes:
        error (TagError400Error):
    """

    error: TagError400Error

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
        from ..models.tag_error_400_error import TagError400Error  # noqa: PLC0415

        d = dict(src_dict)
        error = TagError400Error.from_dict(d.pop("error"))

        tag_error_400 = cls(
            error=error,
        )

        return tag_error_400
