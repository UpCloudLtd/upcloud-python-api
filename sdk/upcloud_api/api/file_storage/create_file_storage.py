from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.file_storage_error_response import FileStorageErrorResponse
from ...models.file_storage_service_create import FileStorageServiceCreate
from ...models.file_storage_service_detail_response import FileStorageServiceDetailResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: FileStorageServiceCreate | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/1.3/file-storage",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FileStorageErrorResponse | FileStorageServiceDetailResponse:
    if response.status_code == 201:
        response_201 = FileStorageServiceDetailResponse.from_dict(response.json())

        return response_201

    response_default = FileStorageErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[FileStorageErrorResponse | FileStorageServiceDetailResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: FileStorageServiceCreate | Unset = UNSET,
) -> Response[FileStorageErrorResponse | FileStorageServiceDetailResponse]:
    """Create service

     Creates a new File Storage service.

    Args:
        body (FileStorageServiceCreate | Unset): Schema for creating a new service.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FileStorageErrorResponse | FileStorageServiceDetailResponse]
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
    body: FileStorageServiceCreate | Unset = UNSET,
) -> FileStorageErrorResponse | FileStorageServiceDetailResponse | None:
    """Create service

     Creates a new File Storage service.

    Args:
        body (FileStorageServiceCreate | Unset): Schema for creating a new service.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FileStorageErrorResponse | FileStorageServiceDetailResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: FileStorageServiceCreate | Unset = UNSET,
) -> Response[FileStorageErrorResponse | FileStorageServiceDetailResponse]:
    """Create service

     Creates a new File Storage service.

    Args:
        body (FileStorageServiceCreate | Unset): Schema for creating a new service.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FileStorageErrorResponse | FileStorageServiceDetailResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: FileStorageServiceCreate | Unset = UNSET,
) -> FileStorageErrorResponse | FileStorageServiceDetailResponse | None:
    """Create service

     Creates a new File Storage service.

    Args:
        body (FileStorageServiceCreate | Unset): Schema for creating a new service.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FileStorageErrorResponse | FileStorageServiceDetailResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
