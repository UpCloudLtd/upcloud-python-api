from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.firewall_ruleset_error_response import FirewallRulesetErrorResponse
from ...models.firewall_ruleset_firewall_rule_list_response import FirewallRulesetFirewallRuleListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    ruleset_uuid: UUID,
    *,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/firewall-ruleset/{ruleset_uuid}/rule".format(
            ruleset_uuid=quote(str(ruleset_uuid), safe=""),
        ),
        "params": params,
    }

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
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> Response[FirewallRulesetErrorResponse | FirewallRulesetFirewallRuleListResponse]:
    """List firewall ruleset rules

     Returns firewall ruleset rules.

    Args:
        ruleset_uuid (UUID): The unique identifier for the server.
        limit (int | Unset): Schema for a query parameter specifying the maximum number of entries
            to return (limit).
        offset (int | Unset): Schema for a query parameter specifying the offset for pagination.
        sort (str | Unset): Schema for a query parameter specifying the sort field.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FirewallRulesetErrorResponse | FirewallRulesetFirewallRuleListResponse]
    """

    kwargs = _get_kwargs(
        ruleset_uuid=ruleset_uuid,
        limit=limit,
        offset=offset,
        sort=sort,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    ruleset_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> FirewallRulesetErrorResponse | FirewallRulesetFirewallRuleListResponse | None:
    """List firewall ruleset rules

     Returns firewall ruleset rules.

    Args:
        ruleset_uuid (UUID): The unique identifier for the server.
        limit (int | Unset): Schema for a query parameter specifying the maximum number of entries
            to return (limit).
        offset (int | Unset): Schema for a query parameter specifying the offset for pagination.
        sort (str | Unset): Schema for a query parameter specifying the sort field.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FirewallRulesetErrorResponse | FirewallRulesetFirewallRuleListResponse
    """

    return sync_detailed(
        ruleset_uuid=ruleset_uuid,
        client=client,
        limit=limit,
        offset=offset,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    ruleset_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> Response[FirewallRulesetErrorResponse | FirewallRulesetFirewallRuleListResponse]:
    """List firewall ruleset rules

     Returns firewall ruleset rules.

    Args:
        ruleset_uuid (UUID): The unique identifier for the server.
        limit (int | Unset): Schema for a query parameter specifying the maximum number of entries
            to return (limit).
        offset (int | Unset): Schema for a query parameter specifying the offset for pagination.
        sort (str | Unset): Schema for a query parameter specifying the sort field.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FirewallRulesetErrorResponse | FirewallRulesetFirewallRuleListResponse]
    """

    kwargs = _get_kwargs(
        ruleset_uuid=ruleset_uuid,
        limit=limit,
        offset=offset,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    ruleset_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> FirewallRulesetErrorResponse | FirewallRulesetFirewallRuleListResponse | None:
    """List firewall ruleset rules

     Returns firewall ruleset rules.

    Args:
        ruleset_uuid (UUID): The unique identifier for the server.
        limit (int | Unset): Schema for a query parameter specifying the maximum number of entries
            to return (limit).
        offset (int | Unset): Schema for a query parameter specifying the offset for pagination.
        sort (str | Unset): Schema for a query parameter specifying the sort field.

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
            limit=limit,
            offset=offset,
            sort=sort,
        )
    ).parsed
