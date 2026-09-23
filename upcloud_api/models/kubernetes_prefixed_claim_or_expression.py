from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="KubernetesPrefixedClaimOrExpression")


@_attrs_define
class KubernetesPrefixedClaimOrExpression:
    """Maps a user attribute from either a JWT claim (optionally prefixed) or a CEL expression. Claim and expression are
    mutually exclusive.

        Attributes:
            claim (str | Unset): JWT claim to use. Mutually exclusive with expression. Example: email.
            prefix (None | str | Unset): Prefix prepended to the claim's value. Must be set (may be empty) when claim is
                set. Mutually exclusive with expression.
                 Example: oidc:.
            expression (str | Unset): CEL expression producing the attribute value. Mutually exclusive with claim and
                prefix. Example: claims.email.
    """

    claim: str | Unset = UNSET
    prefix: None | str | Unset = UNSET
    expression: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        claim = self.claim

        prefix: None | str | Unset
        if isinstance(self.prefix, Unset):
            prefix = UNSET
        else:
            prefix = self.prefix

        expression = self.expression

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if claim is not UNSET:
            field_dict["claim"] = claim
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if expression is not UNSET:
            field_dict["expression"] = expression

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        claim = d.pop("claim", UNSET)

        def _parse_prefix(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        prefix = _parse_prefix(d.pop("prefix", UNSET))

        expression = d.pop("expression", UNSET)

        kubernetes_prefixed_claim_or_expression = cls(
            claim=claim,
            prefix=prefix,
            expression=expression,
        )

        kubernetes_prefixed_claim_or_expression.additional_properties = d
        return kubernetes_prefixed_claim_or_expression

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
