from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.detach_storage_response import DetachStorageResponse
from ...models.storage_error import StorageError
from ...types import Response


def _get_kwargs(
    uuid: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/1.3/storage/{uuid}/detach".format(
            uuid=quote(str(uuid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DetachStorageResponse | StorageError:
    if response.status_code == 200:
        response_200 = DetachStorageResponse.from_dict(response.json())

        return response_200

    response_default = StorageError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DetachStorageResponse | StorageError]:
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
) -> Response[DetachStorageResponse | StorageError]:
    """Detach storage from a Cloud Server

     Detaches the storage resource from its attached Cloud Server. IDE and CD-ROM devices can be detached
    only while the Cloud Server is stopped; SCSI and VirtIO disks can also be detached while it is
    running. If the storage resource is already detached, it is returned unchanged.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DetachStorageResponse | StorageError]
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
) -> DetachStorageResponse | StorageError | None:
    """Detach storage from a Cloud Server

     Detaches the storage resource from its attached Cloud Server. IDE and CD-ROM devices can be detached
    only while the Cloud Server is stopped; SCSI and VirtIO disks can also be detached while it is
    running. If the storage resource is already detached, it is returned unchanged.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DetachStorageResponse | StorageError
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DetachStorageResponse | StorageError]:
    """Detach storage from a Cloud Server

     Detaches the storage resource from its attached Cloud Server. IDE and CD-ROM devices can be detached
    only while the Cloud Server is stopped; SCSI and VirtIO disks can also be detached while it is
    running. If the storage resource is already detached, it is returned unchanged.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DetachStorageResponse | StorageError]
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
) -> DetachStorageResponse | StorageError | None:
    """Detach storage from a Cloud Server

     Detaches the storage resource from its attached Cloud Server. IDE and CD-ROM devices can be detached
    only while the Cloud Server is stopped; SCSI and VirtIO disks can also be detached while it is
    running. If the storage resource is already detached, it is returned unchanged.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DetachStorageResponse | StorageError
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
        )
    ).parsed
