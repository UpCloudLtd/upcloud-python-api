from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.gateway_service_create_request import GatewayServiceCreateRequest
from ...models.gateway_service_details_response import GatewayServiceDetailsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: GatewayServiceCreateRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/1.3/gateway",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GatewayServiceDetailsResponse | None:
    if response.status_code == 200:
        response_200 = GatewayServiceDetailsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GatewayServiceDetailsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GatewayServiceCreateRequest | Unset = UNSET,
) -> Response[GatewayServiceDetailsResponse]:
    """Create Service

     Create a new service.

    Args:
        body (GatewayServiceCreateRequest | Unset): Gateway service

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GatewayServiceDetailsResponse]
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
    body: GatewayServiceCreateRequest | Unset = UNSET,
) -> GatewayServiceDetailsResponse | None:
    """Create Service

     Create a new service.

    Args:
        body (GatewayServiceCreateRequest | Unset): Gateway service

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GatewayServiceDetailsResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GatewayServiceCreateRequest | Unset = UNSET,
) -> Response[GatewayServiceDetailsResponse]:
    """Create Service

     Create a new service.

    Args:
        body (GatewayServiceCreateRequest | Unset): Gateway service

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GatewayServiceDetailsResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: GatewayServiceCreateRequest | Unset = UNSET,
) -> GatewayServiceDetailsResponse | None:
    """Create Service

     Create a new service.

    Args:
        body (GatewayServiceCreateRequest | Unset): Gateway service

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GatewayServiceDetailsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
