from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.load_balancer_frontend_mode import LoadBalancerFrontendMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.load_balancer_frontend_network_create import LoadBalancerFrontendNetworkCreate
    from ..models.load_balancer_frontend_properties_create import LoadBalancerFrontendPropertiesCreate
    from ..models.load_balancer_rule_create import LoadBalancerRuleCreate
    from ..models.load_balancer_tls_config_create import LoadBalancerTlsConfigCreate


T = TypeVar("T", bound="LoadBalancerFrontendCreate")


@_attrs_define
class LoadBalancerFrontendCreate:
    """Load Balancer Frontend

    Attributes:
        name (str): Name of the frontend Example: my-frontend.
        port (int): Port to listen
        mode (LoadBalancerFrontendMode): Mode
        default_backend (str): Default backend
        networks (list[LoadBalancerFrontendNetworkCreate] | Unset): Network names
        tls_configs (list[LoadBalancerTlsConfigCreate] | None | Unset): TLS Configs
        rules (list[LoadBalancerRuleCreate] | None | Unset): Rules
        properties (LoadBalancerFrontendPropertiesCreate | Unset): Frontend Properties Example: {'timeout_client': 60,
            'inbound_proxy_protocol': False, 'http2_enabled': True}.
    """

    name: str
    port: int
    mode: LoadBalancerFrontendMode
    default_backend: str
    networks: list[LoadBalancerFrontendNetworkCreate] | Unset = UNSET
    tls_configs: list[LoadBalancerTlsConfigCreate] | None | Unset = UNSET
    rules: list[LoadBalancerRuleCreate] | None | Unset = UNSET
    properties: LoadBalancerFrontendPropertiesCreate | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        port = self.port

        mode = self.mode.value

        default_backend = self.default_backend

        networks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.networks, Unset):
            networks = []
            for networks_item_data in self.networks:
                networks_item = networks_item_data.to_dict()
                networks.append(networks_item)

        tls_configs: list[dict[str, Any]] | None | Unset
        if isinstance(self.tls_configs, Unset):
            tls_configs = UNSET
        elif isinstance(self.tls_configs, list):
            tls_configs = []
            for tls_configs_type_0_item_data in self.tls_configs:
                tls_configs_type_0_item = tls_configs_type_0_item_data.to_dict()
                tls_configs.append(tls_configs_type_0_item)

        else:
            tls_configs = self.tls_configs

        rules: list[dict[str, Any]] | None | Unset
        if isinstance(self.rules, Unset):
            rules = UNSET
        elif isinstance(self.rules, list):
            rules = []
            for rules_type_0_item_data in self.rules:
                rules_type_0_item = rules_type_0_item_data.to_dict()
                rules.append(rules_type_0_item)

        else:
            rules = self.rules

        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "port": port,
                "mode": mode,
                "default_backend": default_backend,
            }
        )
        if networks is not UNSET:
            field_dict["networks"] = networks
        if tls_configs is not UNSET:
            field_dict["tls_configs"] = tls_configs
        if rules is not UNSET:
            field_dict["rules"] = rules
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.load_balancer_frontend_network_create import LoadBalancerFrontendNetworkCreate  # noqa: PLC0415
        from ..models.load_balancer_frontend_properties_create import (
            LoadBalancerFrontendPropertiesCreate,  # noqa: PLC0415
        )
        from ..models.load_balancer_rule_create import LoadBalancerRuleCreate  # noqa: PLC0415
        from ..models.load_balancer_tls_config_create import LoadBalancerTlsConfigCreate  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        port = d.pop("port")

        mode = LoadBalancerFrontendMode(d.pop("mode"))

        default_backend = d.pop("default_backend")

        _networks = d.pop("networks", UNSET)
        networks: list[LoadBalancerFrontendNetworkCreate] | Unset = UNSET
        if _networks is not UNSET:
            networks = []
            for networks_item_data in _networks:
                networks_item = LoadBalancerFrontendNetworkCreate.from_dict(networks_item_data)

                networks.append(networks_item)

        def _parse_tls_configs(data: object) -> list[LoadBalancerTlsConfigCreate] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tls_configs_type_0 = []
                _tls_configs_type_0 = data
                for tls_configs_type_0_item_data in _tls_configs_type_0:
                    tls_configs_type_0_item = LoadBalancerTlsConfigCreate.from_dict(tls_configs_type_0_item_data)

                    tls_configs_type_0.append(tls_configs_type_0_item)

                return tls_configs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[LoadBalancerTlsConfigCreate] | None | Unset, data)

        tls_configs = _parse_tls_configs(d.pop("tls_configs", UNSET))

        def _parse_rules(data: object) -> list[LoadBalancerRuleCreate] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                rules_type_0 = []
                _rules_type_0 = data
                for rules_type_0_item_data in _rules_type_0:
                    rules_type_0_item = LoadBalancerRuleCreate.from_dict(rules_type_0_item_data)

                    rules_type_0.append(rules_type_0_item)

                return rules_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[LoadBalancerRuleCreate] | None | Unset, data)

        rules = _parse_rules(d.pop("rules", UNSET))

        _properties = d.pop("properties", UNSET)
        properties: LoadBalancerFrontendPropertiesCreate | Unset
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = LoadBalancerFrontendPropertiesCreate.from_dict(_properties)

        load_balancer_frontend_create = cls(
            name=name,
            port=port,
            mode=mode,
            default_backend=default_backend,
            networks=networks,
            tls_configs=tls_configs,
            rules=rules,
            properties=properties,
        )

        return load_balancer_frontend_create
