from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.firewall_ruleset_error_response import FirewallRulesetErrorResponse
from ...models.firewall_ruleset_server_firewall_rule_detail import FirewallRulesetServerFirewallRuleDetail
from ...types import Response


def _get_kwargs(
    server_uuid: UUID,
    position: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/firewall-ruleset/server/{server_uuid}/firewall-rule/{position}".format(
            server_uuid=quote(str(server_uuid), safe=""),
            position=quote(str(position), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FirewallRulesetErrorResponse | FirewallRulesetServerFirewallRuleDetail:
    if response.status_code == 200:
        response_200 = FirewallRulesetServerFirewallRuleDetail.from_dict(response.json())

        return response_200

    response_default = FirewallRulesetErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[FirewallRulesetErrorResponse | FirewallRulesetServerFirewallRuleDetail]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    server_uuid: UUID,
    position: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[FirewallRulesetErrorResponse | FirewallRulesetServerFirewallRuleDetail]:
    """Get server firewall rule details

     Returns server firewall rule details by given {server-uuid} and {position}.

    Args:
        server_uuid (UUID): The unique identifier for the server.
        position (int): The server firewall rule position.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FirewallRulesetErrorResponse | FirewallRulesetServerFirewallRuleDetail]
    """

    kwargs = _get_kwargs(
        server_uuid=server_uuid,
        position=position,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    server_uuid: UUID,
    position: int,
    *,
    client: AuthenticatedClient | Client,
) -> FirewallRulesetErrorResponse | FirewallRulesetServerFirewallRuleDetail | None:
    """Get server firewall rule details

     Returns server firewall rule details by given {server-uuid} and {position}.

    Args:
        server_uuid (UUID): The unique identifier for the server.
        position (int): The server firewall rule position.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FirewallRulesetErrorResponse | FirewallRulesetServerFirewallRuleDetail
    """

    return sync_detailed(
        server_uuid=server_uuid,
        position=position,
        client=client,
    ).parsed


async def asyncio_detailed(
    server_uuid: UUID,
    position: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[FirewallRulesetErrorResponse | FirewallRulesetServerFirewallRuleDetail]:
    """Get server firewall rule details

     Returns server firewall rule details by given {server-uuid} and {position}.

    Args:
        server_uuid (UUID): The unique identifier for the server.
        position (int): The server firewall rule position.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FirewallRulesetErrorResponse | FirewallRulesetServerFirewallRuleDetail]
    """

    kwargs = _get_kwargs(
        server_uuid=server_uuid,
        position=position,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    server_uuid: UUID,
    position: int,
    *,
    client: AuthenticatedClient | Client,
) -> FirewallRulesetErrorResponse | FirewallRulesetServerFirewallRuleDetail | None:
    """Get server firewall rule details

     Returns server firewall rule details by given {server-uuid} and {position}.

    Args:
        server_uuid (UUID): The unique identifier for the server.
        position (int): The server firewall rule position.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FirewallRulesetErrorResponse | FirewallRulesetServerFirewallRuleDetail
    """

    return (
        await asyncio_detailed(
            server_uuid=server_uuid,
            position=position,
            client=client,
        )
    ).parsed
