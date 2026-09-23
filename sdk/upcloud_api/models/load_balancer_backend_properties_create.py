from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.load_balancer_checks_on_down import LoadBalancerChecksOnDown
from ..models.load_balancer_health_check_type import LoadBalancerHealthCheckType
from ..models.load_balancer_proxy_protocol_version_or_disabled_type_1 import (
    LoadBalancerProxyProtocolVersionOrDisabledType1,
)
from ..models.load_balancer_proxy_protocol_version_or_disabled_type_2_type_1 import (
    LoadBalancerProxyProtocolVersionOrDisabledType2Type1,
)
from ..models.load_balancer_proxy_protocol_version_or_disabled_type_3_type_1 import (
    LoadBalancerProxyProtocolVersionOrDisabledType3Type1,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="LoadBalancerBackendPropertiesCreate")


@_attrs_define
class LoadBalancerBackendPropertiesCreate:
    """Backend Properties

    Attributes:
        timeout_server (int | Unset): Server timeout
        timeout_tunnel (int | Unset): Tunnel timeout
        outbound_proxy_protocol (LoadBalancerProxyProtocolVersionOrDisabledType1 |
            LoadBalancerProxyProtocolVersionOrDisabledType2Type1 | LoadBalancerProxyProtocolVersionOrDisabledType3Type1 |
            None | Unset): Empty string means disabled
        health_check_type (LoadBalancerHealthCheckType | Unset): Health check type
        health_check_interval (int | Unset): Interval between health checks
        health_check_fall (int | Unset): Sets how many failed health checks are allowed
        health_check_rise (int | Unset): Sets how many passing checks there must be before returning server to the
            rotation
        health_check_url (str | Unset): Target url for health check HTTP GET requests
        health_check_expected_status (int | Unset): Expected HTTP status code returned by the customer application to
            mark server as healthy Example: 200.
        health_check_on_down (LoadBalancerChecksOnDown | Unset): Checks on down category
        health_check_tls_verify (bool | Unset): Allows health check CA verification on TLS connections
        sticky_session_cookie_name (None | str | Unset): Sets sticky session cookie name. Empty string disables sticky
            session.
        sticky_session_cookie_attributes (None | str | Unset): Controls additional cookie attributes appended to sticky
            session cookies. Supports combinations of: SameSite=Strict|Lax|None, Secure, HttpOnly, Partitioned (semicolon-
            separated). Note: SameSite=None and Partitioned require Secure.
        tls_enabled (bool | Unset): Enables TLS between LB backend and member servers
        tls_verify (bool | Unset): Enables CA verification on TLS backend connections
        tls_use_system_ca (bool | Unset): Force Load Balancer to verify member certificates against system CA bundle
        http2_enabled (bool | Unset): Allows for HTTP2 connection via ALPN
    """

    timeout_server: int | Unset = UNSET
    timeout_tunnel: int | Unset = UNSET
    outbound_proxy_protocol: (
        LoadBalancerProxyProtocolVersionOrDisabledType1
        | LoadBalancerProxyProtocolVersionOrDisabledType2Type1
        | LoadBalancerProxyProtocolVersionOrDisabledType3Type1
        | None
        | Unset
    ) = UNSET
    health_check_type: LoadBalancerHealthCheckType | Unset = UNSET
    health_check_interval: int | Unset = UNSET
    health_check_fall: int | Unset = UNSET
    health_check_rise: int | Unset = UNSET
    health_check_url: str | Unset = UNSET
    health_check_expected_status: int | Unset = UNSET
    health_check_on_down: LoadBalancerChecksOnDown | Unset = UNSET
    health_check_tls_verify: bool | Unset = UNSET
    sticky_session_cookie_name: None | str | Unset = UNSET
    sticky_session_cookie_attributes: None | str | Unset = UNSET
    tls_enabled: bool | Unset = UNSET
    tls_verify: bool | Unset = UNSET
    tls_use_system_ca: bool | Unset = UNSET
    http2_enabled: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        timeout_server = self.timeout_server

        timeout_tunnel = self.timeout_tunnel

        outbound_proxy_protocol: None | str | Unset
        if isinstance(self.outbound_proxy_protocol, Unset):
            outbound_proxy_protocol = UNSET
        elif isinstance(self.outbound_proxy_protocol, LoadBalancerProxyProtocolVersionOrDisabledType1):
            outbound_proxy_protocol = self.outbound_proxy_protocol.value
        elif isinstance(self.outbound_proxy_protocol, LoadBalancerProxyProtocolVersionOrDisabledType2Type1):
            outbound_proxy_protocol = self.outbound_proxy_protocol.value
        elif isinstance(self.outbound_proxy_protocol, LoadBalancerProxyProtocolVersionOrDisabledType3Type1):
            outbound_proxy_protocol = self.outbound_proxy_protocol.value
        else:
            outbound_proxy_protocol = self.outbound_proxy_protocol

        health_check_type: str | Unset = UNSET
        if not isinstance(self.health_check_type, Unset):
            health_check_type = self.health_check_type.value

        health_check_interval = self.health_check_interval

        health_check_fall = self.health_check_fall

        health_check_rise = self.health_check_rise

        health_check_url = self.health_check_url

        health_check_expected_status = self.health_check_expected_status

        health_check_on_down: str | Unset = UNSET
        if not isinstance(self.health_check_on_down, Unset):
            health_check_on_down = self.health_check_on_down.value

        health_check_tls_verify = self.health_check_tls_verify

        sticky_session_cookie_name: None | str | Unset
        if isinstance(self.sticky_session_cookie_name, Unset):
            sticky_session_cookie_name = UNSET
        else:
            sticky_session_cookie_name = self.sticky_session_cookie_name

        sticky_session_cookie_attributes: None | str | Unset
        if isinstance(self.sticky_session_cookie_attributes, Unset):
            sticky_session_cookie_attributes = UNSET
        else:
            sticky_session_cookie_attributes = self.sticky_session_cookie_attributes

        tls_enabled = self.tls_enabled

        tls_verify = self.tls_verify

        tls_use_system_ca = self.tls_use_system_ca

        http2_enabled = self.http2_enabled

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if timeout_server is not UNSET:
            field_dict["timeout_server"] = timeout_server
        if timeout_tunnel is not UNSET:
            field_dict["timeout_tunnel"] = timeout_tunnel
        if outbound_proxy_protocol is not UNSET:
            field_dict["outbound_proxy_protocol"] = outbound_proxy_protocol
        if health_check_type is not UNSET:
            field_dict["health_check_type"] = health_check_type
        if health_check_interval is not UNSET:
            field_dict["health_check_interval"] = health_check_interval
        if health_check_fall is not UNSET:
            field_dict["health_check_fall"] = health_check_fall
        if health_check_rise is not UNSET:
            field_dict["health_check_rise"] = health_check_rise
        if health_check_url is not UNSET:
            field_dict["health_check_url"] = health_check_url
        if health_check_expected_status is not UNSET:
            field_dict["health_check_expected_status"] = health_check_expected_status
        if health_check_on_down is not UNSET:
            field_dict["health_check_on_down"] = health_check_on_down
        if health_check_tls_verify is not UNSET:
            field_dict["health_check_tls_verify"] = health_check_tls_verify
        if sticky_session_cookie_name is not UNSET:
            field_dict["sticky_session_cookie_name"] = sticky_session_cookie_name
        if sticky_session_cookie_attributes is not UNSET:
            field_dict["sticky_session_cookie_attributes"] = sticky_session_cookie_attributes
        if tls_enabled is not UNSET:
            field_dict["tls_enabled"] = tls_enabled
        if tls_verify is not UNSET:
            field_dict["tls_verify"] = tls_verify
        if tls_use_system_ca is not UNSET:
            field_dict["tls_use_system_ca"] = tls_use_system_ca
        if http2_enabled is not UNSET:
            field_dict["http2_enabled"] = http2_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        timeout_server = d.pop("timeout_server", UNSET)

        timeout_tunnel = d.pop("timeout_tunnel", UNSET)

        def _parse_outbound_proxy_protocol(
            data: object,
        ) -> (
            LoadBalancerProxyProtocolVersionOrDisabledType1
            | LoadBalancerProxyProtocolVersionOrDisabledType2Type1
            | LoadBalancerProxyProtocolVersionOrDisabledType3Type1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemasload_balancer_proxy_protocol_version_or_disabled_type_1 = (
                    LoadBalancerProxyProtocolVersionOrDisabledType1(data)
                )

                return componentsschemasload_balancer_proxy_protocol_version_or_disabled_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemasload_balancer_proxy_protocol_version_or_disabled_type_2_type_1 = (
                    LoadBalancerProxyProtocolVersionOrDisabledType2Type1(data)
                )

                return componentsschemasload_balancer_proxy_protocol_version_or_disabled_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemasload_balancer_proxy_protocol_version_or_disabled_type_3_type_1 = (
                    LoadBalancerProxyProtocolVersionOrDisabledType3Type1(data)
                )

                return componentsschemasload_balancer_proxy_protocol_version_or_disabled_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                LoadBalancerProxyProtocolVersionOrDisabledType1
                | LoadBalancerProxyProtocolVersionOrDisabledType2Type1
                | LoadBalancerProxyProtocolVersionOrDisabledType3Type1
                | None
                | Unset,
                data,
            )

        outbound_proxy_protocol = _parse_outbound_proxy_protocol(d.pop("outbound_proxy_protocol", UNSET))

        _health_check_type = d.pop("health_check_type", UNSET)
        health_check_type: LoadBalancerHealthCheckType | Unset
        if isinstance(_health_check_type, Unset):
            health_check_type = UNSET
        else:
            health_check_type = LoadBalancerHealthCheckType(_health_check_type)

        health_check_interval = d.pop("health_check_interval", UNSET)

        health_check_fall = d.pop("health_check_fall", UNSET)

        health_check_rise = d.pop("health_check_rise", UNSET)

        health_check_url = d.pop("health_check_url", UNSET)

        health_check_expected_status = d.pop("health_check_expected_status", UNSET)

        _health_check_on_down = d.pop("health_check_on_down", UNSET)
        health_check_on_down: LoadBalancerChecksOnDown | Unset
        if isinstance(_health_check_on_down, Unset):
            health_check_on_down = UNSET
        else:
            health_check_on_down = LoadBalancerChecksOnDown(_health_check_on_down)

        health_check_tls_verify = d.pop("health_check_tls_verify", UNSET)

        def _parse_sticky_session_cookie_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sticky_session_cookie_name = _parse_sticky_session_cookie_name(d.pop("sticky_session_cookie_name", UNSET))

        def _parse_sticky_session_cookie_attributes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sticky_session_cookie_attributes = _parse_sticky_session_cookie_attributes(
            d.pop("sticky_session_cookie_attributes", UNSET)
        )

        tls_enabled = d.pop("tls_enabled", UNSET)

        tls_verify = d.pop("tls_verify", UNSET)

        tls_use_system_ca = d.pop("tls_use_system_ca", UNSET)

        http2_enabled = d.pop("http2_enabled", UNSET)

        load_balancer_backend_properties_create = cls(
            timeout_server=timeout_server,
            timeout_tunnel=timeout_tunnel,
            outbound_proxy_protocol=outbound_proxy_protocol,
            health_check_type=health_check_type,
            health_check_interval=health_check_interval,
            health_check_fall=health_check_fall,
            health_check_rise=health_check_rise,
            health_check_url=health_check_url,
            health_check_expected_status=health_check_expected_status,
            health_check_on_down=health_check_on_down,
            health_check_tls_verify=health_check_tls_verify,
            sticky_session_cookie_name=sticky_session_cookie_name,
            sticky_session_cookie_attributes=sticky_session_cookie_attributes,
            tls_enabled=tls_enabled,
            tls_verify=tls_verify,
            tls_use_system_ca=tls_use_system_ca,
            http2_enabled=http2_enabled,
        )

        return load_balancer_backend_properties_create
