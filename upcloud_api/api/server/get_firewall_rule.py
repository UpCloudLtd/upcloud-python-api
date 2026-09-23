from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.server_error import ServerError
from ...models.server_error_400 import ServerError400
from ...models.server_error_403 import ServerError403
from ...models.server_error_404 import ServerError404
from ...models.server_firewall_rule import ServerFirewallRule
from ...types import Response


def _get_kwargs(
    uuid: UUID,
    position: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/server/{uuid}/firewall_rule/{position}".format(
            uuid=quote(str(uuid), safe=""),
            position=quote(str(position), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ServerError | ServerError400 | ServerError403 | ServerError404 | ServerFirewallRule:
    if response.status_code == 200:
        response_200 = ServerFirewallRule.from_dict(response.json())

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
) -> Response[ServerError | ServerError400 | ServerError403 | ServerError404 | ServerFirewallRule]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uuid: UUID,
    position: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ServerError | ServerError400 | ServerError403 | ServerError404 | ServerFirewallRule]:
    """Get a firewall rule

     Return the firewall rule at the specified one-based position in the Cloud Server rule chain.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        position (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServerError | ServerError400 | ServerError403 | ServerError404 | ServerFirewallRule]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        position=position,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    position: int,
    *,
    client: AuthenticatedClient | Client,
) -> ServerError | ServerError400 | ServerError403 | ServerError404 | ServerFirewallRule | None:
    """Get a firewall rule

     Return the firewall rule at the specified one-based position in the Cloud Server rule chain.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        position (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServerError | ServerError400 | ServerError403 | ServerError404 | ServerFirewallRule
    """

    return sync_detailed(
        uuid=uuid,
        position=position,
        client=client,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    position: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ServerError | ServerError400 | ServerError403 | ServerError404 | ServerFirewallRule]:
    """Get a firewall rule

     Return the firewall rule at the specified one-based position in the Cloud Server rule chain.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        position (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServerError | ServerError400 | ServerError403 | ServerError404 | ServerFirewallRule]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        position=position,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    position: int,
    *,
    client: AuthenticatedClient | Client,
) -> ServerError | ServerError400 | ServerError403 | ServerError404 | ServerFirewallRule | None:
    """Get a firewall rule

     Return the firewall rule at the specified one-based position in the Cloud Server rule chain.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        position (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServerError | ServerError400 | ServerError403 | ServerError404 | ServerFirewallRule
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            position=position,
            client=client,
        )
    ).parsed
