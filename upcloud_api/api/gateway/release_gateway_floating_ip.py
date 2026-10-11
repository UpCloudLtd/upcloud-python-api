from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.gateway_error_response import GatewayErrorResponse
from ...types import Response


def _get_kwargs(
    service_uuid: UUID,
    address_name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/1.3/gateway/{service_uuid}/addresses/{address_name}/release".format(
            service_uuid=quote(str(service_uuid), safe=""),
            address_name=quote(str(address_name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | GatewayErrorResponse:
    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = GatewayErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GatewayErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    service_uuid: UUID,
    address_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GatewayErrorResponse]:
    """Release Gateway Floating IP

     Release the user-provisioned Floating IP of an existing service address by given {service-address-
    identifier}, reverting it to a service-provisioned address while keeping the same name.

    Args:
        service_uuid (UUID): The unique identifier for the resource.
        address_name (str): The name for the resource.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GatewayErrorResponse]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        address_name=address_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_uuid: UUID,
    address_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GatewayErrorResponse | None:
    """Release Gateway Floating IP

     Release the user-provisioned Floating IP of an existing service address by given {service-address-
    identifier}, reverting it to a service-provisioned address while keeping the same name.

    Args:
        service_uuid (UUID): The unique identifier for the resource.
        address_name (str): The name for the resource.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GatewayErrorResponse
    """

    return sync_detailed(
        service_uuid=service_uuid,
        address_name=address_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    service_uuid: UUID,
    address_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GatewayErrorResponse]:
    """Release Gateway Floating IP

     Release the user-provisioned Floating IP of an existing service address by given {service-address-
    identifier}, reverting it to a service-provisioned address while keeping the same name.

    Args:
        service_uuid (UUID): The unique identifier for the resource.
        address_name (str): The name for the resource.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GatewayErrorResponse]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        address_name=address_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_uuid: UUID,
    address_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GatewayErrorResponse | None:
    """Release Gateway Floating IP

     Release the user-provisioned Floating IP of an existing service address by given {service-address-
    identifier}, reverting it to a service-provisioned address while keeping the same name.

    Args:
        service_uuid (UUID): The unique identifier for the resource.
        address_name (str): The name for the resource.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GatewayErrorResponse
    """

    return (
        await asyncio_detailed(
            service_uuid=service_uuid,
            address_name=address_name,
            client=client,
        )
    ).parsed
