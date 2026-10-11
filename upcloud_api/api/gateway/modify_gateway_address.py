from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.gateway_address_details_response import GatewayAddressDetailsResponse
from ...models.gateway_address_modify_request import GatewayAddressModifyRequest
from ...models.gateway_error_response import GatewayErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    service_uuid: UUID,
    address_name: str,
    *,
    body: GatewayAddressModifyRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/1.3/gateway/{service_uuid}/addresses/{address_name}".format(
            service_uuid=quote(str(service_uuid), safe=""),
            address_name=quote(str(address_name), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GatewayAddressDetailsResponse | GatewayErrorResponse:
    if response.status_code == 200:
        response_200 = GatewayAddressDetailsResponse.from_dict(response.json())

        return response_200

    response_default = GatewayErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GatewayAddressDetailsResponse | GatewayErrorResponse]:
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
    body: GatewayAddressModifyRequest | Unset = UNSET,
) -> Response[GatewayAddressDetailsResponse | GatewayErrorResponse]:
    """Modify Service Address

     Modify existing service address by given {service-address-identifier}.

    Args:
        service_uuid (UUID): The unique identifier for the resource.
        address_name (str): The name for the resource.
        body (GatewayAddressModifyRequest | Unset): Gateway service address modify request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GatewayAddressDetailsResponse | GatewayErrorResponse]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        address_name=address_name,
        body=body,
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
    body: GatewayAddressModifyRequest | Unset = UNSET,
) -> GatewayAddressDetailsResponse | GatewayErrorResponse | None:
    """Modify Service Address

     Modify existing service address by given {service-address-identifier}.

    Args:
        service_uuid (UUID): The unique identifier for the resource.
        address_name (str): The name for the resource.
        body (GatewayAddressModifyRequest | Unset): Gateway service address modify request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GatewayAddressDetailsResponse | GatewayErrorResponse
    """

    return sync_detailed(
        service_uuid=service_uuid,
        address_name=address_name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    service_uuid: UUID,
    address_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: GatewayAddressModifyRequest | Unset = UNSET,
) -> Response[GatewayAddressDetailsResponse | GatewayErrorResponse]:
    """Modify Service Address

     Modify existing service address by given {service-address-identifier}.

    Args:
        service_uuid (UUID): The unique identifier for the resource.
        address_name (str): The name for the resource.
        body (GatewayAddressModifyRequest | Unset): Gateway service address modify request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GatewayAddressDetailsResponse | GatewayErrorResponse]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        address_name=address_name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_uuid: UUID,
    address_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: GatewayAddressModifyRequest | Unset = UNSET,
) -> GatewayAddressDetailsResponse | GatewayErrorResponse | None:
    """Modify Service Address

     Modify existing service address by given {service-address-identifier}.

    Args:
        service_uuid (UUID): The unique identifier for the resource.
        address_name (str): The name for the resource.
        body (GatewayAddressModifyRequest | Unset): Gateway service address modify request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GatewayAddressDetailsResponse | GatewayErrorResponse
    """

    return (
        await asyncio_detailed(
            service_uuid=service_uuid,
            address_name=address_name,
            client=client,
            body=body,
        )
    ).parsed
