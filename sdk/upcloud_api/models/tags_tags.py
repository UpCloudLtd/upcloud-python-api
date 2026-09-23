from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.tags_tags_tag_item import TagsTagsTagItem


T = TypeVar("T", bound="TagsTags")


@_attrs_define
class TagsTags:
    """
    Example:
        {'tag': [{'name': 'PROD', 'description': 'Production servers', 'servers': {'server':
            ['0077fa3d-32db-4b09-9f5f-30d9e9afb565']}}]}

    Attributes:
        tag (list[TagsTagsTagItem]):
    """

    tag: list[TagsTagsTagItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tag = []
        for tag_item_data in self.tag:
            tag_item = tag_item_data.to_dict()
            tag.append(tag_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tag": tag,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tags_tags_tag_item import TagsTagsTagItem  # noqa: PLC0415

        d = dict(src_dict)
        tag = []
        _tag = d.pop("tag")
        for tag_item_data in _tag:
            tag_item = TagsTagsTagItem.from_dict(tag_item_data)

            tag.append(tag_item)

        tags_tags = cls(
            tag=tag,
        )

        tags_tags.additional_properties = d
        return tags_tags

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
