from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.server_firewall_rules_firewall_rules import ServerFirewallRulesFirewallRules


T = TypeVar("T", bound="ServerFirewallRules")


@_attrs_define
class ServerFirewallRules:
    """Ordered firewall rules configured for a Cloud Server.

    Example:
        {'firewall_rules': {'firewall_rule': [{'action': 'accept', 'comment': 'Allow SSH from the office network',
            'destination_address_end': '', 'destination_address_start': '', 'destination_port_end': '22',
            'destination_port_start': '22', 'direction': 'in', 'family': 'IPv4', 'icmp_type': '', 'position': '1',
            'protocol': 'tcp', 'source_address_end': '192.0.2.255', 'source_address_start': '192.0.2.1', 'source_port_end':
            '', 'source_port_start': ''}]}}

    Attributes:
        firewall_rules (ServerFirewallRulesFirewallRules):
    """

    firewall_rules: ServerFirewallRulesFirewallRules

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
        from ..models.server_firewall_rules_firewall_rules import ServerFirewallRulesFirewallRules  # noqa: PLC0415

        d = dict(src_dict)
        firewall_rules = ServerFirewallRulesFirewallRules.from_dict(d.pop("firewall_rules"))

        server_firewall_rules = cls(
            firewall_rules=firewall_rules,
        )

        return server_firewall_rules
