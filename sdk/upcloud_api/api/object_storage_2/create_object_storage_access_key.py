from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.object_storage_2_create_access_key_response import ObjectStorage2CreateAccessKeyResponse
from ...models.object_storage_2_error_response import ObjectStorage2ErrorResponse
from ...types import Response


def _get_kwargs(
    service_uuid: UUID,
    username: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/1.3/object-storage-2/{service_uuid}/users/{username}/access-keys".format(
            service_uuid=quote(str(service_uuid), safe=""),
            username=quote(str(username), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ObjectStorage2CreateAccessKeyResponse | ObjectStorage2ErrorResponse:
    if response.status_code == 201:
        response_201 = ObjectStorage2CreateAccessKeyResponse.from_dict(response.json())

        return response_201

    response_default = ObjectStorage2ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ObjectStorage2CreateAccessKeyResponse | ObjectStorage2ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    service_uuid: UUID,
    username: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ObjectStorage2CreateAccessKeyResponse | ObjectStorage2ErrorResponse]:
    """Create access key

     Creates a new access key by given {service_uuid} and {username}.

    Args:
        service_uuid (UUID): The unique identifier for the service.
        username (str): A resource name.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ObjectStorage2CreateAccessKeyResponse | ObjectStorage2ErrorResponse]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        username=username,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_uuid: UUID,
    username: str,
    *,
    client: AuthenticatedClient | Client,
) -> ObjectStorage2CreateAccessKeyResponse | ObjectStorage2ErrorResponse | None:
    """Create access key

     Creates a new access key by given {service_uuid} and {username}.

    Args:
        service_uuid (UUID): The unique identifier for the service.
        username (str): A resource name.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ObjectStorage2CreateAccessKeyResponse | ObjectStorage2ErrorResponse
    """

    return sync_detailed(
        service_uuid=service_uuid,
        username=username,
        client=client,
    ).parsed


async def asyncio_detailed(
    service_uuid: UUID,
    username: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ObjectStorage2CreateAccessKeyResponse | ObjectStorage2ErrorResponse]:
    """Create access key

     Creates a new access key by given {service_uuid} and {username}.

    Args:
        service_uuid (UUID): The unique identifier for the service.
        username (str): A resource name.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ObjectStorage2CreateAccessKeyResponse | ObjectStorage2ErrorResponse]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        username=username,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_uuid: UUID,
    username: str,
    *,
    client: AuthenticatedClient | Client,
) -> ObjectStorage2CreateAccessKeyResponse | ObjectStorage2ErrorResponse | None:
    """Create access key

     Creates a new access key by given {service_uuid} and {username}.

    Args:
        service_uuid (UUID): The unique identifier for the service.
        username (str): A resource name.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ObjectStorage2CreateAccessKeyResponse | ObjectStorage2ErrorResponse
    """

    return (
        await asyncio_detailed(
            service_uuid=service_uuid,
            username=username,
            client=client,
        )
    ).parsed
