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
    network_name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/file-storage/{service_uuid}/networks/{network_name}".format(
            service_uuid=quote(str(service_uuid), safe=""),
            network_name=quote(str(network_name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FileStorageErrorResponse | FileStorageNetworkDetailResponse:
    if response.status_code == 200:
        response_200 = FileStorageNetworkDetailResponse.from_dict(response.json())

        return response_200

    response_default = FileStorageErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[FileStorageErrorResponse | FileStorageNetworkDetailResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    service_uuid: UUID,
    network_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[FileStorageErrorResponse | FileStorageNetworkDetailResponse]:
    """Get network details

     Returns service network details by given {service_uuid} and {network_name}.

    Args:
        service_uuid (UUID): The unique identifier.
        network_name (str): A resource name.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FileStorageErrorResponse | FileStorageNetworkDetailResponse]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        network_name=network_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_uuid: UUID,
    network_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> FileStorageErrorResponse | FileStorageNetworkDetailResponse | None:
    """Get network details

     Returns service network details by given {service_uuid} and {network_name}.

    Args:
        service_uuid (UUID): The unique identifier.
        network_name (str): A resource name.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FileStorageErrorResponse | FileStorageNetworkDetailResponse
    """

    return sync_detailed(
        service_uuid=service_uuid,
        network_name=network_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    service_uuid: UUID,
    network_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[FileStorageErrorResponse | FileStorageNetworkDetailResponse]:
    """Get network details

     Returns service network details by given {service_uuid} and {network_name}.

    Args:
        service_uuid (UUID): The unique identifier.
        network_name (str): A resource name.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FileStorageErrorResponse | FileStorageNetworkDetailResponse]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        network_name=network_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_uuid: UUID,
    network_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> FileStorageErrorResponse | FileStorageNetworkDetailResponse | None:
    """Get network details

     Returns service network details by given {service_uuid} and {network_name}.

    Args:
        service_uuid (UUID): The unique identifier.
        network_name (str): A resource name.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FileStorageErrorResponse | FileStorageNetworkDetailResponse
    """

    return (
        await asyncio_detailed(
            service_uuid=service_uuid,
            network_name=network_name,
            client=client,
        )
    ).parsed
