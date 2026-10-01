from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.storage_import_error_code import StorageImportErrorCode
from ..models.storage_import_source import StorageImportSource
from ..models.storage_import_state import StorageImportState
from ..types import UNSET, Unset

T = TypeVar("T", bound="StorageImport")


@_attrs_define
class StorageImport:
    """Details and progress of a storage import task.

    Example:
        {'client_content_length': 0, 'client_content_type': '', 'completed': '', 'created': '2020-06-26T08:51:07Z',
            'error_code': '', 'error_message': '', 'md5sum': '', 'read_bytes': 0, 'sha256sum': '', 'source': 'http_import',
            'source_location': 'https://example.com/disk.raw', 'state': 'pending', 'uuid':
            '07a6c9a3-300e-4d0e-b935-624f3dbdff3f', 'written_bytes': 0}

    Attributes:
        client_content_length (int): Content length reported by the import client, in bytes.
        client_content_type (str): Content type reported by the import client.
        completed (datetime.datetime | Literal['']): Completion time in RFC 3339 format, or an empty string while
            unfinished.
        created (datetime.datetime): Time when the import task was created.
        error_code (StorageImportErrorCode): Failure category, empty unless the task failed.
        error_message (str): Failure details, empty unless the task failed.
        md5sum (str): MD5 checksum of the imported data, available after completion.
        read_bytes (int): Number of bytes read from the source.
        sha256sum (str): SHA-256 checksum of the imported data, available after completion.
        source (StorageImportSource): Import mode.
        state (StorageImportState): Current import task state.
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        written_bytes (int): Number of bytes written to the storage resource.
        direct_upload_url (str | Unset): Temporary URL to which image data is uploaded in `direct_upload` mode.
        source_location (str | Unset): HTTP or HTTPS source URL for an `http_import` task.
    """

    client_content_length: int
    client_content_type: str
    completed: datetime.datetime | Literal[""]
    created: datetime.datetime
    error_code: StorageImportErrorCode
    error_message: str
    md5sum: str
    read_bytes: int
    sha256sum: str
    source: StorageImportSource
    state: StorageImportState
    uuid: UUID
    written_bytes: int
    direct_upload_url: str | Unset = UNSET
    source_location: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        client_content_length = self.client_content_length

        client_content_type = self.client_content_type

        completed: Literal[""] | str
        if isinstance(self.completed, datetime.datetime):
            completed = self.completed.isoformat()
        else:
            completed = self.completed

        created = self.created.isoformat()

        error_code = self.error_code.value

        error_message = self.error_message

        md5sum = self.md5sum

        read_bytes = self.read_bytes

        sha256sum = self.sha256sum

        source = self.source.value

        state = self.state.value

        uuid = str(self.uuid)

        written_bytes = self.written_bytes

        direct_upload_url = self.direct_upload_url

        source_location = self.source_location

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "client_content_length": client_content_length,
                "client_content_type": client_content_type,
                "completed": completed,
                "created": created,
                "error_code": error_code,
                "error_message": error_message,
                "md5sum": md5sum,
                "read_bytes": read_bytes,
                "sha256sum": sha256sum,
                "source": source,
                "state": state,
                "uuid": uuid,
                "written_bytes": written_bytes,
            }
        )
        if direct_upload_url is not UNSET:
            field_dict["direct_upload_url"] = direct_upload_url
        if source_location is not UNSET:
            field_dict["source_location"] = source_location

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        client_content_length = d.pop("client_content_length")

        client_content_type = d.pop("client_content_type")

        def _parse_completed(data: object) -> datetime.datetime | Literal[""]:
            completed_type_0 = cast(Literal[""], data)
            if completed_type_0 != "":
                raise ValueError(f"completed_type_0 must match const '', got '{completed_type_0}'")
            return completed_type_0
            if not isinstance(data, str):
                raise TypeError()
            completed_type_1 = datetime.datetime.fromisoformat(data)

            return completed_type_1

        completed = _parse_completed(d.pop("completed"))

        created = datetime.datetime.fromisoformat(d.pop("created"))

        error_code = StorageImportErrorCode(d.pop("error_code"))

        error_message = d.pop("error_message")

        md5sum = d.pop("md5sum")

        read_bytes = d.pop("read_bytes")

        sha256sum = d.pop("sha256sum")

        source = StorageImportSource(d.pop("source"))

        state = StorageImportState(d.pop("state"))

        uuid = UUID(d.pop("uuid"))

        written_bytes = d.pop("written_bytes")

        direct_upload_url = d.pop("direct_upload_url", UNSET)

        source_location = d.pop("source_location", UNSET)

        storage_import = cls(
            client_content_length=client_content_length,
            client_content_type=client_content_type,
            completed=completed,
            created=created,
            error_code=error_code,
            error_message=error_message,
            md5sum=md5sum,
            read_bytes=read_bytes,
            sha256sum=sha256sum,
            source=source,
            state=state,
            uuid=uuid,
            written_bytes=written_bytes,
            direct_upload_url=direct_upload_url,
            source_location=source_location,
        )

        return storage_import
