from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.database_error_response import DatabaseErrorResponse
from ...models.database_pg_available_extensions_response_item import DatabasePGAvailableExtensionsResponseItem
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/database/pg/available-extensions",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DatabaseErrorResponse | list[DatabasePGAvailableExtensionsResponseItem]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemasdatabase_pg_available_extensions_response_item_data in _response_200:
            componentsschemasdatabase_pg_available_extensions_response_item = (
                DatabasePGAvailableExtensionsResponseItem.from_dict(
                    componentsschemasdatabase_pg_available_extensions_response_item_data
                )
            )

            response_200.append(componentsschemasdatabase_pg_available_extensions_response_item)

        return response_200

    response_default = DatabaseErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DatabaseErrorResponse | list[DatabasePGAvailableExtensionsResponseItem]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[DatabaseErrorResponse | list[DatabasePGAvailableExtensionsResponseItem]]:
    """Get available PostgreSQL extensions

     Returns a list of available PostgreSQL extensions grouped by PostgreSQL version.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatabaseErrorResponse | list[DatabasePGAvailableExtensionsResponseItem]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> DatabaseErrorResponse | list[DatabasePGAvailableExtensionsResponseItem] | None:
    """Get available PostgreSQL extensions

     Returns a list of available PostgreSQL extensions grouped by PostgreSQL version.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatabaseErrorResponse | list[DatabasePGAvailableExtensionsResponseItem]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[DatabaseErrorResponse | list[DatabasePGAvailableExtensionsResponseItem]]:
    """Get available PostgreSQL extensions

     Returns a list of available PostgreSQL extensions grouped by PostgreSQL version.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatabaseErrorResponse | list[DatabasePGAvailableExtensionsResponseItem]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> DatabaseErrorResponse | list[DatabasePGAvailableExtensionsResponseItem] | None:
    """Get available PostgreSQL extensions

     Returns a list of available PostgreSQL extensions grouped by PostgreSQL version.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatabaseErrorResponse | list[DatabasePGAvailableExtensionsResponseItem]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
