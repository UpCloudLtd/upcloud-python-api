from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.gateway_plan_details_response import GatewayPlanDetailsResponse
from ...types import Response


def _get_kwargs(
    plan_name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/gateway/plans/{plan_name}".format(
            plan_name=quote(str(plan_name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GatewayPlanDetailsResponse | None:
    if response.status_code == 200:
        response_200 = GatewayPlanDetailsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GatewayPlanDetailsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    plan_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GatewayPlanDetailsResponse]:
    """Get Plan Details

     Get plan details.

    Args:
        plan_name (str): The name for the resource.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GatewayPlanDetailsResponse]
    """

    kwargs = _get_kwargs(
        plan_name=plan_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    plan_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> GatewayPlanDetailsResponse | None:
    """Get Plan Details

     Get plan details.

    Args:
        plan_name (str): The name for the resource.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GatewayPlanDetailsResponse
    """

    return sync_detailed(
        plan_name=plan_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    plan_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GatewayPlanDetailsResponse]:
    """Get Plan Details

     Get plan details.

    Args:
        plan_name (str): The name for the resource.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GatewayPlanDetailsResponse]
    """

    kwargs = _get_kwargs(
        plan_name=plan_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    plan_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> GatewayPlanDetailsResponse | None:
    """Get Plan Details

     Get plan details.

    Args:
        plan_name (str): The name for the resource.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GatewayPlanDetailsResponse
    """

    return (
        await asyncio_detailed(
            plan_name=plan_name,
            client=client,
        )
    ).parsed
