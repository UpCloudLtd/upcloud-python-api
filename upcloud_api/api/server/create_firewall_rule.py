from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.server_create_firewall_rule import ServerCreateFirewallRule
from ...models.server_error import ServerError
from ...models.server_error_400 import ServerError400
from ...models.server_error_403 import ServerError403
from ...models.server_error_404 import ServerError404
from ...models.server_error_409 import ServerError409
from ...models.server_firewall_rule import ServerFirewallRule
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    *,
    body: ServerCreateFirewallRule | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/1.3/server/{uuid}/firewall_rule".format(
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
) -> ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | ServerFirewallRule:
    if response.status_code == 201:
        response_201 = ServerFirewallRule.from_dict(response.json())

        return response_201

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
) -> Response[ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | ServerFirewallRule]:
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
    body: ServerCreateFirewallRule | Unset = UNSET,
) -> Response[ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | ServerFirewallRule]:
    """Create a firewall rule

     Create a firewall rule. Rules are evaluated in position order; if position is omitted, the rule is
    appended. Changes can take 1-2 minutes to take effect.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        body (ServerCreateFirewallRule | Unset): Parameters for creating a firewall rule. Example:
            {'firewall_rule': {'action': 'accept', 'comment': 'Allow SSH from the office network',
            'destination_port_end': '22', 'destination_port_start': '22', 'direction': 'in', 'family':
            'IPv4', 'position': '1', 'protocol': 'tcp', 'source_address_end': '192.0.2.255',
            'source_address_start': '192.0.2.1'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | ServerFirewallRule]
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
    body: ServerCreateFirewallRule | Unset = UNSET,
) -> ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | ServerFirewallRule | None:
    """Create a firewall rule

     Create a firewall rule. Rules are evaluated in position order; if position is omitted, the rule is
    appended. Changes can take 1-2 minutes to take effect.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        body (ServerCreateFirewallRule | Unset): Parameters for creating a firewall rule. Example:
            {'firewall_rule': {'action': 'accept', 'comment': 'Allow SSH from the office network',
            'destination_port_end': '22', 'destination_port_start': '22', 'direction': 'in', 'family':
            'IPv4', 'position': '1', 'protocol': 'tcp', 'source_address_end': '192.0.2.255',
            'source_address_start': '192.0.2.1'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | ServerFirewallRule
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
    body: ServerCreateFirewallRule | Unset = UNSET,
) -> Response[ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | ServerFirewallRule]:
    """Create a firewall rule

     Create a firewall rule. Rules are evaluated in position order; if position is omitted, the rule is
    appended. Changes can take 1-2 minutes to take effect.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        body (ServerCreateFirewallRule | Unset): Parameters for creating a firewall rule. Example:
            {'firewall_rule': {'action': 'accept', 'comment': 'Allow SSH from the office network',
            'destination_port_end': '22', 'destination_port_start': '22', 'direction': 'in', 'family':
            'IPv4', 'position': '1', 'protocol': 'tcp', 'source_address_end': '192.0.2.255',
            'source_address_start': '192.0.2.1'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | ServerFirewallRule]
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
    body: ServerCreateFirewallRule | Unset = UNSET,
) -> ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | ServerFirewallRule | None:
    """Create a firewall rule

     Create a firewall rule. Rules are evaluated in position order; if position is omitted, the rule is
    appended. Changes can take 1-2 minutes to take effect.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        body (ServerCreateFirewallRule | Unset): Parameters for creating a firewall rule. Example:
            {'firewall_rule': {'action': 'accept', 'comment': 'Allow SSH from the office network',
            'destination_port_end': '22', 'destination_port_start': '22', 'direction': 'in', 'family':
            'IPv4', 'position': '1', 'protocol': 'tcp', 'source_address_end': '192.0.2.255',
            'source_address_start': '192.0.2.1'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | ServerFirewallRule
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed
