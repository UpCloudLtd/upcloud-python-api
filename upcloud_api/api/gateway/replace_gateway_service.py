from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.gateway_error_response import GatewayErrorResponse
from ...models.gateway_service_details_response import GatewayServiceDetailsResponse
from ...models.gateway_service_replace_request import GatewayServiceReplaceRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    service_uuid: UUID,
    *,
    body: GatewayServiceReplaceRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/1.3/gateway/{service_uuid}".format(
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
) -> GatewayErrorResponse | GatewayServiceDetailsResponse:
    if response.status_code == 200:
        response_200 = GatewayServiceDetailsResponse.from_dict(response.json())

        return response_200

    response_default = GatewayErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GatewayErrorResponse | GatewayServiceDetailsResponse]:
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
    body: GatewayServiceReplaceRequest | Unset = UNSET,
) -> Response[GatewayErrorResponse | GatewayServiceDetailsResponse]:
    """Replace Service

     Replace service configuration.

    Args:
        service_uuid (UUID): The unique identifier for the resource.
        body (GatewayServiceReplaceRequest | Unset): Request to replace a gateway service

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GatewayErrorResponse | GatewayServiceDetailsResponse]
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
    body: GatewayServiceReplaceRequest | Unset = UNSET,
) -> GatewayErrorResponse | GatewayServiceDetailsResponse | None:
    """Replace Service

     Replace service configuration.

    Args:
        service_uuid (UUID): The unique identifier for the resource.
        body (GatewayServiceReplaceRequest | Unset): Request to replace a gateway service

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GatewayErrorResponse | GatewayServiceDetailsResponse
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
    body: GatewayServiceReplaceRequest | Unset = UNSET,
) -> Response[GatewayErrorResponse | GatewayServiceDetailsResponse]:
    """Replace Service

     Replace service configuration.

    Args:
        service_uuid (UUID): The unique identifier for the resource.
        body (GatewayServiceReplaceRequest | Unset): Request to replace a gateway service

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GatewayErrorResponse | GatewayServiceDetailsResponse]
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
    body: GatewayServiceReplaceRequest | Unset = UNSET,
) -> GatewayErrorResponse | GatewayServiceDetailsResponse | None:
    """Replace Service

     Replace service configuration.

    Args:
        service_uuid (UUID): The unique identifier for the resource.
        body (GatewayServiceReplaceRequest | Unset): Request to replace a gateway service

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GatewayErrorResponse | GatewayServiceDetailsResponse
    """

    return (
        await asyncio_detailed(
            service_uuid=service_uuid,
            client=client,
            body=body,
        )
    ).parsed
