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
    custom_domain_name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/1.3/object-storage-2/{service_uuid}/static-websites/{custom_domain_name}".format(
            service_uuid=quote(str(service_uuid), safe=""),
            custom_domain_name=quote(str(custom_domain_name), safe=""),
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
    custom_domain_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | ObjectStorage2ErrorResponse]:
    """Delete static website configuration

     Deletes a static website configuration.

    Args:
        service_uuid (UUID): The unique identifier for the service.
        custom_domain_name (str): A valid hostname for the custom domain. Supports both apex
            domains (example.com) and subdomains (objects.example.com).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ObjectStorage2ErrorResponse]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        custom_domain_name=custom_domain_name,
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
) -> Any | ObjectStorage2ErrorResponse | None:
    """Delete static website configuration

     Deletes a static website configuration.

    Args:
        service_uuid (UUID): The unique identifier for the service.
        custom_domain_name (str): A valid hostname for the custom domain. Supports both apex
            domains (example.com) and subdomains (objects.example.com).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ObjectStorage2ErrorResponse
    """

    return sync_detailed(
        service_uuid=service_uuid,
        custom_domain_name=custom_domain_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    service_uuid: UUID,
    custom_domain_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | ObjectStorage2ErrorResponse]:
    """Delete static website configuration

     Deletes a static website configuration.

    Args:
        service_uuid (UUID): The unique identifier for the service.
        custom_domain_name (str): A valid hostname for the custom domain. Supports both apex
            domains (example.com) and subdomains (objects.example.com).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ObjectStorage2ErrorResponse]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        custom_domain_name=custom_domain_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_uuid: UUID,
    custom_domain_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | ObjectStorage2ErrorResponse | None:
    """Delete static website configuration

     Deletes a static website configuration.

    Args:
        service_uuid (UUID): The unique identifier for the service.
        custom_domain_name (str): A valid hostname for the custom domain. Supports both apex
            domains (example.com) and subdomains (objects.example.com).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ObjectStorage2ErrorResponse
    """

    return (
        await asyncio_detailed(
            service_uuid=service_uuid,
            custom_domain_name=custom_domain_name,
            client=client,
        )
    ).parsed
