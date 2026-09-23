from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.ip_address_boolean_yesno import IpAddressBooleanYesno
from ..models.ip_address_ip_family import IpAddressIpFamily
from ..models.ip_address_ip_release_policy import IpAddressIpReleasePolicy
from ..models.ip_address_network_type import IpAddressNetworkType
from ..types import UNSET, Unset

T = TypeVar("T", bound="IpAddressDetails")


@_attrs_define
class IpAddressDetails:
    """Details of an IP address

    Attributes:
        access (IpAddressNetworkType): Network access type Example: public.
        address (str): IP address Example: 10.0.0.20.
        account_id (int | Unset): Unique numeric identifier of an account.
        delegated_to_account_id (int | None | Unset): Attached to a resource that is delegated to another account. Null
            means not delegated.
        family (IpAddressIpFamily | Unset): IP address family Example: IPv4.
        floating (IpAddressBooleanYesno | Unset): Boolean value represented as yes/no Example: yes.
        mac (str | Unset): MAC address Example: de:ff:ff:ff:cc:20.
        part_of_plan (IpAddressBooleanYesno | Unset): Boolean value represented as yes/no Example: yes.
        ptr_record (str | Unset):
        release_policy (IpAddressIpReleasePolicy | Unset): Action taken when the resource using the address is deleted:
            release deletes the address, while keep preserves it as a detached floating IP address Example: release.
        server (UUID | Unset): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        zone (str | Unset): Zone identifier
    """

    access: IpAddressNetworkType
    address: str
    account_id: int | Unset = UNSET
    delegated_to_account_id: int | None | Unset = UNSET
    family: IpAddressIpFamily | Unset = UNSET
    floating: IpAddressBooleanYesno | Unset = UNSET
    mac: str | Unset = UNSET
    part_of_plan: IpAddressBooleanYesno | Unset = UNSET
    ptr_record: str | Unset = UNSET
    release_policy: IpAddressIpReleasePolicy | Unset = UNSET
    server: UUID | Unset = UNSET
    zone: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        access = self.access.value

        address: str
        address = self.address

        account_id = self.account_id

        delegated_to_account_id: int | None | Unset
        if isinstance(self.delegated_to_account_id, Unset):
            delegated_to_account_id = UNSET
        else:
            delegated_to_account_id = self.delegated_to_account_id

        family: str | Unset = UNSET
        if not isinstance(self.family, Unset):
            family = self.family.value

        floating: str | Unset = UNSET
        if not isinstance(self.floating, Unset):
            floating = self.floating.value

        mac = self.mac

        part_of_plan: str | Unset = UNSET
        if not isinstance(self.part_of_plan, Unset):
            part_of_plan = self.part_of_plan.value

        ptr_record = self.ptr_record

        release_policy: str | Unset = UNSET
        if not isinstance(self.release_policy, Unset):
            release_policy = self.release_policy.value

        server: str | Unset = UNSET
        if not isinstance(self.server, Unset):
            server = str(self.server)

        zone = self.zone

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "access": access,
                "address": address,
            }
        )
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if delegated_to_account_id is not UNSET:
            field_dict["delegated_to_account_id"] = delegated_to_account_id
        if family is not UNSET:
            field_dict["family"] = family
        if floating is not UNSET:
            field_dict["floating"] = floating
        if mac is not UNSET:
            field_dict["mac"] = mac
        if part_of_plan is not UNSET:
            field_dict["part_of_plan"] = part_of_plan
        if ptr_record is not UNSET:
            field_dict["ptr_record"] = ptr_record
        if release_policy is not UNSET:
            field_dict["release_policy"] = release_policy
        if server is not UNSET:
            field_dict["server"] = server
        if zone is not UNSET:
            field_dict["zone"] = zone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access = IpAddressNetworkType(d.pop("access"))

        def _parse_address(data: object) -> str:
            return cast(str, data)

        address = _parse_address(d.pop("address"))

        account_id = d.pop("account_id", UNSET)

        def _parse_delegated_to_account_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        delegated_to_account_id = _parse_delegated_to_account_id(d.pop("delegated_to_account_id", UNSET))

        _family = d.pop("family", UNSET)
        family: IpAddressIpFamily | Unset
        if isinstance(_family, Unset):
            family = UNSET
        else:
            family = IpAddressIpFamily(_family)

        _floating = d.pop("floating", UNSET)
        floating: IpAddressBooleanYesno | Unset
        if isinstance(_floating, Unset):
            floating = UNSET
        else:
            floating = IpAddressBooleanYesno(_floating)

        mac = d.pop("mac", UNSET)

        _part_of_plan = d.pop("part_of_plan", UNSET)
        part_of_plan: IpAddressBooleanYesno | Unset
        if isinstance(_part_of_plan, Unset):
            part_of_plan = UNSET
        else:
            part_of_plan = IpAddressBooleanYesno(_part_of_plan)

        ptr_record = d.pop("ptr_record", UNSET)

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

        zone = d.pop("zone", UNSET)

        ip_address_details = cls(
            access=access,
            address=address,
            account_id=account_id,
            delegated_to_account_id=delegated_to_account_id,
            family=family,
            floating=floating,
            mac=mac,
            part_of_plan=part_of_plan,
            ptr_record=ptr_record,
            release_policy=release_policy,
            server=server,
            zone=zone,
        )

        return ip_address_details
