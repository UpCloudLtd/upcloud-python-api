from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.load_balancer_backend_metrics_series import LoadBalancerBackendMetricsSeries
from ...models.load_balancer_error_response import LoadBalancerErrorResponse
from ...models.load_balancer_metrics_sort_parameter import LoadBalancerMetricsSortParameter
from ...types import UNSET, Response, Unset


def _get_kwargs(
    service_uuid: UUID,
    *,
    sort: LoadBalancerMetricsSortParameter | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/load-balancer/{service_uuid}/metrics/series/backends".format(
            service_uuid=quote(str(service_uuid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> LoadBalancerErrorResponse | list[LoadBalancerBackendMetricsSeries]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemasload_balancer_backend_metrics_series_response_item_data in _response_200:
            componentsschemasload_balancer_backend_metrics_series_response_item = (
                LoadBalancerBackendMetricsSeries.from_dict(
                    componentsschemasload_balancer_backend_metrics_series_response_item_data
                )
            )

            response_200.append(componentsschemasload_balancer_backend_metrics_series_response_item)

        return response_200

    response_default = LoadBalancerErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[LoadBalancerErrorResponse | list[LoadBalancerBackendMetricsSeries]]:
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
    sort: LoadBalancerMetricsSortParameter | Unset = UNSET,
) -> Response[LoadBalancerErrorResponse | list[LoadBalancerBackendMetricsSeries]]:
    """Get load balancer backend combined metrics series

     Returns combined backend metric series by given {service-uuid}.

    Args:
        service_uuid (UUID): The UUID of the service.
        sort (LoadBalancerMetricsSortParameter | Unset): Sort metrics by field. Prefix with '-'
            for descending order.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LoadBalancerErrorResponse | list[LoadBalancerBackendMetricsSeries]]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        sort=sort,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    sort: LoadBalancerMetricsSortParameter | Unset = UNSET,
) -> LoadBalancerErrorResponse | list[LoadBalancerBackendMetricsSeries] | None:
    """Get load balancer backend combined metrics series

     Returns combined backend metric series by given {service-uuid}.

    Args:
        service_uuid (UUID): The UUID of the service.
        sort (LoadBalancerMetricsSortParameter | Unset): Sort metrics by field. Prefix with '-'
            for descending order.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LoadBalancerErrorResponse | list[LoadBalancerBackendMetricsSeries]
    """

    return sync_detailed(
        service_uuid=service_uuid,
        client=client,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    service_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    sort: LoadBalancerMetricsSortParameter | Unset = UNSET,
) -> Response[LoadBalancerErrorResponse | list[LoadBalancerBackendMetricsSeries]]:
    """Get load balancer backend combined metrics series

     Returns combined backend metric series by given {service-uuid}.

    Args:
        service_uuid (UUID): The UUID of the service.
        sort (LoadBalancerMetricsSortParameter | Unset): Sort metrics by field. Prefix with '-'
            for descending order.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LoadBalancerErrorResponse | list[LoadBalancerBackendMetricsSeries]]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    sort: LoadBalancerMetricsSortParameter | Unset = UNSET,
) -> LoadBalancerErrorResponse | list[LoadBalancerBackendMetricsSeries] | None:
    """Get load balancer backend combined metrics series

     Returns combined backend metric series by given {service-uuid}.

    Args:
        service_uuid (UUID): The UUID of the service.
        sort (LoadBalancerMetricsSortParameter | Unset): Sort metrics by field. Prefix with '-'
            for descending order.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LoadBalancerErrorResponse | list[LoadBalancerBackendMetricsSeries]
    """

    return (
        await asyncio_detailed(
            service_uuid=service_uuid,
            client=client,
            sort=sort,
        )
    ).parsed
