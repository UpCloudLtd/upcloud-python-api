from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.file_storage_acl_create import FileStorageAclCreate
from ...models.file_storage_acl_detail_response import FileStorageAclDetailResponse
from ...models.file_storage_error_response import FileStorageErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    service_uuid: UUID,
    share_name: str,
    *,
    body: FileStorageAclCreate | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/1.3/file-storage/{service_uuid}/shares/{share_name}/acl".format(
            service_uuid=quote(str(service_uuid), safe=""),
            share_name=quote(str(share_name), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FileStorageAclDetailResponse | FileStorageErrorResponse:
    if response.status_code == 201:
        response_201 = FileStorageAclDetailResponse.from_dict(response.json())

        return response_201

    response_default = FileStorageErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[FileStorageAclDetailResponse | FileStorageErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    service_uuid: UUID,
    share_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: FileStorageAclCreate | Unset = UNSET,
) -> Response[FileStorageAclDetailResponse | FileStorageErrorResponse]:
    """Create ACL

     Creates a new share ACL by given {service_uuid} and {share_name}.

    Args:
        service_uuid (UUID): The unique identifier.
        share_name (str): A resource name.
        body (FileStorageAclCreate | Unset): Schema for creating an ACL entry.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FileStorageAclDetailResponse | FileStorageErrorResponse]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        share_name=share_name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_uuid: UUID,
    share_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: FileStorageAclCreate | Unset = UNSET,
) -> FileStorageAclDetailResponse | FileStorageErrorResponse | None:
    """Create ACL

     Creates a new share ACL by given {service_uuid} and {share_name}.

    Args:
        service_uuid (UUID): The unique identifier.
        share_name (str): A resource name.
        body (FileStorageAclCreate | Unset): Schema for creating an ACL entry.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FileStorageAclDetailResponse | FileStorageErrorResponse
    """

    return sync_detailed(
        service_uuid=service_uuid,
        share_name=share_name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    service_uuid: UUID,
    share_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: FileStorageAclCreate | Unset = UNSET,
) -> Response[FileStorageAclDetailResponse | FileStorageErrorResponse]:
    """Create ACL

     Creates a new share ACL by given {service_uuid} and {share_name}.

    Args:
        service_uuid (UUID): The unique identifier.
        share_name (str): A resource name.
        body (FileStorageAclCreate | Unset): Schema for creating an ACL entry.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FileStorageAclDetailResponse | FileStorageErrorResponse]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        share_name=share_name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_uuid: UUID,
    share_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: FileStorageAclCreate | Unset = UNSET,
) -> FileStorageAclDetailResponse | FileStorageErrorResponse | None:
    """Create ACL

     Creates a new share ACL by given {service_uuid} and {share_name}.

    Args:
        service_uuid (UUID): The unique identifier.
        share_name (str): A resource name.
        body (FileStorageAclCreate | Unset): Schema for creating an ACL entry.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FileStorageAclDetailResponse | FileStorageErrorResponse
    """

    return (
        await asyncio_detailed(
            service_uuid=service_uuid,
            share_name=share_name,
            client=client,
            body=body,
        )
    ).parsed
