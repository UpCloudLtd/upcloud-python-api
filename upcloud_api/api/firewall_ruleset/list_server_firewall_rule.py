from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.firewall_ruleset_error_response import FirewallRulesetErrorResponse
from ...models.firewall_ruleset_server_firewall_detail_response import FirewallRulesetServerFirewallDetailResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    server_uuid: UUID,
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
        "url": "/1.3/firewall-ruleset/server/{server_uuid}/firewall-rule".format(
            server_uuid=quote(str(server_uuid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FirewallRulesetErrorResponse | FirewallRulesetServerFirewallDetailResponse:
    if response.status_code == 200:
        response_200 = FirewallRulesetServerFirewallDetailResponse.from_dict(response.json())

        return response_200

    response_default = FirewallRulesetErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[FirewallRulesetErrorResponse | FirewallRulesetServerFirewallDetailResponse]:
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
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> Response[FirewallRulesetErrorResponse | FirewallRulesetServerFirewallDetailResponse]:
    """List server firewall rules

     Returns a list of server firewall rules.

    Args:
        server_uuid (UUID): The unique identifier for the server.
        limit (int | Unset): Schema for a query parameter specifying the maximum number of entries
            to return (limit).
        offset (int | Unset): Schema for a query parameter specifying the offset for pagination.
        sort (str | Unset): Schema for a query parameter specifying the sort field.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FirewallRulesetErrorResponse | FirewallRulesetServerFirewallDetailResponse]
    """

    kwargs = _get_kwargs(
        server_uuid=server_uuid,
        limit=limit,
        offset=offset,
        sort=sort,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    server_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> FirewallRulesetErrorResponse | FirewallRulesetServerFirewallDetailResponse | None:
    """List server firewall rules

     Returns a list of server firewall rules.

    Args:
        server_uuid (UUID): The unique identifier for the server.
        limit (int | Unset): Schema for a query parameter specifying the maximum number of entries
            to return (limit).
        offset (int | Unset): Schema for a query parameter specifying the offset for pagination.
        sort (str | Unset): Schema for a query parameter specifying the sort field.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FirewallRulesetErrorResponse | FirewallRulesetServerFirewallDetailResponse
    """

    return sync_detailed(
        server_uuid=server_uuid,
        client=client,
        limit=limit,
        offset=offset,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    server_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> Response[FirewallRulesetErrorResponse | FirewallRulesetServerFirewallDetailResponse]:
    """List server firewall rules

     Returns a list of server firewall rules.

    Args:
        server_uuid (UUID): The unique identifier for the server.
        limit (int | Unset): Schema for a query parameter specifying the maximum number of entries
            to return (limit).
        offset (int | Unset): Schema for a query parameter specifying the offset for pagination.
        sort (str | Unset): Schema for a query parameter specifying the sort field.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FirewallRulesetErrorResponse | FirewallRulesetServerFirewallDetailResponse]
    """

    kwargs = _get_kwargs(
        server_uuid=server_uuid,
        limit=limit,
        offset=offset,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    server_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> FirewallRulesetErrorResponse | FirewallRulesetServerFirewallDetailResponse | None:
    """List server firewall rules

     Returns a list of server firewall rules.

    Args:
        server_uuid (UUID): The unique identifier for the server.
        limit (int | Unset): Schema for a query parameter specifying the maximum number of entries
            to return (limit).
        offset (int | Unset): Schema for a query parameter specifying the offset for pagination.
        sort (str | Unset): Schema for a query parameter specifying the sort field.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FirewallRulesetErrorResponse | FirewallRulesetServerFirewallDetailResponse
    """

    return (
        await asyncio_detailed(
            server_uuid=server_uuid,
            client=client,
            limit=limit,
            offset=offset,
            sort=sort,
        )
    ).parsed
