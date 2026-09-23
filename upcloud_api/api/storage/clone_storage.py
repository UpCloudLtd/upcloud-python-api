from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.clone_storage_request import CloneStorageRequest
from ...models.create_storage_response import CreateStorageResponse
from ...models.storage_error import StorageError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    *,
    body: CloneStorageRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/1.3/storage/{uuid}/clone".format(
            uuid=quote(str(uuid), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CreateStorageResponse | StorageError:
    if response.status_code == 201:
        response_201 = CreateStorageResponse.from_dict(response.json())

        return response_201

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = StorageError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CreateStorageResponse | StorageError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CloneStorageRequest | Unset = UNSET,
) -> Response[Any | CreateStorageResponse | StorageError]:
    """Clone Block Storage

     Creates a Block Storage copy of a storage resource. Cloning is asynchronous: the returned block
    storage remains in the `maintenance` state until the operation completes and can be monitored with
    the storage resource details endpoint.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        body (CloneStorageRequest | Unset): Request schema for cloning a block storage resource.
            Example: {'storage': {'encrypted': 'yes', 'tier': 'maxiops', 'title': 'Cloned Block
            Storage', 'zone': 'fi-hel1'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateStorageResponse | StorageError]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CloneStorageRequest | Unset = UNSET,
) -> Any | CreateStorageResponse | StorageError | None:
    """Clone Block Storage

     Creates a Block Storage copy of a storage resource. Cloning is asynchronous: the returned block
    storage remains in the `maintenance` state until the operation completes and can be monitored with
    the storage resource details endpoint.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        body (CloneStorageRequest | Unset): Request schema for cloning a block storage resource.
            Example: {'storage': {'encrypted': 'yes', 'tier': 'maxiops', 'title': 'Cloned Block
            Storage', 'zone': 'fi-hel1'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateStorageResponse | StorageError
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CloneStorageRequest | Unset = UNSET,
) -> Response[Any | CreateStorageResponse | StorageError]:
    """Clone Block Storage

     Creates a Block Storage copy of a storage resource. Cloning is asynchronous: the returned block
    storage remains in the `maintenance` state until the operation completes and can be monitored with
    the storage resource details endpoint.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        body (CloneStorageRequest | Unset): Request schema for cloning a block storage resource.
            Example: {'storage': {'encrypted': 'yes', 'tier': 'maxiops', 'title': 'Cloned Block
            Storage', 'zone': 'fi-hel1'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateStorageResponse | StorageError]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CloneStorageRequest | Unset = UNSET,
) -> Any | CreateStorageResponse | StorageError | None:
    """Clone Block Storage

     Creates a Block Storage copy of a storage resource. Cloning is asynchronous: the returned block
    storage remains in the `maintenance` state until the operation completes and can be monitored with
    the storage resource details endpoint.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        body (CloneStorageRequest | Unset): Request schema for cloning a block storage resource.
            Example: {'storage': {'encrypted': 'yes', 'tier': 'maxiops', 'title': 'Cloned Block
            Storage', 'zone': 'fi-hel1'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateStorageResponse | StorageError
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed
