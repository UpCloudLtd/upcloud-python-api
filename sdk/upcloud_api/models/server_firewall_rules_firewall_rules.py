from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.server_firewall_rule_response_item import ServerFirewallRuleResponseItem


T = TypeVar("T", bound="ServerFirewallRulesFirewallRules")


@_attrs_define
class ServerFirewallRulesFirewallRules:
    """
    Attributes:
        firewall_rule (list[ServerFirewallRuleResponseItem]):
    """

    firewall_rule: list[ServerFirewallRuleResponseItem]

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
        from ..models.server_firewall_rule_response_item import ServerFirewallRuleResponseItem  # noqa: PLC0415

        d = dict(src_dict)
        firewall_rule = []
        _firewall_rule = d.pop("firewall_rule")
        for firewall_rule_item_data in _firewall_rule:
            firewall_rule_item = ServerFirewallRuleResponseItem.from_dict(firewall_rule_item_data)

            firewall_rule.append(firewall_rule_item)

        server_firewall_rules_firewall_rules = cls(
            firewall_rule=firewall_rule,
        )

        return server_firewall_rules_firewall_rules
