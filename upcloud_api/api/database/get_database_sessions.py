from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.database_current_sessions_response import DatabaseCurrentSessionsResponse
from ...models.database_error_response import DatabaseErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    *,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    order: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params["order"] = order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/database/{uuid}/sessions".format(
            uuid=quote(str(uuid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DatabaseCurrentSessionsResponse | DatabaseErrorResponse:
    if response.status_code == 200:
        response_200 = DatabaseCurrentSessionsResponse.from_dict(response.json())

        return response_200

    response_default = DatabaseErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DatabaseCurrentSessionsResponse | DatabaseErrorResponse]:
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
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    order: str | Unset = UNSET,
) -> Response[DatabaseCurrentSessionsResponse | DatabaseErrorResponse]:
    """List sessions

     Returns a list of current sessions details for your Managed Database service by its {uuid} and
    optional query parameters {limit}, {offset} and {order}.

    Args:
        uuid (UUID): The unique identifier for the integration.
        limit (int | Unset): Schema for a query parameter specifying the maximum number of entries
            to return (limit).
        offset (int | Unset): Schema for a query parameter specifying the offset for pagination.
        order (str | Unset): Schema for a query parameter specifying the order.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatabaseCurrentSessionsResponse | DatabaseErrorResponse]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        limit=limit,
        offset=offset,
        order=order,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    order: str | Unset = UNSET,
) -> DatabaseCurrentSessionsResponse | DatabaseErrorResponse | None:
    """List sessions

     Returns a list of current sessions details for your Managed Database service by its {uuid} and
    optional query parameters {limit}, {offset} and {order}.

    Args:
        uuid (UUID): The unique identifier for the integration.
        limit (int | Unset): Schema for a query parameter specifying the maximum number of entries
            to return (limit).
        offset (int | Unset): Schema for a query parameter specifying the offset for pagination.
        order (str | Unset): Schema for a query parameter specifying the order.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatabaseCurrentSessionsResponse | DatabaseErrorResponse
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        limit=limit,
        offset=offset,
        order=order,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    order: str | Unset = UNSET,
) -> Response[DatabaseCurrentSessionsResponse | DatabaseErrorResponse]:
    """List sessions

     Returns a list of current sessions details for your Managed Database service by its {uuid} and
    optional query parameters {limit}, {offset} and {order}.

    Args:
        uuid (UUID): The unique identifier for the integration.
        limit (int | Unset): Schema for a query parameter specifying the maximum number of entries
            to return (limit).
        offset (int | Unset): Schema for a query parameter specifying the offset for pagination.
        order (str | Unset): Schema for a query parameter specifying the order.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatabaseCurrentSessionsResponse | DatabaseErrorResponse]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        limit=limit,
        offset=offset,
        order=order,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    order: str | Unset = UNSET,
) -> DatabaseCurrentSessionsResponse | DatabaseErrorResponse | None:
    """List sessions

     Returns a list of current sessions details for your Managed Database service by its {uuid} and
    optional query parameters {limit}, {offset} and {order}.

    Args:
        uuid (UUID): The unique identifier for the integration.
        limit (int | Unset): Schema for a query parameter specifying the maximum number of entries
            to return (limit).
        offset (int | Unset): Schema for a query parameter specifying the offset for pagination.
        order (str | Unset): Schema for a query parameter specifying the order.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatabaseCurrentSessionsResponse | DatabaseErrorResponse
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            limit=limit,
            offset=offset,
            order=order,
        )
    ).parsed
