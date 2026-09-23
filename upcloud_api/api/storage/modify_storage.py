from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.modify_storage_body import ModifyStorageBody
from ...models.modify_storage_response import ModifyStorageResponse
from ...models.storage_error import StorageError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    *,
    body: ModifyStorageBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/1.3/storage/{uuid}".format(
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
) -> ModifyStorageResponse | StorageError:
    if response.status_code == 200:
        response_200 = ModifyStorageResponse.from_dict(response.json())

        return response_200

    response_default = StorageError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ModifyStorageResponse | StorageError]:
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
    body: ModifyStorageBody | Unset = UNSET,
) -> Response[ModifyStorageResponse | StorageError]:
    """Modify Block Storage

     Modifies a block storage title, labels, automatic backup rule, or size. A new size must be greater
    than the current size. Set `filesystem_resize` to `yes` to also resize the last partition and its
    supported filesystem after increasing the block storage size.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        body (ModifyStorageBody | Unset): Request schema for modifying block storage properties.
            Example: {'storage': {'size': 100, 'title': 'Production data expanded'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModifyStorageResponse | StorageError]
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
    body: ModifyStorageBody | Unset = UNSET,
) -> ModifyStorageResponse | StorageError | None:
    """Modify Block Storage

     Modifies a block storage title, labels, automatic backup rule, or size. A new size must be greater
    than the current size. Set `filesystem_resize` to `yes` to also resize the last partition and its
    supported filesystem after increasing the block storage size.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        body (ModifyStorageBody | Unset): Request schema for modifying block storage properties.
            Example: {'storage': {'size': 100, 'title': 'Production data expanded'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModifyStorageResponse | StorageError
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
    body: ModifyStorageBody | Unset = UNSET,
) -> Response[ModifyStorageResponse | StorageError]:
    """Modify Block Storage

     Modifies a block storage title, labels, automatic backup rule, or size. A new size must be greater
    than the current size. Set `filesystem_resize` to `yes` to also resize the last partition and its
    supported filesystem after increasing the block storage size.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        body (ModifyStorageBody | Unset): Request schema for modifying block storage properties.
            Example: {'storage': {'size': 100, 'title': 'Production data expanded'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModifyStorageResponse | StorageError]
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
    body: ModifyStorageBody | Unset = UNSET,
) -> ModifyStorageResponse | StorageError | None:
    """Modify Block Storage

     Modifies a block storage title, labels, automatic backup rule, or size. A new size must be greater
    than the current size. Set `filesystem_resize` to `yes` to also resize the last partition and its
    supported filesystem after increasing the block storage size.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        body (ModifyStorageBody | Unset): Request schema for modifying block storage properties.
            Example: {'storage': {'size': 100, 'title': 'Production data expanded'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModifyStorageResponse | StorageError
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed
