from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.load_balancer_error_response import LoadBalancerErrorResponse
from ...models.load_balancer_metrics import LoadBalancerMetrics
from ...types import Response


def _get_kwargs(
    service_uuid: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/load-balancer/{service_uuid}/metrics/series".format(
            service_uuid=quote(str(service_uuid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> LoadBalancerErrorResponse | list[LoadBalancerMetrics]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemasload_balancer_metrics_series_response_item_data in _response_200:
            componentsschemasload_balancer_metrics_series_response_item = LoadBalancerMetrics.from_dict(
                componentsschemasload_balancer_metrics_series_response_item_data
            )

            response_200.append(componentsschemasload_balancer_metrics_series_response_item)

        return response_200

    response_default = LoadBalancerErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[LoadBalancerErrorResponse | list[LoadBalancerMetrics]]:
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
) -> Response[LoadBalancerErrorResponse | list[LoadBalancerMetrics]]:
    """Get load balancer metrics series

     Returns service metric series by given {service-uuid}.

    Args:
        service_uuid (UUID): The UUID of the service.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LoadBalancerErrorResponse | list[LoadBalancerMetrics]]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> LoadBalancerErrorResponse | list[LoadBalancerMetrics] | None:
    """Get load balancer metrics series

     Returns service metric series by given {service-uuid}.

    Args:
        service_uuid (UUID): The UUID of the service.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LoadBalancerErrorResponse | list[LoadBalancerMetrics]
    """

    return sync_detailed(
        service_uuid=service_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    service_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[LoadBalancerErrorResponse | list[LoadBalancerMetrics]]:
    """Get load balancer metrics series

     Returns service metric series by given {service-uuid}.

    Args:
        service_uuid (UUID): The UUID of the service.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LoadBalancerErrorResponse | list[LoadBalancerMetrics]]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> LoadBalancerErrorResponse | list[LoadBalancerMetrics] | None:
    """Get load balancer metrics series

     Returns service metric series by given {service-uuid}.

    Args:
        service_uuid (UUID): The UUID of the service.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LoadBalancerErrorResponse | list[LoadBalancerMetrics]
    """

    return (
        await asyncio_detailed(
            service_uuid=service_uuid,
            client=client,
        )
    ).parsed
