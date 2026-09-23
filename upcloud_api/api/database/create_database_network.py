from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.database_error_response import DatabaseErrorResponse
from ...models.database_network_create import DatabaseNetworkCreate
from ...models.database_network_information_details_response import DatabaseNetworkInformationDetailsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    *,
    body: DatabaseNetworkCreate | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/1.3/database/{uuid}/networks".format(
            uuid=quote(str(uuid), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DatabaseErrorResponse | DatabaseNetworkInformationDetailsResponse:
    if response.status_code == 201:
        response_201 = DatabaseNetworkInformationDetailsResponse.from_dict(response.json())

        return response_201

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
    *,
    client: AuthenticatedClient | Client,
    body: DatabaseNetworkCreate | Unset = UNSET,
) -> Response[DatabaseErrorResponse | DatabaseNetworkInformationDetailsResponse]:
    """Create network

     Attaches an SDN network to a Managed Database service by its {uuid}.

    Args:
        uuid (UUID): The unique identifier for the integration.
        body (DatabaseNetworkCreate | Unset): Schema for creating a network.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatabaseErrorResponse | DatabaseNetworkInformationDetailsResponse]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: DatabaseNetworkCreate | Unset = UNSET,
) -> DatabaseErrorResponse | DatabaseNetworkInformationDetailsResponse | None:
    """Create network

     Attaches an SDN network to a Managed Database service by its {uuid}.

    Args:
        uuid (UUID): The unique identifier for the integration.
        body (DatabaseNetworkCreate | Unset): Schema for creating a network.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatabaseErrorResponse | DatabaseNetworkInformationDetailsResponse
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: DatabaseNetworkCreate | Unset = UNSET,
) -> Response[DatabaseErrorResponse | DatabaseNetworkInformationDetailsResponse]:
    """Create network

     Attaches an SDN network to a Managed Database service by its {uuid}.

    Args:
        uuid (UUID): The unique identifier for the integration.
        body (DatabaseNetworkCreate | Unset): Schema for creating a network.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatabaseErrorResponse | DatabaseNetworkInformationDetailsResponse]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: DatabaseNetworkCreate | Unset = UNSET,
) -> DatabaseErrorResponse | DatabaseNetworkInformationDetailsResponse | None:
    """Create network

     Attaches an SDN network to a Managed Database service by its {uuid}.

    Args:
        uuid (UUID): The unique identifier for the integration.
        body (DatabaseNetworkCreate | Unset): Schema for creating a network.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatabaseErrorResponse | DatabaseNetworkInformationDetailsResponse
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed
