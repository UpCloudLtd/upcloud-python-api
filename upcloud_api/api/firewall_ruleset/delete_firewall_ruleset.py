from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.firewall_ruleset_error_response import FirewallRulesetErrorResponse
from ...types import Response


def _get_kwargs(
    ruleset_uuid: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/1.3/firewall-ruleset/{ruleset_uuid}".format(
            ruleset_uuid=quote(str(ruleset_uuid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | FirewallRulesetErrorResponse:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    response_default = FirewallRulesetErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | FirewallRulesetErrorResponse]:
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
) -> Response[Any | FirewallRulesetErrorResponse]:
    """Delete firewall ruleset

     Deletes existing firewall ruleset by given {ruleset-uuid}.

    Args:
        ruleset_uuid (UUID): The unique identifier for the server.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FirewallRulesetErrorResponse]
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
) -> Any | FirewallRulesetErrorResponse | None:
    """Delete firewall ruleset

     Deletes existing firewall ruleset by given {ruleset-uuid}.

    Args:
        ruleset_uuid (UUID): The unique identifier for the server.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FirewallRulesetErrorResponse
    """

    return sync_detailed(
        ruleset_uuid=ruleset_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    ruleset_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | FirewallRulesetErrorResponse]:
    """Delete firewall ruleset

     Deletes existing firewall ruleset by given {ruleset-uuid}.

    Args:
        ruleset_uuid (UUID): The unique identifier for the server.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FirewallRulesetErrorResponse]
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
) -> Any | FirewallRulesetErrorResponse | None:
    """Delete firewall ruleset

     Deletes existing firewall ruleset by given {ruleset-uuid}.

    Args:
        ruleset_uuid (UUID): The unique identifier for the server.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FirewallRulesetErrorResponse
    """

    return (
        await asyncio_detailed(
            ruleset_uuid=ruleset_uuid,
            client=client,
        )
    ).parsed
