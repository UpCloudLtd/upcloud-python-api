from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.firewall_ruleset_rule_action import FirewallRulesetRuleAction
from ..models.firewall_ruleset_rule_direction import FirewallRulesetRuleDirection
from ..models.firewall_ruleset_rule_family import FirewallRulesetRuleFamily
from ..models.firewall_ruleset_rule_protocol import FirewallRulesetRuleProtocol
from ..types import UNSET, Unset

T = TypeVar("T", bound="FirewallRulesetFirewallRuleModify")


@_attrs_define
class FirewallRulesetFirewallRuleModify:
    """
    Attributes:
        enabled (bool | Unset): Enabled
        action (FirewallRulesetRuleAction | Unset): Rule action.
        comment (str | Unset): Comments
        destination_address_start (str | Unset):
        destination_address_end (str | Unset):
        destination_port_start (int | Unset):
        destination_port_end (int | Unset):
        destination_address_cidr (str | Unset):
        direction (FirewallRulesetRuleDirection | Unset): Rule direction.
        family (FirewallRulesetRuleFamily | Unset): Rule family.
        icmp_type (int | Unset): ICMP type.
        position (int | Unset):
        protocol (FirewallRulesetRuleProtocol | Unset): Rule protocol.
        source_address_start (str | Unset):
        source_address_end (str | Unset):
        source_port_start (int | Unset):
        source_port_end (int | Unset):
        source_address_cidr (str | Unset):
    """

    enabled: bool | Unset = UNSET
    action: FirewallRulesetRuleAction | Unset = UNSET
    comment: str | Unset = UNSET
    destination_address_start: str | Unset = UNSET
    destination_address_end: str | Unset = UNSET
    destination_port_start: int | Unset = UNSET
    destination_port_end: int | Unset = UNSET
    destination_address_cidr: str | Unset = UNSET
    direction: FirewallRulesetRuleDirection | Unset = UNSET
    family: FirewallRulesetRuleFamily | Unset = UNSET
    icmp_type: int | Unset = UNSET
    position: int | Unset = UNSET
    protocol: FirewallRulesetRuleProtocol | Unset = UNSET
    source_address_start: str | Unset = UNSET
    source_address_end: str | Unset = UNSET
    source_port_start: int | Unset = UNSET
    source_port_end: int | Unset = UNSET
    source_address_cidr: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        action: str | Unset = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.value

        comment = self.comment

        destination_address_start = self.destination_address_start

        destination_address_end = self.destination_address_end

        destination_port_start = self.destination_port_start

        destination_port_end = self.destination_port_end

        destination_address_cidr = self.destination_address_cidr

        direction: str | Unset = UNSET
        if not isinstance(self.direction, Unset):
            direction = self.direction.value

        family: str | Unset = UNSET
        if not isinstance(self.family, Unset):
            family = self.family.value

        icmp_type = self.icmp_type

        position = self.position

        protocol: str | Unset = UNSET
        if not isinstance(self.protocol, Unset):
            protocol = self.protocol.value

        source_address_start = self.source_address_start

        source_address_end = self.source_address_end

        source_port_start = self.source_port_start

        source_port_end = self.source_port_end

        source_address_cidr = self.source_address_cidr

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if action is not UNSET:
            field_dict["action"] = action
        if comment is not UNSET:
            field_dict["comment"] = comment
        if destination_address_start is not UNSET:
            field_dict["destination_address_start"] = destination_address_start
        if destination_address_end is not UNSET:
            field_dict["destination_address_end"] = destination_address_end
        if destination_port_start is not UNSET:
            field_dict["destination_port_start"] = destination_port_start
        if destination_port_end is not UNSET:
            field_dict["destination_port_end"] = destination_port_end
        if destination_address_cidr is not UNSET:
            field_dict["destination_address_cidr"] = destination_address_cidr
        if direction is not UNSET:
            field_dict["direction"] = direction
        if family is not UNSET:
            field_dict["family"] = family
        if icmp_type is not UNSET:
            field_dict["icmp_type"] = icmp_type
        if position is not UNSET:
            field_dict["position"] = position
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if source_address_start is not UNSET:
            field_dict["source_address_start"] = source_address_start
        if source_address_end is not UNSET:
            field_dict["source_address_end"] = source_address_end
        if source_port_start is not UNSET:
            field_dict["source_port_start"] = source_port_start
        if source_port_end is not UNSET:
            field_dict["source_port_end"] = source_port_end
        if source_address_cidr is not UNSET:
            field_dict["source_address_cidr"] = source_address_cidr

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        _action = d.pop("action", UNSET)
        action: FirewallRulesetRuleAction | Unset
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = FirewallRulesetRuleAction(_action)

        comment = d.pop("comment", UNSET)

        destination_address_start = d.pop("destination_address_start", UNSET)

        destination_address_end = d.pop("destination_address_end", UNSET)

        destination_port_start = d.pop("destination_port_start", UNSET)

        destination_port_end = d.pop("destination_port_end", UNSET)

        destination_address_cidr = d.pop("destination_address_cidr", UNSET)

        _direction = d.pop("direction", UNSET)
        direction: FirewallRulesetRuleDirection | Unset
        if isinstance(_direction, Unset):
            direction = UNSET
        else:
            direction = FirewallRulesetRuleDirection(_direction)

        _family = d.pop("family", UNSET)
        family: FirewallRulesetRuleFamily | Unset
        if isinstance(_family, Unset):
            family = UNSET
        else:
            family = FirewallRulesetRuleFamily(_family)

        icmp_type = d.pop("icmp_type", UNSET)

        position = d.pop("position", UNSET)

        _protocol = d.pop("protocol", UNSET)
        protocol: FirewallRulesetRuleProtocol | Unset
        if isinstance(_protocol, Unset):
            protocol = UNSET
        else:
            protocol = FirewallRulesetRuleProtocol(_protocol)

        source_address_start = d.pop("source_address_start", UNSET)

        source_address_end = d.pop("source_address_end", UNSET)

        source_port_start = d.pop("source_port_start", UNSET)

        source_port_end = d.pop("source_port_end", UNSET)

        source_address_cidr = d.pop("source_address_cidr", UNSET)

        firewall_ruleset_firewall_rule_modify = cls(
            enabled=enabled,
            action=action,
            comment=comment,
            destination_address_start=destination_address_start,
            destination_address_end=destination_address_end,
            destination_port_start=destination_port_start,
            destination_port_end=destination_port_end,
            destination_address_cidr=destination_address_cidr,
            direction=direction,
            family=family,
            icmp_type=icmp_type,
            position=position,
            protocol=protocol,
            source_address_start=source_address_start,
            source_address_end=source_address_end,
            source_port_start=source_port_start,
            source_port_end=source_port_end,
            source_address_cidr=source_address_cidr,
        )

        firewall_ruleset_firewall_rule_modify.additional_properties = d
        return firewall_ruleset_firewall_rule_modify

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
