from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.events import Events
from ...models.events_error import EventsError
from ...types import Response


def _get_kwargs(
    server_uuid: UUID,
    offset: int,
    count: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/events/{server_uuid}/{offset},{count}".format(
            server_uuid=quote(str(server_uuid), safe=""),
            offset=quote(str(offset), safe=""),
            count=quote(str(count), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Events | EventsError:
    if response.status_code == 200:
        response_200 = Events.from_dict(response.json())

        return response_200

    response_default = EventsError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Events | EventsError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    server_uuid: UUID,
    offset: int,
    count: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Events | EventsError]:
    """List events

     Retrieves a list of events.

    Args:
        server_uuid (UUID):
        offset (int):
        count (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Events | EventsError]
    """

    kwargs = _get_kwargs(
        server_uuid=server_uuid,
        offset=offset,
        count=count,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    server_uuid: UUID,
    offset: int,
    count: int,
    *,
    client: AuthenticatedClient | Client,
) -> Events | EventsError | None:
    """List events

     Retrieves a list of events.

    Args:
        server_uuid (UUID):
        offset (int):
        count (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Events | EventsError
    """

    return sync_detailed(
        server_uuid=server_uuid,
        offset=offset,
        count=count,
        client=client,
    ).parsed


async def asyncio_detailed(
    server_uuid: UUID,
    offset: int,
    count: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Events | EventsError]:
    """List events

     Retrieves a list of events.

    Args:
        server_uuid (UUID):
        offset (int):
        count (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Events | EventsError]
    """

    kwargs = _get_kwargs(
        server_uuid=server_uuid,
        offset=offset,
        count=count,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    server_uuid: UUID,
    offset: int,
    count: int,
    *,
    client: AuthenticatedClient | Client,
) -> Events | EventsError | None:
    """List events

     Retrieves a list of events.

    Args:
        server_uuid (UUID):
        offset (int):
        count (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Events | EventsError
    """

    return (
        await asyncio_detailed(
            server_uuid=server_uuid,
            offset=offset,
            count=count,
            client=client,
        )
    ).parsed
