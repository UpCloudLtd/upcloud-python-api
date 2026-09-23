from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.network_boolean_yesno import NetworkBooleanYesno
from ..models.network_type import NetworkType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.network_details_ip_networks import NetworkDetailsIpNetworks
    from ..models.network_details_peerings import NetworkDetailsPeerings
    from ..models.network_details_servers import NetworkDetailsServers
    from ..models.network_details_services import NetworkDetailsServices


T = TypeVar("T", bound="NetworkDetails")


@_attrs_define
class NetworkDetails:
    """Detailed network resource attributes.

    Example:
        {'evi': 1234, 'grt_export': 'no', 'ip_networks': {'ip_network': [{'family': 'IPv4', 'address':
            '192.168.150.0/24', 'dhcp': 'yes', 'dhcp_dns': ['192.168.150.1', '192.168.150.254'], 'gateway':
            '192.168.150.1'}]}, 'name': 'Example network', 'network_features': ['allow-linklocal-address', 'allow-
            overlapping-ip-network', 'managed-by-service'], 'parent_network': '037b0e4b-2734-4d5d-89ba-1737fc4593bf',
            'peerings': {'peering': [{'name': 'Peering A->B', 'state': 'pending-peer', 'uuid':
            '0fc82c18-1e5e-4076-afcd-3b85869800e7'}]}, 'router': '0414e0d7-4436-4037-9dd8-6eaf47dce599', 'services':
            {'service': [{'name': 'OBJECT-STORAGE', 'service_routes': ['10.10.10.0/24']}]}, 'type': 'private', 'uuid':
            '039a8811-e279-46c2-8e45-1962767f5a4c', 'zone': 'fi-hel1'}

    Attributes:
        name (str):
        zone (str): Zone identifier
        grt_export (NetworkBooleanYesno | Unset): Boolean value represented as yes/no Example: yes.
        ip_networks (NetworkDetailsIpNetworks | Unset):
        network_features (list[str] | Unset):
        parent_network (UUID | Unset): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        peerings (NetworkDetailsPeerings | Unset): List of network peerings the network is part of
        router (UUID | Unset): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        servers (NetworkDetailsServers | Unset):
        services (NetworkDetailsServices | Unset): List of services this network is joined to
        tags (list[str] | Unset):
        type_ (NetworkType | Unset): Network access type Example: public.
        uuid (UUID | Unset):
    """

    name: str
    zone: str
    grt_export: NetworkBooleanYesno | Unset = UNSET
    ip_networks: NetworkDetailsIpNetworks | Unset = UNSET
    network_features: list[str] | Unset = UNSET
    parent_network: UUID | Unset = UNSET
    peerings: NetworkDetailsPeerings | Unset = UNSET
    router: UUID | Unset = UNSET
    servers: NetworkDetailsServers | Unset = UNSET
    services: NetworkDetailsServices | Unset = UNSET
    tags: list[str] | Unset = UNSET
    type_: NetworkType | Unset = UNSET
    uuid: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        zone = self.zone

        grt_export: str | Unset = UNSET
        if not isinstance(self.grt_export, Unset):
            grt_export = self.grt_export.value

        ip_networks: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ip_networks, Unset):
            ip_networks = self.ip_networks.to_dict()

        network_features: list[str] | Unset = UNSET
        if not isinstance(self.network_features, Unset):
            network_features = self.network_features

        parent_network: str | Unset = UNSET
        if not isinstance(self.parent_network, Unset):
            parent_network = str(self.parent_network)

        peerings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.peerings, Unset):
            peerings = self.peerings.to_dict()

        router: str | Unset = UNSET
        if not isinstance(self.router, Unset):
            router = str(self.router)

        servers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.servers, Unset):
            servers = self.servers.to_dict()

        services: dict[str, Any] | Unset = UNSET
        if not isinstance(self.services, Unset):
            services = self.services.to_dict()

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        uuid: str | Unset = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "zone": zone,
            }
        )
        if grt_export is not UNSET:
            field_dict["grt_export"] = grt_export
        if ip_networks is not UNSET:
            field_dict["ip_networks"] = ip_networks
        if network_features is not UNSET:
            field_dict["network_features"] = network_features
        if parent_network is not UNSET:
            field_dict["parent_network"] = parent_network
        if peerings is not UNSET:
            field_dict["peerings"] = peerings
        if router is not UNSET:
            field_dict["router"] = router
        if servers is not UNSET:
            field_dict["servers"] = servers
        if services is not UNSET:
            field_dict["services"] = services
        if tags is not UNSET:
            field_dict["tags"] = tags
        if type_ is not UNSET:
            field_dict["type"] = type_
        if uuid is not UNSET:
            field_dict["uuid"] = uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.network_details_ip_networks import NetworkDetailsIpNetworks  # noqa: PLC0415
        from ..models.network_details_peerings import NetworkDetailsPeerings  # noqa: PLC0415
        from ..models.network_details_servers import NetworkDetailsServers  # noqa: PLC0415
        from ..models.network_details_services import NetworkDetailsServices  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        zone = d.pop("zone")

        _grt_export = d.pop("grt_export", UNSET)
        grt_export: NetworkBooleanYesno | Unset
        if isinstance(_grt_export, Unset):
            grt_export = UNSET
        else:
            grt_export = NetworkBooleanYesno(_grt_export)

        _ip_networks = d.pop("ip_networks", UNSET)
        ip_networks: NetworkDetailsIpNetworks | Unset
        if isinstance(_ip_networks, Unset):
            ip_networks = UNSET
        else:
            ip_networks = NetworkDetailsIpNetworks.from_dict(_ip_networks)

        network_features = cast(list[str], d.pop("network_features", UNSET))

        _parent_network = d.pop("parent_network", UNSET)
        parent_network: UUID | Unset
        if isinstance(_parent_network, Unset):
            parent_network = UNSET
        else:
            parent_network = UUID(_parent_network)

        _peerings = d.pop("peerings", UNSET)
        peerings: NetworkDetailsPeerings | Unset
        if isinstance(_peerings, Unset):
            peerings = UNSET
        else:
            peerings = NetworkDetailsPeerings.from_dict(_peerings)

        _router = d.pop("router", UNSET)
        router: UUID | Unset
        if isinstance(_router, Unset):
            router = UNSET
        else:
            router = UUID(_router)

        _servers = d.pop("servers", UNSET)
        servers: NetworkDetailsServers | Unset
        if isinstance(_servers, Unset):
            servers = UNSET
        else:
            servers = NetworkDetailsServers.from_dict(_servers)

        _services = d.pop("services", UNSET)
        services: NetworkDetailsServices | Unset
        if isinstance(_services, Unset):
            services = UNSET
        else:
            services = NetworkDetailsServices.from_dict(_services)

        tags = cast(list[str], d.pop("tags", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: NetworkType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = NetworkType(_type_)

        _uuid = d.pop("uuid", UNSET)
        uuid: UUID | Unset
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = UUID(_uuid)

        network_details = cls(
            name=name,
            zone=zone,
            grt_export=grt_export,
            ip_networks=ip_networks,
            network_features=network_features,
            parent_network=parent_network,
            peerings=peerings,
            router=router,
            servers=servers,
            services=services,
            tags=tags,
            type_=type_,
            uuid=uuid,
        )

        network_details.additional_properties = d
        return network_details

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
