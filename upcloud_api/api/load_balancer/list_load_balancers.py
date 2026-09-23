from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.load_balancer_error_response import LoadBalancerErrorResponse
from ...models.load_balancer_service import LoadBalancerService
from ...models.load_balancer_sort_services_parameter import LoadBalancerSortServicesParameter
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    sort: LoadBalancerSortServicesParameter | Unset = UNSET,
    label: list[str] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    json_label: list[str] | Unset = UNSET
    if not isinstance(label, Unset):
        json_label = label

    params["label"] = json_label

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/load-balancer",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> LoadBalancerErrorResponse | list[LoadBalancerService]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemasload_balancer_services_response_item_data in _response_200:
            componentsschemasload_balancer_services_response_item = LoadBalancerService.from_dict(
                componentsschemasload_balancer_services_response_item_data
            )

            response_200.append(componentsschemasload_balancer_services_response_item)

        return response_200

    response_default = LoadBalancerErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[LoadBalancerErrorResponse | list[LoadBalancerService]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    sort: LoadBalancerSortServicesParameter | Unset = UNSET,
    label: list[str] | Unset = UNSET,
) -> Response[LoadBalancerErrorResponse | list[LoadBalancerService]]:
    """List load balancers

     Returns a list of available load balancer services.

    Args:
        limit (int | Unset): Number of entries to receive at most.
        offset (int | Unset): Offset for retrieved results.
        sort (LoadBalancerSortServicesParameter | Unset): Sort services by field. Prefix with '-'
            for descending order.
        label (list[str] | Unset): Filter resources by label. Can be provided multiple times for
            multiple labels. Format: 'key=value' for exact match or 'key' for existence check.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LoadBalancerErrorResponse | list[LoadBalancerService]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        sort=sort,
        label=label,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    sort: LoadBalancerSortServicesParameter | Unset = UNSET,
    label: list[str] | Unset = UNSET,
) -> LoadBalancerErrorResponse | list[LoadBalancerService] | None:
    """List load balancers

     Returns a list of available load balancer services.

    Args:
        limit (int | Unset): Number of entries to receive at most.
        offset (int | Unset): Offset for retrieved results.
        sort (LoadBalancerSortServicesParameter | Unset): Sort services by field. Prefix with '-'
            for descending order.
        label (list[str] | Unset): Filter resources by label. Can be provided multiple times for
            multiple labels. Format: 'key=value' for exact match or 'key' for existence check.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LoadBalancerErrorResponse | list[LoadBalancerService]
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        sort=sort,
        label=label,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    sort: LoadBalancerSortServicesParameter | Unset = UNSET,
    label: list[str] | Unset = UNSET,
) -> Response[LoadBalancerErrorResponse | list[LoadBalancerService]]:
    """List load balancers

     Returns a list of available load balancer services.

    Args:
        limit (int | Unset): Number of entries to receive at most.
        offset (int | Unset): Offset for retrieved results.
        sort (LoadBalancerSortServicesParameter | Unset): Sort services by field. Prefix with '-'
            for descending order.
        label (list[str] | Unset): Filter resources by label. Can be provided multiple times for
            multiple labels. Format: 'key=value' for exact match or 'key' for existence check.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LoadBalancerErrorResponse | list[LoadBalancerService]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        sort=sort,
        label=label,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    sort: LoadBalancerSortServicesParameter | Unset = UNSET,
    label: list[str] | Unset = UNSET,
) -> LoadBalancerErrorResponse | list[LoadBalancerService] | None:
    """List load balancers

     Returns a list of available load balancer services.

    Args:
        limit (int | Unset): Number of entries to receive at most.
        offset (int | Unset): Offset for retrieved results.
        sort (LoadBalancerSortServicesParameter | Unset): Sort services by field. Prefix with '-'
            for descending order.
        label (list[str] | Unset): Filter resources by label. Can be provided multiple times for
            multiple labels. Format: 'key=value' for exact match or 'key' for existence check.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LoadBalancerErrorResponse | list[LoadBalancerService]
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            sort=sort,
            label=label,
        )
    ).parsed
