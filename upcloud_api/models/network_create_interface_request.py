from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.network_create_interface_request_interface import NetworkCreateInterfaceRequestInterface


T = TypeVar("T", bound="NetworkCreateInterfaceRequest")


@_attrs_define
class NetworkCreateInterfaceRequest:
    """Request schema for creating a network interface

    Example:
        {'main_account_id': 123456, 'interface': {'type': 'private', 'network': '8f6d1ec2-8f5e-4b67-8fcb-6fa9c1a8a001',
            'source_ip_filtering': 'yes', 'bootable': 'no'}}

    Attributes:
        main_account_id (int | Unset): Unique numeric identifier of an account.
        interface (NetworkCreateInterfaceRequestInterface | Unset):
    """

    main_account_id: int | Unset = UNSET
    interface: NetworkCreateInterfaceRequestInterface | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        main_account_id = self.main_account_id

        interface: dict[str, Any] | Unset = UNSET
        if not isinstance(self.interface, Unset):
            interface = self.interface.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if main_account_id is not UNSET:
            field_dict["main_account_id"] = main_account_id
        if interface is not UNSET:
            field_dict["interface"] = interface

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.network_create_interface_request_interface import (
            NetworkCreateInterfaceRequestInterface,  # noqa: PLC0415
        )

        d = dict(src_dict)
        main_account_id = d.pop("main_account_id", UNSET)

        _interface = d.pop("interface", UNSET)
        interface: NetworkCreateInterfaceRequestInterface | Unset
        if isinstance(_interface, Unset):
            interface = UNSET
        else:
            interface = NetworkCreateInterfaceRequestInterface.from_dict(_interface)

        network_create_interface_request = cls(
            main_account_id=main_account_id,
            interface=interface,
        )

        network_create_interface_request.additional_properties = d
        return network_create_interface_request

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
