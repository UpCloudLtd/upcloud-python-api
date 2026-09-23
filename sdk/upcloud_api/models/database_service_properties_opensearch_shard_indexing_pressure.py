from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_service_properties_opensearch_shard_indexing_pressure_operating_factor import (
        DatabaseServicePropertiesOpensearchShardIndexingPressureOperatingFactor,
    )
    from ..models.database_service_properties_opensearch_shard_indexing_pressure_primary_parameter import (
        DatabaseServicePropertiesOpensearchShardIndexingPressurePrimaryParameter,
    )


T = TypeVar("T", bound="DatabaseServicePropertiesOpensearchShardIndexingPressure")


@_attrs_define
class DatabaseServicePropertiesOpensearchShardIndexingPressure:
    """
    Attributes:
        enabled (bool | Unset): Enable or disable shard indexing backpressure. Default is false
        enforced (bool | Unset): Run shard indexing backpressure in shadow mode or enforced mode.
                        In shadow mode (value set as false), shard indexing backpressure tracks all granular-level metrics,
                        but it doesn’t actually reject any indexing requests.
                        In enforced mode (value set as true),
                        shard indexing backpressure rejects any requests to the cluster that might cause a dip in its
            performance.
                        Default is false
        operating_factor (DatabaseServicePropertiesOpensearchShardIndexingPressureOperatingFactor | Unset):
        primary_parameter (DatabaseServicePropertiesOpensearchShardIndexingPressurePrimaryParameter | Unset):
    """

    enabled: bool | Unset = UNSET
    enforced: bool | Unset = UNSET
    operating_factor: DatabaseServicePropertiesOpensearchShardIndexingPressureOperatingFactor | Unset = UNSET
    primary_parameter: DatabaseServicePropertiesOpensearchShardIndexingPressurePrimaryParameter | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        enforced = self.enforced

        operating_factor: dict[str, Any] | Unset = UNSET
        if not isinstance(self.operating_factor, Unset):
            operating_factor = self.operating_factor.to_dict()

        primary_parameter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.primary_parameter, Unset):
            primary_parameter = self.primary_parameter.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if enforced is not UNSET:
            field_dict["enforced"] = enforced
        if operating_factor is not UNSET:
            field_dict["operating_factor"] = operating_factor
        if primary_parameter is not UNSET:
            field_dict["primary_parameter"] = primary_parameter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_service_properties_opensearch_shard_indexing_pressure_operating_factor import (
            DatabaseServicePropertiesOpensearchShardIndexingPressureOperatingFactor,  # noqa: PLC0415
        )
        from ..models.database_service_properties_opensearch_shard_indexing_pressure_primary_parameter import (
            DatabaseServicePropertiesOpensearchShardIndexingPressurePrimaryParameter,  # noqa: PLC0415
        )

        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        enforced = d.pop("enforced", UNSET)

        _operating_factor = d.pop("operating_factor", UNSET)
        operating_factor: DatabaseServicePropertiesOpensearchShardIndexingPressureOperatingFactor | Unset
        if isinstance(_operating_factor, Unset):
            operating_factor = UNSET
        else:
            operating_factor = DatabaseServicePropertiesOpensearchShardIndexingPressureOperatingFactor.from_dict(
                _operating_factor
            )

        _primary_parameter = d.pop("primary_parameter", UNSET)
        primary_parameter: DatabaseServicePropertiesOpensearchShardIndexingPressurePrimaryParameter | Unset
        if isinstance(_primary_parameter, Unset):
            primary_parameter = UNSET
        else:
            primary_parameter = DatabaseServicePropertiesOpensearchShardIndexingPressurePrimaryParameter.from_dict(
                _primary_parameter
            )

        database_service_properties_opensearch_shard_indexing_pressure = cls(
            enabled=enabled,
            enforced=enforced,
            operating_factor=operating_factor,
            primary_parameter=primary_parameter,
        )

        return database_service_properties_opensearch_shard_indexing_pressure
