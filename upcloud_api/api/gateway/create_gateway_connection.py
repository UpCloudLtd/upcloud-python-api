from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.gateway_connection_create_request import GatewayConnectionCreateRequest
from ...models.gateway_connection_details_response import GatewayConnectionDetailsResponse
from ...models.gateway_error_response import GatewayErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    service_uuid: UUID,
    *,
    body: GatewayConnectionCreateRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/1.3/gateway/{service_uuid}/connections".format(
            service_uuid=quote(str(service_uuid), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GatewayConnectionDetailsResponse | GatewayErrorResponse:
    if response.status_code == 200:
        response_200 = GatewayConnectionDetailsResponse.from_dict(response.json())

        return response_200

    response_default = GatewayErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GatewayConnectionDetailsResponse | GatewayErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    service_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: GatewayConnectionCreateRequest | Unset = UNSET,
) -> Response[GatewayConnectionDetailsResponse | GatewayErrorResponse]:
    """Create Connection

     Create a new connection.

    Args:
        service_uuid (UUID): The unique identifier for the resource.
        body (GatewayConnectionCreateRequest | Unset): Network gateway VPN connection

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GatewayConnectionDetailsResponse | GatewayErrorResponse]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: GatewayConnectionCreateRequest | Unset = UNSET,
) -> GatewayConnectionDetailsResponse | GatewayErrorResponse | None:
    """Create Connection

     Create a new connection.

    Args:
        service_uuid (UUID): The unique identifier for the resource.
        body (GatewayConnectionCreateRequest | Unset): Network gateway VPN connection

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GatewayConnectionDetailsResponse | GatewayErrorResponse
    """

    return sync_detailed(
        service_uuid=service_uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    service_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: GatewayConnectionCreateRequest | Unset = UNSET,
) -> Response[GatewayConnectionDetailsResponse | GatewayErrorResponse]:
    """Create Connection

     Create a new connection.

    Args:
        service_uuid (UUID): The unique identifier for the resource.
        body (GatewayConnectionCreateRequest | Unset): Network gateway VPN connection

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GatewayConnectionDetailsResponse | GatewayErrorResponse]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: GatewayConnectionCreateRequest | Unset = UNSET,
) -> GatewayConnectionDetailsResponse | GatewayErrorResponse | None:
    """Create Connection

     Create a new connection.

    Args:
        service_uuid (UUID): The unique identifier for the resource.
        body (GatewayConnectionCreateRequest | Unset): Network gateway VPN connection

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GatewayConnectionDetailsResponse | GatewayErrorResponse
    """

    return (
        await asyncio_detailed(
            service_uuid=service_uuid,
            client=client,
            body=body,
        )
    ).parsed
