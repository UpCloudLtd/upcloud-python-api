from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.database_error_response import DatabaseErrorResponse
from ...models.database_service_clone_mysql import DatabaseServiceCloneMysql
from ...models.database_service_clone_opensearch import DatabaseServiceCloneOpensearch
from ...models.database_service_clone_pg import DatabaseServiceClonePg
from ...models.database_service_clone_redis import DatabaseServiceCloneRedis
from ...models.database_service_clone_valkey import DatabaseServiceCloneValkey
from ...models.database_service_information_response import DatabaseServiceInformationResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    *,
    body: DatabaseServiceCloneMysql
    | DatabaseServiceCloneOpensearch
    | DatabaseServiceClonePg
    | DatabaseServiceCloneRedis
    | DatabaseServiceCloneValkey
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/1.3/database/{uuid}/clone".format(
            uuid=quote(str(uuid), safe=""),
        ),
    }

    if isinstance(body, DatabaseServiceCloneMysql):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, DatabaseServiceClonePg):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, DatabaseServiceCloneRedis):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, DatabaseServiceCloneOpensearch):
        _kwargs["json"] = body.to_dict()
    else:
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
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: DatabaseServiceCloneMysql
    | DatabaseServiceCloneOpensearch
    | DatabaseServiceClonePg
    | DatabaseServiceCloneRedis
    | DatabaseServiceCloneValkey
    | Unset = UNSET,
) -> Response[DatabaseErrorResponse | DatabaseServiceInformationResponse]:
    """Clone database

     Creates a clone of a Managed Database service based on its {uuid}. It is possible to change
    location, plans and use the point in time feature to clone your service at a specific time using
    your backups. For PostgreSQL and MySQL, select the clone's plan with the plan_compute,
    plan_node_count, plan_storage_gib and plan_backups fields; the plan name field is deprecated for
    these engines.

    Args:
        uuid (UUID): The unique identifier for the integration.
        body (DatabaseServiceCloneMysql | DatabaseServiceCloneOpensearch | DatabaseServiceClonePg
            | DatabaseServiceCloneRedis | DatabaseServiceCloneValkey | Unset): Schema for cloning a
            service — OpenAPI version.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatabaseErrorResponse | DatabaseServiceInformationResponse]
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
    body: DatabaseServiceCloneMysql
    | DatabaseServiceCloneOpensearch
    | DatabaseServiceClonePg
    | DatabaseServiceCloneRedis
    | DatabaseServiceCloneValkey
    | Unset = UNSET,
) -> DatabaseErrorResponse | DatabaseServiceInformationResponse | None:
    """Clone database

     Creates a clone of a Managed Database service based on its {uuid}. It is possible to change
    location, plans and use the point in time feature to clone your service at a specific time using
    your backups. For PostgreSQL and MySQL, select the clone's plan with the plan_compute,
    plan_node_count, plan_storage_gib and plan_backups fields; the plan name field is deprecated for
    these engines.

    Args:
        uuid (UUID): The unique identifier for the integration.
        body (DatabaseServiceCloneMysql | DatabaseServiceCloneOpensearch | DatabaseServiceClonePg
            | DatabaseServiceCloneRedis | DatabaseServiceCloneValkey | Unset): Schema for cloning a
            service — OpenAPI version.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatabaseErrorResponse | DatabaseServiceInformationResponse
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
    body: DatabaseServiceCloneMysql
    | DatabaseServiceCloneOpensearch
    | DatabaseServiceClonePg
    | DatabaseServiceCloneRedis
    | DatabaseServiceCloneValkey
    | Unset = UNSET,
) -> Response[DatabaseErrorResponse | DatabaseServiceInformationResponse]:
    """Clone database

     Creates a clone of a Managed Database service based on its {uuid}. It is possible to change
    location, plans and use the point in time feature to clone your service at a specific time using
    your backups. For PostgreSQL and MySQL, select the clone's plan with the plan_compute,
    plan_node_count, plan_storage_gib and plan_backups fields; the plan name field is deprecated for
    these engines.

    Args:
        uuid (UUID): The unique identifier for the integration.
        body (DatabaseServiceCloneMysql | DatabaseServiceCloneOpensearch | DatabaseServiceClonePg
            | DatabaseServiceCloneRedis | DatabaseServiceCloneValkey | Unset): Schema for cloning a
            service — OpenAPI version.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatabaseErrorResponse | DatabaseServiceInformationResponse]
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
    body: DatabaseServiceCloneMysql
    | DatabaseServiceCloneOpensearch
    | DatabaseServiceClonePg
    | DatabaseServiceCloneRedis
    | DatabaseServiceCloneValkey
    | Unset = UNSET,
) -> DatabaseErrorResponse | DatabaseServiceInformationResponse | None:
    """Clone database

     Creates a clone of a Managed Database service based on its {uuid}. It is possible to change
    location, plans and use the point in time feature to clone your service at a specific time using
    your backups. For PostgreSQL and MySQL, select the clone's plan with the plan_compute,
    plan_node_count, plan_storage_gib and plan_backups fields; the plan name field is deprecated for
    these engines.

    Args:
        uuid (UUID): The unique identifier for the integration.
        body (DatabaseServiceCloneMysql | DatabaseServiceCloneOpensearch | DatabaseServiceClonePg
            | DatabaseServiceCloneRedis | DatabaseServiceCloneValkey | Unset): Schema for cloning a
            service — OpenAPI version.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatabaseErrorResponse | DatabaseServiceInformationResponse
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed
