from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.database_error_response import DatabaseErrorResponse
from ...models.logical_database_create import LogicalDatabaseCreate
from ...models.logical_database_response import LogicalDatabaseResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    *,
    body: LogicalDatabaseCreate | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/1.3/database/{uuid}/databases".format(
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
) -> DatabaseErrorResponse | LogicalDatabaseResponse:
    if response.status_code == 201:
        response_201 = LogicalDatabaseResponse.from_dict(response.json())

        return response_201

    response_default = DatabaseErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DatabaseErrorResponse | LogicalDatabaseResponse]:
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
    body: LogicalDatabaseCreate | Unset = UNSET,
) -> Response[DatabaseErrorResponse | LogicalDatabaseResponse]:
    """Create logical database

     Creates a new logical database for the Managed Database service {uuid}.

    Args:
        uuid (UUID): The unique identifier for the integration.
        body (LogicalDatabaseCreate | Unset): Schema for creating a logical database.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatabaseErrorResponse | LogicalDatabaseResponse]
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
    body: LogicalDatabaseCreate | Unset = UNSET,
) -> DatabaseErrorResponse | LogicalDatabaseResponse | None:
    """Create logical database

     Creates a new logical database for the Managed Database service {uuid}.

    Args:
        uuid (UUID): The unique identifier for the integration.
        body (LogicalDatabaseCreate | Unset): Schema for creating a logical database.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatabaseErrorResponse | LogicalDatabaseResponse
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
    body: LogicalDatabaseCreate | Unset = UNSET,
) -> Response[DatabaseErrorResponse | LogicalDatabaseResponse]:
    """Create logical database

     Creates a new logical database for the Managed Database service {uuid}.

    Args:
        uuid (UUID): The unique identifier for the integration.
        body (LogicalDatabaseCreate | Unset): Schema for creating a logical database.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatabaseErrorResponse | LogicalDatabaseResponse]
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
    body: LogicalDatabaseCreate | Unset = UNSET,
) -> DatabaseErrorResponse | LogicalDatabaseResponse | None:
    """Create logical database

     Creates a new logical database for the Managed Database service {uuid}.

    Args:
        uuid (UUID): The unique identifier for the integration.
        body (LogicalDatabaseCreate | Unset): Schema for creating a logical database.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatabaseErrorResponse | LogicalDatabaseResponse
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed
