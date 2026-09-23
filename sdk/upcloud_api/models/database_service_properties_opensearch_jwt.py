from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseServicePropertiesOpensearchJwt")


@_attrs_define
class DatabaseServicePropertiesOpensearchJwt:
    """
    Attributes:
        enabled (bool): Enables or disables JWT-based authentication for OpenSearch. When enabled, users can
            authenticate using JWT tokens.
        signing_key (str): The secret key used to sign and verify JWT tokens. This should be a secure, randomly
            generated key HMAC key or public RSA/ECDSA key.
        jwt_clock_skew_tolerance_seconds (int | None | Unset): The maximum allowed time difference in seconds between
            the JWT issuer's clock and the OpenSearch server's clock. This helps prevent token validation failures due to
            minor time synchronization issues.
        jwt_header (None | str | Unset): The HTTP header name where the JWT token is transmitted. Typically
            'Authorization' for Bearer tokens.
        jwt_url_parameter (None | str | Unset): If the JWT token is transmitted as a URL parameter instead of an HTTP
            header, specify the parameter name here.
        required_audience (None | str | Unset): If specified, the JWT must contain an 'aud' claim that matches this
            value. This provides additional security by ensuring the JWT was issued for the expected audience.
        required_issuer (None | str | Unset): If specified, the JWT must contain an 'iss' claim that matches this value.
            This provides additional security by ensuring the JWT was issued by the expected issuer.
        roles_key (None | str | Unset): The key in the JWT payload that contains the user's roles. If specified, roles
            will be extracted from the JWT for authorization.
        subject_key (None | str | Unset): The key in the JWT payload that contains the user's subject identifier. If not
            specified, the 'sub' claim is used by default.
    """

    enabled: bool
    signing_key: str
    jwt_clock_skew_tolerance_seconds: int | None | Unset = UNSET
    jwt_header: None | str | Unset = UNSET
    jwt_url_parameter: None | str | Unset = UNSET
    required_audience: None | str | Unset = UNSET
    required_issuer: None | str | Unset = UNSET
    roles_key: None | str | Unset = UNSET
    subject_key: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        signing_key = self.signing_key

        jwt_clock_skew_tolerance_seconds: int | None | Unset
        if isinstance(self.jwt_clock_skew_tolerance_seconds, Unset):
            jwt_clock_skew_tolerance_seconds = UNSET
        else:
            jwt_clock_skew_tolerance_seconds = self.jwt_clock_skew_tolerance_seconds

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

        required_audience: None | str | Unset
        if isinstance(self.required_audience, Unset):
            required_audience = UNSET
        else:
            required_audience = self.required_audience

        required_issuer: None | str | Unset
        if isinstance(self.required_issuer, Unset):
            required_issuer = UNSET
        else:
            required_issuer = self.required_issuer

        roles_key: None | str | Unset
        if isinstance(self.roles_key, Unset):
            roles_key = UNSET
        else:
            roles_key = self.roles_key

        subject_key: None | str | Unset
        if isinstance(self.subject_key, Unset):
            subject_key = UNSET
        else:
            subject_key = self.subject_key

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "enabled": enabled,
                "signing_key": signing_key,
            }
        )
        if jwt_clock_skew_tolerance_seconds is not UNSET:
            field_dict["jwt_clock_skew_tolerance_seconds"] = jwt_clock_skew_tolerance_seconds
        if jwt_header is not UNSET:
            field_dict["jwt_header"] = jwt_header
        if jwt_url_parameter is not UNSET:
            field_dict["jwt_url_parameter"] = jwt_url_parameter
        if required_audience is not UNSET:
            field_dict["required_audience"] = required_audience
        if required_issuer is not UNSET:
            field_dict["required_issuer"] = required_issuer
        if roles_key is not UNSET:
            field_dict["roles_key"] = roles_key
        if subject_key is not UNSET:
            field_dict["subject_key"] = subject_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled")

        signing_key = d.pop("signing_key")

        def _parse_jwt_clock_skew_tolerance_seconds(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        jwt_clock_skew_tolerance_seconds = _parse_jwt_clock_skew_tolerance_seconds(
            d.pop("jwt_clock_skew_tolerance_seconds", UNSET)
        )

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

        def _parse_required_audience(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        required_audience = _parse_required_audience(d.pop("required_audience", UNSET))

        def _parse_required_issuer(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        required_issuer = _parse_required_issuer(d.pop("required_issuer", UNSET))

        def _parse_roles_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        roles_key = _parse_roles_key(d.pop("roles_key", UNSET))

        def _parse_subject_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subject_key = _parse_subject_key(d.pop("subject_key", UNSET))

        database_service_properties_opensearch_jwt = cls(
            enabled=enabled,
            signing_key=signing_key,
            jwt_clock_skew_tolerance_seconds=jwt_clock_skew_tolerance_seconds,
            jwt_header=jwt_header,
            jwt_url_parameter=jwt_url_parameter,
            required_audience=required_audience,
            required_issuer=required_issuer,
            roles_key=roles_key,
            subject_key=subject_key,
        )

        return database_service_properties_opensearch_jwt
