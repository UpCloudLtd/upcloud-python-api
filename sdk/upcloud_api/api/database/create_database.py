from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.database_error_response import DatabaseErrorResponse
from ...models.database_service_create_open_api import DatabaseServiceCreateOpenAPI
from ...models.database_service_information_response import DatabaseServiceInformationResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: DatabaseServiceCreateOpenAPI | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/1.3/database",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DatabaseErrorResponse | DatabaseServiceInformationResponse:
    if response.status_code == 201:
        response_201 = DatabaseServiceInformationResponse.from_dict(response.json())

        return response_201

    response_default = DatabaseErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DatabaseErrorResponse | DatabaseServiceInformationResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DatabaseServiceCreateOpenAPI | Unset = UNSET,
) -> Response[DatabaseErrorResponse | DatabaseServiceInformationResponse]:
    """Create database

     Creates a new Managed Database instance. New databases are started by default. An initial backup is
    created automatically on startup and the API will be fully functional only after this backup has
    been created. The creation might take a while. Note that different databases have different
    properties that can be passed on creation. For PostgreSQL and MySQL, select the plan with the
    plan_compute, plan_node_count, plan_storage_gib and plan_backups fields; the plan name field is
    deprecated for these engines.

    Args:
        body (DatabaseServiceCreateOpenAPI | Unset): Schema for creating a service — OpenAPI
            version.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatabaseErrorResponse | DatabaseServiceInformationResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: DatabaseServiceCreateOpenAPI | Unset = UNSET,
) -> DatabaseErrorResponse | DatabaseServiceInformationResponse | None:
    """Create database

     Creates a new Managed Database instance. New databases are started by default. An initial backup is
    created automatically on startup and the API will be fully functional only after this backup has
    been created. The creation might take a while. Note that different databases have different
    properties that can be passed on creation. For PostgreSQL and MySQL, select the plan with the
    plan_compute, plan_node_count, plan_storage_gib and plan_backups fields; the plan name field is
    deprecated for these engines.

    Args:
        body (DatabaseServiceCreateOpenAPI | Unset): Schema for creating a service — OpenAPI
            version.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatabaseErrorResponse | DatabaseServiceInformationResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DatabaseServiceCreateOpenAPI | Unset = UNSET,
) -> Response[DatabaseErrorResponse | DatabaseServiceInformationResponse]:
    """Create database

     Creates a new Managed Database instance. New databases are started by default. An initial backup is
    created automatically on startup and the API will be fully functional only after this backup has
    been created. The creation might take a while. Note that different databases have different
    properties that can be passed on creation. For PostgreSQL and MySQL, select the plan with the
    plan_compute, plan_node_count, plan_storage_gib and plan_backups fields; the plan name field is
    deprecated for these engines.

    Args:
        body (DatabaseServiceCreateOpenAPI | Unset): Schema for creating a service — OpenAPI
            version.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatabaseErrorResponse | DatabaseServiceInformationResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: DatabaseServiceCreateOpenAPI | Unset = UNSET,
) -> DatabaseErrorResponse | DatabaseServiceInformationResponse | None:
    """Create database

     Creates a new Managed Database instance. New databases are started by default. An initial backup is
    created automatically on startup and the API will be fully functional only after this backup has
    been created. The creation might take a while. Note that different databases have different
    properties that can be passed on creation. For PostgreSQL and MySQL, select the plan with the
    plan_compute, plan_node_count, plan_storage_gib and plan_backups fields; the plan name field is
    deprecated for these engines.

    Args:
        body (DatabaseServiceCreateOpenAPI | Unset): Schema for creating a service — OpenAPI
            version.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatabaseErrorResponse | DatabaseServiceInformationResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
