from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.load_balancer_backend_properties_response import LoadBalancerBackendPropertiesResponse
    from ..models.load_balancer_member import LoadBalancerMember
    from ..models.load_balancer_tls_config import LoadBalancerTlsConfig


T = TypeVar("T", bound="LoadBalancerBackend")


@_attrs_define
class LoadBalancerBackend:
    """Represents a backend configuration in the load balancer service, containing backend members, resolver settings, TLS
    configurations, and backend-specific properties such as timeouts and health checks.

        Attributes:
            name (str): Human-readable name of the backend Example: api-backend.
            members (list[LoadBalancerMember]): List of backend member servers (nodes) participating in this backend
                configuration. Example: [{'name': 'member-1', 'ip': '192.168.1.10', 'port': 8080, 'weight': 10, 'max_sessions':
                100, 'type': 'static', 'enabled': True, 'backup': False, 'created_at': '2025-11-05T12:30:00.000Z', 'updated_at':
                '2025-11-05T13:45:00.000Z'}, {'name': 'member-2', 'ip': '192.168.1.11', 'port': 8080, 'weight': 8,
                'max_sessions': 120, 'type': 'static', 'enabled': True, 'backup': False, 'created_at':
                '2025-11-05T12:35:00.000Z', 'updated_at': '2025-11-05T13:50:00.000Z'}].
            tls_configs (list[LoadBalancerTlsConfig]): TLS configurations associated with this backend, specifying
                certificate bundles and identifiers. Example: [{'name': 'backend-tls-config', 'certificate_bundle_uuid':
                'a4b9f1a3-9b7c-4f21-8b33-fd68efb7c001', 'created_at': '2025-11-06T10:15:00.000Z', 'updated_at':
                '2025-11-06T11:00:00.000Z'}].
            properties (LoadBalancerBackendPropertiesResponse): Properties of a backend configuration. Example:
                {'backend_id': 401, 'outbound_proxy_protocol': 'v2', 'timeout_server': 30000, 'timeout_tunnel': 30000,
                'health_check_type': 'http', 'health_check_interval': 10, 'health_check_fall': 3, 'health_check_rise': 2,
                'health_check_url': '/status', 'health_check_expected_status': 200, 'health_check_tls_verify': True,
                'health_check_on_down': 'shutdown-sessions', 'sticky_session_cookie_name': 'SESSIONID',
                'sticky_session_cookie_attributes': 'SameSite=Strict; Secure; HttpOnly', 'tls_enabled': True, 'tls_verify':
                False, 'tls_use_system_ca': True, 'http2_enabled': True}.
            created_at (datetime.datetime): Timestamp when the backend was created (RFC 3339 format).
            updated_at (datetime.datetime): Timestamp when the backend was last updated (RFC 3339 format).
            resolver (None | str | Unset): Optional outbound DNS resolver reference used by this backend. Null when not set.
                Example: resolver-default.
    """

    name: str
    members: list[LoadBalancerMember]
    tls_configs: list[LoadBalancerTlsConfig]
    properties: LoadBalancerBackendPropertiesResponse
    created_at: datetime.datetime
    updated_at: datetime.datetime
    resolver: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        members = []
        for members_item_data in self.members:
            members_item = members_item_data.to_dict()
            members.append(members_item)

        tls_configs = []
        for tls_configs_item_data in self.tls_configs:
            tls_configs_item = tls_configs_item_data.to_dict()
            tls_configs.append(tls_configs_item)

        properties = self.properties.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        resolver: None | str | Unset
        if isinstance(self.resolver, Unset):
            resolver = UNSET
        else:
            resolver = self.resolver

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "members": members,
                "tls_configs": tls_configs,
                "properties": properties,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if resolver is not UNSET:
            field_dict["resolver"] = resolver

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.load_balancer_backend_properties_response import (
            LoadBalancerBackendPropertiesResponse,  # noqa: PLC0415
        )
        from ..models.load_balancer_member import LoadBalancerMember  # noqa: PLC0415
        from ..models.load_balancer_tls_config import LoadBalancerTlsConfig  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        members = []
        _members = d.pop("members")
        for members_item_data in _members:
            members_item = LoadBalancerMember.from_dict(members_item_data)

            members.append(members_item)

        tls_configs = []
        _tls_configs = d.pop("tls_configs")
        for tls_configs_item_data in _tls_configs:
            tls_configs_item = LoadBalancerTlsConfig.from_dict(tls_configs_item_data)

            tls_configs.append(tls_configs_item)

        properties = LoadBalancerBackendPropertiesResponse.from_dict(d.pop("properties"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_resolver(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resolver = _parse_resolver(d.pop("resolver", UNSET))

        load_balancer_backend = cls(
            name=name,
            members=members,
            tls_configs=tls_configs,
            properties=properties,
            created_at=created_at,
            updated_at=updated_at,
            resolver=resolver,
        )

        load_balancer_backend.additional_properties = d
        return load_balancer_backend

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
