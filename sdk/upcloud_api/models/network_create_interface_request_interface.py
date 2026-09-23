from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.network_boolean_yesno import NetworkBooleanYesno
from ..models.network_type import NetworkType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.network_create_interface_request_interface_labels_item import (
        NetworkCreateInterfaceRequestInterfaceLabelsItem,
    )


T = TypeVar("T", bound="NetworkCreateInterfaceRequestInterface")


@_attrs_define
class NetworkCreateInterfaceRequestInterface:
    """
    Attributes:
        bootable (NetworkBooleanYesno): Boolean value represented as yes/no Example: yes.
        network (str):
        source_ip_filtering (NetworkBooleanYesno): Boolean value represented as yes/no Example: yes.
        type_ (NetworkType): Network access type Example: public.
        labels (list[NetworkCreateInterfaceRequestInterfaceLabelsItem] | Unset):
    """

    bootable: NetworkBooleanYesno
    network: str
    source_ip_filtering: NetworkBooleanYesno
    type_: NetworkType
    labels: list[NetworkCreateInterfaceRequestInterfaceLabelsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bootable = self.bootable.value

        network = self.network

        source_ip_filtering = self.source_ip_filtering.value

        type_ = self.type_.value

        labels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()
                labels.append(labels_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bootable": bootable,
                "network": network,
                "source_ip_filtering": source_ip_filtering,
                "type": type_,
            }
        )
        if labels is not UNSET:
            field_dict["labels"] = labels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.network_create_interface_request_interface_labels_item import (
            NetworkCreateInterfaceRequestInterfaceLabelsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        bootable = NetworkBooleanYesno(d.pop("bootable"))

        network = d.pop("network")

        source_ip_filtering = NetworkBooleanYesno(d.pop("source_ip_filtering"))

        type_ = NetworkType(d.pop("type"))

        _labels = d.pop("labels", UNSET)
        labels: list[NetworkCreateInterfaceRequestInterfaceLabelsItem] | Unset = UNSET
        if _labels is not UNSET:
            labels = []
            for labels_item_data in _labels:
                labels_item = NetworkCreateInterfaceRequestInterfaceLabelsItem.from_dict(labels_item_data)

                labels.append(labels_item)

        network_create_interface_request_interface = cls(
            bootable=bootable,
            network=network,
            source_ip_filtering=source_ip_filtering,
            type_=type_,
            labels=labels,
        )

        network_create_interface_request_interface.additional_properties = d
        return network_create_interface_request_interface

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
