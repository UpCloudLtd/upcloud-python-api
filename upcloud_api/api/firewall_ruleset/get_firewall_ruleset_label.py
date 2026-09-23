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
    label_key: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/firewall-ruleset/{ruleset_uuid}/labels/{label_key}".format(
            ruleset_uuid=quote(str(ruleset_uuid), safe=""),
            label_key=quote(str(label_key), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FirewallRulesetErrorResponse | FirewallRulesetLabelDetailResponse:
    if response.status_code == 200:
        response_200 = FirewallRulesetLabelDetailResponse.from_dict(response.json())

        return response_200

    response_default = FirewallRulesetErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[FirewallRulesetErrorResponse | FirewallRulesetLabelDetailResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    ruleset_uuid: UUID,
    label_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[FirewallRulesetErrorResponse | FirewallRulesetLabelDetailResponse]:
    """Get firewall ruleset label details

     Returns label details by given {ruleset-uuid} and {label-key}.

    Args:
        ruleset_uuid (UUID): The unique identifier for the server.
        label_key (str): The key of a label.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FirewallRulesetErrorResponse | FirewallRulesetLabelDetailResponse]
    """

    kwargs = _get_kwargs(
        ruleset_uuid=ruleset_uuid,
        label_key=label_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    ruleset_uuid: UUID,
    label_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> FirewallRulesetErrorResponse | FirewallRulesetLabelDetailResponse | None:
    """Get firewall ruleset label details

     Returns label details by given {ruleset-uuid} and {label-key}.

    Args:
        ruleset_uuid (UUID): The unique identifier for the server.
        label_key (str): The key of a label.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FirewallRulesetErrorResponse | FirewallRulesetLabelDetailResponse
    """

    return sync_detailed(
        ruleset_uuid=ruleset_uuid,
        label_key=label_key,
        client=client,
    ).parsed


async def asyncio_detailed(
    ruleset_uuid: UUID,
    label_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[FirewallRulesetErrorResponse | FirewallRulesetLabelDetailResponse]:
    """Get firewall ruleset label details

     Returns label details by given {ruleset-uuid} and {label-key}.

    Args:
        ruleset_uuid (UUID): The unique identifier for the server.
        label_key (str): The key of a label.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FirewallRulesetErrorResponse | FirewallRulesetLabelDetailResponse]
    """

    kwargs = _get_kwargs(
        ruleset_uuid=ruleset_uuid,
        label_key=label_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    ruleset_uuid: UUID,
    label_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> FirewallRulesetErrorResponse | FirewallRulesetLabelDetailResponse | None:
    """Get firewall ruleset label details

     Returns label details by given {ruleset-uuid} and {label-key}.

    Args:
        ruleset_uuid (UUID): The unique identifier for the server.
        label_key (str): The key of a label.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FirewallRulesetErrorResponse | FirewallRulesetLabelDetailResponse
    """

    return (
        await asyncio_detailed(
            ruleset_uuid=ruleset_uuid,
            label_key=label_key,
            client=client,
        )
    ).parsed
