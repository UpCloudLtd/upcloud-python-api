from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.load_balancer_label_create import LoadBalancerLabelCreate


T = TypeVar("T", bound="LoadBalancerCertificateBundleManualModify")


@_attrs_define
class LoadBalancerCertificateBundleManualModify:
    """Load Balancer certificate bundle manual type

    Attributes:
        name (str | Unset): Name of the bundle
        certificate (None | str | Unset): Certificate
        intermediates (None | str | Unset): Intermediate certificates
        private_key (None | str | Unset): Private key
        labels (list[LoadBalancerLabelCreate] | Unset): Labels
    """

    name: str | Unset = UNSET
    certificate: None | str | Unset = UNSET
    intermediates: None | str | Unset = UNSET
    private_key: None | str | Unset = UNSET
    labels: list[LoadBalancerLabelCreate] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        certificate: None | str | Unset
        if isinstance(self.certificate, Unset):
            certificate = UNSET
        else:
            certificate = self.certificate

        intermediates: None | str | Unset
        if isinstance(self.intermediates, Unset):
            intermediates = UNSET
        else:
            intermediates = self.intermediates

        private_key: None | str | Unset
        if isinstance(self.private_key, Unset):
            private_key = UNSET
        else:
            private_key = self.private_key

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
        if intermediates is not UNSET:
            field_dict["intermediates"] = intermediates
        if private_key is not UNSET:
            field_dict["private_key"] = private_key
        if labels is not UNSET:
            field_dict["labels"] = labels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.load_balancer_label_create import LoadBalancerLabelCreate  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_certificate(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        certificate = _parse_certificate(d.pop("certificate", UNSET))

        def _parse_intermediates(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        intermediates = _parse_intermediates(d.pop("intermediates", UNSET))

        def _parse_private_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        private_key = _parse_private_key(d.pop("private_key", UNSET))

        _labels = d.pop("labels", UNSET)
        labels: list[LoadBalancerLabelCreate] | Unset = UNSET
        if _labels is not UNSET:
            labels = []
            for labels_item_data in _labels:
                labels_item = LoadBalancerLabelCreate.from_dict(labels_item_data)

                labels.append(labels_item)

        load_balancer_certificate_bundle_manual_modify = cls(
            name=name,
            certificate=certificate,
            intermediates=intermediates,
            private_key=private_key,
            labels=labels,
        )

        return load_balancer_certificate_bundle_manual_modify
