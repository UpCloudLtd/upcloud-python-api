from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.networks_networks import NetworksNetworks


T = TypeVar("T", bound="Networks")


@_attrs_define
class Networks:
    """Response schema containing a list of networks.

    Example:
        {'networks': {'network': [{'uuid': '8f6d1ec2-8f5e-4b67-8fcb-6fa9c1a8a001', 'name': 'backend-net', 'type':
            'private', 'zone': 'fi-hel2'}]}}

    Attributes:
        networks (NetworksNetworks): Container object for network items. Example: {'network': [{'uuid':
            '8f6d1ec2-8f5e-4b67-8fcb-6fa9c1a8a001', 'name': 'backend-net', 'type': 'private', 'zone': 'fi-hel2'}]}.
    """

    networks: NetworksNetworks

    def to_dict(self) -> dict[str, Any]:
        networks = self.networks.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "networks": networks,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.networks_networks import NetworksNetworks  # noqa: PLC0415

        d = dict(src_dict)
        networks = NetworksNetworks.from_dict(d.pop("networks"))

        networks = cls(
            networks=networks,
        )

        return networks
