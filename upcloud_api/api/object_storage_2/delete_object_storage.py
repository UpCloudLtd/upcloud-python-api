from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.object_storage_2_error_response import ObjectStorage2ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    service_uuid: UUID,
    *,
    force: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["force"] = force

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/1.3/object-storage-2/{service_uuid}".format(
            service_uuid=quote(str(service_uuid), safe=""),
        ),
        "params": params,
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
    *,
    client: AuthenticatedClient | Client,
    force: bool | Unset = UNSET,
) -> Response[Any | ObjectStorage2ErrorResponse]:
    """Delete service

     Deletes existing object storage service by given {service_uuid}.

    Args:
        service_uuid (UUID): The unique identifier for the service.
        force (bool | Unset): Schema for a query parameter specifying whether to force an
            operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ObjectStorage2ErrorResponse]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        force=force,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    force: bool | Unset = UNSET,
) -> Any | ObjectStorage2ErrorResponse | None:
    """Delete service

     Deletes existing object storage service by given {service_uuid}.

    Args:
        service_uuid (UUID): The unique identifier for the service.
        force (bool | Unset): Schema for a query parameter specifying whether to force an
            operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ObjectStorage2ErrorResponse
    """

    return sync_detailed(
        service_uuid=service_uuid,
        client=client,
        force=force,
    ).parsed


async def asyncio_detailed(
    service_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    force: bool | Unset = UNSET,
) -> Response[Any | ObjectStorage2ErrorResponse]:
    """Delete service

     Deletes existing object storage service by given {service_uuid}.

    Args:
        service_uuid (UUID): The unique identifier for the service.
        force (bool | Unset): Schema for a query parameter specifying whether to force an
            operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ObjectStorage2ErrorResponse]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        force=force,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    force: bool | Unset = UNSET,
) -> Any | ObjectStorage2ErrorResponse | None:
    """Delete service

     Deletes existing object storage service by given {service_uuid}.

    Args:
        service_uuid (UUID): The unique identifier for the service.
        force (bool | Unset): Schema for a query parameter specifying whether to force an
            operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ObjectStorage2ErrorResponse
    """

    return (
        await asyncio_detailed(
            service_uuid=service_uuid,
            client=client,
            force=force,
        )
    ).parsed
