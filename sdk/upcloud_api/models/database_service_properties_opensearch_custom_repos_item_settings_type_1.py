from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_service_properties_opensearch_custom_repos_item_settings_type_1_google_service_account_credentials_map import (
        DatabaseServicePropertiesOpensearchCustomReposItemSettingsType1GoogleServiceAccountCredentialsMap,
    )


T = TypeVar("T", bound="DatabaseServicePropertiesOpensearchCustomReposItemSettingsType1")


@_attrs_define
class DatabaseServicePropertiesOpensearchCustomReposItemSettingsType1:
    """
    Attributes:
        base_path (str): The path to the repository data within its container. The value of this setting should not
            start or end with a /
        bucket (str): The path to the repository data within its container
        credentials (DatabaseServicePropertiesOpensearchCustomReposItemSettingsType1GoogleServiceAccountCredentialsMap):
        chunk_size (str | Unset): Big files can be broken down into chunks during snapshotting if needed. Should be the
            same as for the 3rd party repository
        compress (bool | Unset): when set to true metadata files are stored in compressed format
        max_restore_bytes_per_sec (str | Unset): Throttles the restore rate per node. Defaults to unlimited. Note that
            if the recovery settings for managed services are set, this value is overridden by the recovery settings. Value
            should be a byte size with unit, e.g. 40mb, 100kb, 1gb Example: 40mb.
        max_snapshot_bytes_per_sec (str | Unset): Throttles the snapshot rate per node. Defaults to 40mb. Note that if
            the recovery settings for managed services are set, this value is overridden by the recovery settings. Value
            should be a byte size with unit, e.g. 40mb, 100kb, 1gb Example: 40mb.
        readonly (bool | Unset):  Default: False.
    """

    base_path: str
    bucket: str
    credentials: DatabaseServicePropertiesOpensearchCustomReposItemSettingsType1GoogleServiceAccountCredentialsMap
    chunk_size: str | Unset = UNSET
    compress: bool | Unset = UNSET
    max_restore_bytes_per_sec: str | Unset = UNSET
    max_snapshot_bytes_per_sec: str | Unset = UNSET
    readonly: bool | Unset = False

    def to_dict(self) -> dict[str, Any]:
        base_path = self.base_path

        bucket = self.bucket

        credentials = self.credentials.to_dict()

        chunk_size = self.chunk_size

        compress = self.compress

        max_restore_bytes_per_sec = self.max_restore_bytes_per_sec

        max_snapshot_bytes_per_sec = self.max_snapshot_bytes_per_sec

        readonly = self.readonly

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "base_path": base_path,
                "bucket": bucket,
                "credentials": credentials,
            }
        )
        if chunk_size is not UNSET:
            field_dict["chunk_size"] = chunk_size
        if compress is not UNSET:
            field_dict["compress"] = compress
        if max_restore_bytes_per_sec is not UNSET:
            field_dict["max_restore_bytes_per_sec"] = max_restore_bytes_per_sec
        if max_snapshot_bytes_per_sec is not UNSET:
            field_dict["max_snapshot_bytes_per_sec"] = max_snapshot_bytes_per_sec
        if readonly is not UNSET:
            field_dict["readonly"] = readonly

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_service_properties_opensearch_custom_repos_item_settings_type_1_google_service_account_credentials_map import (
            DatabaseServicePropertiesOpensearchCustomReposItemSettingsType1GoogleServiceAccountCredentialsMap,  # noqa: PLC0415
        )

        d = dict(src_dict)
        base_path = d.pop("base_path")

        bucket = d.pop("bucket")

        credentials = (
            DatabaseServicePropertiesOpensearchCustomReposItemSettingsType1GoogleServiceAccountCredentialsMap.from_dict(
                d.pop("credentials")
            )
        )

        chunk_size = d.pop("chunk_size", UNSET)

        compress = d.pop("compress", UNSET)

        max_restore_bytes_per_sec = d.pop("max_restore_bytes_per_sec", UNSET)

        max_snapshot_bytes_per_sec = d.pop("max_snapshot_bytes_per_sec", UNSET)

        readonly = d.pop("readonly", UNSET)

        database_service_properties_opensearch_custom_repos_item_settings_type_1 = cls(
            base_path=base_path,
            bucket=bucket,
            credentials=credentials,
            chunk_size=chunk_size,
            compress=compress,
            max_restore_bytes_per_sec=max_restore_bytes_per_sec,
            max_snapshot_bytes_per_sec=max_snapshot_bytes_per_sec,
            readonly=readonly,
        )

        return database_service_properties_opensearch_custom_repos_item_settings_type_1
