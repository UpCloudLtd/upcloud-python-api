from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.file_storage_error_response import FileStorageErrorResponse
from ...models.file_storage_query_param_sort import FileStorageQueryParamSort
from ...models.file_storage_service_detail_response import FileStorageServiceDetailResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    sort: FileStorageQueryParamSort | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/file-storage",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FileStorageErrorResponse | list[FileStorageServiceDetailResponse]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemasfile_storage_service_list_response_item_data in _response_200:
            componentsschemasfile_storage_service_list_response_item = FileStorageServiceDetailResponse.from_dict(
                componentsschemasfile_storage_service_list_response_item_data
            )

            response_200.append(componentsschemasfile_storage_service_list_response_item)

        return response_200

    response_default = FileStorageErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[FileStorageErrorResponse | list[FileStorageServiceDetailResponse]]:
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
    sort: FileStorageQueryParamSort | Unset = UNSET,
) -> Response[FileStorageErrorResponse | list[FileStorageServiceDetailResponse]]:
    """List services

     Returns a list of File Storage services.

    Args:
        limit (int | Unset): Schema for the limit query parameter, used to specify the maximum
            number of items to return in a paginated response.
        offset (int | Unset): Query parameter to specify the offset for pagination in API
            responses, allowing clients to retrieve results starting from a specific point.
        sort (FileStorageQueryParamSort | Unset): Query parameter to specify the sorting order of
            results in API responses, allowing clients to order data based on specific fields.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FileStorageErrorResponse | list[FileStorageServiceDetailResponse]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        sort=sort,
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
    sort: FileStorageQueryParamSort | Unset = UNSET,
) -> FileStorageErrorResponse | list[FileStorageServiceDetailResponse] | None:
    """List services

     Returns a list of File Storage services.

    Args:
        limit (int | Unset): Schema for the limit query parameter, used to specify the maximum
            number of items to return in a paginated response.
        offset (int | Unset): Query parameter to specify the offset for pagination in API
            responses, allowing clients to retrieve results starting from a specific point.
        sort (FileStorageQueryParamSort | Unset): Query parameter to specify the sorting order of
            results in API responses, allowing clients to order data based on specific fields.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FileStorageErrorResponse | list[FileStorageServiceDetailResponse]
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    sort: FileStorageQueryParamSort | Unset = UNSET,
) -> Response[FileStorageErrorResponse | list[FileStorageServiceDetailResponse]]:
    """List services

     Returns a list of File Storage services.

    Args:
        limit (int | Unset): Schema for the limit query parameter, used to specify the maximum
            number of items to return in a paginated response.
        offset (int | Unset): Query parameter to specify the offset for pagination in API
            responses, allowing clients to retrieve results starting from a specific point.
        sort (FileStorageQueryParamSort | Unset): Query parameter to specify the sorting order of
            results in API responses, allowing clients to order data based on specific fields.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FileStorageErrorResponse | list[FileStorageServiceDetailResponse]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    sort: FileStorageQueryParamSort | Unset = UNSET,
) -> FileStorageErrorResponse | list[FileStorageServiceDetailResponse] | None:
    """List services

     Returns a list of File Storage services.

    Args:
        limit (int | Unset): Schema for the limit query parameter, used to specify the maximum
            number of items to return in a paginated response.
        offset (int | Unset): Query parameter to specify the offset for pagination in API
            responses, allowing clients to retrieve results starting from a specific point.
        sort (FileStorageQueryParamSort | Unset): Query parameter to specify the sorting order of
            results in API responses, allowing clients to order data based on specific fields.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FileStorageErrorResponse | list[FileStorageServiceDetailResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            sort=sort,
        )
    ).parsed
