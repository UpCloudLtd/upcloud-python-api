from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.server import Server
from ...models.server_error import ServerError
from ...models.server_error_400 import ServerError400
from ...models.server_error_403 import ServerError403
from ...models.server_error_404 import ServerError404
from ...models.server_error_409 import ServerError409
from ...models.server_error_511 import ServerError511
from ...models.server_load_cdrom import ServerLoadCdrom
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    *,
    body: ServerLoadCdrom | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/1.3/server/{uuid}/cdrom/load".format(
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
) -> Server | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | ServerError511:
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

    if response.status_code == 511:
        response_511 = ServerError511.from_dict(response.json())

        return response_511

    response_default = ServerError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Server | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | ServerError511
]:
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
    body: ServerLoadCdrom | Unset = UNSET,
) -> Response[
    Server | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | ServerError511
]:
    """Load a CD-ROM image into a Cloud Server

     Load a storage of type normal or cdrom into the Cloud Server's attached CD-ROM device. If media is
    already loaded, it is ejected first.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        body (ServerLoadCdrom | Unset): Parameters for loading a storage into a Cloud Server's CD-
            ROM device. Example: {'storage_device': {'storage':
            '01000000-0000-4000-8000-000060010101'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Server | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | ServerError511]
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
    body: ServerLoadCdrom | Unset = UNSET,
) -> Server | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | ServerError511 | None:
    """Load a CD-ROM image into a Cloud Server

     Load a storage of type normal or cdrom into the Cloud Server's attached CD-ROM device. If media is
    already loaded, it is ejected first.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        body (ServerLoadCdrom | Unset): Parameters for loading a storage into a Cloud Server's CD-
            ROM device. Example: {'storage_device': {'storage':
            '01000000-0000-4000-8000-000060010101'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Server | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | ServerError511
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
    body: ServerLoadCdrom | Unset = UNSET,
) -> Response[
    Server | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | ServerError511
]:
    """Load a CD-ROM image into a Cloud Server

     Load a storage of type normal or cdrom into the Cloud Server's attached CD-ROM device. If media is
    already loaded, it is ejected first.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        body (ServerLoadCdrom | Unset): Parameters for loading a storage into a Cloud Server's CD-
            ROM device. Example: {'storage_device': {'storage':
            '01000000-0000-4000-8000-000060010101'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Server | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | ServerError511]
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
    body: ServerLoadCdrom | Unset = UNSET,
) -> Server | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | ServerError511 | None:
    """Load a CD-ROM image into a Cloud Server

     Load a storage of type normal or cdrom into the Cloud Server's attached CD-ROM device. If media is
    already loaded, it is ejected first.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        body (ServerLoadCdrom | Unset): Parameters for loading a storage into a Cloud Server's CD-
            ROM device. Example: {'storage_device': {'storage':
            '01000000-0000-4000-8000-000060010101'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Server | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | ServerError511
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed
