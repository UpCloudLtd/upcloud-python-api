from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.file_storage_error_response import FileStorageErrorResponse
from ...models.file_storage_service_detail_response import FileStorageServiceDetailResponse
from ...models.file_storage_service_replace import FileStorageServiceReplace
from ...types import UNSET, Response, Unset


def _get_kwargs(
    service_uuid: UUID,
    *,
    body: FileStorageServiceReplace | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/1.3/file-storage/{service_uuid}".format(
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
) -> FileStorageErrorResponse | FileStorageServiceDetailResponse:
    if response.status_code == 200:
        response_200 = FileStorageServiceDetailResponse.from_dict(response.json())

        return response_200

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
    service_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: FileStorageServiceReplace | Unset = UNSET,
) -> Response[FileStorageErrorResponse | FileStorageServiceDetailResponse]:
    """Replace service

     Replaces existing File Storage service by given {service_uuid}.

    Args:
        service_uuid (UUID): The unique identifier.
        body (FileStorageServiceReplace | Unset): Schema for replacing an existing service with a
            new configuration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FileStorageErrorResponse | FileStorageServiceDetailResponse]
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
    body: FileStorageServiceReplace | Unset = UNSET,
) -> FileStorageErrorResponse | FileStorageServiceDetailResponse | None:
    """Replace service

     Replaces existing File Storage service by given {service_uuid}.

    Args:
        service_uuid (UUID): The unique identifier.
        body (FileStorageServiceReplace | Unset): Schema for replacing an existing service with a
            new configuration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FileStorageErrorResponse | FileStorageServiceDetailResponse
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
    body: FileStorageServiceReplace | Unset = UNSET,
) -> Response[FileStorageErrorResponse | FileStorageServiceDetailResponse]:
    """Replace service

     Replaces existing File Storage service by given {service_uuid}.

    Args:
        service_uuid (UUID): The unique identifier.
        body (FileStorageServiceReplace | Unset): Schema for replacing an existing service with a
            new configuration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FileStorageErrorResponse | FileStorageServiceDetailResponse]
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
    body: FileStorageServiceReplace | Unset = UNSET,
) -> FileStorageErrorResponse | FileStorageServiceDetailResponse | None:
    """Replace service

     Replaces existing File Storage service by given {service_uuid}.

    Args:
        service_uuid (UUID): The unique identifier.
        body (FileStorageServiceReplace | Unset): Schema for replacing an existing service with a
            new configuration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FileStorageErrorResponse | FileStorageServiceDetailResponse
    """

    return (
        await asyncio_detailed(
            service_uuid=service_uuid,
            client=client,
            body=body,
        )
    ).parsed
