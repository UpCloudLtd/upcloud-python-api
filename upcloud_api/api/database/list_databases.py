from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.database_error_response import DatabaseErrorResponse
from ...models.database_query_param_sort import DatabaseQueryParamSort
from ...models.database_service_information_response import DatabaseServiceInformationResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    sort: DatabaseQueryParamSort | Unset = UNSET,
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
        "url": "/1.3/database",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DatabaseErrorResponse | list[DatabaseServiceInformationResponse]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemasdatabase_service_information_list_response_item_data in _response_200:
            componentsschemasdatabase_service_information_list_response_item = (
                DatabaseServiceInformationResponse.from_dict(
                    componentsschemasdatabase_service_information_list_response_item_data
                )
            )

            response_200.append(componentsschemasdatabase_service_information_list_response_item)

        return response_200

    response_default = DatabaseErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DatabaseErrorResponse | list[DatabaseServiceInformationResponse]]:
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
    sort: DatabaseQueryParamSort | Unset = UNSET,
) -> Response[DatabaseErrorResponse | list[DatabaseServiceInformationResponse]]:
    """List databases

     Returns a list of all available Managed Database services. Depending on their database type, Managed
    Databases services will have different details.

    Args:
        limit (int | Unset): Schema for a query parameter specifying the maximum number of entries
            to return (limit).
        offset (int | Unset): Schema for a query parameter specifying the offset for pagination.
        sort (DatabaseQueryParamSort | Unset): Schema for a query parameter specifying the sort
            field and direction. Prefix with '-' for descending order.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatabaseErrorResponse | list[DatabaseServiceInformationResponse]]
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
    sort: DatabaseQueryParamSort | Unset = UNSET,
) -> DatabaseErrorResponse | list[DatabaseServiceInformationResponse] | None:
    """List databases

     Returns a list of all available Managed Database services. Depending on their database type, Managed
    Databases services will have different details.

    Args:
        limit (int | Unset): Schema for a query parameter specifying the maximum number of entries
            to return (limit).
        offset (int | Unset): Schema for a query parameter specifying the offset for pagination.
        sort (DatabaseQueryParamSort | Unset): Schema for a query parameter specifying the sort
            field and direction. Prefix with '-' for descending order.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatabaseErrorResponse | list[DatabaseServiceInformationResponse]
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
    sort: DatabaseQueryParamSort | Unset = UNSET,
) -> Response[DatabaseErrorResponse | list[DatabaseServiceInformationResponse]]:
    """List databases

     Returns a list of all available Managed Database services. Depending on their database type, Managed
    Databases services will have different details.

    Args:
        limit (int | Unset): Schema for a query parameter specifying the maximum number of entries
            to return (limit).
        offset (int | Unset): Schema for a query parameter specifying the offset for pagination.
        sort (DatabaseQueryParamSort | Unset): Schema for a query parameter specifying the sort
            field and direction. Prefix with '-' for descending order.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatabaseErrorResponse | list[DatabaseServiceInformationResponse]]
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
    sort: DatabaseQueryParamSort | Unset = UNSET,
) -> DatabaseErrorResponse | list[DatabaseServiceInformationResponse] | None:
    """List databases

     Returns a list of all available Managed Database services. Depending on their database type, Managed
    Databases services will have different details.

    Args:
        limit (int | Unset): Schema for a query parameter specifying the maximum number of entries
            to return (limit).
        offset (int | Unset): Schema for a query parameter specifying the offset for pagination.
        sort (DatabaseQueryParamSort | Unset): Schema for a query parameter specifying the sort
            field and direction. Prefix with '-' for descending order.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatabaseErrorResponse | list[DatabaseServiceInformationResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            sort=sort,
        )
    ).parsed
