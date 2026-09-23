from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.database_error_response import DatabaseErrorResponse
from ...models.database_service_type import DatabaseServiceType
from ...models.database_service_type_response import DatabaseServiceTypeResponse
from ...types import Response


def _get_kwargs(
    service_type_name: DatabaseServiceType,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/database/service-types/{service_type_name}".format(
            service_type_name=quote(str(service_type_name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DatabaseErrorResponse | DatabaseServiceTypeResponse:
    if response.status_code == 200:
        response_200 = DatabaseServiceTypeResponse.from_dict(response.json())

        return response_200

    response_default = DatabaseErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DatabaseErrorResponse | DatabaseServiceTypeResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    service_type_name: DatabaseServiceType,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DatabaseErrorResponse | DatabaseServiceTypeResponse]:
    """Get database type

     Returns database type details by given {database_type}. Contains available legacy plans, zones,
    database versions supported and configuration properties. PostgreSQL and MySQL componentised (rdb.*)
    plans are selected with the plan_* request fields instead of a listed plan name.

    Args:
        service_type_name (DatabaseServiceType): The type of service.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatabaseErrorResponse | DatabaseServiceTypeResponse]
    """

    kwargs = _get_kwargs(
        service_type_name=service_type_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_type_name: DatabaseServiceType,
    *,
    client: AuthenticatedClient | Client,
) -> DatabaseErrorResponse | DatabaseServiceTypeResponse | None:
    """Get database type

     Returns database type details by given {database_type}. Contains available legacy plans, zones,
    database versions supported and configuration properties. PostgreSQL and MySQL componentised (rdb.*)
    plans are selected with the plan_* request fields instead of a listed plan name.

    Args:
        service_type_name (DatabaseServiceType): The type of service.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatabaseErrorResponse | DatabaseServiceTypeResponse
    """

    return sync_detailed(
        service_type_name=service_type_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    service_type_name: DatabaseServiceType,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DatabaseErrorResponse | DatabaseServiceTypeResponse]:
    """Get database type

     Returns database type details by given {database_type}. Contains available legacy plans, zones,
    database versions supported and configuration properties. PostgreSQL and MySQL componentised (rdb.*)
    plans are selected with the plan_* request fields instead of a listed plan name.

    Args:
        service_type_name (DatabaseServiceType): The type of service.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatabaseErrorResponse | DatabaseServiceTypeResponse]
    """

    kwargs = _get_kwargs(
        service_type_name=service_type_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_type_name: DatabaseServiceType,
    *,
    client: AuthenticatedClient | Client,
) -> DatabaseErrorResponse | DatabaseServiceTypeResponse | None:
    """Get database type

     Returns database type details by given {database_type}. Contains available legacy plans, zones,
    database versions supported and configuration properties. PostgreSQL and MySQL componentised (rdb.*)
    plans are selected with the plan_* request fields instead of a listed plan name.

    Args:
        service_type_name (DatabaseServiceType): The type of service.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatabaseErrorResponse | DatabaseServiceTypeResponse
    """

    return (
        await asyncio_detailed(
            service_type_name=service_type_name,
            client=client,
        )
    ).parsed
