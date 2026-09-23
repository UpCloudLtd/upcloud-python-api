from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.firewall_ruleset_error_response import FirewallRulesetErrorResponse
from ...models.firewall_ruleset_firewall_multiple_rule_create import FirewallRulesetFirewallMultipleRuleCreate
from ...models.firewall_ruleset_firewall_rule_list_response import FirewallRulesetFirewallRuleListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    ruleset_uuid: UUID,
    *,
    body: FirewallRulesetFirewallMultipleRuleCreate | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/1.3/firewall-ruleset/{ruleset_uuid}/rule".format(
            ruleset_uuid=quote(str(ruleset_uuid), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FirewallRulesetErrorResponse | FirewallRulesetFirewallRuleListResponse:
    if response.status_code == 200:
        response_200 = FirewallRulesetFirewallRuleListResponse.from_dict(response.json())

        return response_200

    response_default = FirewallRulesetErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[FirewallRulesetErrorResponse | FirewallRulesetFirewallRuleListResponse]:
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
    body: FirewallRulesetFirewallMultipleRuleCreate | Unset = UNSET,
) -> Response[FirewallRulesetErrorResponse | FirewallRulesetFirewallRuleListResponse]:
    """Create multiple firewall ruleset rules

     Creates multiple firewall ruleset rules by the given {ruleset-uuid}.

    Args:
        ruleset_uuid (UUID): The unique identifier for the server.
        body (FirewallRulesetFirewallMultipleRuleCreate | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FirewallRulesetErrorResponse | FirewallRulesetFirewallRuleListResponse]
    """

    kwargs = _get_kwargs(
        ruleset_uuid=ruleset_uuid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    ruleset_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: FirewallRulesetFirewallMultipleRuleCreate | Unset = UNSET,
) -> FirewallRulesetErrorResponse | FirewallRulesetFirewallRuleListResponse | None:
    """Create multiple firewall ruleset rules

     Creates multiple firewall ruleset rules by the given {ruleset-uuid}.

    Args:
        ruleset_uuid (UUID): The unique identifier for the server.
        body (FirewallRulesetFirewallMultipleRuleCreate | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FirewallRulesetErrorResponse | FirewallRulesetFirewallRuleListResponse
    """

    return sync_detailed(
        ruleset_uuid=ruleset_uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    ruleset_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: FirewallRulesetFirewallMultipleRuleCreate | Unset = UNSET,
) -> Response[FirewallRulesetErrorResponse | FirewallRulesetFirewallRuleListResponse]:
    """Create multiple firewall ruleset rules

     Creates multiple firewall ruleset rules by the given {ruleset-uuid}.

    Args:
        ruleset_uuid (UUID): The unique identifier for the server.
        body (FirewallRulesetFirewallMultipleRuleCreate | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FirewallRulesetErrorResponse | FirewallRulesetFirewallRuleListResponse]
    """

    kwargs = _get_kwargs(
        ruleset_uuid=ruleset_uuid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    ruleset_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: FirewallRulesetFirewallMultipleRuleCreate | Unset = UNSET,
) -> FirewallRulesetErrorResponse | FirewallRulesetFirewallRuleListResponse | None:
    """Create multiple firewall ruleset rules

     Creates multiple firewall ruleset rules by the given {ruleset-uuid}.

    Args:
        ruleset_uuid (UUID): The unique identifier for the server.
        body (FirewallRulesetFirewallMultipleRuleCreate | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FirewallRulesetErrorResponse | FirewallRulesetFirewallRuleListResponse
    """

    return (
        await asyncio_detailed(
            ruleset_uuid=ruleset_uuid,
            client=client,
            body=body,
        )
    ).parsed
