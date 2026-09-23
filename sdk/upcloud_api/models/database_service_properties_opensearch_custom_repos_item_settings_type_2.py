from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseServicePropertiesOpensearchCustomReposItemSettingsType2")


@_attrs_define
class DatabaseServicePropertiesOpensearchCustomReposItemSettingsType2:
    """
    Attributes:
        access_key (str):
        base_path (str): The path to the repository data within its container. The value of this setting should not
            start or end with a /
        bucket (str):
        region (str):
        secret_key (str): AWS secret key
        chunk_size (str | Unset): Big files can be broken down into chunks during snapshotting if needed. Should be the
            same as for the 3rd party repository
        compress (bool | Unset): when set to true metadata files are stored in compressed format
        endpoint (str | Unset): The S3 service endpoint to connect to. If you are using an S3-compatible service then
            you should set this to the service’s endpoint
        max_restore_bytes_per_sec (str | Unset): Throttles the restore rate per node. Defaults to unlimited. Note that
            if the recovery settings for managed services are set, this value is overridden by the recovery settings. Value
            should be a byte size with unit, e.g. 40mb, 100kb, 1gb Example: 40mb.
        max_snapshot_bytes_per_sec (str | Unset): Throttles the snapshot rate per node. Defaults to 40mb. Note that if
            the recovery settings for managed services are set, this value is overridden by the recovery settings. Value
            should be a byte size with unit, e.g. 40mb, 100kb, 1gb Example: 40mb.
        readonly (bool | Unset):  Default: False.
        server_side_encryption (bool | Unset): When set to true files are encrypted on server side
    """

    access_key: str
    base_path: str
    bucket: str
    region: str
    secret_key: str
    chunk_size: str | Unset = UNSET
    compress: bool | Unset = UNSET
    endpoint: str | Unset = UNSET
    max_restore_bytes_per_sec: str | Unset = UNSET
    max_snapshot_bytes_per_sec: str | Unset = UNSET
    readonly: bool | Unset = False
    server_side_encryption: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        access_key = self.access_key

        base_path = self.base_path

        bucket = self.bucket

        region = self.region

        secret_key = self.secret_key

        chunk_size = self.chunk_size

        compress = self.compress

        endpoint = self.endpoint

        max_restore_bytes_per_sec = self.max_restore_bytes_per_sec

        max_snapshot_bytes_per_sec = self.max_snapshot_bytes_per_sec

        readonly = self.readonly

        server_side_encryption = self.server_side_encryption

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "access_key": access_key,
                "base_path": base_path,
                "bucket": bucket,
                "region": region,
                "secret_key": secret_key,
            }
        )
        if chunk_size is not UNSET:
            field_dict["chunk_size"] = chunk_size
        if compress is not UNSET:
            field_dict["compress"] = compress
        if endpoint is not UNSET:
            field_dict["endpoint"] = endpoint
        if max_restore_bytes_per_sec is not UNSET:
            field_dict["max_restore_bytes_per_sec"] = max_restore_bytes_per_sec
        if max_snapshot_bytes_per_sec is not UNSET:
            field_dict["max_snapshot_bytes_per_sec"] = max_snapshot_bytes_per_sec
        if readonly is not UNSET:
            field_dict["readonly"] = readonly
        if server_side_encryption is not UNSET:
            field_dict["server_side_encryption"] = server_side_encryption

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_key = d.pop("access_key")

        base_path = d.pop("base_path")

        bucket = d.pop("bucket")

        region = d.pop("region")

        secret_key = d.pop("secret_key")

        chunk_size = d.pop("chunk_size", UNSET)

        compress = d.pop("compress", UNSET)

        endpoint = d.pop("endpoint", UNSET)

        max_restore_bytes_per_sec = d.pop("max_restore_bytes_per_sec", UNSET)

        max_snapshot_bytes_per_sec = d.pop("max_snapshot_bytes_per_sec", UNSET)

        readonly = d.pop("readonly", UNSET)

        server_side_encryption = d.pop("server_side_encryption", UNSET)

        database_service_properties_opensearch_custom_repos_item_settings_type_2 = cls(
            access_key=access_key,
            base_path=base_path,
            bucket=bucket,
            region=region,
            secret_key=secret_key,
            chunk_size=chunk_size,
            compress=compress,
            endpoint=endpoint,
            max_restore_bytes_per_sec=max_restore_bytes_per_sec,
            max_snapshot_bytes_per_sec=max_snapshot_bytes_per_sec,
            readonly=readonly,
            server_side_encryption=server_side_encryption,
        )

        return database_service_properties_opensearch_custom_repos_item_settings_type_2
