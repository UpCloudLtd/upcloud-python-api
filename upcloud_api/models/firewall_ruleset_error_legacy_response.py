from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.firewall_ruleset_error_legacy_response_error import FirewallRulesetErrorLegacyResponseError


T = TypeVar("T", bound="FirewallRulesetErrorLegacyResponse")


@_attrs_define
class FirewallRulesetErrorLegacyResponse:
    """Schema for legacy error responses from API.

    Attributes:
        error (FirewallRulesetErrorLegacyResponseError): Schema for legacy error response.
    """

    error: FirewallRulesetErrorLegacyResponseError

    def to_dict(self) -> dict[str, Any]:
        error = self.error.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "error": error,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.firewall_ruleset_error_legacy_response_error import (
            FirewallRulesetErrorLegacyResponseError,  # noqa: PLC0415
        )

        d = dict(src_dict)
        error = FirewallRulesetErrorLegacyResponseError.from_dict(d.pop("error"))

        firewall_ruleset_error_legacy_response = cls(
            error=error,
        )

        return firewall_ruleset_error_legacy_response
