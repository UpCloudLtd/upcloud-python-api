from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.network_type import NetworkType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_network_request_network_ip_networks import CreateNetworkRequestNetworkIpNetworks
    from ..models.network_labels import NetworkLabels


T = TypeVar("T", bound="CreateNetworkRequestNetwork")


@_attrs_define
class CreateNetworkRequestNetwork:
    """
    Example:
        {'type': 'private', 'name': 'backend-net', 'zone': 'fi-hel2', 'ip_networks': {'ip_network': [{'family': 'IPv4',
            'address': '10.0.0.0/24', 'dhcp': 'yes'}]}}

    Attributes:
        type_ (NetworkType): Network access type Example: public.
        name (str):  Example: backend-net.
        zone (str): Zone identifier
        ip_networks (CreateNetworkRequestNetworkIpNetworks):
        router (UUID | Unset): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        labels (NetworkLabels | Unset): Collection of key/value labels for a resource. Example: {'label': [{'key':
            'env', 'value': 'prod'}, {'key': 'team', 'value': 'network'}]}.
    """

    type_: NetworkType
    name: str
    zone: str
    ip_networks: CreateNetworkRequestNetworkIpNetworks
    router: UUID | Unset = UNSET
    labels: NetworkLabels | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        name = self.name

        zone = self.zone

        ip_networks = self.ip_networks.to_dict()

        router: str | Unset = UNSET
        if not isinstance(self.router, Unset):
            router = str(self.router)

        labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "name": name,
                "zone": zone,
                "ip_networks": ip_networks,
            }
        )
        if router is not UNSET:
            field_dict["router"] = router
        if labels is not UNSET:
            field_dict["labels"] = labels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_network_request_network_ip_networks import (
            CreateNetworkRequestNetworkIpNetworks,  # noqa: PLC0415
        )
        from ..models.network_labels import NetworkLabels  # noqa: PLC0415

        d = dict(src_dict)
        type_ = NetworkType(d.pop("type"))

        name = d.pop("name")

        zone = d.pop("zone")

        ip_networks = CreateNetworkRequestNetworkIpNetworks.from_dict(d.pop("ip_networks"))

        _router = d.pop("router", UNSET)
        router: UUID | Unset
        if isinstance(_router, Unset):
            router = UNSET
        else:
            router = UUID(_router)

        _labels = d.pop("labels", UNSET)
        labels: NetworkLabels | Unset
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = NetworkLabels.from_dict(_labels)

        create_network_request_network = cls(
            type_=type_,
            name=name,
            zone=zone,
            ip_networks=ip_networks,
            router=router,
            labels=labels,
        )

        create_network_request_network.additional_properties = d
        return create_network_request_network

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
