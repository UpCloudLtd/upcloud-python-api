from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.database_error_response import DatabaseErrorResponse
from ...models.database_service_information_response import DatabaseServiceInformationResponse
from ...models.database_service_modify_open_api import DatabaseServiceModifyOpenAPI
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    *,
    body: DatabaseServiceModifyOpenAPI | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/1.3/database/{uuid}".format(
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
) -> DatabaseErrorResponse | DatabaseServiceInformationResponse:
    if response.status_code == 200:
        response_200 = DatabaseServiceInformationResponse.from_dict(response.json())

        return response_200

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
    body: DatabaseServiceModifyOpenAPI | Unset = UNSET,
) -> Response[DatabaseErrorResponse | DatabaseServiceInformationResponse]:
    """Modify database

     Modifies Managed Database service details by its {uuid} including upgrading plans, migration to
    other zones and database type-specific configurations. For PostgreSQL and MySQL, change the plan
    with the plan_compute, plan_node_count, plan_storage_gib and plan_backups fields; the plan name
    field is deprecated for these engines.

    Args:
        uuid (UUID): The unique identifier for the integration.
        body (DatabaseServiceModifyOpenAPI | Unset): Schema for modifying a service — OpenAPI
            version.

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
    body: DatabaseServiceModifyOpenAPI | Unset = UNSET,
) -> DatabaseErrorResponse | DatabaseServiceInformationResponse | None:
    """Modify database

     Modifies Managed Database service details by its {uuid} including upgrading plans, migration to
    other zones and database type-specific configurations. For PostgreSQL and MySQL, change the plan
    with the plan_compute, plan_node_count, plan_storage_gib and plan_backups fields; the plan name
    field is deprecated for these engines.

    Args:
        uuid (UUID): The unique identifier for the integration.
        body (DatabaseServiceModifyOpenAPI | Unset): Schema for modifying a service — OpenAPI
            version.

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
    body: DatabaseServiceModifyOpenAPI | Unset = UNSET,
) -> Response[DatabaseErrorResponse | DatabaseServiceInformationResponse]:
    """Modify database

     Modifies Managed Database service details by its {uuid} including upgrading plans, migration to
    other zones and database type-specific configurations. For PostgreSQL and MySQL, change the plan
    with the plan_compute, plan_node_count, plan_storage_gib and plan_backups fields; the plan name
    field is deprecated for these engines.

    Args:
        uuid (UUID): The unique identifier for the integration.
        body (DatabaseServiceModifyOpenAPI | Unset): Schema for modifying a service — OpenAPI
            version.

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
    body: DatabaseServiceModifyOpenAPI | Unset = UNSET,
) -> DatabaseErrorResponse | DatabaseServiceInformationResponse | None:
    """Modify database

     Modifies Managed Database service details by its {uuid} including upgrading plans, migration to
    other zones and database type-specific configurations. For PostgreSQL and MySQL, change the plan
    with the plan_compute, plan_node_count, plan_storage_gib and plan_backups fields; the plan name
    field is deprecated for these engines.

    Args:
        uuid (UUID): The unique identifier for the integration.
        body (DatabaseServiceModifyOpenAPI | Unset): Schema for modifying a service — OpenAPI
            version.

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
