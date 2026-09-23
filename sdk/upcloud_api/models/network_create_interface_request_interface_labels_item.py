from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.network_boolean_yesno import NetworkBooleanYesno

T = TypeVar("T", bound="NetworkCreateInterfaceRequestInterfaceLabelsItem")


@_attrs_define
class NetworkCreateInterfaceRequestInterfaceLabelsItem:
    """
    Attributes:
        key (str):
        value (str):
        visible (NetworkBooleanYesno): Boolean value represented as yes/no Example: yes.
    """

    key: str
    value: str
    visible: NetworkBooleanYesno
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        value = self.value

        visible = self.visible.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "value": value,
                "visible": visible,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        value = d.pop("value")

        visible = NetworkBooleanYesno(d.pop("visible"))

        network_create_interface_request_interface_labels_item = cls(
            key=key,
            value=value,
            visible=visible,
        )

        network_create_interface_request_interface_labels_item.additional_properties = d
        return network_create_interface_request_interface_labels_item

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
