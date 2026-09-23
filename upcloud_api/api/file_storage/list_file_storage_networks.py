from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.file_storage_error_response import FileStorageErrorResponse
from ...models.file_storage_network_detail_response import FileStorageNetworkDetailResponse
from ...types import Response


def _get_kwargs(
    service_uuid: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/file-storage/{service_uuid}/networks".format(
            service_uuid=quote(str(service_uuid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FileStorageErrorResponse | list[FileStorageNetworkDetailResponse]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemasfile_storage_network_list_response_item_data in _response_200:
            componentsschemasfile_storage_network_list_response_item = FileStorageNetworkDetailResponse.from_dict(
                componentsschemasfile_storage_network_list_response_item_data
            )

            response_200.append(componentsschemasfile_storage_network_list_response_item)

        return response_200

    response_default = FileStorageErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[FileStorageErrorResponse | list[FileStorageNetworkDetailResponse]]:
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
) -> Response[FileStorageErrorResponse | list[FileStorageNetworkDetailResponse]]:
    """List networks

     Returns a list of available service networks by given {service_uuid}.

    Args:
        service_uuid (UUID): The unique identifier.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FileStorageErrorResponse | list[FileStorageNetworkDetailResponse]]
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
) -> FileStorageErrorResponse | list[FileStorageNetworkDetailResponse] | None:
    """List networks

     Returns a list of available service networks by given {service_uuid}.

    Args:
        service_uuid (UUID): The unique identifier.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FileStorageErrorResponse | list[FileStorageNetworkDetailResponse]
    """

    return sync_detailed(
        service_uuid=service_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    service_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[FileStorageErrorResponse | list[FileStorageNetworkDetailResponse]]:
    """List networks

     Returns a list of available service networks by given {service_uuid}.

    Args:
        service_uuid (UUID): The unique identifier.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FileStorageErrorResponse | list[FileStorageNetworkDetailResponse]]
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
) -> FileStorageErrorResponse | list[FileStorageNetworkDetailResponse] | None:
    """List networks

     Returns a list of available service networks by given {service_uuid}.

    Args:
        service_uuid (UUID): The unique identifier.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FileStorageErrorResponse | list[FileStorageNetworkDetailResponse]
    """

    return (
        await asyncio_detailed(
            service_uuid=service_uuid,
            client=client,
        )
    ).parsed
