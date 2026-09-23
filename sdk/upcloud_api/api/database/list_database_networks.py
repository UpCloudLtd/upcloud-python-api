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
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/database/{uuid}/networks".format(
            uuid=quote(str(uuid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DatabaseErrorResponse | list[DatabaseNetworkInformationDetailsResponse]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemasdatabase_networks_information_response_item_data in _response_200:
            componentsschemasdatabase_networks_information_response_item = (
                DatabaseNetworkInformationDetailsResponse.from_dict(
                    componentsschemasdatabase_networks_information_response_item_data
                )
            )

            response_200.append(componentsschemasdatabase_networks_information_response_item)

        return response_200

    response_default = DatabaseErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DatabaseErrorResponse | list[DatabaseNetworkInformationDetailsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DatabaseErrorResponse | list[DatabaseNetworkInformationDetailsResponse]]:
    """List networks

     Returns a list of attached SDN networks to a Managed Database service by its {uuid}.

    Args:
        uuid (UUID): The unique identifier for the integration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatabaseErrorResponse | list[DatabaseNetworkInformationDetailsResponse]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> DatabaseErrorResponse | list[DatabaseNetworkInformationDetailsResponse] | None:
    """List networks

     Returns a list of attached SDN networks to a Managed Database service by its {uuid}.

    Args:
        uuid (UUID): The unique identifier for the integration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatabaseErrorResponse | list[DatabaseNetworkInformationDetailsResponse]
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DatabaseErrorResponse | list[DatabaseNetworkInformationDetailsResponse]]:
    """List networks

     Returns a list of attached SDN networks to a Managed Database service by its {uuid}.

    Args:
        uuid (UUID): The unique identifier for the integration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatabaseErrorResponse | list[DatabaseNetworkInformationDetailsResponse]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> DatabaseErrorResponse | list[DatabaseNetworkInformationDetailsResponse] | None:
    """List networks

     Returns a list of attached SDN networks to a Managed Database service by its {uuid}.

    Args:
        uuid (UUID): The unique identifier for the integration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatabaseErrorResponse | list[DatabaseNetworkInformationDetailsResponse]
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
        )
    ).parsed
