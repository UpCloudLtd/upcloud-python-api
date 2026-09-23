from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.database_connection_pool_create import DatabaseConnectionPoolCreate
from ...models.database_connection_pool_response import DatabaseConnectionPoolResponse
from ...models.database_error_response import DatabaseErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    *,
    body: DatabaseConnectionPoolCreate | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/1.3/database/{uuid}/connection-pools".format(
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
) -> DatabaseConnectionPoolResponse | DatabaseErrorResponse:
    if response.status_code == 201:
        response_201 = DatabaseConnectionPoolResponse.from_dict(response.json())

        return response_201

    response_default = DatabaseErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DatabaseConnectionPoolResponse | DatabaseErrorResponse]:
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
    body: DatabaseConnectionPoolCreate | Unset = UNSET,
) -> Response[DatabaseConnectionPoolResponse | DatabaseErrorResponse]:
    """Create connection pool

     Creates a connection pool for the Managed Database service {uuid}. Connection pool endpoints are for
    PostgreSQL Managed Databases only.

    Args:
        uuid (UUID): The unique identifier for the integration.
        body (DatabaseConnectionPoolCreate | Unset): Schema for creating a connection pool.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatabaseConnectionPoolResponse | DatabaseErrorResponse]
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
    body: DatabaseConnectionPoolCreate | Unset = UNSET,
) -> DatabaseConnectionPoolResponse | DatabaseErrorResponse | None:
    """Create connection pool

     Creates a connection pool for the Managed Database service {uuid}. Connection pool endpoints are for
    PostgreSQL Managed Databases only.

    Args:
        uuid (UUID): The unique identifier for the integration.
        body (DatabaseConnectionPoolCreate | Unset): Schema for creating a connection pool.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatabaseConnectionPoolResponse | DatabaseErrorResponse
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
    body: DatabaseConnectionPoolCreate | Unset = UNSET,
) -> Response[DatabaseConnectionPoolResponse | DatabaseErrorResponse]:
    """Create connection pool

     Creates a connection pool for the Managed Database service {uuid}. Connection pool endpoints are for
    PostgreSQL Managed Databases only.

    Args:
        uuid (UUID): The unique identifier for the integration.
        body (DatabaseConnectionPoolCreate | Unset): Schema for creating a connection pool.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatabaseConnectionPoolResponse | DatabaseErrorResponse]
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
    body: DatabaseConnectionPoolCreate | Unset = UNSET,
) -> DatabaseConnectionPoolResponse | DatabaseErrorResponse | None:
    """Create connection pool

     Creates a connection pool for the Managed Database service {uuid}. Connection pool endpoints are for
    PostgreSQL Managed Databases only.

    Args:
        uuid (UUID): The unique identifier for the integration.
        body (DatabaseConnectionPoolCreate | Unset): Schema for creating a connection pool.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatabaseConnectionPoolResponse | DatabaseErrorResponse
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed
