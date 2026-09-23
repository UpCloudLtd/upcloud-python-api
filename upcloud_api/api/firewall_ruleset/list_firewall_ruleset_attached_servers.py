from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.firewall_ruleset_error_response import FirewallRulesetErrorResponse
from ...models.firewall_ruleset_label_detail_response import FirewallRulesetLabelDetailResponse
from ...types import Response


def _get_kwargs(
    ruleset_uuid: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/firewall-ruleset/{ruleset_uuid}/servers".format(
            ruleset_uuid=quote(str(ruleset_uuid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FirewallRulesetErrorResponse | list[FirewallRulesetLabelDetailResponse]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemasfirewall_ruleset_label_list_response_item_data in _response_200:
            componentsschemasfirewall_ruleset_label_list_response_item = FirewallRulesetLabelDetailResponse.from_dict(
                componentsschemasfirewall_ruleset_label_list_response_item_data
            )

            response_200.append(componentsschemasfirewall_ruleset_label_list_response_item)

        return response_200

    response_default = FirewallRulesetErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[FirewallRulesetErrorResponse | list[FirewallRulesetLabelDetailResponse]]:
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
) -> Response[FirewallRulesetErrorResponse | list[FirewallRulesetLabelDetailResponse]]:
    """List servers attached to a firewall ruleset

     Returns a list of servers that are attached to the firewall ruleset by given {ruleset-uuid}.

    Args:
        ruleset_uuid (UUID): The unique identifier for the server.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FirewallRulesetErrorResponse | list[FirewallRulesetLabelDetailResponse]]
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
) -> FirewallRulesetErrorResponse | list[FirewallRulesetLabelDetailResponse] | None:
    """List servers attached to a firewall ruleset

     Returns a list of servers that are attached to the firewall ruleset by given {ruleset-uuid}.

    Args:
        ruleset_uuid (UUID): The unique identifier for the server.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FirewallRulesetErrorResponse | list[FirewallRulesetLabelDetailResponse]
    """

    return sync_detailed(
        ruleset_uuid=ruleset_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    ruleset_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[FirewallRulesetErrorResponse | list[FirewallRulesetLabelDetailResponse]]:
    """List servers attached to a firewall ruleset

     Returns a list of servers that are attached to the firewall ruleset by given {ruleset-uuid}.

    Args:
        ruleset_uuid (UUID): The unique identifier for the server.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FirewallRulesetErrorResponse | list[FirewallRulesetLabelDetailResponse]]
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
) -> FirewallRulesetErrorResponse | list[FirewallRulesetLabelDetailResponse] | None:
    """List servers attached to a firewall ruleset

     Returns a list of servers that are attached to the firewall ruleset by given {ruleset-uuid}.

    Args:
        ruleset_uuid (UUID): The unique identifier for the server.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FirewallRulesetErrorResponse | list[FirewallRulesetLabelDetailResponse]
    """

    return (
        await asyncio_detailed(
            ruleset_uuid=ruleset_uuid,
            client=client,
        )
    ).parsed
