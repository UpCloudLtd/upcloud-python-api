from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.firewall_ruleset_create_label import FirewallRulesetCreateLabel


T = TypeVar("T", bound="CreateFirewallRuleset")


@_attrs_define
class CreateFirewallRuleset:
    """Create firewall ruleset

    Attributes:
        name (str): Name of the firewall ruleset
        description (str | Unset): Description of the firewall ruleset
        stateful (bool | Unset):
        enabled (bool | Unset):
        default_dns_rules_enabled (bool | Unset):
        labels (list[FirewallRulesetCreateLabel] | Unset): Labels
    """

    name: str
    description: str | Unset = UNSET
    stateful: bool | Unset = UNSET
    enabled: bool | Unset = UNSET
    default_dns_rules_enabled: bool | Unset = UNSET
    labels: list[FirewallRulesetCreateLabel] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        stateful = self.stateful

        enabled = self.enabled

        default_dns_rules_enabled = self.default_dns_rules_enabled

        labels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()
                labels.append(labels_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if stateful is not UNSET:
            field_dict["stateful"] = stateful
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if default_dns_rules_enabled is not UNSET:
            field_dict["default_dns_rules_enabled"] = default_dns_rules_enabled
        if labels is not UNSET:
            field_dict["labels"] = labels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.firewall_ruleset_create_label import FirewallRulesetCreateLabel  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description", UNSET)

        stateful = d.pop("stateful", UNSET)

        enabled = d.pop("enabled", UNSET)

        default_dns_rules_enabled = d.pop("default_dns_rules_enabled", UNSET)

        _labels = d.pop("labels", UNSET)
        labels: list[FirewallRulesetCreateLabel] | Unset = UNSET
        if _labels is not UNSET:
            labels = []
            for labels_item_data in _labels:
                labels_item = FirewallRulesetCreateLabel.from_dict(labels_item_data)

                labels.append(labels_item)

        create_firewall_ruleset = cls(
            name=name,
            description=description,
            stateful=stateful,
            enabled=enabled,
            default_dns_rules_enabled=default_dns_rules_enabled,
            labels=labels,
        )

        return create_firewall_ruleset
