from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.database_error_response import DatabaseErrorResponse
from ...models.database_network_information_details_response import DatabaseNetworkInformationDetailsResponse
from ...types import Response


def _get_kwargs(
    uuid: UUID,
    network_name: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/database/{uuid}/networks/{network_name}".format(
            uuid=quote(str(uuid), safe=""),
            network_name=quote(str(network_name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DatabaseErrorResponse | DatabaseNetworkInformationDetailsResponse:
    if response.status_code == 200:
        response_200 = DatabaseNetworkInformationDetailsResponse.from_dict(response.json())

        return response_200

    response_default = DatabaseErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DatabaseErrorResponse | DatabaseNetworkInformationDetailsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uuid: UUID,
    network_name: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DatabaseErrorResponse | DatabaseNetworkInformationDetailsResponse]:
    """Get network

     Returns the attached SDN network details to service by its {uuid} and {network_name}.

    Args:
        uuid (UUID): The unique identifier for the integration.
        network_name (UUID): The unique identifier for the integration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatabaseErrorResponse | DatabaseNetworkInformationDetailsResponse]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        network_name=network_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    network_name: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> DatabaseErrorResponse | DatabaseNetworkInformationDetailsResponse | None:
    """Get network

     Returns the attached SDN network details to service by its {uuid} and {network_name}.

    Args:
        uuid (UUID): The unique identifier for the integration.
        network_name (UUID): The unique identifier for the integration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatabaseErrorResponse | DatabaseNetworkInformationDetailsResponse
    """

    return sync_detailed(
        uuid=uuid,
        network_name=network_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    network_name: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DatabaseErrorResponse | DatabaseNetworkInformationDetailsResponse]:
    """Get network

     Returns the attached SDN network details to service by its {uuid} and {network_name}.

    Args:
        uuid (UUID): The unique identifier for the integration.
        network_name (UUID): The unique identifier for the integration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatabaseErrorResponse | DatabaseNetworkInformationDetailsResponse]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        network_name=network_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    network_name: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> DatabaseErrorResponse | DatabaseNetworkInformationDetailsResponse | None:
    """Get network

     Returns the attached SDN network details to service by its {uuid} and {network_name}.

    Args:
        uuid (UUID): The unique identifier for the integration.
        network_name (UUID): The unique identifier for the integration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatabaseErrorResponse | DatabaseNetworkInformationDetailsResponse
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            network_name=network_name,
            client=client,
        )
    ).parsed
