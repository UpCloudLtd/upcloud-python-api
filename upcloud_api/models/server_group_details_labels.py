from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.server_group_label import ServerGroupLabel


T = TypeVar("T", bound="ServerGroupDetailsLabels")


@_attrs_define
class ServerGroupDetailsLabels:
    """List of labels associated with the server group.

    Attributes:
        label (list[ServerGroupLabel]):
    """

    label: list[ServerGroupLabel]

    def to_dict(self) -> dict[str, Any]:
        label = []
        for label_item_data in self.label:
            label_item = label_item_data.to_dict()
            label.append(label_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "label": label,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_group_label import ServerGroupLabel  # noqa: PLC0415

        d = dict(src_dict)
        label = []
        _label = d.pop("label")
        for label_item_data in _label:
            label_item = ServerGroupLabel.from_dict(label_item_data)

            label.append(label_item)

        server_group_details_labels = cls(
            label=label,
        )

        return server_group_details_labels
