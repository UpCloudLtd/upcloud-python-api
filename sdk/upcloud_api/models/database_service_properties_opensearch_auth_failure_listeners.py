from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_service_properties_opensearch_auth_failure_listeners_internal_authentication_backend_limiting import (
        DatabaseServicePropertiesOpensearchAuthFailureListenersInternalAuthenticationBackendLimiting,
    )


T = TypeVar("T", bound="DatabaseServicePropertiesOpensearchAuthFailureListeners")


@_attrs_define
class DatabaseServicePropertiesOpensearchAuthFailureListeners:
    """
    Attributes:
        internal_authentication_backend_limiting
            (DatabaseServicePropertiesOpensearchAuthFailureListenersInternalAuthenticationBackendLimiting | Unset):
    """

    internal_authentication_backend_limiting: (
        DatabaseServicePropertiesOpensearchAuthFailureListenersInternalAuthenticationBackendLimiting | Unset
    ) = UNSET

    def to_dict(self) -> dict[str, Any]:
        internal_authentication_backend_limiting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.internal_authentication_backend_limiting, Unset):
            internal_authentication_backend_limiting = self.internal_authentication_backend_limiting.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if internal_authentication_backend_limiting is not UNSET:
            field_dict["internal_authentication_backend_limiting"] = internal_authentication_backend_limiting

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_service_properties_opensearch_auth_failure_listeners_internal_authentication_backend_limiting import (
            DatabaseServicePropertiesOpensearchAuthFailureListenersInternalAuthenticationBackendLimiting,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _internal_authentication_backend_limiting = d.pop("internal_authentication_backend_limiting", UNSET)
        internal_authentication_backend_limiting: (
            DatabaseServicePropertiesOpensearchAuthFailureListenersInternalAuthenticationBackendLimiting | Unset
        )
        if isinstance(_internal_authentication_backend_limiting, Unset):
            internal_authentication_backend_limiting = UNSET
        else:
            internal_authentication_backend_limiting = (
                DatabaseServicePropertiesOpensearchAuthFailureListenersInternalAuthenticationBackendLimiting.from_dict(
                    _internal_authentication_backend_limiting
                )
            )

        database_service_properties_opensearch_auth_failure_listeners = cls(
            internal_authentication_backend_limiting=internal_authentication_backend_limiting,
        )

        return database_service_properties_opensearch_auth_failure_listeners
