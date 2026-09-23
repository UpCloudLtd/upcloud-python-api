from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.database_plan_components_response_backups_name import DatabasePlanComponentsResponseBackupsName
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_plan_components_response_backups_frequent import (
        DatabasePlanComponentsResponseBackupsFrequent,
    )
    from ..models.database_plan_components_response_backups_infrequent import (
        DatabasePlanComponentsResponseBackupsInfrequent,
    )


T = TypeVar("T", bound="DatabasePlanComponentsResponseBackups")


@_attrs_define
class DatabasePlanComponentsResponseBackups:
    """Backup characteristics of the plan

    Attributes:
        name (DatabasePlanComponentsResponseBackupsName | Unset): Backup tier name for tiered plans. Omitted when the
            plan retention does not map to a named tier. Example: standard.
        retention_days (int | Unset): Backup retention in days Example: 15.
        frequent (DatabasePlanComponentsResponseBackupsFrequent | Unset): Frequent backup window, OpenSearch only
        infrequent (DatabasePlanComponentsResponseBackupsInfrequent | Unset): Infrequent backup window, OpenSearch only
    """

    name: DatabasePlanComponentsResponseBackupsName | Unset = UNSET
    retention_days: int | Unset = UNSET
    frequent: DatabasePlanComponentsResponseBackupsFrequent | Unset = UNSET
    infrequent: DatabasePlanComponentsResponseBackupsInfrequent | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: str | Unset = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.value

        retention_days = self.retention_days

        frequent: dict[str, Any] | Unset = UNSET
        if not isinstance(self.frequent, Unset):
            frequent = self.frequent.to_dict()

        infrequent: dict[str, Any] | Unset = UNSET
        if not isinstance(self.infrequent, Unset):
            infrequent = self.infrequent.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if retention_days is not UNSET:
            field_dict["retention_days"] = retention_days
        if frequent is not UNSET:
            field_dict["frequent"] = frequent
        if infrequent is not UNSET:
            field_dict["infrequent"] = infrequent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_plan_components_response_backups_frequent import (
            DatabasePlanComponentsResponseBackupsFrequent,  # noqa: PLC0415
        )
        from ..models.database_plan_components_response_backups_infrequent import (
            DatabasePlanComponentsResponseBackupsInfrequent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _name = d.pop("name", UNSET)
        name: DatabasePlanComponentsResponseBackupsName | Unset
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = DatabasePlanComponentsResponseBackupsName(_name)

        retention_days = d.pop("retention_days", UNSET)

        _frequent = d.pop("frequent", UNSET)
        frequent: DatabasePlanComponentsResponseBackupsFrequent | Unset
        if isinstance(_frequent, Unset):
            frequent = UNSET
        else:
            frequent = DatabasePlanComponentsResponseBackupsFrequent.from_dict(_frequent)

        _infrequent = d.pop("infrequent", UNSET)
        infrequent: DatabasePlanComponentsResponseBackupsInfrequent | Unset
        if isinstance(_infrequent, Unset):
            infrequent = UNSET
        else:
            infrequent = DatabasePlanComponentsResponseBackupsInfrequent.from_dict(_infrequent)

        database_plan_components_response_backups = cls(
            name=name,
            retention_days=retention_days,
            frequent=frequent,
            infrequent=infrequent,
        )

        database_plan_components_response_backups.additional_properties = d
        return database_plan_components_response_backups

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
