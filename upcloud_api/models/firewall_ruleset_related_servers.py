from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.firewall_ruleset_related_servers_servers_item import FirewallRulesetRelatedServersServersItem


T = TypeVar("T", bound="FirewallRulesetRelatedServers")


@_attrs_define
class FirewallRulesetRelatedServers:
    """Accessible Cloud Servers related to a private firewall ruleset and their private ruleset relationships.

    Example:
        {'servers': [{'attached_rulesets': [{'applied_version': 3, 'created_at': 1787652930, 'firewall_ruleset_uuid':
            '190f56d8-4b3f-4a89-9e5f-320fbc3d17c8', 'last_applied_at': 1787652932, 'server_uuid':
            '0077fa3d-32db-4b09-9f5f-30d9e9afb565', 'type': 'private', 'updated_at': None, 'version': 3}], 'firewall': 'on',
            'firewall_private': 'on', 'firewall_private_default_incoming_action': 'drop',
            'firewall_private_default_outgoing_action': 'accept', 'title': 'Application server', 'uuid':
            '0077fa3d-32db-4b09-9f5f-30d9e9afb565'}]}

    Attributes:
        servers (list[FirewallRulesetRelatedServersServersItem]): Cloud Servers visible to the authenticated account
            that are related to the ruleset.
    """

    servers: list[FirewallRulesetRelatedServersServersItem]

    def to_dict(self) -> dict[str, Any]:
        servers = []
        for servers_item_data in self.servers:
            servers_item = servers_item_data.to_dict()
            servers.append(servers_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "servers": servers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.firewall_ruleset_related_servers_servers_item import (
            FirewallRulesetRelatedServersServersItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        servers = []
        _servers = d.pop("servers")
        for servers_item_data in _servers:
            servers_item = FirewallRulesetRelatedServersServersItem.from_dict(servers_item_data)

            servers.append(servers_item)

        firewall_ruleset_related_servers = cls(
            servers=servers,
        )

        return firewall_ruleset_related_servers
