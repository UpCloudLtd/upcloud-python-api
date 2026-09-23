from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.file_storage_error_response import FileStorageErrorResponse
from ...models.file_storage_label_create import FileStorageLabelCreate
from ...models.file_storage_label_details import FileStorageLabelDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    service_uuid: UUID,
    *,
    body: FileStorageLabelCreate | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/1.3/file-storage/{service_uuid}/labels".format(
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
) -> FileStorageErrorResponse | FileStorageLabelDetails:
    if response.status_code == 201:
        response_201 = FileStorageLabelDetails.from_dict(response.json())

        return response_201

    response_default = FileStorageErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[FileStorageErrorResponse | FileStorageLabelDetails]:
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
    body: FileStorageLabelCreate | Unset = UNSET,
) -> Response[FileStorageErrorResponse | FileStorageLabelDetails]:
    """Create label

     Creates a new label by given {service_uuid}. Labels are used for service filtering.

    Args:
        service_uuid (UUID): The unique identifier.
        body (FileStorageLabelCreate | Unset): Schema for creating a new label.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FileStorageErrorResponse | FileStorageLabelDetails]
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
    body: FileStorageLabelCreate | Unset = UNSET,
) -> FileStorageErrorResponse | FileStorageLabelDetails | None:
    """Create label

     Creates a new label by given {service_uuid}. Labels are used for service filtering.

    Args:
        service_uuid (UUID): The unique identifier.
        body (FileStorageLabelCreate | Unset): Schema for creating a new label.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FileStorageErrorResponse | FileStorageLabelDetails
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
    body: FileStorageLabelCreate | Unset = UNSET,
) -> Response[FileStorageErrorResponse | FileStorageLabelDetails]:
    """Create label

     Creates a new label by given {service_uuid}. Labels are used for service filtering.

    Args:
        service_uuid (UUID): The unique identifier.
        body (FileStorageLabelCreate | Unset): Schema for creating a new label.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FileStorageErrorResponse | FileStorageLabelDetails]
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
    body: FileStorageLabelCreate | Unset = UNSET,
) -> FileStorageErrorResponse | FileStorageLabelDetails | None:
    """Create label

     Creates a new label by given {service_uuid}. Labels are used for service filtering.

    Args:
        service_uuid (UUID): The unique identifier.
        body (FileStorageLabelCreate | Unset): Schema for creating a new label.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FileStorageErrorResponse | FileStorageLabelDetails
    """

    return (
        await asyncio_detailed(
            service_uuid=service_uuid,
            client=client,
            body=body,
        )
    ).parsed
