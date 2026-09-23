from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.firewall_ruleset_server_firewall_rules import FirewallRulesetServerFirewallRules


T = TypeVar("T", bound="FirewallRulesetServerFirewallDetailResponse")


@_attrs_define
class FirewallRulesetServerFirewallDetailResponse:
    """Server firewall detail response.

    Attributes:
        firewall_rules (FirewallRulesetServerFirewallRules): Server firewall rules.
    """

    firewall_rules: FirewallRulesetServerFirewallRules

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
        from ..models.firewall_ruleset_server_firewall_rules import FirewallRulesetServerFirewallRules  # noqa: PLC0415

        d = dict(src_dict)
        firewall_rules = FirewallRulesetServerFirewallRules.from_dict(d.pop("firewall_rules"))

        firewall_ruleset_server_firewall_detail_response = cls(
            firewall_rules=firewall_rules,
        )

        return firewall_ruleset_server_firewall_detail_response
