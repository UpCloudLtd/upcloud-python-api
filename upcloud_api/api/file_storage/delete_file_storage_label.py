from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.file_storage_error_response import FileStorageErrorResponse
from ...types import Response


def _get_kwargs(
    service_uuid: UUID,
    label_key: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/1.3/file-storage/{service_uuid}/labels/{label_key}".format(
            service_uuid=quote(str(service_uuid), safe=""),
            label_key=quote(str(label_key), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | FileStorageErrorResponse:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    response_default = FileStorageErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | FileStorageErrorResponse]:
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
) -> Response[Any | FileStorageErrorResponse]:
    """Delete label

     Deletes existing label by given {service_uuid} and {key}.

    Args:
        service_uuid (UUID): The unique identifier.
        label_key (str): Represents the label identifier. The key is unique within a service.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FileStorageErrorResponse]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        label_key=label_key,
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
) -> Any | FileStorageErrorResponse | None:
    """Delete label

     Deletes existing label by given {service_uuid} and {key}.

    Args:
        service_uuid (UUID): The unique identifier.
        label_key (str): Represents the label identifier. The key is unique within a service.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FileStorageErrorResponse
    """

    return sync_detailed(
        service_uuid=service_uuid,
        label_key=label_key,
        client=client,
    ).parsed


async def asyncio_detailed(
    service_uuid: UUID,
    label_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | FileStorageErrorResponse]:
    """Delete label

     Deletes existing label by given {service_uuid} and {key}.

    Args:
        service_uuid (UUID): The unique identifier.
        label_key (str): Represents the label identifier. The key is unique within a service.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FileStorageErrorResponse]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        label_key=label_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_uuid: UUID,
    label_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | FileStorageErrorResponse | None:
    """Delete label

     Deletes existing label by given {service_uuid} and {key}.

    Args:
        service_uuid (UUID): The unique identifier.
        label_key (str): Represents the label identifier. The key is unique within a service.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FileStorageErrorResponse
    """

    return (
        await asyncio_detailed(
            service_uuid=service_uuid,
            label_key=label_key,
            client=client,
        )
    ).parsed
