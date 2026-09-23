from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.server_cpu_stats import ServerCpuStats
from ...models.server_error import ServerError
from ...models.server_error_400 import ServerError400
from ...models.server_error_403 import ServerError403
from ...models.server_error_404 import ServerError404
from ...models.server_stats_period import ServerStatsPeriod
from ...types import Response


def _get_kwargs(
    uuid: UUID,
    period: ServerStatsPeriod,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/server/{uuid}/stats/cpu/{period}".format(
            uuid=quote(str(uuid), safe=""),
            period=quote(str(period), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ServerCpuStats | ServerError | ServerError400 | ServerError403 | ServerError404:
    if response.status_code == 200:
        response_200 = ServerCpuStats.from_dict(response.json())

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
) -> Response[ServerCpuStats | ServerError | ServerError400 | ServerError403 | ServerError404]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uuid: UUID,
    period: ServerStatsPeriod,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ServerCpuStats | ServerError | ServerError400 | ServerError403 | ServerError404]:
    """Get Cloud Server CPU statistics by period

     Returns CPU usage statistics for the selected period.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        period (ServerStatsPeriod): The period for which statistics are calculated. Example:
            weekly.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServerCpuStats | ServerError | ServerError400 | ServerError403 | ServerError404]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        period=period,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    period: ServerStatsPeriod,
    *,
    client: AuthenticatedClient | Client,
) -> ServerCpuStats | ServerError | ServerError400 | ServerError403 | ServerError404 | None:
    """Get Cloud Server CPU statistics by period

     Returns CPU usage statistics for the selected period.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        period (ServerStatsPeriod): The period for which statistics are calculated. Example:
            weekly.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServerCpuStats | ServerError | ServerError400 | ServerError403 | ServerError404
    """

    return sync_detailed(
        uuid=uuid,
        period=period,
        client=client,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    period: ServerStatsPeriod,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ServerCpuStats | ServerError | ServerError400 | ServerError403 | ServerError404]:
    """Get Cloud Server CPU statistics by period

     Returns CPU usage statistics for the selected period.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        period (ServerStatsPeriod): The period for which statistics are calculated. Example:
            weekly.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServerCpuStats | ServerError | ServerError400 | ServerError403 | ServerError404]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        period=period,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    period: ServerStatsPeriod,
    *,
    client: AuthenticatedClient | Client,
) -> ServerCpuStats | ServerError | ServerError400 | ServerError403 | ServerError404 | None:
    """Get Cloud Server CPU statistics by period

     Returns CPU usage statistics for the selected period.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        period (ServerStatsPeriod): The period for which statistics are calculated. Example:
            weekly.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServerCpuStats | ServerError | ServerError400 | ServerError403 | ServerError404
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            period=period,
            client=client,
        )
    ).parsed
