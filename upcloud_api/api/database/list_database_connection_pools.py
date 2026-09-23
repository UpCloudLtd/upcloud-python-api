from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.database_connection_pool_response import DatabaseConnectionPoolResponse
from ...models.database_error_response import DatabaseErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    *,
    sort: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/database/{uuid}/connection-pools".format(
            uuid=quote(str(uuid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DatabaseErrorResponse | list[DatabaseConnectionPoolResponse]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemasdatabase_connection_pools_response_item_data in _response_200:
            componentsschemasdatabase_connection_pools_response_item = DatabaseConnectionPoolResponse.from_dict(
                componentsschemasdatabase_connection_pools_response_item_data
            )

            response_200.append(componentsschemasdatabase_connection_pools_response_item)

        return response_200

    response_default = DatabaseErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DatabaseErrorResponse | list[DatabaseConnectionPoolResponse]]:
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
    sort: str | Unset = UNSET,
) -> Response[DatabaseErrorResponse | list[DatabaseConnectionPoolResponse]]:
    """List connection pools

     Returns a list of available connection pools for a Managed Database service. Connection pools are
    available only for PostgreSQL database services.

    Args:
        uuid (UUID): The unique identifier for the integration.
        sort (str | Unset): Schema for a query parameter specifying the order.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatabaseErrorResponse | list[DatabaseConnectionPoolResponse]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        sort=sort,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    sort: str | Unset = UNSET,
) -> DatabaseErrorResponse | list[DatabaseConnectionPoolResponse] | None:
    """List connection pools

     Returns a list of available connection pools for a Managed Database service. Connection pools are
    available only for PostgreSQL database services.

    Args:
        uuid (UUID): The unique identifier for the integration.
        sort (str | Unset): Schema for a query parameter specifying the order.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatabaseErrorResponse | list[DatabaseConnectionPoolResponse]
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    sort: str | Unset = UNSET,
) -> Response[DatabaseErrorResponse | list[DatabaseConnectionPoolResponse]]:
    """List connection pools

     Returns a list of available connection pools for a Managed Database service. Connection pools are
    available only for PostgreSQL database services.

    Args:
        uuid (UUID): The unique identifier for the integration.
        sort (str | Unset): Schema for a query parameter specifying the order.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatabaseErrorResponse | list[DatabaseConnectionPoolResponse]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    sort: str | Unset = UNSET,
) -> DatabaseErrorResponse | list[DatabaseConnectionPoolResponse] | None:
    """List connection pools

     Returns a list of available connection pools for a Managed Database service. Connection pools are
    available only for PostgreSQL database services.

    Args:
        uuid (UUID): The unique identifier for the integration.
        sort (str | Unset): Schema for a query parameter specifying the order.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatabaseErrorResponse | list[DatabaseConnectionPoolResponse]
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            sort=sort,
        )
    ).parsed
