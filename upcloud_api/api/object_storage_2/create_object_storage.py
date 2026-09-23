from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.object_storage_2_error_response import ObjectStorage2ErrorResponse
from ...models.object_storage_2_service_create import ObjectStorage2ServiceCreate
from ...models.object_storage_2_service_detail_response import ObjectStorage2ServiceDetailResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: ObjectStorage2ServiceCreate | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/1.3/object-storage-2",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ObjectStorage2ErrorResponse | ObjectStorage2ServiceDetailResponse:
    if response.status_code == 201:
        response_201 = ObjectStorage2ServiceDetailResponse.from_dict(response.json())

        return response_201

    response_default = ObjectStorage2ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ObjectStorage2ErrorResponse | ObjectStorage2ServiceDetailResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ObjectStorage2ServiceCreate | Unset = UNSET,
) -> Response[ObjectStorage2ErrorResponse | ObjectStorage2ServiceDetailResponse]:
    """Create service

     Creates a new object storage service.

    Args:
        body (ObjectStorage2ServiceCreate | Unset): Schema for creating a service, including name,
            region, status, networks, domains, labels, and properties.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ObjectStorage2ErrorResponse | ObjectStorage2ServiceDetailResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: ObjectStorage2ServiceCreate | Unset = UNSET,
) -> ObjectStorage2ErrorResponse | ObjectStorage2ServiceDetailResponse | None:
    """Create service

     Creates a new object storage service.

    Args:
        body (ObjectStorage2ServiceCreate | Unset): Schema for creating a service, including name,
            region, status, networks, domains, labels, and properties.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ObjectStorage2ErrorResponse | ObjectStorage2ServiceDetailResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ObjectStorage2ServiceCreate | Unset = UNSET,
) -> Response[ObjectStorage2ErrorResponse | ObjectStorage2ServiceDetailResponse]:
    """Create service

     Creates a new object storage service.

    Args:
        body (ObjectStorage2ServiceCreate | Unset): Schema for creating a service, including name,
            region, status, networks, domains, labels, and properties.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ObjectStorage2ErrorResponse | ObjectStorage2ServiceDetailResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ObjectStorage2ServiceCreate | Unset = UNSET,
) -> ObjectStorage2ErrorResponse | ObjectStorage2ServiceDetailResponse | None:
    """Create service

     Creates a new object storage service.

    Args:
        body (ObjectStorage2ServiceCreate | Unset): Schema for creating a service, including name,
            region, status, networks, domains, labels, and properties.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ObjectStorage2ErrorResponse | ObjectStorage2ServiceDetailResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
