from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.database_service_properties_opensearch_auth_failure_listeners_internal_authentication_backend_limiting_internal_authentication_backend_limiting_authentication_backend import (
    DatabaseServicePropertiesOpensearchAuthFailureListenersInternalAuthenticationBackendLimitingInternalAuthenticationBackendLimitingAuthenticationBackend,
)
from ..models.database_service_properties_opensearch_auth_failure_listeners_internal_authentication_backend_limiting_internal_authentication_backend_limiting_type import (
    DatabaseServicePropertiesOpensearchAuthFailureListenersInternalAuthenticationBackendLimitingInternalAuthenticationBackendLimitingType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseServicePropertiesOpensearchAuthFailureListenersInternalAuthenticationBackendLimiting")


@_attrs_define
class DatabaseServicePropertiesOpensearchAuthFailureListenersInternalAuthenticationBackendLimiting:
    """
    Attributes:
        allowed_tries (int | Unset): The number of login attempts allowed before login is blocked Example: 10.
        authentication_backend (DatabaseServicePropertiesOpensearchAuthFailureListenersInternalAuthenticationBackendLimi
            tingInternalAuthenticationBackendLimitingAuthenticationBackend | Unset): The internal backend. Enter `internal`
            Example: internal.
        block_expiry_seconds (int | Unset): The duration of time that login remains blocked after a failed login
            Example: 600.
        max_blocked_clients (int | Unset): The maximum number of blocked IP addresses Example: 100000.
        max_tracked_clients (int | Unset): The maximum number of tracked IP addresses that have failed login Example:
            100000.
        time_window_seconds (int | Unset): The window of time in which the value for `allowed_tries` is enforced
            Example: 3600.
        type_ (DatabaseServicePropertiesOpensearchAuthFailureListenersInternalAuthenticationBackendLimitingInternalAuthe
            nticationBackendLimitingType | Unset): The type of rate limiting Example: username.
    """

    allowed_tries: int | Unset = UNSET
    authentication_backend: (
        DatabaseServicePropertiesOpensearchAuthFailureListenersInternalAuthenticationBackendLimitingInternalAuthenticationBackendLimitingAuthenticationBackend
        | Unset
    ) = UNSET
    block_expiry_seconds: int | Unset = UNSET
    max_blocked_clients: int | Unset = UNSET
    max_tracked_clients: int | Unset = UNSET
    time_window_seconds: int | Unset = UNSET
    type_: (
        DatabaseServicePropertiesOpensearchAuthFailureListenersInternalAuthenticationBackendLimitingInternalAuthenticationBackendLimitingType
        | Unset
    ) = UNSET

    def to_dict(self) -> dict[str, Any]:
        allowed_tries = self.allowed_tries

        authentication_backend: str | Unset = UNSET
        if not isinstance(self.authentication_backend, Unset):
            authentication_backend = self.authentication_backend.value

        block_expiry_seconds = self.block_expiry_seconds

        max_blocked_clients = self.max_blocked_clients

        max_tracked_clients = self.max_tracked_clients

        time_window_seconds = self.time_window_seconds

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if allowed_tries is not UNSET:
            field_dict["allowed_tries"] = allowed_tries
        if authentication_backend is not UNSET:
            field_dict["authentication_backend"] = authentication_backend
        if block_expiry_seconds is not UNSET:
            field_dict["block_expiry_seconds"] = block_expiry_seconds
        if max_blocked_clients is not UNSET:
            field_dict["max_blocked_clients"] = max_blocked_clients
        if max_tracked_clients is not UNSET:
            field_dict["max_tracked_clients"] = max_tracked_clients
        if time_window_seconds is not UNSET:
            field_dict["time_window_seconds"] = time_window_seconds
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allowed_tries = d.pop("allowed_tries", UNSET)

        _authentication_backend = d.pop("authentication_backend", UNSET)
        authentication_backend: (
            DatabaseServicePropertiesOpensearchAuthFailureListenersInternalAuthenticationBackendLimitingInternalAuthenticationBackendLimitingAuthenticationBackend
            | Unset
        )
        if isinstance(_authentication_backend, Unset):
            authentication_backend = UNSET
        else:
            authentication_backend = DatabaseServicePropertiesOpensearchAuthFailureListenersInternalAuthenticationBackendLimitingInternalAuthenticationBackendLimitingAuthenticationBackend(
                _authentication_backend
            )

        block_expiry_seconds = d.pop("block_expiry_seconds", UNSET)

        max_blocked_clients = d.pop("max_blocked_clients", UNSET)

        max_tracked_clients = d.pop("max_tracked_clients", UNSET)

        time_window_seconds = d.pop("time_window_seconds", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: (
            DatabaseServicePropertiesOpensearchAuthFailureListenersInternalAuthenticationBackendLimitingInternalAuthenticationBackendLimitingType
            | Unset
        )
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = DatabaseServicePropertiesOpensearchAuthFailureListenersInternalAuthenticationBackendLimitingInternalAuthenticationBackendLimitingType(
                _type_
            )

        database_service_properties_opensearch_auth_failure_listeners_internal_authentication_backend_limiting = cls(
            allowed_tries=allowed_tries,
            authentication_backend=authentication_backend,
            block_expiry_seconds=block_expiry_seconds,
            max_blocked_clients=max_blocked_clients,
            max_tracked_clients=max_tracked_clients,
            time_window_seconds=time_window_seconds,
            type_=type_,
        )

        return database_service_properties_opensearch_auth_failure_listeners_internal_authentication_backend_limiting
