from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.firewall_ruleset_rule_action import FirewallRulesetRuleAction
from ..models.firewall_ruleset_rule_direction import FirewallRulesetRuleDirection
from ..models.firewall_ruleset_rule_family import FirewallRulesetRuleFamily
from ..models.firewall_ruleset_rule_protocol import FirewallRulesetRuleProtocol
from ..types import UNSET, Unset

T = TypeVar("T", bound="FirewallRulesetFirewallRuleCreate")


@_attrs_define
class FirewallRulesetFirewallRuleCreate:
    """
    Attributes:
        action (FirewallRulesetRuleAction): Rule action.
        direction (FirewallRulesetRuleDirection): Rule direction.
        family (FirewallRulesetRuleFamily): Rule family.
        enabled (bool | Unset): Enabled
        comment (str | Unset): Comments
        destination_address_start (str | Unset):
        destination_address_end (str | Unset):
        destination_port_start (int | Unset):
        destination_port_end (int | Unset):
        destination_address_cidr (str | Unset):
        icmp_type (int | Unset): ICMP type.
        position (int | Unset):
        protocol (FirewallRulesetRuleProtocol | Unset): Rule protocol.
        source_address_start (str | Unset):
        source_address_end (str | Unset):
        source_port_start (int | Unset):
        source_port_end (int | Unset):
        source_address_cidr (str | Unset):
    """

    action: FirewallRulesetRuleAction
    direction: FirewallRulesetRuleDirection
    family: FirewallRulesetRuleFamily
    enabled: bool | Unset = UNSET
    comment: str | Unset = UNSET
    destination_address_start: str | Unset = UNSET
    destination_address_end: str | Unset = UNSET
    destination_port_start: int | Unset = UNSET
    destination_port_end: int | Unset = UNSET
    destination_address_cidr: str | Unset = UNSET
    icmp_type: int | Unset = UNSET
    position: int | Unset = UNSET
    protocol: FirewallRulesetRuleProtocol | Unset = UNSET
    source_address_start: str | Unset = UNSET
    source_address_end: str | Unset = UNSET
    source_port_start: int | Unset = UNSET
    source_port_end: int | Unset = UNSET
    source_address_cidr: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        action = self.action.value

        direction = self.direction.value

        family = self.family.value

        enabled = self.enabled

        comment = self.comment

        destination_address_start = self.destination_address_start

        destination_address_end = self.destination_address_end

        destination_port_start = self.destination_port_start

        destination_port_end = self.destination_port_end

        destination_address_cidr = self.destination_address_cidr

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

        field_dict.update(
            {
                "action": action,
                "direction": direction,
                "family": family,
            }
        )
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
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
        action = FirewallRulesetRuleAction(d.pop("action"))

        direction = FirewallRulesetRuleDirection(d.pop("direction"))

        family = FirewallRulesetRuleFamily(d.pop("family"))

        enabled = d.pop("enabled", UNSET)

        comment = d.pop("comment", UNSET)

        destination_address_start = d.pop("destination_address_start", UNSET)

        destination_address_end = d.pop("destination_address_end", UNSET)

        destination_port_start = d.pop("destination_port_start", UNSET)

        destination_port_end = d.pop("destination_port_end", UNSET)

        destination_address_cidr = d.pop("destination_address_cidr", UNSET)

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

        firewall_ruleset_firewall_rule_create = cls(
            action=action,
            direction=direction,
            family=family,
            enabled=enabled,
            comment=comment,
            destination_address_start=destination_address_start,
            destination_address_end=destination_address_end,
            destination_port_start=destination_port_start,
            destination_port_end=destination_port_end,
            destination_address_cidr=destination_address_cidr,
            icmp_type=icmp_type,
            position=position,
            protocol=protocol,
            source_address_start=source_address_start,
            source_address_end=source_address_end,
            source_port_start=source_port_start,
            source_port_end=source_port_end,
            source_address_cidr=source_address_cidr,
        )

        return firewall_ruleset_firewall_rule_create
