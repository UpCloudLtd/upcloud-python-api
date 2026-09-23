from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.load_balancer_member_type import LoadBalancerMemberType

T = TypeVar("T", bound="LoadBalancerMember")


@_attrs_define
class LoadBalancerMember:
    """Represents a single backend member (server node) participating in a load balancer backend configuration.

    Attributes:
        name (str): Human-readable name assigned to the backend member. Example: member-1.
        ip (str): IP address of the backend member server. Example: 192.168.1.1.
        port (int): Port number on which the backend member server listens. Example: 80.
        weight (int): Relative weight for load balancing, determining the proportion of requests sent to this member.
            Example: 100.
        max_sessions (int): Maximum number of concurrent connections allowed to this backend member. Example: 1000.
        type_ (LoadBalancerMemberType): Type of backend configuration. Allowed values are 'static' and 'dynamic'.
            Example: static.
        enabled (bool): Indicates whether the backend member is actively participating in load balancing. Example: True.
        backup (bool): Indicates whether this member serves as a backup, only receiving traffic when all primary members
            are unavailable. Example: False.
        created_at (datetime.datetime): Timestamp when the backend member was created (RFC 3339 format).
        updated_at (datetime.datetime): Timestamp when the backend member was last updated (RFC 3339 format).
    """

    name: str
    ip: str
    port: int
    weight: int
    max_sessions: int
    type_: LoadBalancerMemberType
    enabled: bool
    backup: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        ip = self.ip

        port = self.port

        weight = self.weight

        max_sessions = self.max_sessions

        type_ = self.type_.value

        enabled = self.enabled

        backup = self.backup

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "ip": ip,
                "port": port,
                "weight": weight,
                "max_sessions": max_sessions,
                "type": type_,
                "enabled": enabled,
                "backup": backup,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        ip = d.pop("ip")

        port = d.pop("port")

        weight = d.pop("weight")

        max_sessions = d.pop("max_sessions")

        type_ = LoadBalancerMemberType(d.pop("type"))

        enabled = d.pop("enabled")

        backup = d.pop("backup")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        load_balancer_member = cls(
            name=name,
            ip=ip,
            port=port,
            weight=weight,
            max_sessions=max_sessions,
            type_=type_,
            enabled=enabled,
            backup=backup,
            created_at=created_at,
            updated_at=updated_at,
        )

        load_balancer_member.additional_properties = d
        return load_balancer_member

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
