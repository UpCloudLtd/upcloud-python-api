from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.gateway_error_response import GatewayErrorResponse
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
) -> GatewayErrorResponse | GatewayPlanDetailsResponse:
    if response.status_code == 200:
        response_200 = GatewayPlanDetailsResponse.from_dict(response.json())

        return response_200

    response_default = GatewayErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GatewayErrorResponse | GatewayPlanDetailsResponse]:
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
) -> Response[GatewayErrorResponse | GatewayPlanDetailsResponse]:
    """Get Plan Details

     Get plan details.

    Args:
        plan_name (str): The name for the resource.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GatewayErrorResponse | GatewayPlanDetailsResponse]
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
) -> GatewayErrorResponse | GatewayPlanDetailsResponse | None:
    """Get Plan Details

     Get plan details.

    Args:
        plan_name (str): The name for the resource.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GatewayErrorResponse | GatewayPlanDetailsResponse
    """

    return sync_detailed(
        plan_name=plan_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    plan_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GatewayErrorResponse | GatewayPlanDetailsResponse]:
    """Get Plan Details

     Get plan details.

    Args:
        plan_name (str): The name for the resource.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GatewayErrorResponse | GatewayPlanDetailsResponse]
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
) -> GatewayErrorResponse | GatewayPlanDetailsResponse | None:
    """Get Plan Details

     Get plan details.

    Args:
        plan_name (str): The name for the resource.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GatewayErrorResponse | GatewayPlanDetailsResponse
    """

    return (
        await asyncio_detailed(
            plan_name=plan_name,
            client=client,
        )
    ).parsed
