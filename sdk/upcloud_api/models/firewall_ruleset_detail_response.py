from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.firewall_ruleset_create_label import FirewallRulesetCreateLabel


T = TypeVar("T", bound="FirewallRulesetDetailResponse")


@_attrs_define
class FirewallRulesetDetailResponse:
    """Response schema for firewall ruleset details, including UUID, name, description, stateful, enabled, labels and
    serverUUID.

        Attributes:
            uuid (UUID | Unset): The unique identifier for the server.
            name (str | Unset): Name of the firewall ruleset
            description (str | Unset): Description of the firewall ruleset
            stateful (bool | Unset):
            version (int | Unset): The firewall ruleset version.
            enabled (bool | Unset):
            default_dns_rules_enabled (bool | Unset):
            labels (list[FirewallRulesetCreateLabel] | Unset): Labels
            server_uuid (UUID | Unset): The unique identifier for the server.
            created_at (datetime.datetime | Unset):
            updated_at (datetime.datetime | Unset):
    """

    uuid: UUID | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    stateful: bool | Unset = UNSET
    version: int | Unset = UNSET
    enabled: bool | Unset = UNSET
    default_dns_rules_enabled: bool | Unset = UNSET
    labels: list[FirewallRulesetCreateLabel] | Unset = UNSET
    server_uuid: UUID | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        uuid: str | Unset = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        name = self.name

        description = self.description

        stateful = self.stateful

        version = self.version

        enabled = self.enabled

        default_dns_rules_enabled = self.default_dns_rules_enabled

        labels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()
                labels.append(labels_item)

        server_uuid: str | Unset = UNSET
        if not isinstance(self.server_uuid, Unset):
            server_uuid = str(self.server_uuid)

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if stateful is not UNSET:
            field_dict["stateful"] = stateful
        if version is not UNSET:
            field_dict["version"] = version
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if default_dns_rules_enabled is not UNSET:
            field_dict["default_dns_rules_enabled"] = default_dns_rules_enabled
        if labels is not UNSET:
            field_dict["labels"] = labels
        if server_uuid is not UNSET:
            field_dict["server_uuid"] = server_uuid
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.firewall_ruleset_create_label import FirewallRulesetCreateLabel  # noqa: PLC0415

        d = dict(src_dict)
        _uuid = d.pop("uuid", UNSET)
        uuid: UUID | Unset
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = UUID(_uuid)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        stateful = d.pop("stateful", UNSET)

        version = d.pop("version", UNSET)

        enabled = d.pop("enabled", UNSET)

        default_dns_rules_enabled = d.pop("default_dns_rules_enabled", UNSET)

        _labels = d.pop("labels", UNSET)
        labels: list[FirewallRulesetCreateLabel] | Unset = UNSET
        if _labels is not UNSET:
            labels = []
            for labels_item_data in _labels:
                labels_item = FirewallRulesetCreateLabel.from_dict(labels_item_data)

                labels.append(labels_item)

        _server_uuid = d.pop("server_uuid", UNSET)
        server_uuid: UUID | Unset
        if isinstance(_server_uuid, Unset):
            server_uuid = UNSET
        else:
            server_uuid = UUID(_server_uuid)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)

        firewall_ruleset_detail_response = cls(
            uuid=uuid,
            name=name,
            description=description,
            stateful=stateful,
            version=version,
            enabled=enabled,
            default_dns_rules_enabled=default_dns_rules_enabled,
            labels=labels,
            server_uuid=server_uuid,
            created_at=created_at,
            updated_at=updated_at,
        )

        return firewall_ruleset_detail_response
