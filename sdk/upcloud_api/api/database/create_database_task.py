from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.database_error_response import DatabaseErrorResponse
from ...models.database_service_task_create import DatabaseServiceTaskCreate
from ...models.database_service_task_response import DatabaseServiceTaskResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    *,
    body: DatabaseServiceTaskCreate | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/1.3/database/{uuid}/tasks".format(
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
) -> DatabaseErrorResponse | DatabaseServiceTaskResponse:
    if response.status_code == 201:
        response_201 = DatabaseServiceTaskResponse.from_dict(response.json())

        return response_201

    response_default = DatabaseErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DatabaseErrorResponse | DatabaseServiceTaskResponse]:
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
    body: DatabaseServiceTaskCreate | Unset = UNSET,
) -> Response[DatabaseErrorResponse | DatabaseServiceTaskResponse]:
    """Create task

     Creates a task that checks for potential errors before starting a migration or upgrade for a Managed
    Database service by its {uuid}.

    Args:
        uuid (UUID): The unique identifier for the integration.
        body (DatabaseServiceTaskCreate | Unset): Schema for creating a service task with various
            operations such as dataset import and migration checks.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatabaseErrorResponse | DatabaseServiceTaskResponse]
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
    body: DatabaseServiceTaskCreate | Unset = UNSET,
) -> DatabaseErrorResponse | DatabaseServiceTaskResponse | None:
    """Create task

     Creates a task that checks for potential errors before starting a migration or upgrade for a Managed
    Database service by its {uuid}.

    Args:
        uuid (UUID): The unique identifier for the integration.
        body (DatabaseServiceTaskCreate | Unset): Schema for creating a service task with various
            operations such as dataset import and migration checks.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatabaseErrorResponse | DatabaseServiceTaskResponse
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
    body: DatabaseServiceTaskCreate | Unset = UNSET,
) -> Response[DatabaseErrorResponse | DatabaseServiceTaskResponse]:
    """Create task

     Creates a task that checks for potential errors before starting a migration or upgrade for a Managed
    Database service by its {uuid}.

    Args:
        uuid (UUID): The unique identifier for the integration.
        body (DatabaseServiceTaskCreate | Unset): Schema for creating a service task with various
            operations such as dataset import and migration checks.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatabaseErrorResponse | DatabaseServiceTaskResponse]
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
    body: DatabaseServiceTaskCreate | Unset = UNSET,
) -> DatabaseErrorResponse | DatabaseServiceTaskResponse | None:
    """Create task

     Creates a task that checks for potential errors before starting a migration or upgrade for a Managed
    Database service by its {uuid}.

    Args:
        uuid (UUID): The unique identifier for the integration.
        body (DatabaseServiceTaskCreate | Unset): Schema for creating a service task with various
            operations such as dataset import and migration checks.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatabaseErrorResponse | DatabaseServiceTaskResponse
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed
