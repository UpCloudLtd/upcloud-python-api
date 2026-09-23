from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.file_storage_error_response import FileStorageErrorResponse
from ...models.file_storage_label_details import FileStorageLabelDetails
from ...models.file_storage_label_modify import FileStorageLabelModify
from ...types import UNSET, Response, Unset


def _get_kwargs(
    service_uuid: UUID,
    label_key: str,
    *,
    body: FileStorageLabelModify | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/1.3/file-storage/{service_uuid}/labels/{label_key}".format(
            service_uuid=quote(str(service_uuid), safe=""),
            label_key=quote(str(label_key), safe=""),
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
    if response.status_code == 200:
        response_200 = FileStorageLabelDetails.from_dict(response.json())

        return response_200

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
    label_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: FileStorageLabelModify | Unset = UNSET,
) -> Response[FileStorageErrorResponse | FileStorageLabelDetails]:
    """Modify label

     Modifies existing label by given {service_uuid} and {key}.

    Args:
        service_uuid (UUID): The unique identifier.
        label_key (str): Represents the label identifier. The key is unique within a service.
        body (FileStorageLabelModify | Unset): Schema for modifying an existing label.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FileStorageErrorResponse | FileStorageLabelDetails]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        label_key=label_key,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_uuid: UUID,
    label_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: FileStorageLabelModify | Unset = UNSET,
) -> FileStorageErrorResponse | FileStorageLabelDetails | None:
    """Modify label

     Modifies existing label by given {service_uuid} and {key}.

    Args:
        service_uuid (UUID): The unique identifier.
        label_key (str): Represents the label identifier. The key is unique within a service.
        body (FileStorageLabelModify | Unset): Schema for modifying an existing label.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FileStorageErrorResponse | FileStorageLabelDetails
    """

    return sync_detailed(
        service_uuid=service_uuid,
        label_key=label_key,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    service_uuid: UUID,
    label_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: FileStorageLabelModify | Unset = UNSET,
) -> Response[FileStorageErrorResponse | FileStorageLabelDetails]:
    """Modify label

     Modifies existing label by given {service_uuid} and {key}.

    Args:
        service_uuid (UUID): The unique identifier.
        label_key (str): Represents the label identifier. The key is unique within a service.
        body (FileStorageLabelModify | Unset): Schema for modifying an existing label.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FileStorageErrorResponse | FileStorageLabelDetails]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        label_key=label_key,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_uuid: UUID,
    label_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: FileStorageLabelModify | Unset = UNSET,
) -> FileStorageErrorResponse | FileStorageLabelDetails | None:
    """Modify label

     Modifies existing label by given {service_uuid} and {key}.

    Args:
        service_uuid (UUID): The unique identifier.
        label_key (str): Represents the label identifier. The key is unique within a service.
        body (FileStorageLabelModify | Unset): Schema for modifying an existing label.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FileStorageErrorResponse | FileStorageLabelDetails
    """

    return (
        await asyncio_detailed(
            service_uuid=service_uuid,
            label_key=label_key,
            client=client,
            body=body,
        )
    ).parsed
