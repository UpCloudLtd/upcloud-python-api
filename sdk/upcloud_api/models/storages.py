from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.storages_storages import StoragesStorages


T = TypeVar("T", bound="Storages")


@_attrs_define
class Storages:
    """A list of storage resources accessible to the account.

    Example:
        {'storages': {'storage': [{'access': 'private', 'encrypted': 'no', 'created': '2025-02-27T05:50:50Z', 'labels':
            [{'key': 'environment', 'value': 'production'}], 'license': 0, 'size': 50, 'state': 'online', 'tier': 'maxiops',
            'title': 'Production database', 'type': 'normal', 'uuid': '01f3286c-a5ea-4670-8121-d0b9767d625b', 'zone': 'fi-
            hel1'}]}}

    Attributes:
        storages (StoragesStorages):
    """

    storages: StoragesStorages

    def to_dict(self) -> dict[str, Any]:
        storages = self.storages.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "storages": storages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.storages_storages import StoragesStorages  # noqa: PLC0415

        d = dict(src_dict)
        storages = StoragesStorages.from_dict(d.pop("storages"))

        storages = cls(
            storages=storages,
        )

        return storages
