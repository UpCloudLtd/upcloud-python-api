from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.load_balancer_error_response import LoadBalancerErrorResponse
from ...models.load_balancer_frontend_metrics_series import LoadBalancerFrontendMetricsSeries
from ...models.load_balancer_metrics_sort_parameter import LoadBalancerMetricsSortParameter
from ...types import UNSET, Response, Unset


def _get_kwargs(
    service_uuid: UUID,
    frontend_name: str,
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
        "url": "/1.3/load-balancer/{service_uuid}/metrics/series/frontends/{frontend_name}".format(
            service_uuid=quote(str(service_uuid), safe=""),
            frontend_name=quote(str(frontend_name), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> LoadBalancerErrorResponse | list[LoadBalancerFrontendMetricsSeries]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemasload_balancer_frontend_metrics_series_response_item_data in _response_200:
            componentsschemasload_balancer_frontend_metrics_series_response_item = (
                LoadBalancerFrontendMetricsSeries.from_dict(
                    componentsschemasload_balancer_frontend_metrics_series_response_item_data
                )
            )

            response_200.append(componentsschemasload_balancer_frontend_metrics_series_response_item)

        return response_200

    response_default = LoadBalancerErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[LoadBalancerErrorResponse | list[LoadBalancerFrontendMetricsSeries]]:
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
    sort: LoadBalancerMetricsSortParameter | Unset = UNSET,
) -> Response[LoadBalancerErrorResponse | list[LoadBalancerFrontendMetricsSeries]]:
    """Get load balancer frontend metrics series

     Returns frontend metric series by given {service-uuid} and {frontend-name}.

    Args:
        service_uuid (UUID): The UUID of the service.
        frontend_name (str): The name of the frontend.
        sort (LoadBalancerMetricsSortParameter | Unset): Sort metrics by field. Prefix with '-'
            for descending order.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LoadBalancerErrorResponse | list[LoadBalancerFrontendMetricsSeries]]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        frontend_name=frontend_name,
        sort=sort,
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
    sort: LoadBalancerMetricsSortParameter | Unset = UNSET,
) -> LoadBalancerErrorResponse | list[LoadBalancerFrontendMetricsSeries] | None:
    """Get load balancer frontend metrics series

     Returns frontend metric series by given {service-uuid} and {frontend-name}.

    Args:
        service_uuid (UUID): The UUID of the service.
        frontend_name (str): The name of the frontend.
        sort (LoadBalancerMetricsSortParameter | Unset): Sort metrics by field. Prefix with '-'
            for descending order.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LoadBalancerErrorResponse | list[LoadBalancerFrontendMetricsSeries]
    """

    return sync_detailed(
        service_uuid=service_uuid,
        frontend_name=frontend_name,
        client=client,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    service_uuid: UUID,
    frontend_name: str,
    *,
    client: AuthenticatedClient | Client,
    sort: LoadBalancerMetricsSortParameter | Unset = UNSET,
) -> Response[LoadBalancerErrorResponse | list[LoadBalancerFrontendMetricsSeries]]:
    """Get load balancer frontend metrics series

     Returns frontend metric series by given {service-uuid} and {frontend-name}.

    Args:
        service_uuid (UUID): The UUID of the service.
        frontend_name (str): The name of the frontend.
        sort (LoadBalancerMetricsSortParameter | Unset): Sort metrics by field. Prefix with '-'
            for descending order.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LoadBalancerErrorResponse | list[LoadBalancerFrontendMetricsSeries]]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        frontend_name=frontend_name,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_uuid: UUID,
    frontend_name: str,
    *,
    client: AuthenticatedClient | Client,
    sort: LoadBalancerMetricsSortParameter | Unset = UNSET,
) -> LoadBalancerErrorResponse | list[LoadBalancerFrontendMetricsSeries] | None:
    """Get load balancer frontend metrics series

     Returns frontend metric series by given {service-uuid} and {frontend-name}.

    Args:
        service_uuid (UUID): The UUID of the service.
        frontend_name (str): The name of the frontend.
        sort (LoadBalancerMetricsSortParameter | Unset): Sort metrics by field. Prefix with '-'
            for descending order.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LoadBalancerErrorResponse | list[LoadBalancerFrontendMetricsSeries]
    """

    return (
        await asyncio_detailed(
            service_uuid=service_uuid,
            frontend_name=frontend_name,
            client=client,
            sort=sort,
        )
    ).parsed
