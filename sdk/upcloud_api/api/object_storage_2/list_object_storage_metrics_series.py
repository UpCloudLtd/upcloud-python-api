import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.object_storage_2_error_response import ObjectStorage2ErrorResponse
from ...models.object_storage_2_metrics_series_list_response_item import ObjectStorage2MetricsSeriesListResponseItem
from ...models.object_storage_2_query_param_sort import ObjectStorage2QueryParamSort
from ...types import UNSET, Response, Unset


def _get_kwargs(
    service_uuid: UUID,
    *,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    interval: str | Unset = UNSET,
    sort: ObjectStorage2QueryParamSort | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_from_: str | Unset = UNSET
    if not isinstance(from_, Unset):
        json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to: str | Unset = UNSET
    if not isinstance(to, Unset):
        json_to = to.isoformat()
    params["to"] = json_to

    params["interval"] = interval

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/object-storage-2/{service_uuid}/metrics/series".format(
            service_uuid=quote(str(service_uuid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ObjectStorage2ErrorResponse | list[ObjectStorage2MetricsSeriesListResponseItem]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemasobject_storage_2_metrics_series_list_response_item_data in _response_200:
            componentsschemasobject_storage_2_metrics_series_list_response_item = (
                ObjectStorage2MetricsSeriesListResponseItem.from_dict(
                    componentsschemasobject_storage_2_metrics_series_list_response_item_data
                )
            )

            response_200.append(componentsschemasobject_storage_2_metrics_series_list_response_item)

        return response_200

    response_default = ObjectStorage2ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ObjectStorage2ErrorResponse | list[ObjectStorage2MetricsSeriesListResponseItem]]:
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
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    interval: str | Unset = UNSET,
    sort: ObjectStorage2QueryParamSort | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[ObjectStorage2ErrorResponse | list[ObjectStorage2MetricsSeriesListResponseItem]]:
    """List service metrics series

     Returns Object Storage instance metrics series by a given {service_uuid}.

    Args:
        service_uuid (UUID): The unique identifier for the service.
        from_ (datetime.datetime | Unset): Schema for a query parameter specifying a timestamp.
            Example: 2024-01-01T00:00:00Z.
        to (datetime.datetime | Unset): Schema for a query parameter specifying a timestamp.
            Example: 2024-01-01T00:00:00Z.
        interval (str | Unset): Schema for a query parameter specifying the time interval.
        sort (ObjectStorage2QueryParamSort | Unset): Schema for a query parameter specifying the
            sort field and direction. Prefix with '-' for descending order.
        limit (int | Unset): Schema for a query parameter specifying the maximum number of entries
            to return (limit).
        offset (int | Unset): Schema for a query parameter specifying the offset for pagination.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ObjectStorage2ErrorResponse | list[ObjectStorage2MetricsSeriesListResponseItem]]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        from_=from_,
        to=to,
        interval=interval,
        sort=sort,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    interval: str | Unset = UNSET,
    sort: ObjectStorage2QueryParamSort | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> ObjectStorage2ErrorResponse | list[ObjectStorage2MetricsSeriesListResponseItem] | None:
    """List service metrics series

     Returns Object Storage instance metrics series by a given {service_uuid}.

    Args:
        service_uuid (UUID): The unique identifier for the service.
        from_ (datetime.datetime | Unset): Schema for a query parameter specifying a timestamp.
            Example: 2024-01-01T00:00:00Z.
        to (datetime.datetime | Unset): Schema for a query parameter specifying a timestamp.
            Example: 2024-01-01T00:00:00Z.
        interval (str | Unset): Schema for a query parameter specifying the time interval.
        sort (ObjectStorage2QueryParamSort | Unset): Schema for a query parameter specifying the
            sort field and direction. Prefix with '-' for descending order.
        limit (int | Unset): Schema for a query parameter specifying the maximum number of entries
            to return (limit).
        offset (int | Unset): Schema for a query parameter specifying the offset for pagination.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ObjectStorage2ErrorResponse | list[ObjectStorage2MetricsSeriesListResponseItem]
    """

    return sync_detailed(
        service_uuid=service_uuid,
        client=client,
        from_=from_,
        to=to,
        interval=interval,
        sort=sort,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    service_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    interval: str | Unset = UNSET,
    sort: ObjectStorage2QueryParamSort | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[ObjectStorage2ErrorResponse | list[ObjectStorage2MetricsSeriesListResponseItem]]:
    """List service metrics series

     Returns Object Storage instance metrics series by a given {service_uuid}.

    Args:
        service_uuid (UUID): The unique identifier for the service.
        from_ (datetime.datetime | Unset): Schema for a query parameter specifying a timestamp.
            Example: 2024-01-01T00:00:00Z.
        to (datetime.datetime | Unset): Schema for a query parameter specifying a timestamp.
            Example: 2024-01-01T00:00:00Z.
        interval (str | Unset): Schema for a query parameter specifying the time interval.
        sort (ObjectStorage2QueryParamSort | Unset): Schema for a query parameter specifying the
            sort field and direction. Prefix with '-' for descending order.
        limit (int | Unset): Schema for a query parameter specifying the maximum number of entries
            to return (limit).
        offset (int | Unset): Schema for a query parameter specifying the offset for pagination.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ObjectStorage2ErrorResponse | list[ObjectStorage2MetricsSeriesListResponseItem]]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        from_=from_,
        to=to,
        interval=interval,
        sort=sort,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    interval: str | Unset = UNSET,
    sort: ObjectStorage2QueryParamSort | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> ObjectStorage2ErrorResponse | list[ObjectStorage2MetricsSeriesListResponseItem] | None:
    """List service metrics series

     Returns Object Storage instance metrics series by a given {service_uuid}.

    Args:
        service_uuid (UUID): The unique identifier for the service.
        from_ (datetime.datetime | Unset): Schema for a query parameter specifying a timestamp.
            Example: 2024-01-01T00:00:00Z.
        to (datetime.datetime | Unset): Schema for a query parameter specifying a timestamp.
            Example: 2024-01-01T00:00:00Z.
        interval (str | Unset): Schema for a query parameter specifying the time interval.
        sort (ObjectStorage2QueryParamSort | Unset): Schema for a query parameter specifying the
            sort field and direction. Prefix with '-' for descending order.
        limit (int | Unset): Schema for a query parameter specifying the maximum number of entries
            to return (limit).
        offset (int | Unset): Schema for a query parameter specifying the offset for pagination.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ObjectStorage2ErrorResponse | list[ObjectStorage2MetricsSeriesListResponseItem]
    """

    return (
        await asyncio_detailed(
            service_uuid=service_uuid,
            client=client,
            from_=from_,
            to=to,
            interval=interval,
            sort=sort,
            limit=limit,
            offset=offset,
        )
    ).parsed
