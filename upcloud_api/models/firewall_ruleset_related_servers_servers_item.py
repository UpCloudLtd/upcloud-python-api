from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.firewall_ruleset_related_servers_servers_item_firewall_private_default_incoming_action import (
    FirewallRulesetRelatedServersServersItemFirewallPrivateDefaultIncomingAction,
)
from ..models.firewall_ruleset_related_servers_servers_item_firewall_private_default_outgoing_action import (
    FirewallRulesetRelatedServersServersItemFirewallPrivateDefaultOutgoingAction,
)
from ..models.server_boolean_onoff import ServerBooleanOnoff

if TYPE_CHECKING:
    from ..models.server_firewall_ruleset_relationship_internal import ServerFirewallRulesetRelationshipInternal


T = TypeVar("T", bound="FirewallRulesetRelatedServersServersItem")


@_attrs_define
class FirewallRulesetRelatedServersServersItem:
    """
    Attributes:
        attached_rulesets (list[ServerFirewallRulesetRelationshipInternal]): Private firewall rulesets attached to the
            Cloud Server.
        firewall (ServerBooleanOnoff): Boolean value represented as on/off Example: on.
        firewall_private (ServerBooleanOnoff): Boolean value represented as on/off Example: on.
        firewall_private_default_incoming_action
            (FirewallRulesetRelatedServersServersItemFirewallPrivateDefaultIncomingAction): Default action for unmatched
            incoming traffic on private interfaces.
        firewall_private_default_outgoing_action
            (FirewallRulesetRelatedServersServersItemFirewallPrivateDefaultOutgoingAction): Default action for unmatched
            outgoing traffic on private interfaces.
        title (str): Cloud Server title.
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
    """

    attached_rulesets: list[ServerFirewallRulesetRelationshipInternal]
    firewall: ServerBooleanOnoff
    firewall_private: ServerBooleanOnoff
    firewall_private_default_incoming_action: (
        FirewallRulesetRelatedServersServersItemFirewallPrivateDefaultIncomingAction
    )
    firewall_private_default_outgoing_action: (
        FirewallRulesetRelatedServersServersItemFirewallPrivateDefaultOutgoingAction
    )
    title: str
    uuid: UUID

    def to_dict(self) -> dict[str, Any]:
        attached_rulesets = []
        for attached_rulesets_item_data in self.attached_rulesets:
            attached_rulesets_item = attached_rulesets_item_data.to_dict()
            attached_rulesets.append(attached_rulesets_item)

        firewall = self.firewall.value

        firewall_private = self.firewall_private.value

        firewall_private_default_incoming_action = self.firewall_private_default_incoming_action.value

        firewall_private_default_outgoing_action = self.firewall_private_default_outgoing_action.value

        title = self.title

        uuid = str(self.uuid)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "attached_rulesets": attached_rulesets,
                "firewall": firewall,
                "firewall_private": firewall_private,
                "firewall_private_default_incoming_action": firewall_private_default_incoming_action,
                "firewall_private_default_outgoing_action": firewall_private_default_outgoing_action,
                "title": title,
                "uuid": uuid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_firewall_ruleset_relationship_internal import (
            ServerFirewallRulesetRelationshipInternal,  # noqa: PLC0415
        )

        d = dict(src_dict)
        attached_rulesets = []
        _attached_rulesets = d.pop("attached_rulesets")
        for attached_rulesets_item_data in _attached_rulesets:
            attached_rulesets_item = ServerFirewallRulesetRelationshipInternal.from_dict(attached_rulesets_item_data)

            attached_rulesets.append(attached_rulesets_item)

        firewall = ServerBooleanOnoff(d.pop("firewall"))

        firewall_private = ServerBooleanOnoff(d.pop("firewall_private"))

        firewall_private_default_incoming_action = (
            FirewallRulesetRelatedServersServersItemFirewallPrivateDefaultIncomingAction(
                d.pop("firewall_private_default_incoming_action")
            )
        )

        firewall_private_default_outgoing_action = (
            FirewallRulesetRelatedServersServersItemFirewallPrivateDefaultOutgoingAction(
                d.pop("firewall_private_default_outgoing_action")
            )
        )

        title = d.pop("title")

        uuid = UUID(d.pop("uuid"))

        firewall_ruleset_related_servers_servers_item = cls(
            attached_rulesets=attached_rulesets,
            firewall=firewall,
            firewall_private=firewall_private,
            firewall_private_default_incoming_action=firewall_private_default_incoming_action,
            firewall_private_default_outgoing_action=firewall_private_default_outgoing_action,
            title=title,
            uuid=uuid,
        )

        return firewall_ruleset_related_servers_servers_item
