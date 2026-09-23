from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.load_balancer_error_response import LoadBalancerErrorResponse
from ...models.load_balancer_ip_address import LoadBalancerIpAddress
from ...models.load_balancer_ip_address_create import LoadBalancerIpAddressCreate
from ...types import UNSET, Response, Unset


def _get_kwargs(
    service_uuid: UUID,
    *,
    body: LoadBalancerIpAddressCreate | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/1.3/load-balancer/{service_uuid}/ip-addresses".format(
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
) -> LoadBalancerErrorResponse | LoadBalancerIpAddress:
    if response.status_code == 201:
        response_201 = LoadBalancerIpAddress.from_dict(response.json())

        return response_201

    response_default = LoadBalancerErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[LoadBalancerErrorResponse | LoadBalancerIpAddress]:
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
    body: LoadBalancerIpAddressCreate | Unset = UNSET,
) -> Response[LoadBalancerErrorResponse | LoadBalancerIpAddress]:
    """Create load balancer IP address

     Attach a floating public IPv4 address to the service using the specified {service-uuid}. The number
    of attachable floating IPv4 addresses is limited to the number of nodes in the plan, and all
    addresses must be in the same zone as the service and detached.

    Note: Floating public IPv4 addresses have configurable release policies. When the service is deleted
    or an IP address is detached, addresses with the keep policy will be converted to detached floating
    IPs that remain available in your account. Addresses with the release policy will be automatically
    deleted. For more details, see IP Addresses.

    Args:
        service_uuid (UUID): The UUID of the service.
        body (LoadBalancerIpAddressCreate | Unset): IP address object Example: {'address':
            '192.168.1.10', 'network_name': 'private-net-1'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LoadBalancerErrorResponse | LoadBalancerIpAddress]
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
    body: LoadBalancerIpAddressCreate | Unset = UNSET,
) -> LoadBalancerErrorResponse | LoadBalancerIpAddress | None:
    """Create load balancer IP address

     Attach a floating public IPv4 address to the service using the specified {service-uuid}. The number
    of attachable floating IPv4 addresses is limited to the number of nodes in the plan, and all
    addresses must be in the same zone as the service and detached.

    Note: Floating public IPv4 addresses have configurable release policies. When the service is deleted
    or an IP address is detached, addresses with the keep policy will be converted to detached floating
    IPs that remain available in your account. Addresses with the release policy will be automatically
    deleted. For more details, see IP Addresses.

    Args:
        service_uuid (UUID): The UUID of the service.
        body (LoadBalancerIpAddressCreate | Unset): IP address object Example: {'address':
            '192.168.1.10', 'network_name': 'private-net-1'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LoadBalancerErrorResponse | LoadBalancerIpAddress
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
    body: LoadBalancerIpAddressCreate | Unset = UNSET,
) -> Response[LoadBalancerErrorResponse | LoadBalancerIpAddress]:
    """Create load balancer IP address

     Attach a floating public IPv4 address to the service using the specified {service-uuid}. The number
    of attachable floating IPv4 addresses is limited to the number of nodes in the plan, and all
    addresses must be in the same zone as the service and detached.

    Note: Floating public IPv4 addresses have configurable release policies. When the service is deleted
    or an IP address is detached, addresses with the keep policy will be converted to detached floating
    IPs that remain available in your account. Addresses with the release policy will be automatically
    deleted. For more details, see IP Addresses.

    Args:
        service_uuid (UUID): The UUID of the service.
        body (LoadBalancerIpAddressCreate | Unset): IP address object Example: {'address':
            '192.168.1.10', 'network_name': 'private-net-1'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LoadBalancerErrorResponse | LoadBalancerIpAddress]
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
    body: LoadBalancerIpAddressCreate | Unset = UNSET,
) -> LoadBalancerErrorResponse | LoadBalancerIpAddress | None:
    """Create load balancer IP address

     Attach a floating public IPv4 address to the service using the specified {service-uuid}. The number
    of attachable floating IPv4 addresses is limited to the number of nodes in the plan, and all
    addresses must be in the same zone as the service and detached.

    Note: Floating public IPv4 addresses have configurable release policies. When the service is deleted
    or an IP address is detached, addresses with the keep policy will be converted to detached floating
    IPs that remain available in your account. Addresses with the release policy will be automatically
    deleted. For more details, see IP Addresses.

    Args:
        service_uuid (UUID): The UUID of the service.
        body (LoadBalancerIpAddressCreate | Unset): IP address object Example: {'address':
            '192.168.1.10', 'network_name': 'private-net-1'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LoadBalancerErrorResponse | LoadBalancerIpAddress
    """

    return (
        await asyncio_detailed(
            service_uuid=service_uuid,
            client=client,
            body=body,
        )
    ).parsed
