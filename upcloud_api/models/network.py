from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.network_details import NetworkDetails


T = TypeVar("T", bound="Network")


@_attrs_define
class Network:
    """Response schema containing a single network.

    Attributes:
        network (NetworkDetails): Detailed network resource attributes. Example: {'evi': 1234, 'grt_export': 'no',
            'ip_networks': {'ip_network': [{'family': 'IPv4', 'address': '192.168.150.0/24', 'dhcp': 'yes', 'dhcp_dns':
            ['192.168.150.1', '192.168.150.254'], 'gateway': '192.168.150.1'}]}, 'name': 'Example network',
            'network_features': ['allow-linklocal-address', 'allow-overlapping-ip-network', 'managed-by-service'],
            'parent_network': '037b0e4b-2734-4d5d-89ba-1737fc4593bf', 'peerings': {'peering': [{'name': 'Peering A->B',
            'state': 'pending-peer', 'uuid': '0fc82c18-1e5e-4076-afcd-3b85869800e7'}]}, 'router':
            '0414e0d7-4436-4037-9dd8-6eaf47dce599', 'services': {'service': [{'name': 'OBJECT-STORAGE', 'service_routes':
            ['10.10.10.0/24']}]}, 'type': 'private', 'uuid': '039a8811-e279-46c2-8e45-1962767f5a4c', 'zone': 'fi-hel1'}.
    """

    network: NetworkDetails

    def to_dict(self) -> dict[str, Any]:
        network = self.network.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "network": network,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.network_details import NetworkDetails  # noqa: PLC0415

        d = dict(src_dict)
        network = NetworkDetails.from_dict(d.pop("network"))

        network = cls(
            network=network,
        )

        return network
