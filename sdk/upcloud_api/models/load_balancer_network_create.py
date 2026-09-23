from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.load_balancer_network_family import LoadBalancerNetworkFamily
from ..models.load_balancer_network_type import LoadBalancerNetworkType
from ..types import UNSET, Unset

T = TypeVar("T", bound="LoadBalancerNetworkCreate")


@_attrs_define
class LoadBalancerNetworkCreate:
    """Load Balancer Network.

    Attributes:
        name (str): Name of the network
        type_ (LoadBalancerNetworkType): Network type
        family (LoadBalancerNetworkFamily): Network family
        uuid (UUID | Unset): Network UUID
    """

    name: str
    type_: LoadBalancerNetworkType
    family: LoadBalancerNetworkFamily
    uuid: UUID | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_.value

        family = self.family.value

        uuid: str | Unset = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "type": type_,
                "family": family,
            }
        )
        if uuid is not UNSET:
            field_dict["uuid"] = uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        type_ = LoadBalancerNetworkType(d.pop("type"))

        family = LoadBalancerNetworkFamily(d.pop("family"))

        _uuid = d.pop("uuid", UNSET)
        uuid: UUID | Unset
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = UUID(_uuid)

        load_balancer_network_create = cls(
            name=name,
            type_=type_,
            family=family,
            uuid=uuid,
        )

        return load_balancer_network_create
