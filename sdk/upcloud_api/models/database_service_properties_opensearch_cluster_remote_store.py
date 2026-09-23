from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseServicePropertiesOpensearchClusterRemoteStore")


@_attrs_define
class DatabaseServicePropertiesOpensearchClusterRemoteStore:
    """
    Attributes:
        state_global_metadata_upload_timeout (str | Unset): The amount of time to wait for the cluster state upload to
            complete. Defaults to 20s.
        state_metadata_manifest_upload_timeout (str | Unset): The amount of time to wait for the manifest file upload to
            complete. The manifest file contains the details of each of the files uploaded for a single cluster state, both
            index metadata files and global metadata files. Defaults to 20s.
        translog_buffer_interval (str | Unset): The default value of the translog buffer interval used when performing
            periodic translog updates. This setting is only effective when the index setting
            `index.remote_store.translog.buffer_interval` is not present. Defaults to 650ms.
        translog_max_readers (int | Unset): Sets the maximum number of open translog files for remote-backed indexes.
            This limits the total number of translog files per shard. After reaching this limit, the remote store flushes
            the translog files. Default is 1000. The minimum required is 100.
    """

    state_global_metadata_upload_timeout: str | Unset = UNSET
    state_metadata_manifest_upload_timeout: str | Unset = UNSET
    translog_buffer_interval: str | Unset = UNSET
    translog_max_readers: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        state_global_metadata_upload_timeout = self.state_global_metadata_upload_timeout

        state_metadata_manifest_upload_timeout = self.state_metadata_manifest_upload_timeout

        translog_buffer_interval = self.translog_buffer_interval

        translog_max_readers = self.translog_max_readers

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if state_global_metadata_upload_timeout is not UNSET:
            field_dict["state.global_metadata.upload_timeout"] = state_global_metadata_upload_timeout
        if state_metadata_manifest_upload_timeout is not UNSET:
            field_dict["state.metadata_manifest.upload_timeout"] = state_metadata_manifest_upload_timeout
        if translog_buffer_interval is not UNSET:
            field_dict["translog.buffer_interval"] = translog_buffer_interval
        if translog_max_readers is not UNSET:
            field_dict["translog.max_readers"] = translog_max_readers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        state_global_metadata_upload_timeout = d.pop("state.global_metadata.upload_timeout", UNSET)

        state_metadata_manifest_upload_timeout = d.pop("state.metadata_manifest.upload_timeout", UNSET)

        translog_buffer_interval = d.pop("translog.buffer_interval", UNSET)

        translog_max_readers = d.pop("translog.max_readers", UNSET)

        database_service_properties_opensearch_cluster_remote_store = cls(
            state_global_metadata_upload_timeout=state_global_metadata_upload_timeout,
            state_metadata_manifest_upload_timeout=state_metadata_manifest_upload_timeout,
            translog_buffer_interval=translog_buffer_interval,
            translog_max_readers=translog_max_readers,
        )

        return database_service_properties_opensearch_cluster_remote_store
