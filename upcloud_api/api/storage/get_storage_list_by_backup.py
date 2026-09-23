from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.storage_error import StorageError
from ...models.storage_order_by import StorageOrderBy
from ...models.storage_sort_by import StorageSortBy
from ...models.storages import Storages
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    label: str | Unset = UNSET,
    search: str | Unset = UNSET,
    sort_by: StorageSortBy | Unset = UNSET,
    order_by: StorageOrderBy | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["label"] = label

    params["search"] = search

    json_sort_by: str | Unset = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = sort_by.value

    params["sort_by"] = json_sort_by

    json_order_by: str | Unset = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by.value

    params["order_by"] = json_order_by

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/storage/backup",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> StorageError | Storages:
    if response.status_code == 200:
        response_200 = Storages.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = StorageError.from_dict(response.json())

        return response_400

    response_default = StorageError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[StorageError | Storages]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    label: str | Unset = UNSET,
    search: str | Unset = UNSET,
    sort_by: StorageSortBy | Unset = UNSET,
    order_by: StorageOrderBy | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[StorageError | Storages]:
    """List storage backups

     Returns accessible storage resources whose type is `backup`.

    Args:
        label (str | Unset): Label key or key-value pair to match. A key-only filter matches any
            value. Repeat the query parameter to require all specified labels; keys are matched case-
            insensitively.
        search (str | Unset): Partial match against the storage resource title or UUID.
        sort_by (StorageSortBy | Unset): Storage resource field by which to sort the results.
        order_by (StorageOrderBy | Unset): Sort direction. This parameter is used only when
            `sort_by` is specified.
        limit (int | Unset): Maximum number of storage resources to return. Default is 25.
        offset (int | Unset): Number of items to skip before starting to return results. Default
            is 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StorageError | Storages]
    """

    kwargs = _get_kwargs(
        label=label,
        search=search,
        sort_by=sort_by,
        order_by=order_by,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    label: str | Unset = UNSET,
    search: str | Unset = UNSET,
    sort_by: StorageSortBy | Unset = UNSET,
    order_by: StorageOrderBy | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> StorageError | Storages | None:
    """List storage backups

     Returns accessible storage resources whose type is `backup`.

    Args:
        label (str | Unset): Label key or key-value pair to match. A key-only filter matches any
            value. Repeat the query parameter to require all specified labels; keys are matched case-
            insensitively.
        search (str | Unset): Partial match against the storage resource title or UUID.
        sort_by (StorageSortBy | Unset): Storage resource field by which to sort the results.
        order_by (StorageOrderBy | Unset): Sort direction. This parameter is used only when
            `sort_by` is specified.
        limit (int | Unset): Maximum number of storage resources to return. Default is 25.
        offset (int | Unset): Number of items to skip before starting to return results. Default
            is 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StorageError | Storages
    """

    return sync_detailed(
        client=client,
        label=label,
        search=search,
        sort_by=sort_by,
        order_by=order_by,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    label: str | Unset = UNSET,
    search: str | Unset = UNSET,
    sort_by: StorageSortBy | Unset = UNSET,
    order_by: StorageOrderBy | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[StorageError | Storages]:
    """List storage backups

     Returns accessible storage resources whose type is `backup`.

    Args:
        label (str | Unset): Label key or key-value pair to match. A key-only filter matches any
            value. Repeat the query parameter to require all specified labels; keys are matched case-
            insensitively.
        search (str | Unset): Partial match against the storage resource title or UUID.
        sort_by (StorageSortBy | Unset): Storage resource field by which to sort the results.
        order_by (StorageOrderBy | Unset): Sort direction. This parameter is used only when
            `sort_by` is specified.
        limit (int | Unset): Maximum number of storage resources to return. Default is 25.
        offset (int | Unset): Number of items to skip before starting to return results. Default
            is 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StorageError | Storages]
    """

    kwargs = _get_kwargs(
        label=label,
        search=search,
        sort_by=sort_by,
        order_by=order_by,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    label: str | Unset = UNSET,
    search: str | Unset = UNSET,
    sort_by: StorageSortBy | Unset = UNSET,
    order_by: StorageOrderBy | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> StorageError | Storages | None:
    """List storage backups

     Returns accessible storage resources whose type is `backup`.

    Args:
        label (str | Unset): Label key or key-value pair to match. A key-only filter matches any
            value. Repeat the query parameter to require all specified labels; keys are matched case-
            insensitively.
        search (str | Unset): Partial match against the storage resource title or UUID.
        sort_by (StorageSortBy | Unset): Storage resource field by which to sort the results.
        order_by (StorageOrderBy | Unset): Sort direction. This parameter is used only when
            `sort_by` is specified.
        limit (int | Unset): Maximum number of storage resources to return. Default is 25.
        offset (int | Unset): Number of items to skip before starting to return results. Default
            is 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StorageError | Storages
    """

    return (
        await asyncio_detailed(
            client=client,
            label=label,
            search=search,
            sort_by=sort_by,
            order_by=order_by,
            limit=limit,
            offset=offset,
        )
    ).parsed
