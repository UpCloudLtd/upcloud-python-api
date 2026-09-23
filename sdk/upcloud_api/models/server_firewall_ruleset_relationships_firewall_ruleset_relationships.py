from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.server_firewall_ruleset_relationship_details import ServerFirewallRulesetRelationshipDetails


T = TypeVar("T", bound="ServerFirewallRulesetRelationshipsFirewallRulesetRelationships")


@_attrs_define
class ServerFirewallRulesetRelationshipsFirewallRulesetRelationships:
    """
    Attributes:
        private (list[ServerFirewallRulesetRelationshipDetails]): Private firewall rulesets attached to the Cloud
            Server.
    """

    private: list[ServerFirewallRulesetRelationshipDetails]

    def to_dict(self) -> dict[str, Any]:
        private = []
        for private_item_data in self.private:
            private_item = private_item_data.to_dict()
            private.append(private_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "private": private,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_firewall_ruleset_relationship_details import (
            ServerFirewallRulesetRelationshipDetails,  # noqa: PLC0415
        )

        d = dict(src_dict)
        private = []
        _private = d.pop("private")
        for private_item_data in _private:
            private_item = ServerFirewallRulesetRelationshipDetails.from_dict(private_item_data)

            private.append(private_item)

        server_firewall_ruleset_relationships_firewall_ruleset_relationships = cls(
            private=private,
        )

        return server_firewall_ruleset_relationships_firewall_ruleset_relationships
