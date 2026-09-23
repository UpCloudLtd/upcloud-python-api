from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.create_storage_backup_request import CreateStorageBackupRequest
from ...models.create_storage_backup_response import CreateStorageBackupResponse
from ...models.storage_error import StorageError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    *,
    body: CreateStorageBackupRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/1.3/storage/{uuid}/backup".format(
            uuid=quote(str(uuid), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateStorageBackupResponse | StorageError:
    if response.status_code == 201:
        response_201 = CreateStorageBackupResponse.from_dict(response.json())

        return response_201

    response_default = StorageError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateStorageBackupResponse | StorageError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CreateStorageBackupRequest | Unset = UNSET,
) -> Response[CreateStorageBackupResponse | StorageError]:
    """Create on-demand backup

     Creates a point-in-time backup of private normal block storage. The operation is asynchronous: the
    source block storage is `backuping` while the backup is created, and the returned backup remains in
    `maintenance` until it is ready.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        body (CreateStorageBackupRequest | Unset): Request schema for creating an on-demand block
            storage backup. Example: {'storage': {'title': 'Manually created backup'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateStorageBackupResponse | StorageError]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CreateStorageBackupRequest | Unset = UNSET,
) -> CreateStorageBackupResponse | StorageError | None:
    """Create on-demand backup

     Creates a point-in-time backup of private normal block storage. The operation is asynchronous: the
    source block storage is `backuping` while the backup is created, and the returned backup remains in
    `maintenance` until it is ready.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        body (CreateStorageBackupRequest | Unset): Request schema for creating an on-demand block
            storage backup. Example: {'storage': {'title': 'Manually created backup'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateStorageBackupResponse | StorageError
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CreateStorageBackupRequest | Unset = UNSET,
) -> Response[CreateStorageBackupResponse | StorageError]:
    """Create on-demand backup

     Creates a point-in-time backup of private normal block storage. The operation is asynchronous: the
    source block storage is `backuping` while the backup is created, and the returned backup remains in
    `maintenance` until it is ready.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        body (CreateStorageBackupRequest | Unset): Request schema for creating an on-demand block
            storage backup. Example: {'storage': {'title': 'Manually created backup'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateStorageBackupResponse | StorageError]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CreateStorageBackupRequest | Unset = UNSET,
) -> CreateStorageBackupResponse | StorageError | None:
    """Create on-demand backup

     Creates a point-in-time backup of private normal block storage. The operation is asynchronous: the
    source block storage is `backuping` while the backup is created, and the returned backup remains in
    `maintenance` until it is ready.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        body (CreateStorageBackupRequest | Unset): Request schema for creating an on-demand block
            storage backup. Example: {'storage': {'title': 'Manually created backup'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateStorageBackupResponse | StorageError
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed
