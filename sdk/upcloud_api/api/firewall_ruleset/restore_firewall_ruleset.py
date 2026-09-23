from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.firewall_ruleset_detail_response import FirewallRulesetDetailResponse
from ...models.firewall_ruleset_error_response import FirewallRulesetErrorResponse
from ...types import Response


def _get_kwargs(
    ruleset_uuid: UUID,
    ruleset_version: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/1.3/firewall-ruleset/{ruleset_uuid}/restore/{ruleset_version}".format(
            ruleset_uuid=quote(str(ruleset_uuid), safe=""),
            ruleset_version=quote(str(ruleset_version), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FirewallRulesetDetailResponse | FirewallRulesetErrorResponse:
    if response.status_code == 200:
        response_200 = FirewallRulesetDetailResponse.from_dict(response.json())

        return response_200

    response_default = FirewallRulesetErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[FirewallRulesetDetailResponse | FirewallRulesetErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    ruleset_uuid: UUID,
    ruleset_version: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[FirewallRulesetDetailResponse | FirewallRulesetErrorResponse]:
    """Restore firewall ruleset

     Restores existing firewall ruleset by given {ruleset-uuid} and {ruleset-version}.

    Args:
        ruleset_uuid (UUID): The unique identifier for the server.
        ruleset_version (int): The firewall ruleset version.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FirewallRulesetDetailResponse | FirewallRulesetErrorResponse]
    """

    kwargs = _get_kwargs(
        ruleset_uuid=ruleset_uuid,
        ruleset_version=ruleset_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    ruleset_uuid: UUID,
    ruleset_version: int,
    *,
    client: AuthenticatedClient | Client,
) -> FirewallRulesetDetailResponse | FirewallRulesetErrorResponse | None:
    """Restore firewall ruleset

     Restores existing firewall ruleset by given {ruleset-uuid} and {ruleset-version}.

    Args:
        ruleset_uuid (UUID): The unique identifier for the server.
        ruleset_version (int): The firewall ruleset version.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FirewallRulesetDetailResponse | FirewallRulesetErrorResponse
    """

    return sync_detailed(
        ruleset_uuid=ruleset_uuid,
        ruleset_version=ruleset_version,
        client=client,
    ).parsed


async def asyncio_detailed(
    ruleset_uuid: UUID,
    ruleset_version: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[FirewallRulesetDetailResponse | FirewallRulesetErrorResponse]:
    """Restore firewall ruleset

     Restores existing firewall ruleset by given {ruleset-uuid} and {ruleset-version}.

    Args:
        ruleset_uuid (UUID): The unique identifier for the server.
        ruleset_version (int): The firewall ruleset version.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FirewallRulesetDetailResponse | FirewallRulesetErrorResponse]
    """

    kwargs = _get_kwargs(
        ruleset_uuid=ruleset_uuid,
        ruleset_version=ruleset_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    ruleset_uuid: UUID,
    ruleset_version: int,
    *,
    client: AuthenticatedClient | Client,
) -> FirewallRulesetDetailResponse | FirewallRulesetErrorResponse | None:
    """Restore firewall ruleset

     Restores existing firewall ruleset by given {ruleset-uuid} and {ruleset-version}.

    Args:
        ruleset_uuid (UUID): The unique identifier for the server.
        ruleset_version (int): The firewall ruleset version.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FirewallRulesetDetailResponse | FirewallRulesetErrorResponse
    """

    return (
        await asyncio_detailed(
            ruleset_uuid=ruleset_uuid,
            ruleset_version=ruleset_version,
            client=client,
        )
    ).parsed
