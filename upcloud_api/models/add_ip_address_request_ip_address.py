from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ip_address_boolean_yesno import IpAddressBooleanYesno
from ..models.ip_address_ip_family import IpAddressIpFamily
from ..models.ip_address_ip_release_policy import IpAddressIpReleasePolicy
from ..types import UNSET, Unset

T = TypeVar("T", bound="AddIpAddressRequestIpAddress")


@_attrs_define
class AddIpAddressRequestIpAddress:
    """
    Attributes:
        access (str):
        family (IpAddressIpFamily): IP address family Example: IPv4.
        floating (IpAddressBooleanYesno | Unset): Boolean value represented as yes/no Example: yes.
        mac (str | Unset): MAC address Example: de:ff:ff:ff:cc:20.
        prefix (str | Unset):
        release_policy (IpAddressIpReleasePolicy | Unset): Action taken when the resource using the address is deleted:
            release deletes the address, while keep preserves it as a detached floating IP address Example: release.
        server (UUID | Unset): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        vlan_id (str | Unset):
        zone (str | Unset): Zone identifier
    """

    access: str
    family: IpAddressIpFamily
    floating: IpAddressBooleanYesno | Unset = UNSET
    mac: str | Unset = UNSET
    prefix: str | Unset = UNSET
    release_policy: IpAddressIpReleasePolicy | Unset = UNSET
    server: UUID | Unset = UNSET
    vlan_id: str | Unset = UNSET
    zone: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access = self.access

        family = self.family.value

        floating: str | Unset = UNSET
        if not isinstance(self.floating, Unset):
            floating = self.floating.value

        mac = self.mac

        prefix = self.prefix

        release_policy: str | Unset = UNSET
        if not isinstance(self.release_policy, Unset):
            release_policy = self.release_policy.value

        server: str | Unset = UNSET
        if not isinstance(self.server, Unset):
            server = str(self.server)

        vlan_id = self.vlan_id

        zone = self.zone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "access": access,
                "family": family,
            }
        )
        if floating is not UNSET:
            field_dict["floating"] = floating
        if mac is not UNSET:
            field_dict["mac"] = mac
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if release_policy is not UNSET:
            field_dict["release_policy"] = release_policy
        if server is not UNSET:
            field_dict["server"] = server
        if vlan_id is not UNSET:
            field_dict["vlan_id"] = vlan_id
        if zone is not UNSET:
            field_dict["zone"] = zone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access = d.pop("access")

        family = IpAddressIpFamily(d.pop("family"))

        _floating = d.pop("floating", UNSET)
        floating: IpAddressBooleanYesno | Unset
        if isinstance(_floating, Unset):
            floating = UNSET
        else:
            floating = IpAddressBooleanYesno(_floating)

        mac = d.pop("mac", UNSET)

        prefix = d.pop("prefix", UNSET)

        _release_policy = d.pop("release_policy", UNSET)
        release_policy: IpAddressIpReleasePolicy | Unset
        if isinstance(_release_policy, Unset):
            release_policy = UNSET
        else:
            release_policy = IpAddressIpReleasePolicy(_release_policy)

        _server = d.pop("server", UNSET)
        server: UUID | Unset
        if isinstance(_server, Unset):
            server = UNSET
        else:
            server = UUID(_server)

        vlan_id = d.pop("vlan_id", UNSET)

        zone = d.pop("zone", UNSET)

        add_ip_address_request_ip_address = cls(
            access=access,
            family=family,
            floating=floating,
            mac=mac,
            prefix=prefix,
            release_policy=release_policy,
            server=server,
            vlan_id=vlan_id,
            zone=zone,
        )

        add_ip_address_request_ip_address.additional_properties = d
        return add_ip_address_request_ip_address

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
