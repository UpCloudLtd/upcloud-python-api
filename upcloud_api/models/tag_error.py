from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.tag_error_error import TagErrorError


T = TypeVar("T", bound="TagError")


@_attrs_define
class TagError:
    """A general error response indicating that the request could not be fulfilled due to a technical issue.

    Attributes:
        error (TagErrorError):
    """

    error: TagErrorError

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
        from ..models.tag_error_error import TagErrorError  # noqa: PLC0415

        d = dict(src_dict)
        error = TagErrorError.from_dict(d.pop("error"))

        tag_error = cls(
            error=error,
        )

        return tag_error
