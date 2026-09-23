from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="ServerTagsType1")


@_attrs_define
class ServerTagsType1:
    """
    Attributes:
        tag (list[str]):
    """

    tag: list[str]

    def to_dict(self) -> dict[str, Any]:
        tag = self.tag

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "tag": tag,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tag = cast(list[str], d.pop("tag"))

        server_tags_type_1 = cls(
            tag=tag,
        )

        return server_tags_type_1
