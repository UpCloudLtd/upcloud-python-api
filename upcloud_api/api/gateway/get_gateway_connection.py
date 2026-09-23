from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.gateway_connection_details_response import GatewayConnectionDetailsResponse
from ...types import Response


def _get_kwargs(
    service_uuid: UUID,
    connection_uuid: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/gateway/{service_uuid}/connections/{connection_uuid}".format(
            service_uuid=quote(str(service_uuid), safe=""),
            connection_uuid=quote(str(connection_uuid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GatewayConnectionDetailsResponse | None:
    if response.status_code == 200:
        response_200 = GatewayConnectionDetailsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GatewayConnectionDetailsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    service_uuid: UUID,
    connection_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GatewayConnectionDetailsResponse]:
    """Get Connection Details

     Get connection details.

    Args:
        service_uuid (UUID): The unique identifier for the resource.
        connection_uuid (UUID): The unique identifier for the resource.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GatewayConnectionDetailsResponse]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        connection_uuid=connection_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_uuid: UUID,
    connection_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> GatewayConnectionDetailsResponse | None:
    """Get Connection Details

     Get connection details.

    Args:
        service_uuid (UUID): The unique identifier for the resource.
        connection_uuid (UUID): The unique identifier for the resource.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GatewayConnectionDetailsResponse
    """

    return sync_detailed(
        service_uuid=service_uuid,
        connection_uuid=connection_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    service_uuid: UUID,
    connection_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GatewayConnectionDetailsResponse]:
    """Get Connection Details

     Get connection details.

    Args:
        service_uuid (UUID): The unique identifier for the resource.
        connection_uuid (UUID): The unique identifier for the resource.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GatewayConnectionDetailsResponse]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        connection_uuid=connection_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_uuid: UUID,
    connection_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> GatewayConnectionDetailsResponse | None:
    """Get Connection Details

     Get connection details.

    Args:
        service_uuid (UUID): The unique identifier for the resource.
        connection_uuid (UUID): The unique identifier for the resource.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GatewayConnectionDetailsResponse
    """

    return (
        await asyncio_detailed(
            service_uuid=service_uuid,
            connection_uuid=connection_uuid,
            client=client,
        )
    ).parsed
