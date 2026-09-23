from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.firewall_ruleset_server_multiple_firewall_rules_create_firewall_rules_type_1 import (
        FirewallRulesetServerMultipleFirewallRulesCreateFirewallRulesType1,
    )


T = TypeVar("T", bound="FirewallRulesetServerMultipleFirewallRulesCreate")


@_attrs_define
class FirewallRulesetServerMultipleFirewallRulesCreate:
    """Creates multiple server firewall rules.

    Attributes:
        firewall_rules (FirewallRulesetServerMultipleFirewallRulesCreateFirewallRulesType1 | None):
    """

    firewall_rules: FirewallRulesetServerMultipleFirewallRulesCreateFirewallRulesType1 | None

    def to_dict(self) -> dict[str, Any]:
        from ..models.firewall_ruleset_server_multiple_firewall_rules_create_firewall_rules_type_1 import (
            FirewallRulesetServerMultipleFirewallRulesCreateFirewallRulesType1,  # noqa: PLC0415
        )

        firewall_rules: dict[str, Any] | None
        if isinstance(self.firewall_rules, FirewallRulesetServerMultipleFirewallRulesCreateFirewallRulesType1):
            firewall_rules = self.firewall_rules.to_dict()
        else:
            firewall_rules = self.firewall_rules

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "firewall_rules": firewall_rules,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.firewall_ruleset_server_multiple_firewall_rules_create_firewall_rules_type_1 import (
            FirewallRulesetServerMultipleFirewallRulesCreateFirewallRulesType1,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_firewall_rules(
            data: object,
        ) -> FirewallRulesetServerMultipleFirewallRulesCreateFirewallRulesType1 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                firewall_rules_type_1 = FirewallRulesetServerMultipleFirewallRulesCreateFirewallRulesType1.from_dict(
                    data
                )

                return firewall_rules_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FirewallRulesetServerMultipleFirewallRulesCreateFirewallRulesType1 | None, data)

        firewall_rules = _parse_firewall_rules(d.pop("firewall_rules"))

        firewall_ruleset_server_multiple_firewall_rules_create = cls(
            firewall_rules=firewall_rules,
        )

        return firewall_ruleset_server_multiple_firewall_rules_create
