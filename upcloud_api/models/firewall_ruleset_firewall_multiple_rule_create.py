from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.firewall_ruleset_firewall_rule_create import FirewallRulesetFirewallRuleCreate


T = TypeVar("T", bound="FirewallRulesetFirewallMultipleRuleCreate")


@_attrs_define
class FirewallRulesetFirewallMultipleRuleCreate:
    """
    Attributes:
        rules (list[FirewallRulesetFirewallRuleCreate]):
    """

    rules: list[FirewallRulesetFirewallRuleCreate]

    def to_dict(self) -> dict[str, Any]:
        rules = []
        for rules_item_data in self.rules:
            rules_item = rules_item_data.to_dict()
            rules.append(rules_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "rules": rules,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.firewall_ruleset_firewall_rule_create import FirewallRulesetFirewallRuleCreate  # noqa: PLC0415

        d = dict(src_dict)
        rules = []
        _rules = d.pop("rules")
        for rules_item_data in _rules:
            rules_item = FirewallRulesetFirewallRuleCreate.from_dict(rules_item_data)

            rules.append(rules_item)

        firewall_ruleset_firewall_multiple_rule_create = cls(
            rules=rules,
        )

        return firewall_ruleset_firewall_multiple_rule_create
