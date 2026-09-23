from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.file_storage_error_response import FileStorageErrorResponse
from ...models.file_storage_label_details import FileStorageLabelDetails
from ...types import Response


def _get_kwargs(
    service_uuid: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/file-storage/{service_uuid}/labels".format(
            service_uuid=quote(str(service_uuid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FileStorageErrorResponse | list[FileStorageLabelDetails]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemasfile_storage_labels_list_response_item_data in _response_200:
            componentsschemasfile_storage_labels_list_response_item = FileStorageLabelDetails.from_dict(
                componentsschemasfile_storage_labels_list_response_item_data
            )

            response_200.append(componentsschemasfile_storage_labels_list_response_item)

        return response_200

    response_default = FileStorageErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[FileStorageErrorResponse | list[FileStorageLabelDetails]]:
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
) -> Response[FileStorageErrorResponse | list[FileStorageLabelDetails]]:
    """List labels

     Returns a list of available service labels by given {service_uuid}.

    Args:
        service_uuid (UUID): The unique identifier.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FileStorageErrorResponse | list[FileStorageLabelDetails]]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> FileStorageErrorResponse | list[FileStorageLabelDetails] | None:
    """List labels

     Returns a list of available service labels by given {service_uuid}.

    Args:
        service_uuid (UUID): The unique identifier.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FileStorageErrorResponse | list[FileStorageLabelDetails]
    """

    return sync_detailed(
        service_uuid=service_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    service_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[FileStorageErrorResponse | list[FileStorageLabelDetails]]:
    """List labels

     Returns a list of available service labels by given {service_uuid}.

    Args:
        service_uuid (UUID): The unique identifier.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FileStorageErrorResponse | list[FileStorageLabelDetails]]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> FileStorageErrorResponse | list[FileStorageLabelDetails] | None:
    """List labels

     Returns a list of available service labels by given {service_uuid}.

    Args:
        service_uuid (UUID): The unique identifier.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FileStorageErrorResponse | list[FileStorageLabelDetails]
    """

    return (
        await asyncio_detailed(
            service_uuid=service_uuid,
            client=client,
        )
    ).parsed
