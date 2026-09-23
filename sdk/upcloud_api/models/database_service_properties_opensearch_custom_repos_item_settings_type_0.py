from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseServicePropertiesOpensearchCustomReposItemSettingsType0")


@_attrs_define
class DatabaseServicePropertiesOpensearchCustomReposItemSettingsType0:
    """
    Attributes:
        account (str):
        base_path (str): The path to the repository data within its container. The value of this setting should not
            start or end with a /
        container (str): Azure container name
        chunk_size (str | Unset): Big files can be broken down into chunks during snapshotting if needed. Should be the
            same as for the 3rd party repository
        compress (bool | Unset): when set to true metadata files are stored in compressed format
        endpoint_suffix (str | Unset): Defines the DNS suffix for Azure Storage endpoints.
        key (str | Unset): Azure account secret key. One of key or sas_token should be specified
        max_restore_bytes_per_sec (str | Unset): Throttles the restore rate per node. Defaults to unlimited. Note that
            if the recovery settings for managed services are set, this value is overridden by the recovery settings. Value
            should be a byte size with unit, e.g. 40mb, 100kb, 1gb Example: 40mb.
        max_snapshot_bytes_per_sec (str | Unset): Throttles the snapshot rate per node. Defaults to 40mb. Note that if
            the recovery settings for managed services are set, this value is overridden by the recovery settings. Value
            should be a byte size with unit, e.g. 40mb, 100kb, 1gb Example: 40mb.
        readonly (bool | Unset):  Default: False.
        sas_token (str | Unset): A shared access signatures (SAS) token. One of key or sas_token should be specified
    """

    account: str
    base_path: str
    container: str
    chunk_size: str | Unset = UNSET
    compress: bool | Unset = UNSET
    endpoint_suffix: str | Unset = UNSET
    key: str | Unset = UNSET
    max_restore_bytes_per_sec: str | Unset = UNSET
    max_snapshot_bytes_per_sec: str | Unset = UNSET
    readonly: bool | Unset = False
    sas_token: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        account = self.account

        base_path = self.base_path

        container = self.container

        chunk_size = self.chunk_size

        compress = self.compress

        endpoint_suffix = self.endpoint_suffix

        key = self.key

        max_restore_bytes_per_sec = self.max_restore_bytes_per_sec

        max_snapshot_bytes_per_sec = self.max_snapshot_bytes_per_sec

        readonly = self.readonly

        sas_token = self.sas_token

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "account": account,
                "base_path": base_path,
                "container": container,
            }
        )
        if chunk_size is not UNSET:
            field_dict["chunk_size"] = chunk_size
        if compress is not UNSET:
            field_dict["compress"] = compress
        if endpoint_suffix is not UNSET:
            field_dict["endpoint_suffix"] = endpoint_suffix
        if key is not UNSET:
            field_dict["key"] = key
        if max_restore_bytes_per_sec is not UNSET:
            field_dict["max_restore_bytes_per_sec"] = max_restore_bytes_per_sec
        if max_snapshot_bytes_per_sec is not UNSET:
            field_dict["max_snapshot_bytes_per_sec"] = max_snapshot_bytes_per_sec
        if readonly is not UNSET:
            field_dict["readonly"] = readonly
        if sas_token is not UNSET:
            field_dict["sas_token"] = sas_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account = d.pop("account")

        base_path = d.pop("base_path")

        container = d.pop("container")

        chunk_size = d.pop("chunk_size", UNSET)

        compress = d.pop("compress", UNSET)

        endpoint_suffix = d.pop("endpoint_suffix", UNSET)

        key = d.pop("key", UNSET)

        max_restore_bytes_per_sec = d.pop("max_restore_bytes_per_sec", UNSET)

        max_snapshot_bytes_per_sec = d.pop("max_snapshot_bytes_per_sec", UNSET)

        readonly = d.pop("readonly", UNSET)

        sas_token = d.pop("sas_token", UNSET)

        database_service_properties_opensearch_custom_repos_item_settings_type_0 = cls(
            account=account,
            base_path=base_path,
            container=container,
            chunk_size=chunk_size,
            compress=compress,
            endpoint_suffix=endpoint_suffix,
            key=key,
            max_restore_bytes_per_sec=max_restore_bytes_per_sec,
            max_snapshot_bytes_per_sec=max_snapshot_bytes_per_sec,
            readonly=readonly,
            sas_token=sas_token,
        )

        return database_service_properties_opensearch_custom_repos_item_settings_type_0
