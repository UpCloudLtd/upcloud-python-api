from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.firewall_ruleset_detail_response import FirewallRulesetDetailResponse
from ...models.firewall_ruleset_error_response import FirewallRulesetErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
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
        "url": "/1.3/firewall-ruleset",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FirewallRulesetErrorResponse | list[FirewallRulesetDetailResponse]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemasfirewall_ruleset_list_response_item_data in _response_200:
            componentsschemasfirewall_ruleset_list_response_item = FirewallRulesetDetailResponse.from_dict(
                componentsschemasfirewall_ruleset_list_response_item_data
            )

            response_200.append(componentsschemasfirewall_ruleset_list_response_item)

        return response_200

    response_default = FirewallRulesetErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[FirewallRulesetErrorResponse | list[FirewallRulesetDetailResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> Response[FirewallRulesetErrorResponse | list[FirewallRulesetDetailResponse]]:
    """List firewall rulesets

     Returns a list of firewall rulesets.

    Args:
        limit (int | Unset): Schema for a query parameter specifying the maximum number of entries
            to return (limit).
        offset (int | Unset): Schema for a query parameter specifying the offset for pagination.
        sort (str | Unset): Schema for a query parameter specifying the sort field.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FirewallRulesetErrorResponse | list[FirewallRulesetDetailResponse]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        sort=sort,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> FirewallRulesetErrorResponse | list[FirewallRulesetDetailResponse] | None:
    """List firewall rulesets

     Returns a list of firewall rulesets.

    Args:
        limit (int | Unset): Schema for a query parameter specifying the maximum number of entries
            to return (limit).
        offset (int | Unset): Schema for a query parameter specifying the offset for pagination.
        sort (str | Unset): Schema for a query parameter specifying the sort field.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FirewallRulesetErrorResponse | list[FirewallRulesetDetailResponse]
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> Response[FirewallRulesetErrorResponse | list[FirewallRulesetDetailResponse]]:
    """List firewall rulesets

     Returns a list of firewall rulesets.

    Args:
        limit (int | Unset): Schema for a query parameter specifying the maximum number of entries
            to return (limit).
        offset (int | Unset): Schema for a query parameter specifying the offset for pagination.
        sort (str | Unset): Schema for a query parameter specifying the sort field.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FirewallRulesetErrorResponse | list[FirewallRulesetDetailResponse]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> FirewallRulesetErrorResponse | list[FirewallRulesetDetailResponse] | None:
    """List firewall rulesets

     Returns a list of firewall rulesets.

    Args:
        limit (int | Unset): Schema for a query parameter specifying the maximum number of entries
            to return (limit).
        offset (int | Unset): Schema for a query parameter specifying the offset for pagination.
        sort (str | Unset): Schema for a query parameter specifying the sort field.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FirewallRulesetErrorResponse | list[FirewallRulesetDetailResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            sort=sort,
        )
    ).parsed
