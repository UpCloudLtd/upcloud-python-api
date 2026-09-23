from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="KubernetesClaimValidationRule")


@_attrs_define
class KubernetesClaimValidationRule:
    """CEL expression used to validate a token claim.

    Attributes:
        claim (str | Unset):  Example: hd.
        required_value (str | Unset):  Example: upcloud.com.
        expression (str | Unset):  Example: claims.hd == 'upcloud.com'.
        message (str | Unset):  Example: User must belong to the upcloud.com organization domain..
    """

    claim: str | Unset = UNSET
    required_value: str | Unset = UNSET
    expression: str | Unset = UNSET
    message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        claim = self.claim

        required_value = self.required_value

        expression = self.expression

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if claim is not UNSET:
            field_dict["claim"] = claim
        if required_value is not UNSET:
            field_dict["required_value"] = required_value
        if expression is not UNSET:
            field_dict["expression"] = expression
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        claim = d.pop("claim", UNSET)

        required_value = d.pop("required_value", UNSET)

        expression = d.pop("expression", UNSET)

        message = d.pop("message", UNSET)

        kubernetes_claim_validation_rule = cls(
            claim=claim,
            required_value=required_value,
            expression=expression,
            message=message,
        )

        kubernetes_claim_validation_rule.additional_properties = d
        return kubernetes_claim_validation_rule

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
