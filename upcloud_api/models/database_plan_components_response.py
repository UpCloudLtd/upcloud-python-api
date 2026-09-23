from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_plan_components_response_backups import DatabasePlanComponentsResponseBackups
    from ..models.database_plan_components_response_compute import DatabasePlanComponentsResponseCompute
    from ..models.database_plan_components_response_storage import DatabasePlanComponentsResponseStorage


T = TypeVar("T", bound="DatabasePlanComponentsResponse")


@_attrs_define
class DatabasePlanComponentsResponse:
    """Structured breakdown of a service plan into compute, storage and backups components. Sizes are expressed in GB to
    match plan naming; the classic MB/MiB fields on the plan object are unchanged.

        Attributes:
            compute (DatabasePlanComponentsResponseCompute | Unset): Compute resources per service
            storage (DatabasePlanComponentsResponseStorage | Unset): Storage included in the plan. Omitted for service types
                without persistent storage.
            backups (DatabasePlanComponentsResponseBackups | Unset): Backup characteristics of the plan
    """

    compute: DatabasePlanComponentsResponseCompute | Unset = UNSET
    storage: DatabasePlanComponentsResponseStorage | Unset = UNSET
    backups: DatabasePlanComponentsResponseBackups | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        compute: dict[str, Any] | Unset = UNSET
        if not isinstance(self.compute, Unset):
            compute = self.compute.to_dict()

        storage: dict[str, Any] | Unset = UNSET
        if not isinstance(self.storage, Unset):
            storage = self.storage.to_dict()

        backups: dict[str, Any] | Unset = UNSET
        if not isinstance(self.backups, Unset):
            backups = self.backups.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if compute is not UNSET:
            field_dict["compute"] = compute
        if storage is not UNSET:
            field_dict["storage"] = storage
        if backups is not UNSET:
            field_dict["backups"] = backups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_plan_components_response_backups import (
            DatabasePlanComponentsResponseBackups,  # noqa: PLC0415
        )
        from ..models.database_plan_components_response_compute import (
            DatabasePlanComponentsResponseCompute,  # noqa: PLC0415
        )
        from ..models.database_plan_components_response_storage import (
            DatabasePlanComponentsResponseStorage,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _compute = d.pop("compute", UNSET)
        compute: DatabasePlanComponentsResponseCompute | Unset
        if isinstance(_compute, Unset):
            compute = UNSET
        else:
            compute = DatabasePlanComponentsResponseCompute.from_dict(_compute)

        _storage = d.pop("storage", UNSET)
        storage: DatabasePlanComponentsResponseStorage | Unset
        if isinstance(_storage, Unset):
            storage = UNSET
        else:
            storage = DatabasePlanComponentsResponseStorage.from_dict(_storage)

        _backups = d.pop("backups", UNSET)
        backups: DatabasePlanComponentsResponseBackups | Unset
        if isinstance(_backups, Unset):
            backups = UNSET
        else:
            backups = DatabasePlanComponentsResponseBackups.from_dict(_backups)

        database_plan_components_response = cls(
            compute=compute,
            storage=storage,
            backups=backups,
        )

        database_plan_components_response.additional_properties = d
        return database_plan_components_response

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
