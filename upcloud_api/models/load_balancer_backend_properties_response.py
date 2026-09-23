from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

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

T = TypeVar("T", bound="LoadBalancerBackendPropertiesResponse")


@_attrs_define
class LoadBalancerBackendPropertiesResponse:
    """Properties of a backend configuration.

    Example:
        {'backend_id': 401, 'outbound_proxy_protocol': 'v2', 'timeout_server': 30000, 'timeout_tunnel': 30000,
            'health_check_type': 'http', 'health_check_interval': 10, 'health_check_fall': 3, 'health_check_rise': 2,
            'health_check_url': '/status', 'health_check_expected_status': 200, 'health_check_tls_verify': True,
            'health_check_on_down': 'shutdown-sessions', 'sticky_session_cookie_name': 'SESSIONID',
            'sticky_session_cookie_attributes': 'SameSite=Strict; Secure; HttpOnly', 'tls_enabled': True, 'tls_verify':
            False, 'tls_use_system_ca': True, 'http2_enabled': True}

    Attributes:
        backend_id (int): Identifier of the backend. Example: 401.
        timeout_server (int): Server timeout in milliseconds. Example: 30000.
        timeout_tunnel (int): Tunnel timeout in milliseconds. Example: 30000.
        health_check_type (str): Type of health check. Example: http.
        health_check_interval (int): Interval between health checks in seconds. Example: 10.
        health_check_fall (int): Number of failed checks before marking as unhealthy. Example: 3.
        health_check_rise (int): Number of successful checks before marking as healthy. Example: 2.
        health_check_url (str): URL for HTTP health checks. Example: /status.
        health_check_expected_status (int): Expected HTTP status code from health check. Example: 200.
        health_check_tls_verify (bool): Whether to verify TLS in health check. Example: True.
        health_check_on_down (str): Action to take when backend is down. Example: shutdown-sessions.
        tls_enabled (bool): Whether TLS is enabled. Example: True.
        tls_verify (bool): Whether to verify backend TLS certificate. Example: False.
        tls_use_system_ca (bool): Whether to use system CA for backend TLS. Example: True.
        http2_enabled (bool): Whether HTTP/2 is enabled for the backend. Example: True.
        outbound_proxy_protocol (LoadBalancerProxyProtocolVersionOrDisabledType1 |
            LoadBalancerProxyProtocolVersionOrDisabledType2Type1 | LoadBalancerProxyProtocolVersionOrDisabledType3Type1 |
            None | Unset): Empty string means disabled
        sticky_session_cookie_name (None | str | Unset): Name of the sticky session cookie. Example: SESSIONID.
        sticky_session_cookie_attributes (None | str | Unset): Additional cookie attributes appended to sticky session
            cookies. Supports combinations of: SameSite=Strict|Lax|None, Secure, HttpOnly, Partitioned (semicolon-
            separated). Example: SameSite=Strict; Secure; HttpOnly.
    """

    backend_id: int
    timeout_server: int
    timeout_tunnel: int
    health_check_type: str
    health_check_interval: int
    health_check_fall: int
    health_check_rise: int
    health_check_url: str
    health_check_expected_status: int
    health_check_tls_verify: bool
    health_check_on_down: str
    tls_enabled: bool
    tls_verify: bool
    tls_use_system_ca: bool
    http2_enabled: bool
    outbound_proxy_protocol: (
        LoadBalancerProxyProtocolVersionOrDisabledType1
        | LoadBalancerProxyProtocolVersionOrDisabledType2Type1
        | LoadBalancerProxyProtocolVersionOrDisabledType3Type1
        | None
        | Unset
    ) = UNSET
    sticky_session_cookie_name: None | str | Unset = UNSET
    sticky_session_cookie_attributes: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        backend_id = self.backend_id

        timeout_server = self.timeout_server

        timeout_tunnel = self.timeout_tunnel

        health_check_type = self.health_check_type

        health_check_interval = self.health_check_interval

        health_check_fall = self.health_check_fall

        health_check_rise = self.health_check_rise

        health_check_url = self.health_check_url

        health_check_expected_status = self.health_check_expected_status

        health_check_tls_verify = self.health_check_tls_verify

        health_check_on_down = self.health_check_on_down

        tls_enabled = self.tls_enabled

        tls_verify = self.tls_verify

        tls_use_system_ca = self.tls_use_system_ca

        http2_enabled = self.http2_enabled

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

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "backend_id": backend_id,
                "timeout_server": timeout_server,
                "timeout_tunnel": timeout_tunnel,
                "health_check_type": health_check_type,
                "health_check_interval": health_check_interval,
                "health_check_fall": health_check_fall,
                "health_check_rise": health_check_rise,
                "health_check_url": health_check_url,
                "health_check_expected_status": health_check_expected_status,
                "health_check_tls_verify": health_check_tls_verify,
                "health_check_on_down": health_check_on_down,
                "tls_enabled": tls_enabled,
                "tls_verify": tls_verify,
                "tls_use_system_ca": tls_use_system_ca,
                "http2_enabled": http2_enabled,
            }
        )
        if outbound_proxy_protocol is not UNSET:
            field_dict["outbound_proxy_protocol"] = outbound_proxy_protocol
        if sticky_session_cookie_name is not UNSET:
            field_dict["sticky_session_cookie_name"] = sticky_session_cookie_name
        if sticky_session_cookie_attributes is not UNSET:
            field_dict["sticky_session_cookie_attributes"] = sticky_session_cookie_attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        backend_id = d.pop("backend_id")

        timeout_server = d.pop("timeout_server")

        timeout_tunnel = d.pop("timeout_tunnel")

        health_check_type = d.pop("health_check_type")

        health_check_interval = d.pop("health_check_interval")

        health_check_fall = d.pop("health_check_fall")

        health_check_rise = d.pop("health_check_rise")

        health_check_url = d.pop("health_check_url")

        health_check_expected_status = d.pop("health_check_expected_status")

        health_check_tls_verify = d.pop("health_check_tls_verify")

        health_check_on_down = d.pop("health_check_on_down")

        tls_enabled = d.pop("tls_enabled")

        tls_verify = d.pop("tls_verify")

        tls_use_system_ca = d.pop("tls_use_system_ca")

        http2_enabled = d.pop("http2_enabled")

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

        load_balancer_backend_properties_response = cls(
            backend_id=backend_id,
            timeout_server=timeout_server,
            timeout_tunnel=timeout_tunnel,
            health_check_type=health_check_type,
            health_check_interval=health_check_interval,
            health_check_fall=health_check_fall,
            health_check_rise=health_check_rise,
            health_check_url=health_check_url,
            health_check_expected_status=health_check_expected_status,
            health_check_tls_verify=health_check_tls_verify,
            health_check_on_down=health_check_on_down,
            tls_enabled=tls_enabled,
            tls_verify=tls_verify,
            tls_use_system_ca=tls_use_system_ca,
            http2_enabled=http2_enabled,
            outbound_proxy_protocol=outbound_proxy_protocol,
            sticky_session_cookie_name=sticky_session_cookie_name,
            sticky_session_cookie_attributes=sticky_session_cookie_attributes,
        )

        return load_balancer_backend_properties_response
