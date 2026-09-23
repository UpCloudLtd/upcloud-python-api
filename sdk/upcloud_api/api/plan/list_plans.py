from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.plan import Plan
from ...models.plan_error import PlanError
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/plan",
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Plan | PlanError:
    if response.status_code == 200:
        response_200 = Plan.from_dict(response.json())

        return response_200

    response_default = PlanError.from_dict(response.json())

    return response_default


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Plan | PlanError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Plan | PlanError]:
    """List available plans

     Returns a list of available plans. All plans are available in all zones but pricing may differ. See
    _List prices_ for how to obtain current price list.

    In addition to listed plans, server can be freely configured with "custom" plan which allows freely
    scalable CPU cores, memory amount and storage resources. __Note!__ Custom plans are available for
    new customers through contact with sales.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Plan | PlanError]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> Plan | PlanError | None:
    """List available plans

     Returns a list of available plans. All plans are available in all zones but pricing may differ. See
    _List prices_ for how to obtain current price list.

    In addition to listed plans, server can be freely configured with "custom" plan which allows freely
    scalable CPU cores, memory amount and storage resources. __Note!__ Custom plans are available for
    new customers through contact with sales.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Plan | PlanError
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Plan | PlanError]:
    """List available plans

     Returns a list of available plans. All plans are available in all zones but pricing may differ. See
    _List prices_ for how to obtain current price list.

    In addition to listed plans, server can be freely configured with "custom" plan which allows freely
    scalable CPU cores, memory amount and storage resources. __Note!__ Custom plans are available for
    new customers through contact with sales.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Plan | PlanError]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> Plan | PlanError | None:
    """List available plans

     Returns a list of available plans. All plans are available in all zones but pricing may differ. See
    _List prices_ for how to obtain current price list.

    In addition to listed plans, server can be freely configured with "custom" plan which allows freely
    scalable CPU cores, memory amount and storage resources. __Note!__ Custom plans are available for
    new customers through contact with sales.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Plan | PlanError
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
