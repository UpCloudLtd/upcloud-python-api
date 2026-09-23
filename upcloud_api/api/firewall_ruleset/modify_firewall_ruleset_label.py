from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.firewall_ruleset_error_response import FirewallRulesetErrorResponse
from ...models.firewall_ruleset_label_detail_response import FirewallRulesetLabelDetailResponse
from ...models.firewall_ruleset_label_modify import FirewallRulesetLabelModify
from ...types import UNSET, Response, Unset


def _get_kwargs(
    ruleset_uuid: UUID,
    label_key: str,
    *,
    body: FirewallRulesetLabelModify | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/1.3/firewall-ruleset/{ruleset_uuid}/labels/{label_key}".format(
            ruleset_uuid=quote(str(ruleset_uuid), safe=""),
            label_key=quote(str(label_key), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    body: FirewallRulesetLabelModify | Unset = UNSET,
) -> Response[FirewallRulesetErrorResponse | FirewallRulesetLabelDetailResponse]:
    """Modify firewall ruleset label

     Modifies existing label by given {ruleset-uuid} and {label-key}.

    Args:
        ruleset_uuid (UUID): The unique identifier for the server.
        label_key (str): The key of a label.
        body (FirewallRulesetLabelModify | Unset): Schema for modifying a label with a key-value
            pair.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FirewallRulesetErrorResponse | FirewallRulesetLabelDetailResponse]
    """

    kwargs = _get_kwargs(
        ruleset_uuid=ruleset_uuid,
        label_key=label_key,
        body=body,
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
    body: FirewallRulesetLabelModify | Unset = UNSET,
) -> FirewallRulesetErrorResponse | FirewallRulesetLabelDetailResponse | None:
    """Modify firewall ruleset label

     Modifies existing label by given {ruleset-uuid} and {label-key}.

    Args:
        ruleset_uuid (UUID): The unique identifier for the server.
        label_key (str): The key of a label.
        body (FirewallRulesetLabelModify | Unset): Schema for modifying a label with a key-value
            pair.

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
        body=body,
    ).parsed


async def asyncio_detailed(
    ruleset_uuid: UUID,
    label_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: FirewallRulesetLabelModify | Unset = UNSET,
) -> Response[FirewallRulesetErrorResponse | FirewallRulesetLabelDetailResponse]:
    """Modify firewall ruleset label

     Modifies existing label by given {ruleset-uuid} and {label-key}.

    Args:
        ruleset_uuid (UUID): The unique identifier for the server.
        label_key (str): The key of a label.
        body (FirewallRulesetLabelModify | Unset): Schema for modifying a label with a key-value
            pair.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FirewallRulesetErrorResponse | FirewallRulesetLabelDetailResponse]
    """

    kwargs = _get_kwargs(
        ruleset_uuid=ruleset_uuid,
        label_key=label_key,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    ruleset_uuid: UUID,
    label_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: FirewallRulesetLabelModify | Unset = UNSET,
) -> FirewallRulesetErrorResponse | FirewallRulesetLabelDetailResponse | None:
    """Modify firewall ruleset label

     Modifies existing label by given {ruleset-uuid} and {label-key}.

    Args:
        ruleset_uuid (UUID): The unique identifier for the server.
        label_key (str): The key of a label.
        body (FirewallRulesetLabelModify | Unset): Schema for modifying a label with a key-value
            pair.

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
            body=body,
        )
    ).parsed
