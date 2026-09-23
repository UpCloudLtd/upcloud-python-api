from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.server import Server
from ...models.server_attach_storage import ServerAttachStorage
from ...models.server_error import ServerError
from ...models.server_error_400 import ServerError400
from ...models.server_error_403 import ServerError403
from ...models.server_error_404 import ServerError404
from ...models.server_error_409 import ServerError409
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    *,
    body: ServerAttachStorage | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/1.3/server/{uuid}/storage/attach".format(
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
) -> Server | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409:
    if response.status_code == 200:
        response_200 = Server.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ServerError400.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = ServerError403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ServerError404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ServerError409.from_dict(response.json())

        return response_409

    response_default = ServerError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Server | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409]:
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
    body: ServerAttachStorage | Unset = UNSET,
) -> Response[Server | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409]:
    """Attach a storage device to a Cloud Server

     Attach a storage resource as a disk or CD-ROM device to a Cloud Server. SCSI and virtio disks can be
    attached while the Cloud Server is started; IDE and CD-ROM devices require a stopped Cloud Server.
    An empty CD-ROM device can be attached without specifying a storage resource.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        body (ServerAttachStorage | Unset): Parameters for attaching a storage device to a Cloud
            Server. Example: {'storage_device': {'address': 'virtio:0', 'boot_disk': 1, 'storage':
            '012580a1-32a1-466e-a323-689ca16f2d43', 'type': 'disk'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Server | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409]
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
    body: ServerAttachStorage | Unset = UNSET,
) -> Server | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | None:
    """Attach a storage device to a Cloud Server

     Attach a storage resource as a disk or CD-ROM device to a Cloud Server. SCSI and virtio disks can be
    attached while the Cloud Server is started; IDE and CD-ROM devices require a stopped Cloud Server.
    An empty CD-ROM device can be attached without specifying a storage resource.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        body (ServerAttachStorage | Unset): Parameters for attaching a storage device to a Cloud
            Server. Example: {'storage_device': {'address': 'virtio:0', 'boot_disk': 1, 'storage':
            '012580a1-32a1-466e-a323-689ca16f2d43', 'type': 'disk'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Server | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409
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
    body: ServerAttachStorage | Unset = UNSET,
) -> Response[Server | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409]:
    """Attach a storage device to a Cloud Server

     Attach a storage resource as a disk or CD-ROM device to a Cloud Server. SCSI and virtio disks can be
    attached while the Cloud Server is started; IDE and CD-ROM devices require a stopped Cloud Server.
    An empty CD-ROM device can be attached without specifying a storage resource.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        body (ServerAttachStorage | Unset): Parameters for attaching a storage device to a Cloud
            Server. Example: {'storage_device': {'address': 'virtio:0', 'boot_disk': 1, 'storage':
            '012580a1-32a1-466e-a323-689ca16f2d43', 'type': 'disk'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Server | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409]
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
    body: ServerAttachStorage | Unset = UNSET,
) -> Server | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | None:
    """Attach a storage device to a Cloud Server

     Attach a storage resource as a disk or CD-ROM device to a Cloud Server. SCSI and virtio disks can be
    attached while the Cloud Server is started; IDE and CD-ROM devices require a stopped Cloud Server.
    An empty CD-ROM device can be attached without specifying a storage resource.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        body (ServerAttachStorage | Unset): Parameters for attaching a storage device to a Cloud
            Server. Example: {'storage_device': {'address': 'virtio:0', 'boot_disk': 1, 'storage':
            '012580a1-32a1-466e-a323-689ca16f2d43', 'type': 'disk'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Server | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed
