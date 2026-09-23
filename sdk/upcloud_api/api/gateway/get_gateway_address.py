from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.gateway_address_details_response import GatewayAddressDetailsResponse
from ...types import Response


def _get_kwargs(
    service_uuid: UUID,
    address_name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/gateway/{service_uuid}/addresses/{address_name}".format(
            service_uuid=quote(str(service_uuid), safe=""),
            address_name=quote(str(address_name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GatewayAddressDetailsResponse | None:
    if response.status_code == 200:
        response_200 = GatewayAddressDetailsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GatewayAddressDetailsResponse]:
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
) -> Response[GatewayAddressDetailsResponse]:
    """Get Service Address Details

     Get service address details.

    Args:
        service_uuid (UUID): The unique identifier for the resource.
        address_name (str): The name for the resource.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GatewayAddressDetailsResponse]
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
) -> GatewayAddressDetailsResponse | None:
    """Get Service Address Details

     Get service address details.

    Args:
        service_uuid (UUID): The unique identifier for the resource.
        address_name (str): The name for the resource.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GatewayAddressDetailsResponse
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
) -> Response[GatewayAddressDetailsResponse]:
    """Get Service Address Details

     Get service address details.

    Args:
        service_uuid (UUID): The unique identifier for the resource.
        address_name (str): The name for the resource.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GatewayAddressDetailsResponse]
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
) -> GatewayAddressDetailsResponse | None:
    """Get Service Address Details

     Get service address details.

    Args:
        service_uuid (UUID): The unique identifier for the resource.
        address_name (str): The name for the resource.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GatewayAddressDetailsResponse
    """

    return (
        await asyncio_detailed(
            service_uuid=service_uuid,
            address_name=address_name,
            client=client,
        )
    ).parsed
