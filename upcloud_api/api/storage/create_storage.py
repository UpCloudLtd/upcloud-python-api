from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.create_storage_request import CreateStorageRequest
from ...models.create_storage_response import CreateStorageResponse
from ...models.storage_error import StorageError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreateStorageRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/1.3/storage",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateStorageResponse | StorageError:
    if response.status_code == 201:
        response_201 = CreateStorageResponse.from_dict(response.json())

        return response_201

    response_default = StorageError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateStorageResponse | StorageError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateStorageRequest | Unset = UNSET,
) -> Response[CreateStorageResponse | StorageError]:
    """Create Block Storage

     Creates a block storage resource in a specific zone. The new block storage is not attached to a
    Cloud Server.

    Args:
        body (CreateStorageRequest | Unset): Request schema for creating block storage. Example:
            {'storage': {'backup_rule': {'interval': 'daily', 'retention': '7', 'time': '0400'},
            'encrypted': 'yes', 'labels': [{'key': 'environment', 'value': 'production'}], 'size': 50,
            'tier': 'maxiops', 'title': 'Block Storage 1', 'zone': 'fi-hel1'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateStorageResponse | StorageError]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CreateStorageRequest | Unset = UNSET,
) -> CreateStorageResponse | StorageError | None:
    """Create Block Storage

     Creates a block storage resource in a specific zone. The new block storage is not attached to a
    Cloud Server.

    Args:
        body (CreateStorageRequest | Unset): Request schema for creating block storage. Example:
            {'storage': {'backup_rule': {'interval': 'daily', 'retention': '7', 'time': '0400'},
            'encrypted': 'yes', 'labels': [{'key': 'environment', 'value': 'production'}], 'size': 50,
            'tier': 'maxiops', 'title': 'Block Storage 1', 'zone': 'fi-hel1'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateStorageResponse | StorageError
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateStorageRequest | Unset = UNSET,
) -> Response[CreateStorageResponse | StorageError]:
    """Create Block Storage

     Creates a block storage resource in a specific zone. The new block storage is not attached to a
    Cloud Server.

    Args:
        body (CreateStorageRequest | Unset): Request schema for creating block storage. Example:
            {'storage': {'backup_rule': {'interval': 'daily', 'retention': '7', 'time': '0400'},
            'encrypted': 'yes', 'labels': [{'key': 'environment', 'value': 'production'}], 'size': 50,
            'tier': 'maxiops', 'title': 'Block Storage 1', 'zone': 'fi-hel1'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateStorageResponse | StorageError]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateStorageRequest | Unset = UNSET,
) -> CreateStorageResponse | StorageError | None:
    """Create Block Storage

     Creates a block storage resource in a specific zone. The new block storage is not attached to a
    Cloud Server.

    Args:
        body (CreateStorageRequest | Unset): Request schema for creating block storage. Example:
            {'storage': {'backup_rule': {'interval': 'daily', 'retention': '7', 'time': '0400'},
            'encrypted': 'yes', 'labels': [{'key': 'environment', 'value': 'production'}], 'size': 50,
            'tier': 'maxiops', 'title': 'Block Storage 1', 'zone': 'fi-hel1'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateStorageResponse | StorageError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
