from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="LoadBalancerNetwork")


@_attrs_define
class LoadBalancerNetwork:
    """Represent a network from where traffic is consumed and routed.

    Attributes:
        name (str): Human-readable name assigned to the network. Example: public-network.
        uuid (str): UUID represented as a string Example: 1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d.
        type_ (str): Network type indicating the visibility scope (public or private). Example: public.
        family (str): IP address family used by this network (IPv4 or IPv6). Example: IPv4.
        created_at (datetime.datetime): Timestamp when the network was created (RFC 3339 format).
        updated_at (datetime.datetime): Timestamp when the network was last updated (RFC 3339 format).
        dns_name (str | Unset): Fully qualified domain name (FQDN) for accessing the load balancer through this network.
            Example: lb-0a498284629e4629a55d0415a6e89dda-1.upcloudlb.com.
    """

    name: str
    uuid: str
    type_: str
    family: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    dns_name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        uuid = self.uuid

        type_ = self.type_

        family = self.family

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        dns_name = self.dns_name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "uuid": uuid,
                "type": type_,
                "family": family,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if dns_name is not UNSET:
            field_dict["dns_name"] = dns_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        uuid = d.pop("uuid")

        type_ = d.pop("type")

        family = d.pop("family")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        dns_name = d.pop("dns_name", UNSET)

        load_balancer_network = cls(
            name=name,
            uuid=uuid,
            type_=type_,
            family=family,
            created_at=created_at,
            updated_at=updated_at,
            dns_name=dns_name,
        )

        return load_balancer_network
