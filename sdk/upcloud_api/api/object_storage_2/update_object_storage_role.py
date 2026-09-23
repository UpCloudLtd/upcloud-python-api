from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.object_storage_2_error_response import ObjectStorage2ErrorResponse
from ...models.object_storage_2_role_response import ObjectStorage2RoleResponse
from ...models.object_storage_2_role_update import ObjectStorage2RoleUpdate
from ...types import UNSET, Response, Unset


def _get_kwargs(
    service_uuid: UUID,
    role_name: str,
    *,
    body: ObjectStorage2RoleUpdate | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/1.3/object-storage-2/{service_uuid}/roles/{role_name}".format(
            service_uuid=quote(str(service_uuid), safe=""),
            role_name=quote(str(role_name), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ObjectStorage2ErrorResponse | ObjectStorage2RoleResponse:
    if response.status_code == 200:
        response_200 = ObjectStorage2RoleResponse.from_dict(response.json())

        return response_200

    response_default = ObjectStorage2ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ObjectStorage2ErrorResponse | ObjectStorage2RoleResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    service_uuid: UUID,
    role_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: ObjectStorage2RoleUpdate | Unset = UNSET,
) -> Response[ObjectStorage2ErrorResponse | ObjectStorage2RoleResponse]:
    """Update Role

     Updates a service's IAM role.

    Args:
        service_uuid (UUID): The unique identifier for the service.
        role_name (str): A resource name.
        body (ObjectStorage2RoleUpdate | Unset): Schema for updating an existing role.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ObjectStorage2ErrorResponse | ObjectStorage2RoleResponse]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        role_name=role_name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_uuid: UUID,
    role_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: ObjectStorage2RoleUpdate | Unset = UNSET,
) -> ObjectStorage2ErrorResponse | ObjectStorage2RoleResponse | None:
    """Update Role

     Updates a service's IAM role.

    Args:
        service_uuid (UUID): The unique identifier for the service.
        role_name (str): A resource name.
        body (ObjectStorage2RoleUpdate | Unset): Schema for updating an existing role.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ObjectStorage2ErrorResponse | ObjectStorage2RoleResponse
    """

    return sync_detailed(
        service_uuid=service_uuid,
        role_name=role_name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    service_uuid: UUID,
    role_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: ObjectStorage2RoleUpdate | Unset = UNSET,
) -> Response[ObjectStorage2ErrorResponse | ObjectStorage2RoleResponse]:
    """Update Role

     Updates a service's IAM role.

    Args:
        service_uuid (UUID): The unique identifier for the service.
        role_name (str): A resource name.
        body (ObjectStorage2RoleUpdate | Unset): Schema for updating an existing role.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ObjectStorage2ErrorResponse | ObjectStorage2RoleResponse]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        role_name=role_name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_uuid: UUID,
    role_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: ObjectStorage2RoleUpdate | Unset = UNSET,
) -> ObjectStorage2ErrorResponse | ObjectStorage2RoleResponse | None:
    """Update Role

     Updates a service's IAM role.

    Args:
        service_uuid (UUID): The unique identifier for the service.
        role_name (str): A resource name.
        body (ObjectStorage2RoleUpdate | Unset): Schema for updating an existing role.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ObjectStorage2ErrorResponse | ObjectStorage2RoleResponse
    """

    return (
        await asyncio_detailed(
            service_uuid=service_uuid,
            role_name=role_name,
            client=client,
            body=body,
        )
    ).parsed
