from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.load_balancer_label_create import LoadBalancerLabelCreate


T = TypeVar("T", bound="LoadBalancerCertificateBundleAuthorityModify")


@_attrs_define
class LoadBalancerCertificateBundleAuthorityModify:
    """Load Balancer certificate bundle dynamic type

    Attributes:
        name (str | Unset): Name of the bundle
        certificate (str | Unset): Certificate
        labels (list[LoadBalancerLabelCreate] | Unset): Labels
    """

    name: str | Unset = UNSET
    certificate: str | Unset = UNSET
    labels: list[LoadBalancerLabelCreate] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        certificate = self.certificate

        labels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()
                labels.append(labels_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if certificate is not UNSET:
            field_dict["certificate"] = certificate
        if labels is not UNSET:
            field_dict["labels"] = labels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.load_balancer_label_create import LoadBalancerLabelCreate  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        certificate = d.pop("certificate", UNSET)

        _labels = d.pop("labels", UNSET)
        labels: list[LoadBalancerLabelCreate] | Unset = UNSET
        if _labels is not UNSET:
            labels = []
            for labels_item_data in _labels:
                labels_item = LoadBalancerLabelCreate.from_dict(labels_item_data)

                labels.append(labels_item)

        load_balancer_certificate_bundle_authority_modify = cls(
            name=name,
            certificate=certificate,
            labels=labels,
        )

        return load_balancer_certificate_bundle_authority_modify
