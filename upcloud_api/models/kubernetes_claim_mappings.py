from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.kubernetes_claim_or_expression import KubernetesClaimOrExpression
    from ..models.kubernetes_extra_mapping import KubernetesExtraMapping
    from ..models.kubernetes_prefixed_claim_or_expression import KubernetesPrefixedClaimOrExpression


T = TypeVar("T", bound="KubernetesClaimMappings")


@_attrs_define
class KubernetesClaimMappings:
    """Rules for mapping token claims to Kubernetes user attributes.

    Attributes:
        username (KubernetesPrefixedClaimOrExpression | Unset): Maps a user attribute from either a JWT claim
            (optionally prefixed) or a CEL expression. Claim and expression are mutually exclusive.
        groups (KubernetesPrefixedClaimOrExpression | Unset): Maps a user attribute from either a JWT claim (optionally
            prefixed) or a CEL expression. Claim and expression are mutually exclusive.
        uid (KubernetesClaimOrExpression | Unset): Maps a user attribute from either a JWT claim or a CEL expression.
            Claim and expression are mutually exclusive.
        extra (list[KubernetesExtraMapping] | Unset):
    """

    username: KubernetesPrefixedClaimOrExpression | Unset = UNSET
    groups: KubernetesPrefixedClaimOrExpression | Unset = UNSET
    uid: KubernetesClaimOrExpression | Unset = UNSET
    extra: list[KubernetesExtraMapping] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username: dict[str, Any] | Unset = UNSET
        if not isinstance(self.username, Unset):
            username = self.username.to_dict()

        groups: dict[str, Any] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups.to_dict()

        uid: dict[str, Any] | Unset = UNSET
        if not isinstance(self.uid, Unset):
            uid = self.uid.to_dict()

        extra: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.extra, Unset):
            extra = []
            for extra_item_data in self.extra:
                extra_item = extra_item_data.to_dict()
                extra.append(extra_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if username is not UNSET:
            field_dict["username"] = username
        if groups is not UNSET:
            field_dict["groups"] = groups
        if uid is not UNSET:
            field_dict["uid"] = uid
        if extra is not UNSET:
            field_dict["extra"] = extra

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.kubernetes_claim_or_expression import KubernetesClaimOrExpression  # noqa: PLC0415
        from ..models.kubernetes_extra_mapping import KubernetesExtraMapping  # noqa: PLC0415
        from ..models.kubernetes_prefixed_claim_or_expression import (
            KubernetesPrefixedClaimOrExpression,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _username = d.pop("username", UNSET)
        username: KubernetesPrefixedClaimOrExpression | Unset
        if isinstance(_username, Unset):
            username = UNSET
        else:
            username = KubernetesPrefixedClaimOrExpression.from_dict(_username)

        _groups = d.pop("groups", UNSET)
        groups: KubernetesPrefixedClaimOrExpression | Unset
        if isinstance(_groups, Unset):
            groups = UNSET
        else:
            groups = KubernetesPrefixedClaimOrExpression.from_dict(_groups)

        _uid = d.pop("uid", UNSET)
        uid: KubernetesClaimOrExpression | Unset
        if isinstance(_uid, Unset):
            uid = UNSET
        else:
            uid = KubernetesClaimOrExpression.from_dict(_uid)

        _extra = d.pop("extra", UNSET)
        extra: list[KubernetesExtraMapping] | Unset = UNSET
        if _extra is not UNSET:
            extra = []
            for extra_item_data in _extra:
                extra_item = KubernetesExtraMapping.from_dict(extra_item_data)

                extra.append(extra_item)

        kubernetes_claim_mappings = cls(
            username=username,
            groups=groups,
            uid=uid,
            extra=extra,
        )

        kubernetes_claim_mappings.additional_properties = d
        return kubernetes_claim_mappings

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
