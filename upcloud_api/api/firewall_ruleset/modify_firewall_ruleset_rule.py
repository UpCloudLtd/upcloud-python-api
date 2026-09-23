from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.firewall_ruleset_error_response import FirewallRulesetErrorResponse
from ...models.firewall_ruleset_firewall_rule_modify import FirewallRulesetFirewallRuleModify
from ...models.firewall_ruleset_rule_detail_response import FirewallRulesetRuleDetailResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    ruleset_uuid: UUID,
    rule_id: UUID,
    *,
    body: FirewallRulesetFirewallRuleModify | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/1.3/firewall-ruleset/{ruleset_uuid}/rule/{rule_id}".format(
            ruleset_uuid=quote(str(ruleset_uuid), safe=""),
            rule_id=quote(str(rule_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FirewallRulesetErrorResponse | FirewallRulesetRuleDetailResponse:
    if response.status_code == 200:
        response_200 = FirewallRulesetRuleDetailResponse.from_dict(response.json())

        return response_200

    response_default = FirewallRulesetErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[FirewallRulesetErrorResponse | FirewallRulesetRuleDetailResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    ruleset_uuid: UUID,
    rule_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: FirewallRulesetFirewallRuleModify | Unset = UNSET,
) -> Response[FirewallRulesetErrorResponse | FirewallRulesetRuleDetailResponse]:
    """Modify firewall ruleset rule

     Modifies existing firewall ruleset rule by given {ruleset_uuid} and {rule-uuid}.

    Args:
        ruleset_uuid (UUID): The unique identifier for the server.
        rule_id (UUID): The unique identifier for the server.
        body (FirewallRulesetFirewallRuleModify | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FirewallRulesetErrorResponse | FirewallRulesetRuleDetailResponse]
    """

    kwargs = _get_kwargs(
        ruleset_uuid=ruleset_uuid,
        rule_id=rule_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    ruleset_uuid: UUID,
    rule_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: FirewallRulesetFirewallRuleModify | Unset = UNSET,
) -> FirewallRulesetErrorResponse | FirewallRulesetRuleDetailResponse | None:
    """Modify firewall ruleset rule

     Modifies existing firewall ruleset rule by given {ruleset_uuid} and {rule-uuid}.

    Args:
        ruleset_uuid (UUID): The unique identifier for the server.
        rule_id (UUID): The unique identifier for the server.
        body (FirewallRulesetFirewallRuleModify | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FirewallRulesetErrorResponse | FirewallRulesetRuleDetailResponse
    """

    return sync_detailed(
        ruleset_uuid=ruleset_uuid,
        rule_id=rule_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    ruleset_uuid: UUID,
    rule_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: FirewallRulesetFirewallRuleModify | Unset = UNSET,
) -> Response[FirewallRulesetErrorResponse | FirewallRulesetRuleDetailResponse]:
    """Modify firewall ruleset rule

     Modifies existing firewall ruleset rule by given {ruleset_uuid} and {rule-uuid}.

    Args:
        ruleset_uuid (UUID): The unique identifier for the server.
        rule_id (UUID): The unique identifier for the server.
        body (FirewallRulesetFirewallRuleModify | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FirewallRulesetErrorResponse | FirewallRulesetRuleDetailResponse]
    """

    kwargs = _get_kwargs(
        ruleset_uuid=ruleset_uuid,
        rule_id=rule_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    ruleset_uuid: UUID,
    rule_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: FirewallRulesetFirewallRuleModify | Unset = UNSET,
) -> FirewallRulesetErrorResponse | FirewallRulesetRuleDetailResponse | None:
    """Modify firewall ruleset rule

     Modifies existing firewall ruleset rule by given {ruleset_uuid} and {rule-uuid}.

    Args:
        ruleset_uuid (UUID): The unique identifier for the server.
        rule_id (UUID): The unique identifier for the server.
        body (FirewallRulesetFirewallRuleModify | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FirewallRulesetErrorResponse | FirewallRulesetRuleDetailResponse
    """

    return (
        await asyncio_detailed(
            ruleset_uuid=ruleset_uuid,
            rule_id=rule_id,
            client=client,
            body=body,
        )
    ).parsed
