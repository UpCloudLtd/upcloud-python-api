from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.server_error import ServerError
from ...models.server_error_400 import ServerError400
from ...models.server_error_403 import ServerError403
from ...models.server_error_404 import ServerError404
from ...models.server_error_409 import ServerError409
from ...types import Response


def _get_kwargs(
    uuid: UUID,
    index: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/1.3/server/{uuid}/networking/interface/{index}".format(
            uuid=quote(str(uuid), safe=""),
            index=quote(str(index), safe=""),
        ),
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
    index: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409]:
    """Delete a network interface

     Delete a network interface from a stopped Cloud Server. IP addresses attached to the interface are
    released according to their release policies.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        index (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        index=index,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    index: int,
    *,
    client: AuthenticatedClient | Client,
) -> Any | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | None:
    """Delete a network interface

     Delete a network interface from a stopped Cloud Server. IP addresses attached to the interface are
    released according to their release policies.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        index (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409
    """

    return sync_detailed(
        uuid=uuid,
        index=index,
        client=client,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    index: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409]:
    """Delete a network interface

     Delete a network interface from a stopped Cloud Server. IP addresses attached to the interface are
    released according to their release policies.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        index (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        index=index,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    index: int,
    *,
    client: AuthenticatedClient | Client,
) -> Any | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | None:
    """Delete a network interface

     Delete a network interface from a stopped Cloud Server. IP addresses attached to the interface are
    released according to their release policies.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        index (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            index=index,
            client=client,
        )
    ).parsed
