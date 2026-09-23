from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.firewall_ruleset_error_legacy_response import FirewallRulesetErrorLegacyResponse
from ...models.firewall_ruleset_error_response import FirewallRulesetErrorResponse
from ...models.firewall_ruleset_server_firewall_detail_response import FirewallRulesetServerFirewallDetailResponse
from ...models.firewall_ruleset_server_multiple_firewall_rules_create import (
    FirewallRulesetServerMultipleFirewallRulesCreate,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    server_uuid: UUID,
    *,
    body: FirewallRulesetServerMultipleFirewallRulesCreate | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
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
) -> FirewallRulesetErrorLegacyResponse | FirewallRulesetErrorResponse | FirewallRulesetServerFirewallDetailResponse:
    if response.status_code == 200:
        response_200 = FirewallRulesetServerFirewallDetailResponse.from_dict(response.json())

        return response_200

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
    FirewallRulesetErrorLegacyResponse | FirewallRulesetErrorResponse | FirewallRulesetServerFirewallDetailResponse
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
    body: FirewallRulesetServerMultipleFirewallRulesCreate | Unset = UNSET,
) -> Response[
    FirewallRulesetErrorLegacyResponse | FirewallRulesetErrorResponse | FirewallRulesetServerFirewallDetailResponse
]:
    """Create multiple server firewall rules

     Creates multiple server firewall rules by given {server-uuid}.

    Args:
        server_uuid (UUID): The unique identifier for the server.
        body (FirewallRulesetServerMultipleFirewallRulesCreate | Unset): Creates multiple server
            firewall rules.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FirewallRulesetErrorLegacyResponse | FirewallRulesetErrorResponse | FirewallRulesetServerFirewallDetailResponse]
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
    body: FirewallRulesetServerMultipleFirewallRulesCreate | Unset = UNSET,
) -> (
    FirewallRulesetErrorLegacyResponse
    | FirewallRulesetErrorResponse
    | FirewallRulesetServerFirewallDetailResponse
    | None
):
    """Create multiple server firewall rules

     Creates multiple server firewall rules by given {server-uuid}.

    Args:
        server_uuid (UUID): The unique identifier for the server.
        body (FirewallRulesetServerMultipleFirewallRulesCreate | Unset): Creates multiple server
            firewall rules.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FirewallRulesetErrorLegacyResponse | FirewallRulesetErrorResponse | FirewallRulesetServerFirewallDetailResponse
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
    body: FirewallRulesetServerMultipleFirewallRulesCreate | Unset = UNSET,
) -> Response[
    FirewallRulesetErrorLegacyResponse | FirewallRulesetErrorResponse | FirewallRulesetServerFirewallDetailResponse
]:
    """Create multiple server firewall rules

     Creates multiple server firewall rules by given {server-uuid}.

    Args:
        server_uuid (UUID): The unique identifier for the server.
        body (FirewallRulesetServerMultipleFirewallRulesCreate | Unset): Creates multiple server
            firewall rules.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FirewallRulesetErrorLegacyResponse | FirewallRulesetErrorResponse | FirewallRulesetServerFirewallDetailResponse]
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
    body: FirewallRulesetServerMultipleFirewallRulesCreate | Unset = UNSET,
) -> (
    FirewallRulesetErrorLegacyResponse
    | FirewallRulesetErrorResponse
    | FirewallRulesetServerFirewallDetailResponse
    | None
):
    """Create multiple server firewall rules

     Creates multiple server firewall rules by given {server-uuid}.

    Args:
        server_uuid (UUID): The unique identifier for the server.
        body (FirewallRulesetServerMultipleFirewallRulesCreate | Unset): Creates multiple server
            firewall rules.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FirewallRulesetErrorLegacyResponse | FirewallRulesetErrorResponse | FirewallRulesetServerFirewallDetailResponse
    """

    return (
        await asyncio_detailed(
            server_uuid=server_uuid,
            client=client,
            body=body,
        )
    ).parsed
