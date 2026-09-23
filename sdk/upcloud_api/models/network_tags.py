from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.network_tags_tags import NetworkTagsTags


T = TypeVar("T", bound="NetworkTags")


@_attrs_define
class NetworkTags:
    """Container object for resource tags.

    Example:
        {'tags': {'tag': [{'name': 'PROD', 'description': 'Production servers', 'servers': {'server':
            ['0077fa3d-32db-4b09-9f5f-30d9e9afb565']}}]}}

    Attributes:
        tags (NetworkTagsTags):  Example: {'tag': [{'name': 'PROD', 'description': 'Production servers', 'servers':
            {'server': ['0077fa3d-32db-4b09-9f5f-30d9e9afb565']}}]}.
    """

    tags: NetworkTagsTags
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tags = self.tags.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tags": tags,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.network_tags_tags import NetworkTagsTags  # noqa: PLC0415

        d = dict(src_dict)
        tags = NetworkTagsTags.from_dict(d.pop("tags"))

        network_tags = cls(
            tags=tags,
        )

        network_tags.additional_properties = d
        return network_tags

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
