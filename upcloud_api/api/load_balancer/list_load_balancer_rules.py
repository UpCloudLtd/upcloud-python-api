from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.load_balancer_error_response import LoadBalancerErrorResponse
from ...models.load_balancer_rule import LoadBalancerRule
from ...types import Response


def _get_kwargs(
    service_uuid: UUID,
    frontend_name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/load-balancer/{service_uuid}/frontends/{frontend_name}/rules".format(
            service_uuid=quote(str(service_uuid), safe=""),
            frontend_name=quote(str(frontend_name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> LoadBalancerErrorResponse | list[LoadBalancerRule]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemasload_balancer_rules_response_item_data in _response_200:
            componentsschemasload_balancer_rules_response_item = LoadBalancerRule.from_dict(
                componentsschemasload_balancer_rules_response_item_data
            )

            response_200.append(componentsschemasload_balancer_rules_response_item)

        return response_200

    response_default = LoadBalancerErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[LoadBalancerErrorResponse | list[LoadBalancerRule]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    service_uuid: UUID,
    frontend_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[LoadBalancerErrorResponse | list[LoadBalancerRule]]:
    """List load balancer rules

     Returns a list of available frontend rules by given {service-uuid} and {frontend-name}.

    Args:
        service_uuid (UUID): The UUID of the service.
        frontend_name (str): The name of the frontend.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LoadBalancerErrorResponse | list[LoadBalancerRule]]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        frontend_name=frontend_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_uuid: UUID,
    frontend_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> LoadBalancerErrorResponse | list[LoadBalancerRule] | None:
    """List load balancer rules

     Returns a list of available frontend rules by given {service-uuid} and {frontend-name}.

    Args:
        service_uuid (UUID): The UUID of the service.
        frontend_name (str): The name of the frontend.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LoadBalancerErrorResponse | list[LoadBalancerRule]
    """

    return sync_detailed(
        service_uuid=service_uuid,
        frontend_name=frontend_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    service_uuid: UUID,
    frontend_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[LoadBalancerErrorResponse | list[LoadBalancerRule]]:
    """List load balancer rules

     Returns a list of available frontend rules by given {service-uuid} and {frontend-name}.

    Args:
        service_uuid (UUID): The UUID of the service.
        frontend_name (str): The name of the frontend.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LoadBalancerErrorResponse | list[LoadBalancerRule]]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        frontend_name=frontend_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_uuid: UUID,
    frontend_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> LoadBalancerErrorResponse | list[LoadBalancerRule] | None:
    """List load balancer rules

     Returns a list of available frontend rules by given {service-uuid} and {frontend-name}.

    Args:
        service_uuid (UUID): The UUID of the service.
        frontend_name (str): The name of the frontend.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LoadBalancerErrorResponse | list[LoadBalancerRule]
    """

    return (
        await asyncio_detailed(
            service_uuid=service_uuid,
            frontend_name=frontend_name,
            client=client,
        )
    ).parsed
