from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_server_backups import DeleteServerBackups
from ...models.server_error import ServerError
from ...models.server_error_400 import ServerError400
from ...models.server_error_403 import ServerError403
from ...models.server_error_404 import ServerError404
from ...models.server_error_409 import ServerError409
from ...models.server_legacy_boolean import ServerLegacyBoolean
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    *,
    storages: ServerLegacyBoolean | Unset = UNSET,
    backups: DeleteServerBackups | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_storages: str | Unset = UNSET
    if not isinstance(storages, Unset):
        json_storages = storages.value

    params["storages"] = json_storages

    json_backups: str | Unset = UNSET
    if not isinstance(backups, Unset):
        json_backups = backups.value

    params["backups"] = json_backups

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/1.3/server/{uuid}".format(
            uuid=quote(str(uuid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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
) -> Response[Any | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409]:
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
    storages: ServerLegacyBoolean | Unset = UNSET,
    backups: DeleteServerBackups | Unset = UNSET,
) -> Response[Any | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409]:
    """Delete a Cloud Server

     Deletes a stopped Cloud Server and releases its IP addresses. Deleting backups requires deleting the
    associated storage devices.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        storages (ServerLegacyBoolean | Unset): Boolean value accepted by the legacy API
        backups (DeleteServerBackups | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        storages=storages,
        backups=backups,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    storages: ServerLegacyBoolean | Unset = UNSET,
    backups: DeleteServerBackups | Unset = UNSET,
) -> Any | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | None:
    """Delete a Cloud Server

     Deletes a stopped Cloud Server and releases its IP addresses. Deleting backups requires deleting the
    associated storage devices.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        storages (ServerLegacyBoolean | Unset): Boolean value accepted by the legacy API
        backups (DeleteServerBackups | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        storages=storages,
        backups=backups,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    storages: ServerLegacyBoolean | Unset = UNSET,
    backups: DeleteServerBackups | Unset = UNSET,
) -> Response[Any | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409]:
    """Delete a Cloud Server

     Deletes a stopped Cloud Server and releases its IP addresses. Deleting backups requires deleting the
    associated storage devices.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        storages (ServerLegacyBoolean | Unset): Boolean value accepted by the legacy API
        backups (DeleteServerBackups | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        storages=storages,
        backups=backups,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    storages: ServerLegacyBoolean | Unset = UNSET,
    backups: DeleteServerBackups | Unset = UNSET,
) -> Any | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | None:
    """Delete a Cloud Server

     Deletes a stopped Cloud Server and releases its IP addresses. Deleting backups requires deleting the
    associated storage devices.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        storages (ServerLegacyBoolean | Unset): Boolean value accepted by the legacy API
        backups (DeleteServerBackups | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            storages=storages,
            backups=backups,
        )
    ).parsed
