from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.file_storage_error_response import FileStorageErrorResponse
from ...models.file_storage_share_create import FileStorageShareCreate
from ...models.file_storage_share_detail_response import FileStorageShareDetailResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    service_uuid: UUID,
    *,
    body: FileStorageShareCreate | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/1.3/file-storage/{service_uuid}/shares".format(
            service_uuid=quote(str(service_uuid), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FileStorageErrorResponse | FileStorageShareDetailResponse:
    if response.status_code == 201:
        response_201 = FileStorageShareDetailResponse.from_dict(response.json())

        return response_201

    response_default = FileStorageErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[FileStorageErrorResponse | FileStorageShareDetailResponse]:
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
    body: FileStorageShareCreate | Unset = UNSET,
) -> Response[FileStorageErrorResponse | FileStorageShareDetailResponse]:
    """Create share

     Creates a new service share by given {service_uuid}.

    Args:
        service_uuid (UUID): The unique identifier.
        body (FileStorageShareCreate | Unset): Schema for creating a new share with access control
            lists (ACLs).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FileStorageErrorResponse | FileStorageShareDetailResponse]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: FileStorageShareCreate | Unset = UNSET,
) -> FileStorageErrorResponse | FileStorageShareDetailResponse | None:
    """Create share

     Creates a new service share by given {service_uuid}.

    Args:
        service_uuid (UUID): The unique identifier.
        body (FileStorageShareCreate | Unset): Schema for creating a new share with access control
            lists (ACLs).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FileStorageErrorResponse | FileStorageShareDetailResponse
    """

    return sync_detailed(
        service_uuid=service_uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    service_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: FileStorageShareCreate | Unset = UNSET,
) -> Response[FileStorageErrorResponse | FileStorageShareDetailResponse]:
    """Create share

     Creates a new service share by given {service_uuid}.

    Args:
        service_uuid (UUID): The unique identifier.
        body (FileStorageShareCreate | Unset): Schema for creating a new share with access control
            lists (ACLs).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FileStorageErrorResponse | FileStorageShareDetailResponse]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: FileStorageShareCreate | Unset = UNSET,
) -> FileStorageErrorResponse | FileStorageShareDetailResponse | None:
    """Create share

     Creates a new service share by given {service_uuid}.

    Args:
        service_uuid (UUID): The unique identifier.
        body (FileStorageShareCreate | Unset): Schema for creating a new share with access control
            lists (ACLs).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FileStorageErrorResponse | FileStorageShareDetailResponse
    """

    return (
        await asyncio_detailed(
            service_uuid=service_uuid,
            client=client,
            body=body,
        )
    ).parsed
