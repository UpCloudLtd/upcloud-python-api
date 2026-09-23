from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.database_error_response import DatabaseErrorResponse
from ...models.database_integration_endpoint_response import DatabaseIntegrationEndpointResponse
from ...types import Response


def _get_kwargs(
    integration_uuid: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/database/integration-endpoints/{integration_uuid}".format(
            integration_uuid=quote(str(integration_uuid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DatabaseErrorResponse | DatabaseIntegrationEndpointResponse:
    if response.status_code == 200:
        response_200 = DatabaseIntegrationEndpointResponse.from_dict(response.json())

        return response_200

    response_default = DatabaseErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DatabaseErrorResponse | DatabaseIntegrationEndpointResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    integration_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DatabaseErrorResponse | DatabaseIntegrationEndpointResponse]:
    """Get integration endpoint

     Returns integration endpoint details by given {integration-uuid}.

    Args:
        integration_uuid (UUID): The unique identifier for the service.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatabaseErrorResponse | DatabaseIntegrationEndpointResponse]
    """

    kwargs = _get_kwargs(
        integration_uuid=integration_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    integration_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> DatabaseErrorResponse | DatabaseIntegrationEndpointResponse | None:
    """Get integration endpoint

     Returns integration endpoint details by given {integration-uuid}.

    Args:
        integration_uuid (UUID): The unique identifier for the service.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatabaseErrorResponse | DatabaseIntegrationEndpointResponse
    """

    return sync_detailed(
        integration_uuid=integration_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    integration_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DatabaseErrorResponse | DatabaseIntegrationEndpointResponse]:
    """Get integration endpoint

     Returns integration endpoint details by given {integration-uuid}.

    Args:
        integration_uuid (UUID): The unique identifier for the service.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatabaseErrorResponse | DatabaseIntegrationEndpointResponse]
    """

    kwargs = _get_kwargs(
        integration_uuid=integration_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    integration_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> DatabaseErrorResponse | DatabaseIntegrationEndpointResponse | None:
    """Get integration endpoint

     Returns integration endpoint details by given {integration-uuid}.

    Args:
        integration_uuid (UUID): The unique identifier for the service.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatabaseErrorResponse | DatabaseIntegrationEndpointResponse
    """

    return (
        await asyncio_detailed(
            integration_uuid=integration_uuid,
            client=client,
        )
    ).parsed
