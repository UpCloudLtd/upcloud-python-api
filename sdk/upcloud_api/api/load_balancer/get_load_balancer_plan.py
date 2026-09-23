from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.load_balancer_error_response import LoadBalancerErrorResponse
from ...models.load_balancer_plan import LoadBalancerPlan
from ...types import Response


def _get_kwargs(
    plan_name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/load-balancer/plans/{plan_name}".format(
            plan_name=quote(str(plan_name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> LoadBalancerErrorResponse | LoadBalancerPlan:
    if response.status_code == 200:
        response_200 = LoadBalancerPlan.from_dict(response.json())

        return response_200

    response_default = LoadBalancerErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[LoadBalancerErrorResponse | LoadBalancerPlan]:
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
) -> Response[LoadBalancerErrorResponse | LoadBalancerPlan]:
    """Get load balancer plan

     Returns load balancer plan details by given {plan-name}.

    Args:
        plan_name (str): The name of the plan.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LoadBalancerErrorResponse | LoadBalancerPlan]
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
) -> LoadBalancerErrorResponse | LoadBalancerPlan | None:
    """Get load balancer plan

     Returns load balancer plan details by given {plan-name}.

    Args:
        plan_name (str): The name of the plan.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LoadBalancerErrorResponse | LoadBalancerPlan
    """

    return sync_detailed(
        plan_name=plan_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    plan_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[LoadBalancerErrorResponse | LoadBalancerPlan]:
    """Get load balancer plan

     Returns load balancer plan details by given {plan-name}.

    Args:
        plan_name (str): The name of the plan.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LoadBalancerErrorResponse | LoadBalancerPlan]
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
) -> LoadBalancerErrorResponse | LoadBalancerPlan | None:
    """Get load balancer plan

     Returns load balancer plan details by given {plan-name}.

    Args:
        plan_name (str): The name of the plan.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LoadBalancerErrorResponse | LoadBalancerPlan
    """

    return (
        await asyncio_detailed(
            plan_name=plan_name,
            client=client,
        )
    ).parsed
