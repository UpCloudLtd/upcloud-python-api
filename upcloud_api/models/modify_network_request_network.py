from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.network_boolean_01 import NetworkBoolean01
from ..models.network_features import NetworkFeatures
from ..models.network_type import NetworkType

if TYPE_CHECKING:
    from ..models.modify_network_request_network_ip_networks import ModifyNetworkRequestNetworkIpNetworks
    from ..models.network_labels import NetworkLabels
    from ..models.network_tags import NetworkTags


T = TypeVar("T", bound="ModifyNetworkRequestNetwork")


@_attrs_define
class ModifyNetworkRequestNetwork:
    """
    Attributes:
        type_ (NetworkType): Network access type Example: public.
        name (str):
        zone (str): Zone identifier
        tags (NetworkTags): Container object for resource tags. Example: {'tags': {'tag': [{'name': 'PROD',
            'description': 'Production servers', 'servers': {'server': ['0077fa3d-32db-4b09-9f5f-30d9e9afb565']}}]}}.
        labels (NetworkLabels): Collection of key/value labels for a resource. Example: {'label': [{'key': 'env',
            'value': 'prod'}, {'key': 'team', 'value': 'network'}]}.
        router (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        grt_export (NetworkBoolean01): Schema for boolean-like values encoded as 0 or 1.
        parent_network (str):
        ip_networks (ModifyNetworkRequestNetworkIpNetworks):
        network_features (NetworkFeatures): Features available for a network
        main_account_id (int): Unique numeric identifier of an account.
    """

    type_: NetworkType
    name: str
    zone: str
    tags: NetworkTags
    labels: NetworkLabels
    router: UUID
    grt_export: NetworkBoolean01
    parent_network: str
    ip_networks: ModifyNetworkRequestNetworkIpNetworks
    network_features: NetworkFeatures
    main_account_id: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        name = self.name

        zone = self.zone

        tags = self.tags.to_dict()

        labels = self.labels.to_dict()

        router = str(self.router)

        grt_export = self.grt_export.value

        parent_network = self.parent_network

        ip_networks = self.ip_networks.to_dict()

        network_features = self.network_features.value

        main_account_id = self.main_account_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "name": name,
                "zone": zone,
                "tags": tags,
                "labels": labels,
                "router": router,
                "grt_export": grt_export,
                "parent_network": parent_network,
                "ip_networks": ip_networks,
                "network_features": network_features,
                "main_account_id": main_account_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.modify_network_request_network_ip_networks import (
            ModifyNetworkRequestNetworkIpNetworks,  # noqa: PLC0415
        )
        from ..models.network_labels import NetworkLabels  # noqa: PLC0415
        from ..models.network_tags import NetworkTags  # noqa: PLC0415

        d = dict(src_dict)
        type_ = NetworkType(d.pop("type"))

        name = d.pop("name")

        zone = d.pop("zone")

        tags = NetworkTags.from_dict(d.pop("tags"))

        labels = NetworkLabels.from_dict(d.pop("labels"))

        router = UUID(d.pop("router"))

        grt_export = NetworkBoolean01(d.pop("grt_export"))

        parent_network = d.pop("parent_network")

        ip_networks = ModifyNetworkRequestNetworkIpNetworks.from_dict(d.pop("ip_networks"))

        network_features = NetworkFeatures(d.pop("network_features"))

        main_account_id = d.pop("main_account_id")

        modify_network_request_network = cls(
            type_=type_,
            name=name,
            zone=zone,
            tags=tags,
            labels=labels,
            router=router,
            grt_export=grt_export,
            parent_network=parent_network,
            ip_networks=ip_networks,
            network_features=network_features,
            main_account_id=main_account_id,
        )

        modify_network_request_network.additional_properties = d
        return modify_network_request_network

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
