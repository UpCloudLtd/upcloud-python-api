from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

T = TypeVar("T", bound="ServerDetachPrivateFirewallRulesetFirewallRuleset")


@_attrs_define
class ServerDetachPrivateFirewallRulesetFirewallRuleset:
    """Private firewall ruleset to detach.

    Attributes:
        firewall_ruleset_uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
    """

    firewall_ruleset_uuid: UUID

    def to_dict(self) -> dict[str, Any]:
        firewall_ruleset_uuid = str(self.firewall_ruleset_uuid)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "firewall_ruleset_uuid": firewall_ruleset_uuid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        firewall_ruleset_uuid = UUID(d.pop("firewall_ruleset_uuid"))

        server_detach_private_firewall_ruleset_firewall_ruleset = cls(
            firewall_ruleset_uuid=firewall_ruleset_uuid,
        )

        return server_detach_private_firewall_ruleset_firewall_ruleset
