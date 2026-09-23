from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.object_storage_2_error_response import ObjectStorage2ErrorResponse
from ...types import Response


def _get_kwargs(
    service_uuid: UUID,
    username: str,
    access_key_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/1.3/object-storage-2/{service_uuid}/users/{username}/access-keys/{access_key_id}".format(
            service_uuid=quote(str(service_uuid), safe=""),
            username=quote(str(username), safe=""),
            access_key_id=quote(str(access_key_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ObjectStorage2ErrorResponse:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    response_default = ObjectStorage2ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ObjectStorage2ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    service_uuid: UUID,
    username: str,
    access_key_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | ObjectStorage2ErrorResponse]:
    """Delete access key

     Deletes existing access key by given {service_uuid}, {username}, and {access-key-id}.

    Args:
        service_uuid (UUID): The unique identifier for the service.
        username (str): A resource name.
        access_key_id (str): The public identifier for an access key.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ObjectStorage2ErrorResponse]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        username=username,
        access_key_id=access_key_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_uuid: UUID,
    username: str,
    access_key_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | ObjectStorage2ErrorResponse | None:
    """Delete access key

     Deletes existing access key by given {service_uuid}, {username}, and {access-key-id}.

    Args:
        service_uuid (UUID): The unique identifier for the service.
        username (str): A resource name.
        access_key_id (str): The public identifier for an access key.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ObjectStorage2ErrorResponse
    """

    return sync_detailed(
        service_uuid=service_uuid,
        username=username,
        access_key_id=access_key_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    service_uuid: UUID,
    username: str,
    access_key_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | ObjectStorage2ErrorResponse]:
    """Delete access key

     Deletes existing access key by given {service_uuid}, {username}, and {access-key-id}.

    Args:
        service_uuid (UUID): The unique identifier for the service.
        username (str): A resource name.
        access_key_id (str): The public identifier for an access key.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ObjectStorage2ErrorResponse]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        username=username,
        access_key_id=access_key_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_uuid: UUID,
    username: str,
    access_key_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | ObjectStorage2ErrorResponse | None:
    """Delete access key

     Deletes existing access key by given {service_uuid}, {username}, and {access-key-id}.

    Args:
        service_uuid (UUID): The unique identifier for the service.
        username (str): A resource name.
        access_key_id (str): The public identifier for an access key.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ObjectStorage2ErrorResponse
    """

    return (
        await asyncio_detailed(
            service_uuid=service_uuid,
            username=username,
            access_key_id=access_key_id,
            client=client,
        )
    ).parsed
