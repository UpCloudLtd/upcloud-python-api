from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.firewall_ruleset_server_firewall_rule import FirewallRulesetServerFirewallRule


T = TypeVar("T", bound="FirewallRulesetServerFirewallRules")


@_attrs_define
class FirewallRulesetServerFirewallRules:
    """Server firewall rules.

    Attributes:
        firewall_rule (list[FirewallRulesetServerFirewallRule] | None):
    """

    firewall_rule: list[FirewallRulesetServerFirewallRule] | None

    def to_dict(self) -> dict[str, Any]:
        firewall_rule: list[dict[str, Any]] | None
        if isinstance(self.firewall_rule, list):
            firewall_rule = []
            for firewall_rule_type_0_item_data in self.firewall_rule:
                firewall_rule_type_0_item = firewall_rule_type_0_item_data.to_dict()
                firewall_rule.append(firewall_rule_type_0_item)

        else:
            firewall_rule = self.firewall_rule

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

        def _parse_firewall_rule(data: object) -> list[FirewallRulesetServerFirewallRule] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                firewall_rule_type_0 = []
                _firewall_rule_type_0 = data
                for firewall_rule_type_0_item_data in _firewall_rule_type_0:
                    firewall_rule_type_0_item = FirewallRulesetServerFirewallRule.from_dict(
                        firewall_rule_type_0_item_data
                    )

                    firewall_rule_type_0.append(firewall_rule_type_0_item)

                return firewall_rule_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FirewallRulesetServerFirewallRule] | None, data)

        firewall_rule = _parse_firewall_rule(d.pop("firewall_rule"))

        firewall_ruleset_server_firewall_rules = cls(
            firewall_rule=firewall_rule,
        )

        return firewall_ruleset_server_firewall_rules
