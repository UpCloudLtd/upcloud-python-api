from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.server_firewall_ruleset_relationships_firewall_ruleset_relationships import (
        ServerFirewallRulesetRelationshipsFirewallRulesetRelationships,
    )


T = TypeVar("T", bound="ServerFirewallRulesetRelationships")


@_attrs_define
class ServerFirewallRulesetRelationships:
    """Private firewall ruleset relationships for a Cloud Server.

    Example:
        {'firewall_ruleset_relationships': {'private': [{'applied_version': 3, 'created_at': '2026-08-25T10:15:30Z',
            'firewall_ruleset_uuid': '190f56d8-4b3f-4a89-9e5f-320fbc3d17c8', 'last_applied_at': '2026-08-25T10:15:32Z',
            'server_uuid': '0077fa3d-32db-4b09-9f5f-30d9e9afb565', 'type': 'private', 'updated_at': None, 'version': 3}]}}

    Attributes:
        firewall_ruleset_relationships (ServerFirewallRulesetRelationshipsFirewallRulesetRelationships):
    """

    firewall_ruleset_relationships: ServerFirewallRulesetRelationshipsFirewallRulesetRelationships

    def to_dict(self) -> dict[str, Any]:
        firewall_ruleset_relationships = self.firewall_ruleset_relationships.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "firewall_ruleset_relationships": firewall_ruleset_relationships,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_firewall_ruleset_relationships_firewall_ruleset_relationships import (
            ServerFirewallRulesetRelationshipsFirewallRulesetRelationships,  # noqa: PLC0415
        )

        d = dict(src_dict)
        firewall_ruleset_relationships = ServerFirewallRulesetRelationshipsFirewallRulesetRelationships.from_dict(
            d.pop("firewall_ruleset_relationships")
        )

        server_firewall_ruleset_relationships = cls(
            firewall_ruleset_relationships=firewall_ruleset_relationships,
        )

        return server_firewall_ruleset_relationships
