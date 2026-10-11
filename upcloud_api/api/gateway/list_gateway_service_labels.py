from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.gateway_error_response import GatewayErrorResponse
from ...models.gateway_label_details_response import GatewayLabelDetailsResponse
from ...types import Response


def _get_kwargs(
    service_uuid: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/gateway/{service_uuid}/labels".format(
            service_uuid=quote(str(service_uuid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GatewayErrorResponse | list[GatewayLabelDetailsResponse]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemasgateway_service_label_list_response_item_data in _response_200:
            componentsschemasgateway_service_label_list_response_item = GatewayLabelDetailsResponse.from_dict(
                componentsschemasgateway_service_label_list_response_item_data
            )

            response_200.append(componentsschemasgateway_service_label_list_response_item)

        return response_200

    response_default = GatewayErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GatewayErrorResponse | list[GatewayLabelDetailsResponse]]:
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
) -> Response[GatewayErrorResponse | list[GatewayLabelDetailsResponse]]:
    """List Service Labels

     List available service labels for service.

    Args:
        service_uuid (UUID): The unique identifier for the resource.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GatewayErrorResponse | list[GatewayLabelDetailsResponse]]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> GatewayErrorResponse | list[GatewayLabelDetailsResponse] | None:
    """List Service Labels

     List available service labels for service.

    Args:
        service_uuid (UUID): The unique identifier for the resource.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GatewayErrorResponse | list[GatewayLabelDetailsResponse]
    """

    return sync_detailed(
        service_uuid=service_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    service_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GatewayErrorResponse | list[GatewayLabelDetailsResponse]]:
    """List Service Labels

     List available service labels for service.

    Args:
        service_uuid (UUID): The unique identifier for the resource.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GatewayErrorResponse | list[GatewayLabelDetailsResponse]]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> GatewayErrorResponse | list[GatewayLabelDetailsResponse] | None:
    """List Service Labels

     List available service labels for service.

    Args:
        service_uuid (UUID): The unique identifier for the resource.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GatewayErrorResponse | list[GatewayLabelDetailsResponse]
    """

    return (
        await asyncio_detailed(
            service_uuid=service_uuid,
            client=client,
        )
    ).parsed
