from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.firewall_ruleset_rule_detail_response import FirewallRulesetRuleDetailResponse


T = TypeVar("T", bound="FirewallRulesetFirewallRuleListResponse")


@_attrs_define
class FirewallRulesetFirewallRuleListResponse:
    """Response schema for a list of firewall ruleset rules.

    Attributes:
        rules (list[FirewallRulesetRuleDetailResponse]):
    """

    rules: list[FirewallRulesetRuleDetailResponse]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rules = []
        for rules_item_data in self.rules:
            rules_item = rules_item_data.to_dict()
            rules.append(rules_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rules": rules,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.firewall_ruleset_rule_detail_response import FirewallRulesetRuleDetailResponse  # noqa: PLC0415

        d = dict(src_dict)
        rules = []
        _rules = d.pop("rules")
        for rules_item_data in _rules:
            rules_item = FirewallRulesetRuleDetailResponse.from_dict(rules_item_data)

            rules.append(rules_item)

        firewall_ruleset_firewall_rule_list_response = cls(
            rules=rules,
        )

        firewall_ruleset_firewall_rule_list_response.additional_properties = d
        return firewall_ruleset_firewall_rule_list_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
