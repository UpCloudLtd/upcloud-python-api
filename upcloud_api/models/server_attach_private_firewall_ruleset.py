from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.server_attach_private_firewall_ruleset_firewall_ruleset import (
        ServerAttachPrivateFirewallRulesetFirewallRuleset,
    )


T = TypeVar("T", bound="ServerAttachPrivateFirewallRuleset")


@_attrs_define
class ServerAttachPrivateFirewallRuleset:
    """Parameters for attaching a private firewall ruleset to a Cloud Server.

    Example:
        {'firewall_ruleset': {'firewall_ruleset_uuid': '190f56d8-4b3f-4a89-9e5f-320fbc3d17c8'}}

    Attributes:
        firewall_ruleset (ServerAttachPrivateFirewallRulesetFirewallRuleset): Private firewall ruleset to attach.
    """

    firewall_ruleset: ServerAttachPrivateFirewallRulesetFirewallRuleset

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
        from ..models.server_attach_private_firewall_ruleset_firewall_ruleset import (
            ServerAttachPrivateFirewallRulesetFirewallRuleset,  # noqa: PLC0415
        )

        d = dict(src_dict)
        firewall_ruleset = ServerAttachPrivateFirewallRulesetFirewallRuleset.from_dict(d.pop("firewall_ruleset"))

        server_attach_private_firewall_ruleset = cls(
            firewall_ruleset=firewall_ruleset,
        )

        return server_attach_private_firewall_ruleset
