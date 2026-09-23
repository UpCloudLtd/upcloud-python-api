from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.server_firewall_ruleset_relationship_internal_type import ServerFirewallRulesetRelationshipInternalType

T = TypeVar("T", bound="ServerFirewallRulesetRelationshipInternal")


@_attrs_define
class ServerFirewallRulesetRelationshipInternal:
    """Firewall ruleset relationship with Unix timestamps.

    Attributes:
        applied_version (int | None):
        created_at (int):
        firewall_ruleset_uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        last_applied_at (int | None):
        server_uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        type_ (ServerFirewallRulesetRelationshipInternalType):
        updated_at (int | None):
        version (int):
    """

    applied_version: int | None
    created_at: int
    firewall_ruleset_uuid: UUID
    last_applied_at: int | None
    server_uuid: UUID
    type_: ServerFirewallRulesetRelationshipInternalType
    updated_at: int | None
    version: int

    def to_dict(self) -> dict[str, Any]:
        applied_version: int | None
        applied_version = self.applied_version

        created_at = self.created_at

        firewall_ruleset_uuid = str(self.firewall_ruleset_uuid)

        last_applied_at: int | None
        last_applied_at = self.last_applied_at

        server_uuid = str(self.server_uuid)

        type_ = self.type_.value

        updated_at: int | None
        updated_at = self.updated_at

        version = self.version

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "applied_version": applied_version,
                "created_at": created_at,
                "firewall_ruleset_uuid": firewall_ruleset_uuid,
                "last_applied_at": last_applied_at,
                "server_uuid": server_uuid,
                "type": type_,
                "updated_at": updated_at,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_applied_version(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        applied_version = _parse_applied_version(d.pop("applied_version"))

        created_at = d.pop("created_at")

        firewall_ruleset_uuid = UUID(d.pop("firewall_ruleset_uuid"))

        def _parse_last_applied_at(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        last_applied_at = _parse_last_applied_at(d.pop("last_applied_at"))

        server_uuid = UUID(d.pop("server_uuid"))

        type_ = ServerFirewallRulesetRelationshipInternalType(d.pop("type"))

        def _parse_updated_at(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        updated_at = _parse_updated_at(d.pop("updated_at"))

        version = d.pop("version")

        server_firewall_ruleset_relationship_internal = cls(
            applied_version=applied_version,
            created_at=created_at,
            firewall_ruleset_uuid=firewall_ruleset_uuid,
            last_applied_at=last_applied_at,
            server_uuid=server_uuid,
            type_=type_,
            updated_at=updated_at,
            version=version,
        )

        return server_firewall_ruleset_relationship_internal
