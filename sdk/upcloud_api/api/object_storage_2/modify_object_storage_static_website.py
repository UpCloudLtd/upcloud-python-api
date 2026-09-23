from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.object_storage_2_error_response import ObjectStorage2ErrorResponse
from ...models.object_storage_2_static_website_config import ObjectStorage2StaticWebsiteConfig
from ...models.object_storage_2_static_website_config_modify import ObjectStorage2StaticWebsiteConfigModify
from ...types import UNSET, Response, Unset


def _get_kwargs(
    service_uuid: UUID,
    custom_domain_name: str,
    *,
    body: ObjectStorage2StaticWebsiteConfigModify | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/1.3/object-storage-2/{service_uuid}/static-websites/{custom_domain_name}".format(
            service_uuid=quote(str(service_uuid), safe=""),
            custom_domain_name=quote(str(custom_domain_name), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ObjectStorage2ErrorResponse | ObjectStorage2StaticWebsiteConfig:
    if response.status_code == 200:
        response_200 = ObjectStorage2StaticWebsiteConfig.from_dict(response.json())

        return response_200

    response_default = ObjectStorage2ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ObjectStorage2ErrorResponse | ObjectStorage2StaticWebsiteConfig]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    service_uuid: UUID,
    custom_domain_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: ObjectStorage2StaticWebsiteConfigModify | Unset = UNSET,
) -> Response[ObjectStorage2ErrorResponse | ObjectStorage2StaticWebsiteConfig]:
    """Modify static website configuration

     Updates an existing static website configuration.

    Args:
        service_uuid (UUID): The unique identifier for the service.
        custom_domain_name (str): A valid hostname for the custom domain. Supports both apex
            domains (example.com) and subdomains (objects.example.com).
        body (ObjectStorage2StaticWebsiteConfigModify | Unset): Request body for updating a static
            website configuration

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ObjectStorage2ErrorResponse | ObjectStorage2StaticWebsiteConfig]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        custom_domain_name=custom_domain_name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_uuid: UUID,
    custom_domain_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: ObjectStorage2StaticWebsiteConfigModify | Unset = UNSET,
) -> ObjectStorage2ErrorResponse | ObjectStorage2StaticWebsiteConfig | None:
    """Modify static website configuration

     Updates an existing static website configuration.

    Args:
        service_uuid (UUID): The unique identifier for the service.
        custom_domain_name (str): A valid hostname for the custom domain. Supports both apex
            domains (example.com) and subdomains (objects.example.com).
        body (ObjectStorage2StaticWebsiteConfigModify | Unset): Request body for updating a static
            website configuration

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ObjectStorage2ErrorResponse | ObjectStorage2StaticWebsiteConfig
    """

    return sync_detailed(
        service_uuid=service_uuid,
        custom_domain_name=custom_domain_name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    service_uuid: UUID,
    custom_domain_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: ObjectStorage2StaticWebsiteConfigModify | Unset = UNSET,
) -> Response[ObjectStorage2ErrorResponse | ObjectStorage2StaticWebsiteConfig]:
    """Modify static website configuration

     Updates an existing static website configuration.

    Args:
        service_uuid (UUID): The unique identifier for the service.
        custom_domain_name (str): A valid hostname for the custom domain. Supports both apex
            domains (example.com) and subdomains (objects.example.com).
        body (ObjectStorage2StaticWebsiteConfigModify | Unset): Request body for updating a static
            website configuration

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ObjectStorage2ErrorResponse | ObjectStorage2StaticWebsiteConfig]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        custom_domain_name=custom_domain_name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_uuid: UUID,
    custom_domain_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: ObjectStorage2StaticWebsiteConfigModify | Unset = UNSET,
) -> ObjectStorage2ErrorResponse | ObjectStorage2StaticWebsiteConfig | None:
    """Modify static website configuration

     Updates an existing static website configuration.

    Args:
        service_uuid (UUID): The unique identifier for the service.
        custom_domain_name (str): A valid hostname for the custom domain. Supports both apex
            domains (example.com) and subdomains (objects.example.com).
        body (ObjectStorage2StaticWebsiteConfigModify | Unset): Request body for updating a static
            website configuration

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ObjectStorage2ErrorResponse | ObjectStorage2StaticWebsiteConfig
    """

    return (
        await asyncio_detailed(
            service_uuid=service_uuid,
            custom_domain_name=custom_domain_name,
            client=client,
            body=body,
        )
    ).parsed
