from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.load_balancer_error_response import LoadBalancerErrorResponse
from ...models.load_balancer_service import LoadBalancerService
from ...models.load_balancer_service_create import LoadBalancerServiceCreate
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: LoadBalancerServiceCreate | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/1.3/load-balancer",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> LoadBalancerErrorResponse | LoadBalancerService:
    if response.status_code == 201:
        response_201 = LoadBalancerService.from_dict(response.json())

        return response_201

    response_default = LoadBalancerErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[LoadBalancerErrorResponse | LoadBalancerService]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: LoadBalancerServiceCreate | Unset = UNSET,
) -> Response[LoadBalancerErrorResponse | LoadBalancerService]:
    """Create load balancer

     Creates a new load balancer service.

    Args:
        body (LoadBalancerServiceCreate | Unset): Load Balancer Service

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LoadBalancerErrorResponse | LoadBalancerService]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: LoadBalancerServiceCreate | Unset = UNSET,
) -> LoadBalancerErrorResponse | LoadBalancerService | None:
    """Create load balancer

     Creates a new load balancer service.

    Args:
        body (LoadBalancerServiceCreate | Unset): Load Balancer Service

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LoadBalancerErrorResponse | LoadBalancerService
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: LoadBalancerServiceCreate | Unset = UNSET,
) -> Response[LoadBalancerErrorResponse | LoadBalancerService]:
    """Create load balancer

     Creates a new load balancer service.

    Args:
        body (LoadBalancerServiceCreate | Unset): Load Balancer Service

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LoadBalancerErrorResponse | LoadBalancerService]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: LoadBalancerServiceCreate | Unset = UNSET,
) -> LoadBalancerErrorResponse | LoadBalancerService | None:
    """Create load balancer

     Creates a new load balancer service.

    Args:
        body (LoadBalancerServiceCreate | Unset): Load Balancer Service

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LoadBalancerErrorResponse | LoadBalancerService
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
