from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.gateway_error_response import GatewayErrorResponse
from ...models.gateway_service_log_session_create_request import GatewayServiceLogSessionCreateRequest
from ...models.gateway_service_log_session_create_response import GatewayServiceLogSessionCreateResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    service_uuid: UUID,
    *,
    body: GatewayServiceLogSessionCreateRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/1.3/gateway/{service_uuid}/logs".format(
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
) -> GatewayErrorResponse | GatewayServiceLogSessionCreateResponse:
    if response.status_code == 200:
        response_200 = GatewayServiceLogSessionCreateResponse.from_dict(response.json())

        return response_200

    response_default = GatewayErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GatewayErrorResponse | GatewayServiceLogSessionCreateResponse]:
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
    body: GatewayServiceLogSessionCreateRequest | Unset = UNSET,
) -> Response[GatewayErrorResponse | GatewayServiceLogSessionCreateResponse]:
    """Create Service Log Session

     Create a new service log session.

    Args:
        service_uuid (UUID): The unique identifier for the resource.
        body (GatewayServiceLogSessionCreateRequest | Unset): Request to create a new log session
            for a service.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GatewayErrorResponse | GatewayServiceLogSessionCreateResponse]
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
    body: GatewayServiceLogSessionCreateRequest | Unset = UNSET,
) -> GatewayErrorResponse | GatewayServiceLogSessionCreateResponse | None:
    """Create Service Log Session

     Create a new service log session.

    Args:
        service_uuid (UUID): The unique identifier for the resource.
        body (GatewayServiceLogSessionCreateRequest | Unset): Request to create a new log session
            for a service.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GatewayErrorResponse | GatewayServiceLogSessionCreateResponse
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
    body: GatewayServiceLogSessionCreateRequest | Unset = UNSET,
) -> Response[GatewayErrorResponse | GatewayServiceLogSessionCreateResponse]:
    """Create Service Log Session

     Create a new service log session.

    Args:
        service_uuid (UUID): The unique identifier for the resource.
        body (GatewayServiceLogSessionCreateRequest | Unset): Request to create a new log session
            for a service.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GatewayErrorResponse | GatewayServiceLogSessionCreateResponse]
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
    body: GatewayServiceLogSessionCreateRequest | Unset = UNSET,
) -> GatewayErrorResponse | GatewayServiceLogSessionCreateResponse | None:
    """Create Service Log Session

     Create a new service log session.

    Args:
        service_uuid (UUID): The unique identifier for the resource.
        body (GatewayServiceLogSessionCreateRequest | Unset): Request to create a new log session
            for a service.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GatewayErrorResponse | GatewayServiceLogSessionCreateResponse
    """

    return (
        await asyncio_detailed(
            service_uuid=service_uuid,
            client=client,
            body=body,
        )
    ).parsed
