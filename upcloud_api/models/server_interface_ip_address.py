from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.server_boolean_yesno import ServerBooleanYesno
from ..models.server_ip_family import ServerIpFamily
from ..models.server_ip_release_policy import ServerIpReleasePolicy
from ..types import UNSET, Unset

T = TypeVar("T", bound="ServerInterfaceIpAddress")


@_attrs_define
class ServerInterfaceIpAddress:
    """Network interface IP address

    Example:
        {'address': '10.0.0.20', 'dhcp_provided': 'yes', 'family': 'IPv4', 'floating': 'no', 'release_policy':
            'release'}

    Attributes:
        address (str): IP address Example: 10.0.0.20.
        family (ServerIpFamily): IP address family Example: IPv4.
        dhcp_provided (ServerBooleanYesno | Unset): Boolean value represented as yes/no Example: yes.
        floating (ServerBooleanYesno | Unset): Boolean value represented as yes/no Example: yes.
        release_policy (ServerIpReleasePolicy | Unset): Action taken when the resource using the address is deleted:
            release deletes the address, while keep preserves it as a detached floating IP address Example: release.
    """

    address: str
    family: ServerIpFamily
    dhcp_provided: ServerBooleanYesno | Unset = UNSET
    floating: ServerBooleanYesno | Unset = UNSET
    release_policy: ServerIpReleasePolicy | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address: str
        address = self.address

        family = self.family.value

        dhcp_provided: str | Unset = UNSET
        if not isinstance(self.dhcp_provided, Unset):
            dhcp_provided = self.dhcp_provided.value

        floating: str | Unset = UNSET
        if not isinstance(self.floating, Unset):
            floating = self.floating.value

        release_policy: str | Unset = UNSET
        if not isinstance(self.release_policy, Unset):
            release_policy = self.release_policy.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "address": address,
                "family": family,
            }
        )
        if dhcp_provided is not UNSET:
            field_dict["dhcp_provided"] = dhcp_provided
        if floating is not UNSET:
            field_dict["floating"] = floating
        if release_policy is not UNSET:
            field_dict["release_policy"] = release_policy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_address(data: object) -> str:
            return cast(str, data)

        address = _parse_address(d.pop("address"))

        family = ServerIpFamily(d.pop("family"))

        _dhcp_provided = d.pop("dhcp_provided", UNSET)
        dhcp_provided: ServerBooleanYesno | Unset
        if isinstance(_dhcp_provided, Unset):
            dhcp_provided = UNSET
        else:
            dhcp_provided = ServerBooleanYesno(_dhcp_provided)

        _floating = d.pop("floating", UNSET)
        floating: ServerBooleanYesno | Unset
        if isinstance(_floating, Unset):
            floating = UNSET
        else:
            floating = ServerBooleanYesno(_floating)

        _release_policy = d.pop("release_policy", UNSET)
        release_policy: ServerIpReleasePolicy | Unset
        if isinstance(_release_policy, Unset):
            release_policy = UNSET
        else:
            release_policy = ServerIpReleasePolicy(_release_policy)

        server_interface_ip_address = cls(
            address=address,
            family=family,
            dhcp_provided=dhcp_provided,
            floating=floating,
            release_policy=release_policy,
        )

        server_interface_ip_address.additional_properties = d
        return server_interface_ip_address

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
