from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.kubernetes_authentication_issuer_config_audience_match_policy import (
    KubernetesAuthenticationIssuerConfigAudienceMatchPolicy,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.kubernetes_claim_mappings import KubernetesClaimMappings
    from ..models.kubernetes_claim_validation_rule import KubernetesClaimValidationRule
    from ..models.kubernetes_user_validation_rule import KubernetesUserValidationRule


T = TypeVar("T", bound="KubernetesAuthenticationIssuerConfig")


@_attrs_define
class KubernetesAuthenticationIssuerConfig:
    """
    Attributes:
        name (str): Name
        issuer_url (str):  Example: https://accounts.myoidcprovider.com.
        audiences (list[str]): Accepted audiences for tokens from this issuer. The first audience is used as the OIDC
            client id in generated kubeconfigs by default; the OIDC kubeconfig endpoint's `audience` query parameter can
            select a different one.
             Example: ['client-id-123'].
        discovery_url (str | Unset):  Example: https://accounts.myoidcprovider.com/.well-known/openid-configuration.
        audience_match_policy (KubernetesAuthenticationIssuerConfigAudienceMatchPolicy | Unset):  Default:
            KubernetesAuthenticationIssuerConfigAudienceMatchPolicy.VALUE_1.
        certificate_authority (str | Unset): Base64-encoded PEM certificate authority bundle.
        claim_mappings (KubernetesClaimMappings | Unset): Rules for mapping token claims to Kubernetes user attributes.
        claim_validation_rules (list[KubernetesClaimValidationRule] | Unset):
        user_validation_rules (list[KubernetesUserValidationRule] | Unset):
    """

    name: str
    issuer_url: str
    audiences: list[str]
    discovery_url: str | Unset = UNSET
    audience_match_policy: KubernetesAuthenticationIssuerConfigAudienceMatchPolicy | Unset = (
        KubernetesAuthenticationIssuerConfigAudienceMatchPolicy.VALUE_1
    )
    certificate_authority: str | Unset = UNSET
    claim_mappings: KubernetesClaimMappings | Unset = UNSET
    claim_validation_rules: list[KubernetesClaimValidationRule] | Unset = UNSET
    user_validation_rules: list[KubernetesUserValidationRule] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        issuer_url = self.issuer_url

        audiences = self.audiences

        discovery_url = self.discovery_url

        audience_match_policy: str | Unset = UNSET
        if not isinstance(self.audience_match_policy, Unset):
            audience_match_policy = self.audience_match_policy.value

        certificate_authority = self.certificate_authority

        claim_mappings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.claim_mappings, Unset):
            claim_mappings = self.claim_mappings.to_dict()

        claim_validation_rules: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.claim_validation_rules, Unset):
            claim_validation_rules = []
            for claim_validation_rules_item_data in self.claim_validation_rules:
                claim_validation_rules_item = claim_validation_rules_item_data.to_dict()
                claim_validation_rules.append(claim_validation_rules_item)

        user_validation_rules: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.user_validation_rules, Unset):
            user_validation_rules = []
            for user_validation_rules_item_data in self.user_validation_rules:
                user_validation_rules_item = user_validation_rules_item_data.to_dict()
                user_validation_rules.append(user_validation_rules_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "issuer_url": issuer_url,
                "audiences": audiences,
            }
        )
        if discovery_url is not UNSET:
            field_dict["discovery_url"] = discovery_url
        if audience_match_policy is not UNSET:
            field_dict["audience_match_policy"] = audience_match_policy
        if certificate_authority is not UNSET:
            field_dict["certificate_authority"] = certificate_authority
        if claim_mappings is not UNSET:
            field_dict["claim_mappings"] = claim_mappings
        if claim_validation_rules is not UNSET:
            field_dict["claim_validation_rules"] = claim_validation_rules
        if user_validation_rules is not UNSET:
            field_dict["user_validation_rules"] = user_validation_rules

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.kubernetes_claim_mappings import KubernetesClaimMappings  # noqa: PLC0415
        from ..models.kubernetes_claim_validation_rule import KubernetesClaimValidationRule  # noqa: PLC0415
        from ..models.kubernetes_user_validation_rule import KubernetesUserValidationRule  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        issuer_url = d.pop("issuer_url")

        audiences = cast(list[str], d.pop("audiences"))

        discovery_url = d.pop("discovery_url", UNSET)

        _audience_match_policy = d.pop("audience_match_policy", UNSET)
        audience_match_policy: KubernetesAuthenticationIssuerConfigAudienceMatchPolicy | Unset
        if isinstance(_audience_match_policy, Unset):
            audience_match_policy = UNSET
        else:
            audience_match_policy = KubernetesAuthenticationIssuerConfigAudienceMatchPolicy(_audience_match_policy)

        certificate_authority = d.pop("certificate_authority", UNSET)

        _claim_mappings = d.pop("claim_mappings", UNSET)
        claim_mappings: KubernetesClaimMappings | Unset
        if isinstance(_claim_mappings, Unset):
            claim_mappings = UNSET
        else:
            claim_mappings = KubernetesClaimMappings.from_dict(_claim_mappings)

        _claim_validation_rules = d.pop("claim_validation_rules", UNSET)
        claim_validation_rules: list[KubernetesClaimValidationRule] | Unset = UNSET
        if _claim_validation_rules is not UNSET:
            claim_validation_rules = []
            for claim_validation_rules_item_data in _claim_validation_rules:
                claim_validation_rules_item = KubernetesClaimValidationRule.from_dict(claim_validation_rules_item_data)

                claim_validation_rules.append(claim_validation_rules_item)

        _user_validation_rules = d.pop("user_validation_rules", UNSET)
        user_validation_rules: list[KubernetesUserValidationRule] | Unset = UNSET
        if _user_validation_rules is not UNSET:
            user_validation_rules = []
            for user_validation_rules_item_data in _user_validation_rules:
                user_validation_rules_item = KubernetesUserValidationRule.from_dict(user_validation_rules_item_data)

                user_validation_rules.append(user_validation_rules_item)

        kubernetes_authentication_issuer_config = cls(
            name=name,
            issuer_url=issuer_url,
            audiences=audiences,
            discovery_url=discovery_url,
            audience_match_policy=audience_match_policy,
            certificate_authority=certificate_authority,
            claim_mappings=claim_mappings,
            claim_validation_rules=claim_validation_rules,
            user_validation_rules=user_validation_rules,
        )

        kubernetes_authentication_issuer_config.additional_properties = d
        return kubernetes_authentication_issuer_config

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
