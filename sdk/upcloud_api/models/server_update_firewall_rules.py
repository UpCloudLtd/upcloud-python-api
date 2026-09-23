from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.server_update_firewall_rules_firewall_rules import ServerUpdateFirewallRulesFirewallRules


T = TypeVar("T", bound="ServerUpdateFirewallRules")


@_attrs_define
class ServerUpdateFirewallRules:
    """Complete replacement for a Cloud Server's firewall rule chain. Array order determines rule positions.

    Example:
        {'firewall_rules': {'firewall_rule': [{'action': 'accept', 'comment': 'Allow SSH', 'destination_port_end': '22',
            'destination_port_start': '22', 'direction': 'in', 'family': 'IPv4', 'protocol': 'tcp'}, {'action': 'drop',
            'direction': 'in'}]}}

    Attributes:
        firewall_rules (ServerUpdateFirewallRulesFirewallRules):
    """

    firewall_rules: ServerUpdateFirewallRulesFirewallRules

    def to_dict(self) -> dict[str, Any]:
        firewall_rules = self.firewall_rules.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "firewall_rules": firewall_rules,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_update_firewall_rules_firewall_rules import (
            ServerUpdateFirewallRulesFirewallRules,  # noqa: PLC0415
        )

        d = dict(src_dict)
        firewall_rules = ServerUpdateFirewallRulesFirewallRules.from_dict(d.pop("firewall_rules"))

        server_update_firewall_rules = cls(
            firewall_rules=firewall_rules,
        )

        return server_update_firewall_rules
