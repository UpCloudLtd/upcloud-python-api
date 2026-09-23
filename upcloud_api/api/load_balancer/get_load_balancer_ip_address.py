from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.load_balancer_error_response import LoadBalancerErrorResponse
from ...models.load_balancer_ip_address import LoadBalancerIpAddress
from ...types import Response


def _get_kwargs(
    service_uuid: UUID,
    ip_address: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/load-balancer/{service_uuid}/ip-addresses/{ip_address}".format(
            service_uuid=quote(str(service_uuid), safe=""),
            ip_address=quote(str(ip_address), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> LoadBalancerErrorResponse | list[LoadBalancerIpAddress]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemasload_balancer_ip_addresses_response_item_data in _response_200:
            componentsschemasload_balancer_ip_addresses_response_item = LoadBalancerIpAddress.from_dict(
                componentsschemasload_balancer_ip_addresses_response_item_data
            )

            response_200.append(componentsschemasload_balancer_ip_addresses_response_item)

        return response_200

    response_default = LoadBalancerErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[LoadBalancerErrorResponse | list[LoadBalancerIpAddress]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    service_uuid: UUID,
    ip_address: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[LoadBalancerErrorResponse | list[LoadBalancerIpAddress]]:
    """Get load balancer IP address

     Returns IP address details by given {service-uuid} and {ip-address}.

    Args:
        service_uuid (UUID): The UUID of the service.
        ip_address (str): The IP address parameter.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LoadBalancerErrorResponse | list[LoadBalancerIpAddress]]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        ip_address=ip_address,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_uuid: UUID,
    ip_address: str,
    *,
    client: AuthenticatedClient | Client,
) -> LoadBalancerErrorResponse | list[LoadBalancerIpAddress] | None:
    """Get load balancer IP address

     Returns IP address details by given {service-uuid} and {ip-address}.

    Args:
        service_uuid (UUID): The UUID of the service.
        ip_address (str): The IP address parameter.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LoadBalancerErrorResponse | list[LoadBalancerIpAddress]
    """

    return sync_detailed(
        service_uuid=service_uuid,
        ip_address=ip_address,
        client=client,
    ).parsed


async def asyncio_detailed(
    service_uuid: UUID,
    ip_address: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[LoadBalancerErrorResponse | list[LoadBalancerIpAddress]]:
    """Get load balancer IP address

     Returns IP address details by given {service-uuid} and {ip-address}.

    Args:
        service_uuid (UUID): The UUID of the service.
        ip_address (str): The IP address parameter.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LoadBalancerErrorResponse | list[LoadBalancerIpAddress]]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        ip_address=ip_address,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_uuid: UUID,
    ip_address: str,
    *,
    client: AuthenticatedClient | Client,
) -> LoadBalancerErrorResponse | list[LoadBalancerIpAddress] | None:
    """Get load balancer IP address

     Returns IP address details by given {service-uuid} and {ip-address}.

    Args:
        service_uuid (UUID): The UUID of the service.
        ip_address (str): The IP address parameter.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LoadBalancerErrorResponse | list[LoadBalancerIpAddress]
    """

    return (
        await asyncio_detailed(
            service_uuid=service_uuid,
            ip_address=ip_address,
            client=client,
        )
    ).parsed
