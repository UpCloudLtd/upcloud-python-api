from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.attach_storage_request import AttachStorageRequest
from ...models.attach_storage_response import AttachStorageResponse
from ...models.storage_error import StorageError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    *,
    body: AttachStorageRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/1.3/storage/{uuid}/attach".format(
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
) -> AttachStorageResponse | StorageError:
    if response.status_code == 200:
        response_200 = AttachStorageResponse.from_dict(response.json())

        return response_200

    response_default = StorageError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AttachStorageResponse | StorageError]:
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
    body: AttachStorageRequest | Unset = UNSET,
) -> Response[AttachStorageResponse | StorageError]:
    """Attach storage to a Cloud Server

     Attaches the storage resource to a Cloud Server in the same zone. The device defaults to a disk at
    the next available address. IDE and CD-ROM devices can be attached only while the Cloud Server is
    stopped; SCSI and VirtIO disks can also be attached while it is running.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        body (AttachStorageRequest | Unset): Request schema for attaching this storage resource to
            a Cloud Server. Example: {'storage_device': {'server':
            '00798b85-efdc-41ca-8021-f6ef457b8531', 'type': 'disk'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AttachStorageResponse | StorageError]
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
    body: AttachStorageRequest | Unset = UNSET,
) -> AttachStorageResponse | StorageError | None:
    """Attach storage to a Cloud Server

     Attaches the storage resource to a Cloud Server in the same zone. The device defaults to a disk at
    the next available address. IDE and CD-ROM devices can be attached only while the Cloud Server is
    stopped; SCSI and VirtIO disks can also be attached while it is running.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        body (AttachStorageRequest | Unset): Request schema for attaching this storage resource to
            a Cloud Server. Example: {'storage_device': {'server':
            '00798b85-efdc-41ca-8021-f6ef457b8531', 'type': 'disk'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AttachStorageResponse | StorageError
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
    body: AttachStorageRequest | Unset = UNSET,
) -> Response[AttachStorageResponse | StorageError]:
    """Attach storage to a Cloud Server

     Attaches the storage resource to a Cloud Server in the same zone. The device defaults to a disk at
    the next available address. IDE and CD-ROM devices can be attached only while the Cloud Server is
    stopped; SCSI and VirtIO disks can also be attached while it is running.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        body (AttachStorageRequest | Unset): Request schema for attaching this storage resource to
            a Cloud Server. Example: {'storage_device': {'server':
            '00798b85-efdc-41ca-8021-f6ef457b8531', 'type': 'disk'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AttachStorageResponse | StorageError]
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
    body: AttachStorageRequest | Unset = UNSET,
) -> AttachStorageResponse | StorageError | None:
    """Attach storage to a Cloud Server

     Attaches the storage resource to a Cloud Server in the same zone. The device defaults to a disk at
    the next available address. IDE and CD-ROM devices can be attached only while the Cloud Server is
    stopped; SCSI and VirtIO disks can also be attached while it is running.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        body (AttachStorageRequest | Unset): Request schema for attaching this storage resource to
            a Cloud Server. Example: {'storage_device': {'server':
            '00798b85-efdc-41ca-8021-f6ef457b8531', 'type': 'disk'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AttachStorageResponse | StorageError
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed
