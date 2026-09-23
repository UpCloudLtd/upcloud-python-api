from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.load_balancer_frontend_mode import LoadBalancerFrontendMode

if TYPE_CHECKING:
    from ..models.load_balancer_frontend_networks_item import LoadBalancerFrontendNetworksItem
    from ..models.load_balancer_frontend_properties_response import LoadBalancerFrontendPropertiesResponse
    from ..models.load_balancer_rule import LoadBalancerRule
    from ..models.load_balancer_tls_config import LoadBalancerTlsConfig


T = TypeVar("T", bound="LoadBalancerFrontend")


@_attrs_define
class LoadBalancerFrontend:
    """Represents a frontend configuration in the load balancer service, defining how client connections are received, the
    listening port and protocol, TLS settings, routing rules, and default backend association.

        Attributes:
            name (str): Human-readable name assigned to the frontend. Example: frontend-1.
            port (int): Port number on which the frontend listens for incoming connections. Example: 80.
            mode (LoadBalancerFrontendMode): Operating mode defining the protocol layer at which the frontend operates.
                Example: http.
            default_backend (str): Name of the backend used when no routing rules match the incoming request. Example:
                backend-1.
            tls_configs (list[LoadBalancerTlsConfig]): Represents a list of TLS configuration for a frontend or backend,
                defining the certificate bundle and associated identifiers within the load balancer service.
            rules (list[LoadBalancerRule]): Represents a list of load balancer rules that define how incoming requests are
                matched and processed, including conditions, actions, and backend target associations.
            properties (LoadBalancerFrontendPropertiesResponse): Defines configurable properties for a frontend, such as
                client timeout settings, protocol options, and linkage to its parent frontend resource. Example:
                {'inbound_proxy_protocol': False, 'timeout_client': 50000, 'http2_enabled': True, 'frontend_id': 301}.
            networks (list[LoadBalancerFrontendNetworksItem]):  Example: [{'name': 'public-network'}, {'name': 'private-
                network'}].
            created_at (datetime.datetime): Timestamp when the frontend was created (RFC 3339 format).
            updated_at (datetime.datetime): Timestamp when the frontend was last updated (RFC 3339 format).
    """

    name: str
    port: int
    mode: LoadBalancerFrontendMode
    default_backend: str
    tls_configs: list[LoadBalancerTlsConfig]
    rules: list[LoadBalancerRule]
    properties: LoadBalancerFrontendPropertiesResponse
    networks: list[LoadBalancerFrontendNetworksItem]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        port = self.port

        mode = self.mode.value

        default_backend = self.default_backend

        tls_configs = []
        for componentsschemasload_balancer_tls_configs_response_item_data in self.tls_configs:
            componentsschemasload_balancer_tls_configs_response_item = (
                componentsschemasload_balancer_tls_configs_response_item_data.to_dict()
            )
            tls_configs.append(componentsschemasload_balancer_tls_configs_response_item)

        rules = []
        for componentsschemasload_balancer_rules_response_item_data in self.rules:
            componentsschemasload_balancer_rules_response_item = (
                componentsschemasload_balancer_rules_response_item_data.to_dict()
            )
            rules.append(componentsschemasload_balancer_rules_response_item)

        properties = self.properties.to_dict()

        networks = []
        for networks_item_data in self.networks:
            networks_item = networks_item_data.to_dict()
            networks.append(networks_item)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "port": port,
                "mode": mode,
                "default_backend": default_backend,
                "tls_configs": tls_configs,
                "rules": rules,
                "properties": properties,
                "networks": networks,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.load_balancer_frontend_networks_item import LoadBalancerFrontendNetworksItem  # noqa: PLC0415
        from ..models.load_balancer_frontend_properties_response import (
            LoadBalancerFrontendPropertiesResponse,  # noqa: PLC0415
        )
        from ..models.load_balancer_rule import LoadBalancerRule  # noqa: PLC0415
        from ..models.load_balancer_tls_config import LoadBalancerTlsConfig  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        port = d.pop("port")

        mode = LoadBalancerFrontendMode(d.pop("mode"))

        default_backend = d.pop("default_backend")

        tls_configs = []
        _tls_configs = d.pop("tls_configs")
        for componentsschemasload_balancer_tls_configs_response_item_data in _tls_configs:
            componentsschemasload_balancer_tls_configs_response_item = LoadBalancerTlsConfig.from_dict(
                componentsschemasload_balancer_tls_configs_response_item_data
            )

            tls_configs.append(componentsschemasload_balancer_tls_configs_response_item)

        rules = []
        _rules = d.pop("rules")
        for componentsschemasload_balancer_rules_response_item_data in _rules:
            componentsschemasload_balancer_rules_response_item = LoadBalancerRule.from_dict(
                componentsschemasload_balancer_rules_response_item_data
            )

            rules.append(componentsschemasload_balancer_rules_response_item)

        properties = LoadBalancerFrontendPropertiesResponse.from_dict(d.pop("properties"))

        networks = []
        _networks = d.pop("networks")
        for networks_item_data in _networks:
            networks_item = LoadBalancerFrontendNetworksItem.from_dict(networks_item_data)

            networks.append(networks_item)

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        load_balancer_frontend = cls(
            name=name,
            port=port,
            mode=mode,
            default_backend=default_backend,
            tls_configs=tls_configs,
            rules=rules,
            properties=properties,
            networks=networks,
            created_at=created_at,
            updated_at=updated_at,
        )

        load_balancer_frontend.additional_properties = d
        return load_balancer_frontend

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
