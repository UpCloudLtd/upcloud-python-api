from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.object_storage_2_error_response import ObjectStorage2ErrorResponse
from ...models.object_storage_2_tag_list_response_item import ObjectStorage2TagListResponseItem
from ...models.tag_list_request import TagListRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    service_uuid: UUID,
    role_name: str,
    *,
    body: list[TagListRequest] | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/1.3/object-storage-2/{service_uuid}/roles/{role_name}/tags".format(
            service_uuid=quote(str(service_uuid), safe=""),
            role_name=quote(str(role_name), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = []
        for componentsschemasobject_storage_2_tag_list_request_item_data in body:
            componentsschemasobject_storage_2_tag_list_request_item = (
                componentsschemasobject_storage_2_tag_list_request_item_data.to_dict()
            )
            _kwargs["json"].append(componentsschemasobject_storage_2_tag_list_request_item)

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ObjectStorage2ErrorResponse | list[ObjectStorage2TagListResponseItem]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemasobject_storage_2_tag_list_response_item_data in _response_200:
            componentsschemasobject_storage_2_tag_list_response_item = ObjectStorage2TagListResponseItem.from_dict(
                componentsschemasobject_storage_2_tag_list_response_item_data
            )

            response_200.append(componentsschemasobject_storage_2_tag_list_response_item)

        return response_200

    response_default = ObjectStorage2ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ObjectStorage2ErrorResponse | list[ObjectStorage2TagListResponseItem]]:
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
    body: list[TagListRequest] | Unset = UNSET,
) -> Response[ObjectStorage2ErrorResponse | list[ObjectStorage2TagListResponseItem]]:
    """Replace role tags

     Replaces a role's tags by the given {service_uuid}, and {role_name}.

    Args:
        service_uuid (UUID): The unique identifier for the service.
        role_name (str): A resource name.
        body (list[TagListRequest] | Unset): Schema for a list of tags to apply to a resource.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ObjectStorage2ErrorResponse | list[ObjectStorage2TagListResponseItem]]
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
    body: list[TagListRequest] | Unset = UNSET,
) -> ObjectStorage2ErrorResponse | list[ObjectStorage2TagListResponseItem] | None:
    """Replace role tags

     Replaces a role's tags by the given {service_uuid}, and {role_name}.

    Args:
        service_uuid (UUID): The unique identifier for the service.
        role_name (str): A resource name.
        body (list[TagListRequest] | Unset): Schema for a list of tags to apply to a resource.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ObjectStorage2ErrorResponse | list[ObjectStorage2TagListResponseItem]
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
    body: list[TagListRequest] | Unset = UNSET,
) -> Response[ObjectStorage2ErrorResponse | list[ObjectStorage2TagListResponseItem]]:
    """Replace role tags

     Replaces a role's tags by the given {service_uuid}, and {role_name}.

    Args:
        service_uuid (UUID): The unique identifier for the service.
        role_name (str): A resource name.
        body (list[TagListRequest] | Unset): Schema for a list of tags to apply to a resource.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ObjectStorage2ErrorResponse | list[ObjectStorage2TagListResponseItem]]
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
    body: list[TagListRequest] | Unset = UNSET,
) -> ObjectStorage2ErrorResponse | list[ObjectStorage2TagListResponseItem] | None:
    """Replace role tags

     Replaces a role's tags by the given {service_uuid}, and {role_name}.

    Args:
        service_uuid (UUID): The unique identifier for the service.
        role_name (str): A resource name.
        body (list[TagListRequest] | Unset): Schema for a list of tags to apply to a resource.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ObjectStorage2ErrorResponse | list[ObjectStorage2TagListResponseItem]
    """

    return (
        await asyncio_detailed(
            service_uuid=service_uuid,
            role_name=role_name,
            client=client,
            body=body,
        )
    ).parsed
