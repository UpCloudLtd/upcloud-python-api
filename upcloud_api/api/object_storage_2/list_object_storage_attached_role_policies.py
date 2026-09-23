from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.object_storage_2_error_response import ObjectStorage2ErrorResponse
from ...models.object_storage_2_policy_attachment_response import ObjectStorage2PolicyAttachmentResponse
from ...types import Response


def _get_kwargs(
    service_uuid: UUID,
    role_name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/object-storage-2/{service_uuid}/roles/{role_name}/policies".format(
            service_uuid=quote(str(service_uuid), safe=""),
            role_name=quote(str(role_name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ObjectStorage2ErrorResponse | list[ObjectStorage2PolicyAttachmentResponse]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemasobject_storage_2_policy_attachment_list_response_item_data in _response_200:
            componentsschemasobject_storage_2_policy_attachment_list_response_item = (
                ObjectStorage2PolicyAttachmentResponse.from_dict(
                    componentsschemasobject_storage_2_policy_attachment_list_response_item_data
                )
            )

            response_200.append(componentsschemasobject_storage_2_policy_attachment_list_response_item)

        return response_200

    response_default = ObjectStorage2ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ObjectStorage2ErrorResponse | list[ObjectStorage2PolicyAttachmentResponse]]:
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
) -> Response[ObjectStorage2ErrorResponse | list[ObjectStorage2PolicyAttachmentResponse]]:
    """List Attached Role Policies

     Lists all policies attached to a service's IAM role.

    Args:
        service_uuid (UUID): The unique identifier for the service.
        role_name (str): A resource name.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ObjectStorage2ErrorResponse | list[ObjectStorage2PolicyAttachmentResponse]]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        role_name=role_name,
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
) -> ObjectStorage2ErrorResponse | list[ObjectStorage2PolicyAttachmentResponse] | None:
    """List Attached Role Policies

     Lists all policies attached to a service's IAM role.

    Args:
        service_uuid (UUID): The unique identifier for the service.
        role_name (str): A resource name.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ObjectStorage2ErrorResponse | list[ObjectStorage2PolicyAttachmentResponse]
    """

    return sync_detailed(
        service_uuid=service_uuid,
        role_name=role_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    service_uuid: UUID,
    role_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ObjectStorage2ErrorResponse | list[ObjectStorage2PolicyAttachmentResponse]]:
    """List Attached Role Policies

     Lists all policies attached to a service's IAM role.

    Args:
        service_uuid (UUID): The unique identifier for the service.
        role_name (str): A resource name.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ObjectStorage2ErrorResponse | list[ObjectStorage2PolicyAttachmentResponse]]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        role_name=role_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_uuid: UUID,
    role_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> ObjectStorage2ErrorResponse | list[ObjectStorage2PolicyAttachmentResponse] | None:
    """List Attached Role Policies

     Lists all policies attached to a service's IAM role.

    Args:
        service_uuid (UUID): The unique identifier for the service.
        role_name (str): A resource name.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ObjectStorage2ErrorResponse | list[ObjectStorage2PolicyAttachmentResponse]
    """

    return (
        await asyncio_detailed(
            service_uuid=service_uuid,
            role_name=role_name,
            client=client,
        )
    ).parsed
