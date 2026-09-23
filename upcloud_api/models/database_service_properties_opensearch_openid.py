from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseServicePropertiesOpensearchOpenid")


@_attrs_define
class DatabaseServicePropertiesOpensearchOpenid:
    """
    Attributes:
        client_id (str): The ID of the OpenID Connect client configured in your IdP. Required.
        client_secret (str): The client secret of the OpenID Connect client configured in your IdP. Required.
        connect_url (str): The URL of your IdP where the Security plugin can find the OpenID Connect
            metadata/configuration settings.
        enabled (bool): Enables or disables OpenID Connect authentication for OpenSearch. When enabled, users can
            authenticate using OpenID Connect with an Identity Provider.
        header (str | Unset): HTTP header name of the JWT token. Optional. Default is Authorization.
        jwt_header (None | str | Unset): The HTTP header that stores the token. Typically the Authorization header with
            the Bearer schema: Authorization: Bearer <token>. Optional. Default is Authorization.
        jwt_url_parameter (None | str | Unset): If the token is not transmitted in the HTTP header, but as an URL
            parameter, define the name of the parameter here. Optional.
        refresh_rate_limit_count (int | None | Unset): The maximum number of unknown key IDs in the time frame. Default
            is 10. Optional.
        refresh_rate_limit_time_window_ms (int | None | Unset): The time frame to use when checking the maximum number
            of unknown key IDs, in milliseconds. Optional.Default is 10000 (10 seconds).
        roles_key (None | str | Unset): The key in the JSON payload that stores the user’s roles. The value of this key
            must be a comma-separated list of roles. Required only if you want to use roles in the JWT
        scope (str | Unset): The scope of the identity token issued by the IdP. Optional. Default is openid profile
            email address phone.
        subject_key (None | str | Unset): The key in the JSON payload that stores the user’s name. If not defined, the
            subject registered claim is used. Most IdP providers use the preferred_username claim. Optional.
    """

    client_id: str
    client_secret: str
    connect_url: str
    enabled: bool
    header: str | Unset = UNSET
    jwt_header: None | str | Unset = UNSET
    jwt_url_parameter: None | str | Unset = UNSET
    refresh_rate_limit_count: int | None | Unset = UNSET
    refresh_rate_limit_time_window_ms: int | None | Unset = UNSET
    roles_key: None | str | Unset = UNSET
    scope: str | Unset = UNSET
    subject_key: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        client_id = self.client_id

        client_secret = self.client_secret

        connect_url = self.connect_url

        enabled = self.enabled

        header = self.header

        jwt_header: None | str | Unset
        if isinstance(self.jwt_header, Unset):
            jwt_header = UNSET
        else:
            jwt_header = self.jwt_header

        jwt_url_parameter: None | str | Unset
        if isinstance(self.jwt_url_parameter, Unset):
            jwt_url_parameter = UNSET
        else:
            jwt_url_parameter = self.jwt_url_parameter

        refresh_rate_limit_count: int | None | Unset
        if isinstance(self.refresh_rate_limit_count, Unset):
            refresh_rate_limit_count = UNSET
        else:
            refresh_rate_limit_count = self.refresh_rate_limit_count

        refresh_rate_limit_time_window_ms: int | None | Unset
        if isinstance(self.refresh_rate_limit_time_window_ms, Unset):
            refresh_rate_limit_time_window_ms = UNSET
        else:
            refresh_rate_limit_time_window_ms = self.refresh_rate_limit_time_window_ms

        roles_key: None | str | Unset
        if isinstance(self.roles_key, Unset):
            roles_key = UNSET
        else:
            roles_key = self.roles_key

        scope = self.scope

        subject_key: None | str | Unset
        if isinstance(self.subject_key, Unset):
            subject_key = UNSET
        else:
            subject_key = self.subject_key

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "client_id": client_id,
                "client_secret": client_secret,
                "connect_url": connect_url,
                "enabled": enabled,
            }
        )
        if header is not UNSET:
            field_dict["header"] = header
        if jwt_header is not UNSET:
            field_dict["jwt_header"] = jwt_header
        if jwt_url_parameter is not UNSET:
            field_dict["jwt_url_parameter"] = jwt_url_parameter
        if refresh_rate_limit_count is not UNSET:
            field_dict["refresh_rate_limit_count"] = refresh_rate_limit_count
        if refresh_rate_limit_time_window_ms is not UNSET:
            field_dict["refresh_rate_limit_time_window_ms"] = refresh_rate_limit_time_window_ms
        if roles_key is not UNSET:
            field_dict["roles_key"] = roles_key
        if scope is not UNSET:
            field_dict["scope"] = scope
        if subject_key is not UNSET:
            field_dict["subject_key"] = subject_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        client_id = d.pop("client_id")

        client_secret = d.pop("client_secret")

        connect_url = d.pop("connect_url")

        enabled = d.pop("enabled")

        header = d.pop("header", UNSET)

        def _parse_jwt_header(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        jwt_header = _parse_jwt_header(d.pop("jwt_header", UNSET))

        def _parse_jwt_url_parameter(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        jwt_url_parameter = _parse_jwt_url_parameter(d.pop("jwt_url_parameter", UNSET))

        def _parse_refresh_rate_limit_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        refresh_rate_limit_count = _parse_refresh_rate_limit_count(d.pop("refresh_rate_limit_count", UNSET))

        def _parse_refresh_rate_limit_time_window_ms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        refresh_rate_limit_time_window_ms = _parse_refresh_rate_limit_time_window_ms(
            d.pop("refresh_rate_limit_time_window_ms", UNSET)
        )

        def _parse_roles_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        roles_key = _parse_roles_key(d.pop("roles_key", UNSET))

        scope = d.pop("scope", UNSET)

        def _parse_subject_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subject_key = _parse_subject_key(d.pop("subject_key", UNSET))

        database_service_properties_opensearch_openid = cls(
            client_id=client_id,
            client_secret=client_secret,
            connect_url=connect_url,
            enabled=enabled,
            header=header,
            jwt_header=jwt_header,
            jwt_url_parameter=jwt_url_parameter,
            refresh_rate_limit_count=refresh_rate_limit_count,
            refresh_rate_limit_time_window_ms=refresh_rate_limit_time_window_ms,
            roles_key=roles_key,
            scope=scope,
            subject_key=subject_key,
        )

        return database_service_properties_opensearch_openid
