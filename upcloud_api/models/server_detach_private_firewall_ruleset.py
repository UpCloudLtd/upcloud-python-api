from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.server_detach_private_firewall_ruleset_firewall_ruleset import (
        ServerDetachPrivateFirewallRulesetFirewallRuleset,
    )


T = TypeVar("T", bound="ServerDetachPrivateFirewallRuleset")


@_attrs_define
class ServerDetachPrivateFirewallRuleset:
    """Parameters for detaching a private firewall ruleset from a Cloud Server.

    Example:
        {'firewall_ruleset': {'firewall_ruleset_uuid': '190f56d8-4b3f-4a89-9e5f-320fbc3d17c8'}}

    Attributes:
        firewall_ruleset (ServerDetachPrivateFirewallRulesetFirewallRuleset): Private firewall ruleset to detach.
    """

    firewall_ruleset: ServerDetachPrivateFirewallRulesetFirewallRuleset

    def to_dict(self) -> dict[str, Any]:
        firewall_ruleset = self.firewall_ruleset.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "firewall_ruleset": firewall_ruleset,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_detach_private_firewall_ruleset_firewall_ruleset import (
            ServerDetachPrivateFirewallRulesetFirewallRuleset,  # noqa: PLC0415
        )

        d = dict(src_dict)
        firewall_ruleset = ServerDetachPrivateFirewallRulesetFirewallRuleset.from_dict(d.pop("firewall_ruleset"))

        server_detach_private_firewall_ruleset = cls(
            firewall_ruleset=firewall_ruleset,
        )

        return server_detach_private_firewall_ruleset
