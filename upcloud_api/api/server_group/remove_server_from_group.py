from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.server_group_error import ServerGroupError
from ...types import Response


def _get_kwargs(
    uuid: UUID,
    server_uuid: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/1.3/server-group/{uuid}/servers/{server_uuid}".format(
            uuid=quote(str(uuid), safe=""),
            server_uuid=quote(str(server_uuid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ServerGroupError:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    response_default = ServerGroupError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ServerGroupError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uuid: UUID,
    server_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | ServerGroupError]:
    """Remove server from group

     Removes a server from a specific server group.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        server_uuid (UUID): Universally unique identifier Example:
            0414e0d7-4436-4037-9dd8-6eaf47dce599.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ServerGroupError]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        server_uuid=server_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    server_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Any | ServerGroupError | None:
    """Remove server from group

     Removes a server from a specific server group.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        server_uuid (UUID): Universally unique identifier Example:
            0414e0d7-4436-4037-9dd8-6eaf47dce599.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ServerGroupError
    """

    return sync_detailed(
        uuid=uuid,
        server_uuid=server_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    server_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | ServerGroupError]:
    """Remove server from group

     Removes a server from a specific server group.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        server_uuid (UUID): Universally unique identifier Example:
            0414e0d7-4436-4037-9dd8-6eaf47dce599.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ServerGroupError]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        server_uuid=server_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    server_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Any | ServerGroupError | None:
    """Remove server from group

     Removes a server from a specific server group.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        server_uuid (UUID): Universally unique identifier Example:
            0414e0d7-4436-4037-9dd8-6eaf47dce599.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ServerGroupError
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            server_uuid=server_uuid,
            client=client,
        )
    ).parsed
