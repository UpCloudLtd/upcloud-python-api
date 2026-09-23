from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.server_group_label import ServerGroupLabel


T = TypeVar("T", bound="ServerGroupModifyServerGroupLabels")


@_attrs_define
class ServerGroupModifyServerGroupLabels:
    """Labels to categorize the server group

    Example:
        {'label': [{'key': 'env', 'value': 'prod'}]}

    Attributes:
        label (list[ServerGroupLabel] | Unset):
    """

    label: list[ServerGroupLabel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.label, Unset):
            label = []
            for label_item_data in self.label:
                label_item = label_item_data.to_dict()
                label.append(label_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_group_label import ServerGroupLabel  # noqa: PLC0415

        d = dict(src_dict)
        _label = d.pop("label", UNSET)
        label: list[ServerGroupLabel] | Unset = UNSET
        if _label is not UNSET:
            label = []
            for label_item_data in _label:
                label_item = ServerGroupLabel.from_dict(label_item_data)

                label.append(label_item)

        server_group_modify_server_group_labels = cls(
            label=label,
        )

        server_group_modify_server_group_labels.additional_properties = d
        return server_group_modify_server_group_labels

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
