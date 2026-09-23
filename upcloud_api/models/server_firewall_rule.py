from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.server_firewall_rule_response_item import ServerFirewallRuleResponseItem


T = TypeVar("T", bound="ServerFirewallRule")


@_attrs_define
class ServerFirewallRule:
    """A firewall rule with its position in the Cloud Server's rule chain.

    Example:
        {'firewall_rule': {'action': 'accept', 'comment': 'Allow SSH from the office network',
            'destination_address_end': '', 'destination_address_start': '', 'destination_port_end': '22',
            'destination_port_start': '22', 'direction': 'in', 'family': 'IPv4', 'icmp_type': '', 'position': '1',
            'protocol': 'tcp', 'source_address_end': '192.0.2.255', 'source_address_start': '192.0.2.1', 'source_port_end':
            '', 'source_port_start': ''}}

    Attributes:
        firewall_rule (ServerFirewallRuleResponseItem): A firewall rule with its position in the Cloud Server's rule
            chain.
    """

    firewall_rule: ServerFirewallRuleResponseItem

    def to_dict(self) -> dict[str, Any]:
        firewall_rule = self.firewall_rule.to_dict()

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
        firewall_rule = ServerFirewallRuleResponseItem.from_dict(d.pop("firewall_rule"))

        server_firewall_rule = cls(
            firewall_rule=firewall_rule,
        )

        return server_firewall_rule
