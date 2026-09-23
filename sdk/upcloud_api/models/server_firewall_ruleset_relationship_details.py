from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

T = TypeVar("T", bound="ServerFirewallRulesetRelationshipDetails")


@_attrs_define
class ServerFirewallRulesetRelationshipDetails:
    """Detailed private firewall ruleset relationship for a Cloud Server.

    Example:
        {'applied_version': 3, 'created_at': '2026-08-25T10:15:30Z', 'firewall_ruleset_uuid':
            '190f56d8-4b3f-4a89-9e5f-320fbc3d17c8', 'last_applied_at': '2026-08-25T10:15:32Z', 'server_uuid':
            '0077fa3d-32db-4b09-9f5f-30d9e9afb565', 'type': 'private', 'updated_at': None, 'version': 3}

    Attributes:
        applied_version (int | None): Ruleset version most recently applied to the Cloud Server.
        created_at (datetime.datetime): Datetime in RFC 3339 format
        firewall_ruleset_uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        last_applied_at (datetime.datetime | None): Time when this ruleset was last applied, or null if it has not been
            applied.
        server_uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        type_ (Literal['private']): Network interface class to which the ruleset applies.
        updated_at (datetime.datetime | None): Time when the relationship was last updated, or null if it has not been
            updated.
        version (int): Ruleset version selected for the relationship.
    """

    applied_version: int | None
    created_at: datetime.datetime
    firewall_ruleset_uuid: UUID
    last_applied_at: datetime.datetime | None
    server_uuid: UUID
    type_: Literal["private"]
    updated_at: datetime.datetime | None
    version: int

    def to_dict(self) -> dict[str, Any]:
        applied_version: int | None
        applied_version = self.applied_version

        created_at = self.created_at.isoformat()

        firewall_ruleset_uuid = str(self.firewall_ruleset_uuid)

        last_applied_at: None | str
        if isinstance(self.last_applied_at, datetime.datetime):
            last_applied_at = self.last_applied_at.isoformat()
        else:
            last_applied_at = self.last_applied_at

        server_uuid = str(self.server_uuid)

        type_ = self.type_

        updated_at: None | str
        if isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
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

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        firewall_ruleset_uuid = UUID(d.pop("firewall_ruleset_uuid"))

        def _parse_last_applied_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_applied_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_applied_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_applied_at = _parse_last_applied_at(d.pop("last_applied_at"))

        server_uuid = UUID(d.pop("server_uuid"))

        type_ = cast(Literal["private"], d.pop("type"))
        if type_ != "private":
            raise ValueError(f"type must match const 'private', got '{type_}'")

        def _parse_updated_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = datetime.datetime.fromisoformat(data)

                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        updated_at = _parse_updated_at(d.pop("updated_at"))

        version = d.pop("version")

        server_firewall_ruleset_relationship_details = cls(
            applied_version=applied_version,
            created_at=created_at,
            firewall_ruleset_uuid=firewall_ruleset_uuid,
            last_applied_at=last_applied_at,
            server_uuid=server_uuid,
            type_=type_,
            updated_at=updated_at,
            version=version,
        )

        return server_firewall_ruleset_relationship_details
