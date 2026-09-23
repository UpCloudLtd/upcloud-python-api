from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.load_balancer_label_create import LoadBalancerLabelCreate


T = TypeVar("T", bound="LoadBalancerCertificateBundleDynamicModify")


@_attrs_define
class LoadBalancerCertificateBundleDynamicModify:
    """Load Balancer certificate bundle dynamic type

    Attributes:
        name (str | Unset): Name of the bundle
        hostnames (list[str] | Unset): Array of hostnames
        labels (list[LoadBalancerLabelCreate] | Unset): Labels
        challenge_key (str | Unset): Unique key used for ACME DNS challenge validation when obtaining certificates
            dynamically.
    """

    name: str | Unset = UNSET
    hostnames: list[str] | Unset = UNSET
    labels: list[LoadBalancerLabelCreate] | Unset = UNSET
    challenge_key: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        hostnames: list[str] | Unset = UNSET
        if not isinstance(self.hostnames, Unset):
            hostnames = self.hostnames

        labels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()
                labels.append(labels_item)

        challenge_key = self.challenge_key

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if hostnames is not UNSET:
            field_dict["hostnames"] = hostnames
        if labels is not UNSET:
            field_dict["labels"] = labels
        if challenge_key is not UNSET:
            field_dict["challenge_key"] = challenge_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.load_balancer_label_create import LoadBalancerLabelCreate  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        hostnames = cast(list[str], d.pop("hostnames", UNSET))

        _labels = d.pop("labels", UNSET)
        labels: list[LoadBalancerLabelCreate] | Unset = UNSET
        if _labels is not UNSET:
            labels = []
            for labels_item_data in _labels:
                labels_item = LoadBalancerLabelCreate.from_dict(labels_item_data)

                labels.append(labels_item)

        challenge_key = d.pop("challenge_key", UNSET)

        load_balancer_certificate_bundle_dynamic_modify = cls(
            name=name,
            hostnames=hostnames,
            labels=labels,
            challenge_key=challenge_key,
        )

        return load_balancer_certificate_bundle_dynamic_modify
