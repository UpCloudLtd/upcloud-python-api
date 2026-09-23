from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.gateway_tunnel_details_response import GatewayTunnelDetailsResponse
from ...models.gateway_tunnel_modify_request import GatewayTunnelModifyRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    service_uuid: UUID,
    connection_uuid: UUID,
    tunnel_uuid: UUID,
    *,
    body: GatewayTunnelModifyRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/1.3/gateway/{service_uuid}/connections/{connection_uuid}/tunnels/{tunnel_uuid}".format(
            service_uuid=quote(str(service_uuid), safe=""),
            connection_uuid=quote(str(connection_uuid), safe=""),
            tunnel_uuid=quote(str(tunnel_uuid), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GatewayTunnelDetailsResponse | None:
    if response.status_code == 200:
        response_200 = GatewayTunnelDetailsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GatewayTunnelDetailsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    service_uuid: UUID,
    connection_uuid: UUID,
    tunnel_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: GatewayTunnelModifyRequest | Unset = UNSET,
) -> Response[GatewayTunnelDetailsResponse]:
    """Modify Tunnel

     Modify tunnel configuration.

    Args:
        service_uuid (UUID): The unique identifier for the resource.
        connection_uuid (UUID): The unique identifier for the resource.
        tunnel_uuid (UUID): The unique identifier for the resource.
        body (GatewayTunnelModifyRequest | Unset): Request to modify a VPN tunnel

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GatewayTunnelDetailsResponse]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        connection_uuid=connection_uuid,
        tunnel_uuid=tunnel_uuid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_uuid: UUID,
    connection_uuid: UUID,
    tunnel_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: GatewayTunnelModifyRequest | Unset = UNSET,
) -> GatewayTunnelDetailsResponse | None:
    """Modify Tunnel

     Modify tunnel configuration.

    Args:
        service_uuid (UUID): The unique identifier for the resource.
        connection_uuid (UUID): The unique identifier for the resource.
        tunnel_uuid (UUID): The unique identifier for the resource.
        body (GatewayTunnelModifyRequest | Unset): Request to modify a VPN tunnel

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GatewayTunnelDetailsResponse
    """

    return sync_detailed(
        service_uuid=service_uuid,
        connection_uuid=connection_uuid,
        tunnel_uuid=tunnel_uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    service_uuid: UUID,
    connection_uuid: UUID,
    tunnel_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: GatewayTunnelModifyRequest | Unset = UNSET,
) -> Response[GatewayTunnelDetailsResponse]:
    """Modify Tunnel

     Modify tunnel configuration.

    Args:
        service_uuid (UUID): The unique identifier for the resource.
        connection_uuid (UUID): The unique identifier for the resource.
        tunnel_uuid (UUID): The unique identifier for the resource.
        body (GatewayTunnelModifyRequest | Unset): Request to modify a VPN tunnel

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GatewayTunnelDetailsResponse]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        connection_uuid=connection_uuid,
        tunnel_uuid=tunnel_uuid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_uuid: UUID,
    connection_uuid: UUID,
    tunnel_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: GatewayTunnelModifyRequest | Unset = UNSET,
) -> GatewayTunnelDetailsResponse | None:
    """Modify Tunnel

     Modify tunnel configuration.

    Args:
        service_uuid (UUID): The unique identifier for the resource.
        connection_uuid (UUID): The unique identifier for the resource.
        tunnel_uuid (UUID): The unique identifier for the resource.
        body (GatewayTunnelModifyRequest | Unset): Request to modify a VPN tunnel

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GatewayTunnelDetailsResponse
    """

    return (
        await asyncio_detailed(
            service_uuid=service_uuid,
            connection_uuid=connection_uuid,
            tunnel_uuid=tunnel_uuid,
            client=client,
            body=body,
        )
    ).parsed
