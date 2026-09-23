from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.firewall_ruleset_create_label import FirewallRulesetCreateLabel


T = TypeVar("T", bound="FirewallRulesetModify")


@_attrs_define
class FirewallRulesetModify:
    """Modify firewall ruleset

    Attributes:
        name (str | Unset): Name of the ruleset
        description (str | Unset): Description of the firewall ruleset
        labels (list[FirewallRulesetCreateLabel] | Unset): Labels
        enabled (bool | Unset): Enabled
        default_dns_rules_enabled (bool | Unset):
    """

    name: str | Unset = UNSET
    description: str | Unset = UNSET
    labels: list[FirewallRulesetCreateLabel] | Unset = UNSET
    enabled: bool | Unset = UNSET
    default_dns_rules_enabled: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        labels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()
                labels.append(labels_item)

        enabled = self.enabled

        default_dns_rules_enabled = self.default_dns_rules_enabled

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if labels is not UNSET:
            field_dict["labels"] = labels
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if default_dns_rules_enabled is not UNSET:
            field_dict["default_dns_rules_enabled"] = default_dns_rules_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.firewall_ruleset_create_label import FirewallRulesetCreateLabel  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _labels = d.pop("labels", UNSET)
        labels: list[FirewallRulesetCreateLabel] | Unset = UNSET
        if _labels is not UNSET:
            labels = []
            for labels_item_data in _labels:
                labels_item = FirewallRulesetCreateLabel.from_dict(labels_item_data)

                labels.append(labels_item)

        enabled = d.pop("enabled", UNSET)

        default_dns_rules_enabled = d.pop("default_dns_rules_enabled", UNSET)

        firewall_ruleset_modify = cls(
            name=name,
            description=description,
            labels=labels,
            enabled=enabled,
            default_dns_rules_enabled=default_dns_rules_enabled,
        )

        return firewall_ruleset_modify
