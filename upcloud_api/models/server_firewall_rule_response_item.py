from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.server_firewall_rule_response_item_action import ServerFirewallRuleResponseItemAction
from ..models.server_firewall_rule_response_item_direction import ServerFirewallRuleResponseItemDirection
from ..models.server_firewall_rule_response_item_family import ServerFirewallRuleResponseItemFamily
from ..models.server_firewall_rule_response_item_protocol import ServerFirewallRuleResponseItemProtocol

T = TypeVar("T", bound="ServerFirewallRuleResponseItem")


@_attrs_define
class ServerFirewallRuleResponseItem:
    """A firewall rule with its position in the Cloud Server's rule chain.

    Attributes:
        action (ServerFirewallRuleResponseItemAction): Action taken when the rule matches.
        comment (str): Free-form rule description.
        destination_address_end (str): Last destination IP address in the matched range, or an empty string when
            unrestricted.
        destination_address_start (str): First destination IP address in the matched range, or an empty string when
            unrestricted.
        destination_port_end (str): Last destination port in the matched range, or an empty string when unrestricted.
        destination_port_start (str): First destination port in the matched range, or an empty string when unrestricted.
        direction (ServerFirewallRuleResponseItemDirection): Traffic direction to which the rule applies.
        family (ServerFirewallRuleResponseItemFamily): IP address family, or an empty string when unrestricted.
        icmp_type (str): ICMP packet type, or an empty string when unrestricted.
        position (str): One-based position in the Cloud Server's firewall rule chain.
        protocol (ServerFirewallRuleResponseItemProtocol): Matched network protocol, or an empty string when
            unrestricted.
        source_address_end (str): Last source IP address in the matched range, or an empty string when unrestricted.
        source_address_start (str): First source IP address in the matched range, or an empty string when unrestricted.
        source_port_end (str): Last source port in the matched range, or an empty string when unrestricted.
        source_port_start (str): First source port in the matched range, or an empty string when unrestricted.
    """

    action: ServerFirewallRuleResponseItemAction
    comment: str
    destination_address_end: str
    destination_address_start: str
    destination_port_end: str
    destination_port_start: str
    direction: ServerFirewallRuleResponseItemDirection
    family: ServerFirewallRuleResponseItemFamily
    icmp_type: str
    position: str
    protocol: ServerFirewallRuleResponseItemProtocol
    source_address_end: str
    source_address_start: str
    source_port_end: str
    source_port_start: str

    def to_dict(self) -> dict[str, Any]:
        action = self.action.value

        comment = self.comment

        destination_address_end = self.destination_address_end

        destination_address_start = self.destination_address_start

        destination_port_end = self.destination_port_end

        destination_port_start = self.destination_port_start

        direction = self.direction.value

        family = self.family.value

        icmp_type = self.icmp_type

        position = self.position

        protocol = self.protocol.value

        source_address_end = self.source_address_end

        source_address_start = self.source_address_start

        source_port_end = self.source_port_end

        source_port_start = self.source_port_start

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "action": action,
                "comment": comment,
                "destination_address_end": destination_address_end,
                "destination_address_start": destination_address_start,
                "destination_port_end": destination_port_end,
                "destination_port_start": destination_port_start,
                "direction": direction,
                "family": family,
                "icmp_type": icmp_type,
                "position": position,
                "protocol": protocol,
                "source_address_end": source_address_end,
                "source_address_start": source_address_start,
                "source_port_end": source_port_end,
                "source_port_start": source_port_start,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = ServerFirewallRuleResponseItemAction(d.pop("action"))

        comment = d.pop("comment")

        destination_address_end = d.pop("destination_address_end")

        destination_address_start = d.pop("destination_address_start")

        destination_port_end = d.pop("destination_port_end")

        destination_port_start = d.pop("destination_port_start")

        direction = ServerFirewallRuleResponseItemDirection(d.pop("direction"))

        family = ServerFirewallRuleResponseItemFamily(d.pop("family"))

        icmp_type = d.pop("icmp_type")

        position = d.pop("position")

        protocol = ServerFirewallRuleResponseItemProtocol(d.pop("protocol"))

        source_address_end = d.pop("source_address_end")

        source_address_start = d.pop("source_address_start")

        source_port_end = d.pop("source_port_end")

        source_port_start = d.pop("source_port_start")

        server_firewall_rule_response_item = cls(
            action=action,
            comment=comment,
            destination_address_end=destination_address_end,
            destination_address_start=destination_address_start,
            destination_port_end=destination_port_end,
            destination_port_start=destination_port_start,
            direction=direction,
            family=family,
            icmp_type=icmp_type,
            position=position,
            protocol=protocol,
            source_address_end=source_address_end,
            source_address_start=source_address_start,
            source_port_end=source_port_end,
            source_port_start=source_port_start,
        )

        return server_firewall_rule_response_item
