from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_server_list import GetServerList
from ...models.list_servers_order_by import ListServersOrderBy
from ...models.list_servers_sort_by import ListServersSortBy
from ...models.list_servers_state import ListServersState
from ...models.server_error import ServerError
from ...models.server_error_400 import ServerError400
from ...models.server_error_403 import ServerError403
from ...models.server_error_404 import ServerError404
from ...models.server_error_409 import ServerError409
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    label: str | Unset = UNSET,
    uuid: UUID | Unset = UNSET,
    host: int | Unset = UNSET,
    device: str | Unset = UNSET,
    state: ListServersState | Unset = UNSET,
    tag: str | Unset = UNSET,
    search: str | Unset = UNSET,
    sort_by: ListServersSortBy | Unset = UNSET,
    order_by: ListServersOrderBy | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["label"] = label

    json_uuid: str | Unset = UNSET
    if not isinstance(uuid, Unset):
        json_uuid = str(uuid)
    params["uuid"] = json_uuid

    params["host"] = host

    params["device"] = device

    json_state: str | Unset = UNSET
    if not isinstance(state, Unset):
        json_state = state.value

    params["state"] = json_state

    params["tag"] = tag

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
        "url": "/1.3/server",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetServerList | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409:
    if response.status_code == 200:
        response_200 = GetServerList.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ServerError400.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = ServerError403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ServerError404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ServerError409.from_dict(response.json())

        return response_409

    response_default = ServerError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetServerList | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409]:
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
    uuid: UUID | Unset = UNSET,
    host: int | Unset = UNSET,
    device: str | Unset = UNSET,
    state: ListServersState | Unset = UNSET,
    tag: str | Unset = UNSET,
    search: str | Unset = UNSET,
    sort_by: ListServersSortBy | Unset = UNSET,
    order_by: ListServersOrderBy | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[GetServerList | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409]:
    """List Cloud Servers

     Returns the most relevant information for Cloud Servers associated with the current account.

    Args:
        label (str | Unset):
        uuid (UUID | Unset): Universally unique identifier Example:
            0414e0d7-4436-4037-9dd8-6eaf47dce599.
        host (int | Unset): Encoded Private Cloud host ID
        device (str | Unset):
        state (ListServersState | Unset):
        tag (str | Unset): One or more tag names. Use commas to match any tag, or colons to
            require all tags. Example: prod,web.
        search (str | Unset):
        sort_by (ListServersSortBy | Unset):
        order_by (ListServersOrderBy | Unset):
        limit (int | Unset): Maximum number of items to return. Default is 25.
        offset (int | Unset): Number of items to skip before starting to return results. Default
            is 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetServerList | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409]
    """

    kwargs = _get_kwargs(
        label=label,
        uuid=uuid,
        host=host,
        device=device,
        state=state,
        tag=tag,
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
    uuid: UUID | Unset = UNSET,
    host: int | Unset = UNSET,
    device: str | Unset = UNSET,
    state: ListServersState | Unset = UNSET,
    tag: str | Unset = UNSET,
    search: str | Unset = UNSET,
    sort_by: ListServersSortBy | Unset = UNSET,
    order_by: ListServersOrderBy | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> GetServerList | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | None:
    """List Cloud Servers

     Returns the most relevant information for Cloud Servers associated with the current account.

    Args:
        label (str | Unset):
        uuid (UUID | Unset): Universally unique identifier Example:
            0414e0d7-4436-4037-9dd8-6eaf47dce599.
        host (int | Unset): Encoded Private Cloud host ID
        device (str | Unset):
        state (ListServersState | Unset):
        tag (str | Unset): One or more tag names. Use commas to match any tag, or colons to
            require all tags. Example: prod,web.
        search (str | Unset):
        sort_by (ListServersSortBy | Unset):
        order_by (ListServersOrderBy | Unset):
        limit (int | Unset): Maximum number of items to return. Default is 25.
        offset (int | Unset): Number of items to skip before starting to return results. Default
            is 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetServerList | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409
    """

    return sync_detailed(
        client=client,
        label=label,
        uuid=uuid,
        host=host,
        device=device,
        state=state,
        tag=tag,
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
    uuid: UUID | Unset = UNSET,
    host: int | Unset = UNSET,
    device: str | Unset = UNSET,
    state: ListServersState | Unset = UNSET,
    tag: str | Unset = UNSET,
    search: str | Unset = UNSET,
    sort_by: ListServersSortBy | Unset = UNSET,
    order_by: ListServersOrderBy | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[GetServerList | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409]:
    """List Cloud Servers

     Returns the most relevant information for Cloud Servers associated with the current account.

    Args:
        label (str | Unset):
        uuid (UUID | Unset): Universally unique identifier Example:
            0414e0d7-4436-4037-9dd8-6eaf47dce599.
        host (int | Unset): Encoded Private Cloud host ID
        device (str | Unset):
        state (ListServersState | Unset):
        tag (str | Unset): One or more tag names. Use commas to match any tag, or colons to
            require all tags. Example: prod,web.
        search (str | Unset):
        sort_by (ListServersSortBy | Unset):
        order_by (ListServersOrderBy | Unset):
        limit (int | Unset): Maximum number of items to return. Default is 25.
        offset (int | Unset): Number of items to skip before starting to return results. Default
            is 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetServerList | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409]
    """

    kwargs = _get_kwargs(
        label=label,
        uuid=uuid,
        host=host,
        device=device,
        state=state,
        tag=tag,
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
    uuid: UUID | Unset = UNSET,
    host: int | Unset = UNSET,
    device: str | Unset = UNSET,
    state: ListServersState | Unset = UNSET,
    tag: str | Unset = UNSET,
    search: str | Unset = UNSET,
    sort_by: ListServersSortBy | Unset = UNSET,
    order_by: ListServersOrderBy | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> GetServerList | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | None:
    """List Cloud Servers

     Returns the most relevant information for Cloud Servers associated with the current account.

    Args:
        label (str | Unset):
        uuid (UUID | Unset): Universally unique identifier Example:
            0414e0d7-4436-4037-9dd8-6eaf47dce599.
        host (int | Unset): Encoded Private Cloud host ID
        device (str | Unset):
        state (ListServersState | Unset):
        tag (str | Unset): One or more tag names. Use commas to match any tag, or colons to
            require all tags. Example: prod,web.
        search (str | Unset):
        sort_by (ListServersSortBy | Unset):
        order_by (ListServersOrderBy | Unset):
        limit (int | Unset): Maximum number of items to return. Default is 25.
        offset (int | Unset): Number of items to skip before starting to return results. Default
            is 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetServerList | ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409
    """

    return (
        await asyncio_detailed(
            client=client,
            label=label,
            uuid=uuid,
            host=host,
            device=device,
            state=state,
            tag=tag,
            search=search,
            sort_by=sort_by,
            order_by=order_by,
            limit=limit,
            offset=offset,
        )
    ).parsed
