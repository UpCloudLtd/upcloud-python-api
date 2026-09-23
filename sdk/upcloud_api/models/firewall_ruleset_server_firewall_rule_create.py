from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.firewall_ruleset_server_firewall_rule import FirewallRulesetServerFirewallRule


T = TypeVar("T", bound="FirewallRulesetServerFirewallRuleCreate")


@_attrs_define
class FirewallRulesetServerFirewallRuleCreate:
    """
    Attributes:
        firewall_rule (FirewallRulesetServerFirewallRule): Server firewall rule
    """

    firewall_rule: FirewallRulesetServerFirewallRule

    def to_dict(self) -> dict[str, Any]:
        firewall_rule = self.firewall_rule.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "firewall_rule": firewall_rule,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.firewall_ruleset_server_firewall_rule import FirewallRulesetServerFirewallRule  # noqa: PLC0415

        d = dict(src_dict)
        firewall_rule = FirewallRulesetServerFirewallRule.from_dict(d.pop("firewall_rule"))

        firewall_ruleset_server_firewall_rule_create = cls(
            firewall_rule=firewall_rule,
        )

        return firewall_ruleset_server_firewall_rule_create
