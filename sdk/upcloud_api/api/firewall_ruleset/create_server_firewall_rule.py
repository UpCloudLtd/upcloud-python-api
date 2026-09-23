from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.firewall_ruleset_error_legacy_response import FirewallRulesetErrorLegacyResponse
from ...models.firewall_ruleset_error_response import FirewallRulesetErrorResponse
from ...models.firewall_ruleset_server_firewall_rule_create import FirewallRulesetServerFirewallRuleCreate
from ...models.firewall_ruleset_server_firewall_rule_detail import FirewallRulesetServerFirewallRuleDetail
from ...types import UNSET, Response, Unset


def _get_kwargs(
    server_uuid: UUID,
    *,
    body: FirewallRulesetServerFirewallRuleCreate | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/1.3/firewall-ruleset/server/{server_uuid}/firewall-rule".format(
            server_uuid=quote(str(server_uuid), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FirewallRulesetErrorLegacyResponse | FirewallRulesetErrorResponse | FirewallRulesetServerFirewallRuleDetail:
    if response.status_code == 201:
        response_201 = FirewallRulesetServerFirewallRuleDetail.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = FirewallRulesetErrorLegacyResponse.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = FirewallRulesetErrorLegacyResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = FirewallRulesetErrorLegacyResponse.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = FirewallRulesetErrorLegacyResponse.from_dict(response.json())

        return response_409

    response_default = FirewallRulesetErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FirewallRulesetErrorLegacyResponse | FirewallRulesetErrorResponse | FirewallRulesetServerFirewallRuleDetail
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    server_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: FirewallRulesetServerFirewallRuleCreate | Unset = UNSET,
) -> Response[
    FirewallRulesetErrorLegacyResponse | FirewallRulesetErrorResponse | FirewallRulesetServerFirewallRuleDetail
]:
    """Create server firewall rule

     Creates a new server firewall rule.

    Args:
        server_uuid (UUID): The unique identifier for the server.
        body (FirewallRulesetServerFirewallRuleCreate | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FirewallRulesetErrorLegacyResponse | FirewallRulesetErrorResponse | FirewallRulesetServerFirewallRuleDetail]
    """

    kwargs = _get_kwargs(
        server_uuid=server_uuid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    server_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: FirewallRulesetServerFirewallRuleCreate | Unset = UNSET,
) -> FirewallRulesetErrorLegacyResponse | FirewallRulesetErrorResponse | FirewallRulesetServerFirewallRuleDetail | None:
    """Create server firewall rule

     Creates a new server firewall rule.

    Args:
        server_uuid (UUID): The unique identifier for the server.
        body (FirewallRulesetServerFirewallRuleCreate | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FirewallRulesetErrorLegacyResponse | FirewallRulesetErrorResponse | FirewallRulesetServerFirewallRuleDetail
    """

    return sync_detailed(
        server_uuid=server_uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    server_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: FirewallRulesetServerFirewallRuleCreate | Unset = UNSET,
) -> Response[
    FirewallRulesetErrorLegacyResponse | FirewallRulesetErrorResponse | FirewallRulesetServerFirewallRuleDetail
]:
    """Create server firewall rule

     Creates a new server firewall rule.

    Args:
        server_uuid (UUID): The unique identifier for the server.
        body (FirewallRulesetServerFirewallRuleCreate | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FirewallRulesetErrorLegacyResponse | FirewallRulesetErrorResponse | FirewallRulesetServerFirewallRuleDetail]
    """

    kwargs = _get_kwargs(
        server_uuid=server_uuid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    server_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: FirewallRulesetServerFirewallRuleCreate | Unset = UNSET,
) -> FirewallRulesetErrorLegacyResponse | FirewallRulesetErrorResponse | FirewallRulesetServerFirewallRuleDetail | None:
    """Create server firewall rule

     Creates a new server firewall rule.

    Args:
        server_uuid (UUID): The unique identifier for the server.
        body (FirewallRulesetServerFirewallRuleCreate | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FirewallRulesetErrorLegacyResponse | FirewallRulesetErrorResponse | FirewallRulesetServerFirewallRuleDetail
    """

    return (
        await asyncio_detailed(
            server_uuid=server_uuid,
            client=client,
            body=body,
        )
    ).parsed
