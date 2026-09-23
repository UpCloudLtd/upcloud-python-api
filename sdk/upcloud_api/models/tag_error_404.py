from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.tag_error_404_error import TagError404Error


T = TypeVar("T", bound="TagError404")


@_attrs_define
class TagError404:
    """404 Not Found errors for tag operations.

    Attributes:
        error (TagError404Error):
    """

    error: TagError404Error

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
        from ..models.tag_error_404_error import TagError404Error  # noqa: PLC0415

        d = dict(src_dict)
        error = TagError404Error.from_dict(d.pop("error"))

        tag_error_404 = cls(
            error=error,
        )

        return tag_error_404
