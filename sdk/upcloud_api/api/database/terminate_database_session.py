from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.database_error_response import DatabaseErrorResponse
from ...models.database_terminate_session_response import DatabaseTerminateSessionResponse
from ...types import Response


def _get_kwargs(
    uuid: UUID,
    pid: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/1.3/database/{uuid}/sessions/{pid}".format(
            uuid=quote(str(uuid), safe=""),
            pid=quote(str(pid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DatabaseErrorResponse | DatabaseTerminateSessionResponse:
    if response.status_code == 204:
        response_204 = DatabaseTerminateSessionResponse.from_dict(response.json())

        return response_204

    response_default = DatabaseErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DatabaseErrorResponse | DatabaseTerminateSessionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uuid: UUID,
    pid: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DatabaseErrorResponse | DatabaseTerminateSessionResponse]:
    """Terminate session

     Terminates a sessions or kills a running query for a Managed Database service by its {uuid}, session
    {pid} and optional query parameter {terminate}.

    Args:
        uuid (UUID): The unique identifier for the integration.
        pid (int): The unique identifier for the integration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatabaseErrorResponse | DatabaseTerminateSessionResponse]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        pid=pid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    pid: int,
    *,
    client: AuthenticatedClient | Client,
) -> DatabaseErrorResponse | DatabaseTerminateSessionResponse | None:
    """Terminate session

     Terminates a sessions or kills a running query for a Managed Database service by its {uuid}, session
    {pid} and optional query parameter {terminate}.

    Args:
        uuid (UUID): The unique identifier for the integration.
        pid (int): The unique identifier for the integration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatabaseErrorResponse | DatabaseTerminateSessionResponse
    """

    return sync_detailed(
        uuid=uuid,
        pid=pid,
        client=client,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    pid: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DatabaseErrorResponse | DatabaseTerminateSessionResponse]:
    """Terminate session

     Terminates a sessions or kills a running query for a Managed Database service by its {uuid}, session
    {pid} and optional query parameter {terminate}.

    Args:
        uuid (UUID): The unique identifier for the integration.
        pid (int): The unique identifier for the integration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatabaseErrorResponse | DatabaseTerminateSessionResponse]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        pid=pid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    pid: int,
    *,
    client: AuthenticatedClient | Client,
) -> DatabaseErrorResponse | DatabaseTerminateSessionResponse | None:
    """Terminate session

     Terminates a sessions or kills a running query for a Managed Database service by its {uuid}, session
    {pid} and optional query parameter {terminate}.

    Args:
        uuid (UUID): The unique identifier for the integration.
        pid (int): The unique identifier for the integration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatabaseErrorResponse | DatabaseTerminateSessionResponse
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            pid=pid,
            client=client,
        )
    ).parsed
