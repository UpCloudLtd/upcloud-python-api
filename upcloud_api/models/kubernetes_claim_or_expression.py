from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="KubernetesClaimOrExpression")


@_attrs_define
class KubernetesClaimOrExpression:
    """Maps a user attribute from either a JWT claim or a CEL expression. Claim and expression are mutually exclusive.

    Attributes:
        claim (str | Unset): JWT claim to use. Mutually exclusive with expression. Example: sub.
        expression (str | Unset): CEL expression producing the attribute value. Mutually exclusive with claim. Example:
            claims.sub.
    """

    claim: str | Unset = UNSET
    expression: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        claim = self.claim

        expression = self.expression

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if claim is not UNSET:
            field_dict["claim"] = claim
        if expression is not UNSET:
            field_dict["expression"] = expression

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        claim = d.pop("claim", UNSET)

        expression = d.pop("expression", UNSET)

        kubernetes_claim_or_expression = cls(
            claim=claim,
            expression=expression,
        )

        kubernetes_claim_or_expression.additional_properties = d
        return kubernetes_claim_or_expression

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
