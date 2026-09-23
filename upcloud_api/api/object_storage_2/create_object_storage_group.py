from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.object_storage_2_error_response import ObjectStorage2ErrorResponse
from ...models.object_storage_2_group_create import ObjectStorage2GroupCreate
from ...models.object_storage_2_group_response import ObjectStorage2GroupResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    service_uuid: UUID,
    *,
    body: ObjectStorage2GroupCreate | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/1.3/object-storage-2/{service_uuid}/groups".format(
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
) -> ObjectStorage2ErrorResponse | ObjectStorage2GroupResponse:
    if response.status_code == 201:
        response_201 = ObjectStorage2GroupResponse.from_dict(response.json())

        return response_201

    response_default = ObjectStorage2ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ObjectStorage2ErrorResponse | ObjectStorage2GroupResponse]:
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
    body: ObjectStorage2GroupCreate | Unset = UNSET,
) -> Response[ObjectStorage2ErrorResponse | ObjectStorage2GroupResponse]:
    """Create group

     Creates an iam group.

    Args:
        service_uuid (UUID): The unique identifier for the service.
        body (ObjectStorage2GroupCreate | Unset): Schema for creating a new IAM group.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ObjectStorage2ErrorResponse | ObjectStorage2GroupResponse]
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
    body: ObjectStorage2GroupCreate | Unset = UNSET,
) -> ObjectStorage2ErrorResponse | ObjectStorage2GroupResponse | None:
    """Create group

     Creates an iam group.

    Args:
        service_uuid (UUID): The unique identifier for the service.
        body (ObjectStorage2GroupCreate | Unset): Schema for creating a new IAM group.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ObjectStorage2ErrorResponse | ObjectStorage2GroupResponse
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
    body: ObjectStorage2GroupCreate | Unset = UNSET,
) -> Response[ObjectStorage2ErrorResponse | ObjectStorage2GroupResponse]:
    """Create group

     Creates an iam group.

    Args:
        service_uuid (UUID): The unique identifier for the service.
        body (ObjectStorage2GroupCreate | Unset): Schema for creating a new IAM group.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ObjectStorage2ErrorResponse | ObjectStorage2GroupResponse]
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
    body: ObjectStorage2GroupCreate | Unset = UNSET,
) -> ObjectStorage2ErrorResponse | ObjectStorage2GroupResponse | None:
    """Create group

     Creates an iam group.

    Args:
        service_uuid (UUID): The unique identifier for the service.
        body (ObjectStorage2GroupCreate | Unset): Schema for creating a new IAM group.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ObjectStorage2ErrorResponse | ObjectStorage2GroupResponse
    """

    return (
        await asyncio_detailed(
            service_uuid=service_uuid,
            client=client,
            body=body,
        )
    ).parsed
