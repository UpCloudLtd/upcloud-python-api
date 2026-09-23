from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.firewall_ruleset_related_servers import FirewallRulesetRelatedServers
from ...models.server_error import ServerError
from ...models.server_error_400 import ServerError400
from ...types import Response


def _get_kwargs(
    ruleset_uuid: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/server/firewall_ruleset_relationships/private/{ruleset_uuid}".format(
            ruleset_uuid=quote(str(ruleset_uuid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FirewallRulesetRelatedServers | ServerError | ServerError400:
    if response.status_code == 200:
        response_200 = FirewallRulesetRelatedServers.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ServerError400.from_dict(response.json())

        return response_400

    response_default = ServerError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[FirewallRulesetRelatedServers | ServerError | ServerError400]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    ruleset_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[FirewallRulesetRelatedServers | ServerError | ServerError400]:
    """List Cloud Servers related to a private firewall ruleset

     Return Cloud Servers visible to the authenticated account that are related to a private firewall
    ruleset, including each Cloud Server's private ruleset relationships.

    Args:
        ruleset_uuid (UUID): Universally unique identifier Example:
            0414e0d7-4436-4037-9dd8-6eaf47dce599.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FirewallRulesetRelatedServers | ServerError | ServerError400]
    """

    kwargs = _get_kwargs(
        ruleset_uuid=ruleset_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    ruleset_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> FirewallRulesetRelatedServers | ServerError | ServerError400 | None:
    """List Cloud Servers related to a private firewall ruleset

     Return Cloud Servers visible to the authenticated account that are related to a private firewall
    ruleset, including each Cloud Server's private ruleset relationships.

    Args:
        ruleset_uuid (UUID): Universally unique identifier Example:
            0414e0d7-4436-4037-9dd8-6eaf47dce599.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FirewallRulesetRelatedServers | ServerError | ServerError400
    """

    return sync_detailed(
        ruleset_uuid=ruleset_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    ruleset_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[FirewallRulesetRelatedServers | ServerError | ServerError400]:
    """List Cloud Servers related to a private firewall ruleset

     Return Cloud Servers visible to the authenticated account that are related to a private firewall
    ruleset, including each Cloud Server's private ruleset relationships.

    Args:
        ruleset_uuid (UUID): Universally unique identifier Example:
            0414e0d7-4436-4037-9dd8-6eaf47dce599.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FirewallRulesetRelatedServers | ServerError | ServerError400]
    """

    kwargs = _get_kwargs(
        ruleset_uuid=ruleset_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    ruleset_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> FirewallRulesetRelatedServers | ServerError | ServerError400 | None:
    """List Cloud Servers related to a private firewall ruleset

     Return Cloud Servers visible to the authenticated account that are related to a private firewall
    ruleset, including each Cloud Server's private ruleset relationships.

    Args:
        ruleset_uuid (UUID): Universally unique identifier Example:
            0414e0d7-4436-4037-9dd8-6eaf47dce599.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FirewallRulesetRelatedServers | ServerError | ServerError400
    """

    return (
        await asyncio_detailed(
            ruleset_uuid=ruleset_uuid,
            client=client,
        )
    ).parsed
