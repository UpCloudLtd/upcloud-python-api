from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.database_available_extensions_response_item import DatabaseAvailableExtensionsResponseItem
from ...models.database_error_response import DatabaseErrorResponse
from ...types import Response


def _get_kwargs(
    uuid: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/database/{uuid}/available-extensions".format(
            uuid=quote(str(uuid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DatabaseErrorResponse | list[DatabaseAvailableExtensionsResponseItem]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemasdatabase_available_extensions_response_item_data in _response_200:
            componentsschemasdatabase_available_extensions_response_item = (
                DatabaseAvailableExtensionsResponseItem.from_dict(
                    componentsschemasdatabase_available_extensions_response_item_data
                )
            )

            response_200.append(componentsschemasdatabase_available_extensions_response_item)

        return response_200

    response_default = DatabaseErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DatabaseErrorResponse | list[DatabaseAvailableExtensionsResponseItem]]:
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
) -> Response[DatabaseErrorResponse | list[DatabaseAvailableExtensionsResponseItem]]:
    """Get available extensions

     Returns a list of available PostgreSQL extensions for the Managed Database service by its {service-
    uuid}. Only supported for PostgreSQL services.

    Args:
        uuid (UUID): The unique identifier for the integration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatabaseErrorResponse | list[DatabaseAvailableExtensionsResponseItem]]
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
) -> DatabaseErrorResponse | list[DatabaseAvailableExtensionsResponseItem] | None:
    """Get available extensions

     Returns a list of available PostgreSQL extensions for the Managed Database service by its {service-
    uuid}. Only supported for PostgreSQL services.

    Args:
        uuid (UUID): The unique identifier for the integration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatabaseErrorResponse | list[DatabaseAvailableExtensionsResponseItem]
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DatabaseErrorResponse | list[DatabaseAvailableExtensionsResponseItem]]:
    """Get available extensions

     Returns a list of available PostgreSQL extensions for the Managed Database service by its {service-
    uuid}. Only supported for PostgreSQL services.

    Args:
        uuid (UUID): The unique identifier for the integration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatabaseErrorResponse | list[DatabaseAvailableExtensionsResponseItem]]
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
) -> DatabaseErrorResponse | list[DatabaseAvailableExtensionsResponseItem] | None:
    """Get available extensions

     Returns a list of available PostgreSQL extensions for the Managed Database service by its {service-
    uuid}. Only supported for PostgreSQL services.

    Args:
        uuid (UUID): The unique identifier for the integration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatabaseErrorResponse | list[DatabaseAvailableExtensionsResponseItem]
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
        )
    ).parsed
