from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.database_error_response import DatabaseErrorResponse
from ...models.database_integration_endpoint_response import DatabaseIntegrationEndpointResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/database/integration-endpoints",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DatabaseErrorResponse | list[DatabaseIntegrationEndpointResponse]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemasdatabase_integration_endpoints_response_item_data in _response_200:
            componentsschemasdatabase_integration_endpoints_response_item = (
                DatabaseIntegrationEndpointResponse.from_dict(
                    componentsschemasdatabase_integration_endpoints_response_item_data
                )
            )

            response_200.append(componentsschemasdatabase_integration_endpoints_response_item)

        return response_200

    response_default = DatabaseErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DatabaseErrorResponse | list[DatabaseIntegrationEndpointResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[DatabaseErrorResponse | list[DatabaseIntegrationEndpointResponse]]:
    """List integration endpoints

     Returns a list of available integration endpoints.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatabaseErrorResponse | list[DatabaseIntegrationEndpointResponse]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> DatabaseErrorResponse | list[DatabaseIntegrationEndpointResponse] | None:
    """List integration endpoints

     Returns a list of available integration endpoints.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatabaseErrorResponse | list[DatabaseIntegrationEndpointResponse]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[DatabaseErrorResponse | list[DatabaseIntegrationEndpointResponse]]:
    """List integration endpoints

     Returns a list of available integration endpoints.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatabaseErrorResponse | list[DatabaseIntegrationEndpointResponse]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> DatabaseErrorResponse | list[DatabaseIntegrationEndpointResponse] | None:
    """List integration endpoints

     Returns a list of available integration endpoints.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatabaseErrorResponse | list[DatabaseIntegrationEndpointResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
