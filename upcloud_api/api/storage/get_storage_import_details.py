from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.storage_error import StorageError
from ...models.storage_import_response import StorageImportResponse
from ...types import Response


def _get_kwargs(
    uuid: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/storage/{uuid}/import".format(
            uuid=quote(str(uuid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> StorageError | StorageImportResponse:
    if response.status_code == 200:
        response_200 = StorageImportResponse.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = StorageError.from_dict(response.json())

        return response_404

    response_default = StorageError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[StorageError | StorageImportResponse]:
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
) -> Response[StorageError | StorageImportResponse]:
    """Get storage import details

     Returns details of the latest import task for a storage resource, including its state, transferred
    byte counts, checksums, and any error information.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StorageError | StorageImportResponse]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> StorageError | StorageImportResponse | None:
    """Get storage import details

     Returns details of the latest import task for a storage resource, including its state, transferred
    byte counts, checksums, and any error information.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StorageError | StorageImportResponse
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[StorageError | StorageImportResponse]:
    """Get storage import details

     Returns details of the latest import task for a storage resource, including its state, transferred
    byte counts, checksums, and any error information.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StorageError | StorageImportResponse]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> StorageError | StorageImportResponse | None:
    """Get storage import details

     Returns details of the latest import task for a storage resource, including its state, transferred
    byte counts, checksums, and any error information.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StorageError | StorageImportResponse
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
        )
    ).parsed
