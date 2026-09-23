from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.server_error import ServerError
from ...models.server_error_400 import ServerError400
from ...models.server_error_403 import ServerError403
from ...models.server_error_404 import ServerError404
from ...models.server_network_stats import ServerNetworkStats
from ...models.server_stats_network_type import ServerStatsNetworkType
from ...types import Response


def _get_kwargs(
    uuid: UUID,
    type_: ServerStatsNetworkType,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/server/{uuid}/stats/network/{type_}".format(
            uuid=quote(str(uuid), safe=""),
            type_=quote(str(type_), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ServerError | ServerError400 | ServerError403 | ServerError404 | ServerNetworkStats:
    if response.status_code == 200:
        response_200 = ServerNetworkStats.from_dict(response.json())

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

    response_default = ServerError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ServerError | ServerError400 | ServerError403 | ServerError404 | ServerNetworkStats]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uuid: UUID,
    type_: ServerStatsNetworkType,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ServerError | ServerError400 | ServerError403 | ServerError404 | ServerNetworkStats]:
    """Get Cloud Server network statistics

     Returns aggregate inbound and outbound network statistics for all interfaces and periods.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        type_ (ServerStatsNetworkType): Unit used to measure network activity. Example: bytes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServerError | ServerError400 | ServerError403 | ServerError404 | ServerNetworkStats]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        type_=type_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    type_: ServerStatsNetworkType,
    *,
    client: AuthenticatedClient | Client,
) -> ServerError | ServerError400 | ServerError403 | ServerError404 | ServerNetworkStats | None:
    """Get Cloud Server network statistics

     Returns aggregate inbound and outbound network statistics for all interfaces and periods.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        type_ (ServerStatsNetworkType): Unit used to measure network activity. Example: bytes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServerError | ServerError400 | ServerError403 | ServerError404 | ServerNetworkStats
    """

    return sync_detailed(
        uuid=uuid,
        type_=type_,
        client=client,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    type_: ServerStatsNetworkType,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ServerError | ServerError400 | ServerError403 | ServerError404 | ServerNetworkStats]:
    """Get Cloud Server network statistics

     Returns aggregate inbound and outbound network statistics for all interfaces and periods.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        type_ (ServerStatsNetworkType): Unit used to measure network activity. Example: bytes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServerError | ServerError400 | ServerError403 | ServerError404 | ServerNetworkStats]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        type_=type_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    type_: ServerStatsNetworkType,
    *,
    client: AuthenticatedClient | Client,
) -> ServerError | ServerError400 | ServerError403 | ServerError404 | ServerNetworkStats | None:
    """Get Cloud Server network statistics

     Returns aggregate inbound and outbound network statistics for all interfaces and periods.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        type_ (ServerStatsNetworkType): Unit used to measure network activity. Example: bytes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServerError | ServerError400 | ServerError403 | ServerError404 | ServerNetworkStats
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            type_=type_,
            client=client,
        )
    ).parsed
