from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.server_firewall_ruleset_relationship_type import ServerFirewallRulesetRelationshipType

T = TypeVar("T", bound="ServerFirewallRulesetRelationship")


@_attrs_define
class ServerFirewallRulesetRelationship:
    """Relationship between a Cloud Server and a firewall ruleset.

    Example:
        {'firewall_ruleset_uuid': '190f56d8-4b3f-4a89-9e5f-320fbc3d17c8', 'server_uuid':
            '0077fa3d-32db-4b09-9f5f-30d9e9afb565', 'type': 'private'}

    Attributes:
        firewall_ruleset_uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        server_uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        type_ (ServerFirewallRulesetRelationshipType): Network interface class to which the ruleset applies.
    """

    firewall_ruleset_uuid: UUID
    server_uuid: UUID
    type_: ServerFirewallRulesetRelationshipType

    def to_dict(self) -> dict[str, Any]:
        firewall_ruleset_uuid = str(self.firewall_ruleset_uuid)

        server_uuid = str(self.server_uuid)

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "firewall_ruleset_uuid": firewall_ruleset_uuid,
                "server_uuid": server_uuid,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        firewall_ruleset_uuid = UUID(d.pop("firewall_ruleset_uuid"))

        server_uuid = UUID(d.pop("server_uuid"))

        type_ = ServerFirewallRulesetRelationshipType(d.pop("type"))

        server_firewall_ruleset_relationship = cls(
            firewall_ruleset_uuid=firewall_ruleset_uuid,
            server_uuid=server_uuid,
            type_=type_,
        )

        return server_firewall_ruleset_relationship
