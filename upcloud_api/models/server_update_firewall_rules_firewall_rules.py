from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.server_firewall_rule_requirements import ServerFirewallRuleRequirements


T = TypeVar("T", bound="ServerUpdateFirewallRulesFirewallRules")


@_attrs_define
class ServerUpdateFirewallRulesFirewallRules:
    """
    Attributes:
        firewall_rule (list[ServerFirewallRuleRequirements]): Ordered firewall rules. Supplying an empty array removes
            all rules.
    """

    firewall_rule: list[ServerFirewallRuleRequirements]

    def to_dict(self) -> dict[str, Any]:
        firewall_rule = []
        for firewall_rule_item_data in self.firewall_rule:
            firewall_rule_item = firewall_rule_item_data.to_dict()
            firewall_rule.append(firewall_rule_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "firewall_rule": firewall_rule,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_firewall_rule_requirements import ServerFirewallRuleRequirements  # noqa: PLC0415

        d = dict(src_dict)
        firewall_rule = []
        _firewall_rule = d.pop("firewall_rule")
        for firewall_rule_item_data in _firewall_rule:
            firewall_rule_item = ServerFirewallRuleRequirements.from_dict(firewall_rule_item_data)

            firewall_rule.append(firewall_rule_item)

        server_update_firewall_rules_firewall_rules = cls(
            firewall_rule=firewall_rule,
        )

        return server_update_firewall_rules_firewall_rules
