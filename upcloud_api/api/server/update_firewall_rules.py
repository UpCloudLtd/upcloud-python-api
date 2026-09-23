from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.server_error import ServerError
from ...models.server_error_400 import ServerError400
from ...models.server_error_403 import ServerError403
from ...models.server_error_404 import ServerError404
from ...models.server_error_409 import ServerError409
from ...models.server_update_firewall_rules import ServerUpdateFirewallRules
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    *,
    body: ServerUpdateFirewallRules | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
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
) -> Any | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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
) -> Response[Any | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409]:
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
    body: ServerUpdateFirewallRules | Unset = UNSET,
) -> Response[Any | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409]:
    """Replace firewall rules

     Replace the Cloud Server's complete firewall rule chain. Array order determines rule positions.
    Changes can take 1-2 minutes to take effect.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        body (ServerUpdateFirewallRules | Unset): Complete replacement for a Cloud Server's
            firewall rule chain. Array order determines rule positions. Example: {'firewall_rules':
            {'firewall_rule': [{'action': 'accept', 'comment': 'Allow SSH', 'destination_port_end':
            '22', 'destination_port_start': '22', 'direction': 'in', 'family': 'IPv4', 'protocol':
            'tcp'}, {'action': 'drop', 'direction': 'in'}]}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409]
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
    body: ServerUpdateFirewallRules | Unset = UNSET,
) -> Any | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | None:
    """Replace firewall rules

     Replace the Cloud Server's complete firewall rule chain. Array order determines rule positions.
    Changes can take 1-2 minutes to take effect.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        body (ServerUpdateFirewallRules | Unset): Complete replacement for a Cloud Server's
            firewall rule chain. Array order determines rule positions. Example: {'firewall_rules':
            {'firewall_rule': [{'action': 'accept', 'comment': 'Allow SSH', 'destination_port_end':
            '22', 'destination_port_start': '22', 'direction': 'in', 'family': 'IPv4', 'protocol':
            'tcp'}, {'action': 'drop', 'direction': 'in'}]}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409
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
    body: ServerUpdateFirewallRules | Unset = UNSET,
) -> Response[Any | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409]:
    """Replace firewall rules

     Replace the Cloud Server's complete firewall rule chain. Array order determines rule positions.
    Changes can take 1-2 minutes to take effect.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        body (ServerUpdateFirewallRules | Unset): Complete replacement for a Cloud Server's
            firewall rule chain. Array order determines rule positions. Example: {'firewall_rules':
            {'firewall_rule': [{'action': 'accept', 'comment': 'Allow SSH', 'destination_port_end':
            '22', 'destination_port_start': '22', 'direction': 'in', 'family': 'IPv4', 'protocol':
            'tcp'}, {'action': 'drop', 'direction': 'in'}]}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409]
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
    body: ServerUpdateFirewallRules | Unset = UNSET,
) -> Any | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | None:
    """Replace firewall rules

     Replace the Cloud Server's complete firewall rule chain. Array order determines rule positions.
    Changes can take 1-2 minutes to take effect.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        body (ServerUpdateFirewallRules | Unset): Complete replacement for a Cloud Server's
            firewall rule chain. Array order determines rule positions. Example: {'firewall_rules':
            {'firewall_rule': [{'action': 'accept', 'comment': 'Allow SSH', 'destination_port_end':
            '22', 'destination_port_start': '22', 'direction': 'in', 'family': 'IPv4', 'protocol':
            'tcp'}, {'action': 'drop', 'direction': 'in'}]}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed
