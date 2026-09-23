from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.database_connection_pool_modify import DatabaseConnectionPoolModify
from ...models.database_connection_pool_response import DatabaseConnectionPoolResponse
from ...models.database_error_response import DatabaseErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    pool_name: str,
    *,
    body: DatabaseConnectionPoolModify | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/1.3/database/{uuid}/connection-pools/{pool_name}".format(
            uuid=quote(str(uuid), safe=""),
            pool_name=quote(str(pool_name), safe=""),
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
    if response.status_code == 200:
        response_200 = DatabaseConnectionPoolResponse.from_dict(response.json())

        return response_200

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
    pool_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: DatabaseConnectionPoolModify | Unset = UNSET,
) -> Response[DatabaseConnectionPoolResponse | DatabaseErrorResponse]:
    """Modify connection pool

     Modifies the connection pool {pool-name} for the Managed Database service {uuid}.

    Args:
        uuid (UUID): The unique identifier for the integration.
        pool_name (str): The title of an entity.
        body (DatabaseConnectionPoolModify | Unset): Schema for modifying a connection pool.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatabaseConnectionPoolResponse | DatabaseErrorResponse]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        pool_name=pool_name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    pool_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: DatabaseConnectionPoolModify | Unset = UNSET,
) -> DatabaseConnectionPoolResponse | DatabaseErrorResponse | None:
    """Modify connection pool

     Modifies the connection pool {pool-name} for the Managed Database service {uuid}.

    Args:
        uuid (UUID): The unique identifier for the integration.
        pool_name (str): The title of an entity.
        body (DatabaseConnectionPoolModify | Unset): Schema for modifying a connection pool.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatabaseConnectionPoolResponse | DatabaseErrorResponse
    """

    return sync_detailed(
        uuid=uuid,
        pool_name=pool_name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    pool_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: DatabaseConnectionPoolModify | Unset = UNSET,
) -> Response[DatabaseConnectionPoolResponse | DatabaseErrorResponse]:
    """Modify connection pool

     Modifies the connection pool {pool-name} for the Managed Database service {uuid}.

    Args:
        uuid (UUID): The unique identifier for the integration.
        pool_name (str): The title of an entity.
        body (DatabaseConnectionPoolModify | Unset): Schema for modifying a connection pool.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatabaseConnectionPoolResponse | DatabaseErrorResponse]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        pool_name=pool_name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    pool_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: DatabaseConnectionPoolModify | Unset = UNSET,
) -> DatabaseConnectionPoolResponse | DatabaseErrorResponse | None:
    """Modify connection pool

     Modifies the connection pool {pool-name} for the Managed Database service {uuid}.

    Args:
        uuid (UUID): The unique identifier for the integration.
        pool_name (str): The title of an entity.
        body (DatabaseConnectionPoolModify | Unset): Schema for modifying a connection pool.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatabaseConnectionPoolResponse | DatabaseErrorResponse
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            pool_name=pool_name,
            client=client,
            body=body,
        )
    ).parsed
