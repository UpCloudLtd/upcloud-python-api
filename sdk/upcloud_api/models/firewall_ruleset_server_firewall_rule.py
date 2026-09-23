from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.firewall_ruleset_rule_action import FirewallRulesetRuleAction
from ..models.firewall_ruleset_rule_direction import FirewallRulesetRuleDirection
from ..types import UNSET, Unset

T = TypeVar("T", bound="FirewallRulesetServerFirewallRule")


@_attrs_define
class FirewallRulesetServerFirewallRule:
    """Server firewall rule

    Attributes:
        direction (FirewallRulesetRuleDirection): Rule direction.
        action (FirewallRulesetRuleAction): Rule action.
        position (int | str | Unset): Rule position
        family (None | str | Unset):
        protocol (None | str | Unset): Rule protocol
        enabled (str | Unset): Rule enabled
        icmp_type (int | None | str | Unset): ICMP type
        destination_port_start (int | None | str | Unset): Destination port range starts from this port number
        destination_port_end (int | None | str | Unset): Destination port range ends at this port number
        source_port_start (int | None | str | Unset): Source port range starts from this port number
        source_port_end (int | None | str | Unset): Source port range ends at this port number
        destination_address_start (None | str | Unset): Destination address range starts from this address
        destination_address_end (None | str | Unset): Destination address range ends from to this address
        source_address_start (None | str | Unset): Source address range starts from this address
        source_address_end (None | str | Unset): Source address range ends at this address
        comment (str | Unset): Comment
    """

    direction: FirewallRulesetRuleDirection
    action: FirewallRulesetRuleAction
    position: int | str | Unset = UNSET
    family: None | str | Unset = UNSET
    protocol: None | str | Unset = UNSET
    enabled: str | Unset = UNSET
    icmp_type: int | None | str | Unset = UNSET
    destination_port_start: int | None | str | Unset = UNSET
    destination_port_end: int | None | str | Unset = UNSET
    source_port_start: int | None | str | Unset = UNSET
    source_port_end: int | None | str | Unset = UNSET
    destination_address_start: None | str | Unset = UNSET
    destination_address_end: None | str | Unset = UNSET
    source_address_start: None | str | Unset = UNSET
    source_address_end: None | str | Unset = UNSET
    comment: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        direction = self.direction.value

        action = self.action.value

        position: int | str | Unset
        if isinstance(self.position, Unset):
            position = UNSET
        else:
            position = self.position

        family: None | str | Unset
        if isinstance(self.family, Unset):
            family = UNSET
        else:
            family = self.family

        protocol: None | str | Unset
        if isinstance(self.protocol, Unset):
            protocol = UNSET
        else:
            protocol = self.protocol

        enabled = self.enabled

        icmp_type: int | None | str | Unset
        if isinstance(self.icmp_type, Unset):
            icmp_type = UNSET
        else:
            icmp_type = self.icmp_type

        destination_port_start: int | None | str | Unset
        if isinstance(self.destination_port_start, Unset):
            destination_port_start = UNSET
        else:
            destination_port_start = self.destination_port_start

        destination_port_end: int | None | str | Unset
        if isinstance(self.destination_port_end, Unset):
            destination_port_end = UNSET
        else:
            destination_port_end = self.destination_port_end

        source_port_start: int | None | str | Unset
        if isinstance(self.source_port_start, Unset):
            source_port_start = UNSET
        else:
            source_port_start = self.source_port_start

        source_port_end: int | None | str | Unset
        if isinstance(self.source_port_end, Unset):
            source_port_end = UNSET
        else:
            source_port_end = self.source_port_end

        destination_address_start: None | str | Unset
        if isinstance(self.destination_address_start, Unset):
            destination_address_start = UNSET
        else:
            destination_address_start = self.destination_address_start

        destination_address_end: None | str | Unset
        if isinstance(self.destination_address_end, Unset):
            destination_address_end = UNSET
        else:
            destination_address_end = self.destination_address_end

        source_address_start: None | str | Unset
        if isinstance(self.source_address_start, Unset):
            source_address_start = UNSET
        else:
            source_address_start = self.source_address_start

        source_address_end: None | str | Unset
        if isinstance(self.source_address_end, Unset):
            source_address_end = UNSET
        else:
            source_address_end = self.source_address_end

        comment = self.comment

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "direction": direction,
                "action": action,
            }
        )
        if position is not UNSET:
            field_dict["position"] = position
        if family is not UNSET:
            field_dict["family"] = family
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if icmp_type is not UNSET:
            field_dict["icmp_type"] = icmp_type
        if destination_port_start is not UNSET:
            field_dict["destination_port_start"] = destination_port_start
        if destination_port_end is not UNSET:
            field_dict["destination_port_end"] = destination_port_end
        if source_port_start is not UNSET:
            field_dict["source_port_start"] = source_port_start
        if source_port_end is not UNSET:
            field_dict["source_port_end"] = source_port_end
        if destination_address_start is not UNSET:
            field_dict["destination_address_start"] = destination_address_start
        if destination_address_end is not UNSET:
            field_dict["destination_address_end"] = destination_address_end
        if source_address_start is not UNSET:
            field_dict["source_address_start"] = source_address_start
        if source_address_end is not UNSET:
            field_dict["source_address_end"] = source_address_end
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        direction = FirewallRulesetRuleDirection(d.pop("direction"))

        action = FirewallRulesetRuleAction(d.pop("action"))

        def _parse_position(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        position = _parse_position(d.pop("position", UNSET))

        def _parse_family(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        family = _parse_family(d.pop("family", UNSET))

        def _parse_protocol(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        protocol = _parse_protocol(d.pop("protocol", UNSET))

        enabled = d.pop("enabled", UNSET)

        def _parse_icmp_type(data: object) -> int | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | str | Unset, data)

        icmp_type = _parse_icmp_type(d.pop("icmp_type", UNSET))

        def _parse_destination_port_start(data: object) -> int | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | str | Unset, data)

        destination_port_start = _parse_destination_port_start(d.pop("destination_port_start", UNSET))

        def _parse_destination_port_end(data: object) -> int | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | str | Unset, data)

        destination_port_end = _parse_destination_port_end(d.pop("destination_port_end", UNSET))

        def _parse_source_port_start(data: object) -> int | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | str | Unset, data)

        source_port_start = _parse_source_port_start(d.pop("source_port_start", UNSET))

        def _parse_source_port_end(data: object) -> int | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | str | Unset, data)

        source_port_end = _parse_source_port_end(d.pop("source_port_end", UNSET))

        def _parse_destination_address_start(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        destination_address_start = _parse_destination_address_start(d.pop("destination_address_start", UNSET))

        def _parse_destination_address_end(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        destination_address_end = _parse_destination_address_end(d.pop("destination_address_end", UNSET))

        def _parse_source_address_start(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_address_start = _parse_source_address_start(d.pop("source_address_start", UNSET))

        def _parse_source_address_end(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_address_end = _parse_source_address_end(d.pop("source_address_end", UNSET))

        comment = d.pop("comment", UNSET)

        firewall_ruleset_server_firewall_rule = cls(
            direction=direction,
            action=action,
            position=position,
            family=family,
            protocol=protocol,
            enabled=enabled,
            icmp_type=icmp_type,
            destination_port_start=destination_port_start,
            destination_port_end=destination_port_end,
            source_port_start=source_port_start,
            source_port_end=source_port_end,
            destination_address_start=destination_address_start,
            destination_address_end=destination_address_end,
            source_address_start=source_address_start,
            source_address_end=source_address_end,
            comment=comment,
        )

        return firewall_ruleset_server_firewall_rule
