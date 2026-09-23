from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ip_address_ip_release_policy import IpAddressIpReleasePolicy
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchIpAddressRequestV13IpAddress")


@_attrs_define
class PatchIpAddressRequestV13IpAddress:
    """
    Attributes:
        ptr_record (str | Unset):
        mac (str | Unset): MAC address Example: de:ff:ff:ff:cc:20.
        release_policy (IpAddressIpReleasePolicy | Unset): Action taken when the resource using the address is deleted:
            release deletes the address, while keep preserves it as a detached floating IP address Example: release.
    """

    ptr_record: str | Unset = UNSET
    mac: str | Unset = UNSET
    release_policy: IpAddressIpReleasePolicy | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ptr_record = self.ptr_record

        mac = self.mac

        release_policy: str | Unset = UNSET
        if not isinstance(self.release_policy, Unset):
            release_policy = self.release_policy.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ptr_record is not UNSET:
            field_dict["ptr_record"] = ptr_record
        if mac is not UNSET:
            field_dict["mac"] = mac
        if release_policy is not UNSET:
            field_dict["release_policy"] = release_policy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ptr_record = d.pop("ptr_record", UNSET)

        mac = d.pop("mac", UNSET)

        _release_policy = d.pop("release_policy", UNSET)
        release_policy: IpAddressIpReleasePolicy | Unset
        if isinstance(_release_policy, Unset):
            release_policy = UNSET
        else:
            release_policy = IpAddressIpReleasePolicy(_release_policy)

        patch_ip_address_request_v13_ip_address = cls(
            ptr_record=ptr_record,
            mac=mac,
            release_policy=release_policy,
        )

        patch_ip_address_request_v13_ip_address.additional_properties = d
        return patch_ip_address_request_v13_ip_address

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
