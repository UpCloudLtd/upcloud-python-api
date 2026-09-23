from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.create_server import CreateServer
from ...models.create_server_response import CreateServerResponse
from ...models.server_error import ServerError
from ...models.server_error_400 import ServerError400
from ...models.server_error_403 import ServerError403
from ...models.server_error_404 import ServerError404
from ...models.server_error_409 import ServerError409
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreateServer | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/1.3/server",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateServerResponse | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409:
    if response.status_code == 202:
        response_202 = CreateServerResponse.from_dict(response.json())

        return response_202

    if response.status_code == 400:
        response_400 = ServerError400.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = ServerError403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ServerError404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ServerError409.from_dict(response.json())

        return response_409

    response_default = ServerError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateServerResponse | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateServer | Unset = UNSET,
) -> Response[CreateServerResponse | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409]:
    """Create a new Cloud Server

     Creates a new Cloud Server

    Args:
        body (CreateServer | Unset): Cloud Server creation parameters Example: {'server':
            {'hostname': 'my-server.example.com', 'title': 'My Server', 'zone': 'fi-hel1',
            'storage_devices': {'storage_device': [{'action': 'clone', 'storage': '01234567-89ab-
            cdef-0123-456789abcdef', 'title': 'Operating System'}]}}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateServerResponse | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CreateServer | Unset = UNSET,
) -> CreateServerResponse | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | None:
    """Create a new Cloud Server

     Creates a new Cloud Server

    Args:
        body (CreateServer | Unset): Cloud Server creation parameters Example: {'server':
            {'hostname': 'my-server.example.com', 'title': 'My Server', 'zone': 'fi-hel1',
            'storage_devices': {'storage_device': [{'action': 'clone', 'storage': '01234567-89ab-
            cdef-0123-456789abcdef', 'title': 'Operating System'}]}}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateServerResponse | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateServer | Unset = UNSET,
) -> Response[CreateServerResponse | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409]:
    """Create a new Cloud Server

     Creates a new Cloud Server

    Args:
        body (CreateServer | Unset): Cloud Server creation parameters Example: {'server':
            {'hostname': 'my-server.example.com', 'title': 'My Server', 'zone': 'fi-hel1',
            'storage_devices': {'storage_device': [{'action': 'clone', 'storage': '01234567-89ab-
            cdef-0123-456789abcdef', 'title': 'Operating System'}]}}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateServerResponse | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateServer | Unset = UNSET,
) -> CreateServerResponse | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | None:
    """Create a new Cloud Server

     Creates a new Cloud Server

    Args:
        body (CreateServer | Unset): Cloud Server creation parameters Example: {'server':
            {'hostname': 'my-server.example.com', 'title': 'My Server', 'zone': 'fi-hel1',
            'storage_devices': {'storage_device': [{'action': 'clone', 'storage': '01234567-89ab-
            cdef-0123-456789abcdef', 'title': 'Operating System'}]}}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateServerResponse | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
