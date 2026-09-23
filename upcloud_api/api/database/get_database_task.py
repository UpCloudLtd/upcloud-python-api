from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.database_error_response import DatabaseErrorResponse
from ...models.database_service_task_details_response import DatabaseServiceTaskDetailsResponse
from ...types import Response


def _get_kwargs(
    uuid: UUID,
    task_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/database/{uuid}/tasks/{task_id}".format(
            uuid=quote(str(uuid), safe=""),
            task_id=quote(str(task_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DatabaseErrorResponse | DatabaseServiceTaskDetailsResponse:
    if response.status_code == 200:
        response_200 = DatabaseServiceTaskDetailsResponse.from_dict(response.json())

        return response_200

    response_default = DatabaseErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DatabaseErrorResponse | DatabaseServiceTaskDetailsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uuid: UUID,
    task_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DatabaseErrorResponse | DatabaseServiceTaskDetailsResponse]:
    """Get task

     Returns task details of a Managed Database service by its {uuid} and the task {id} obtained from
    Create Managed Database task.

    Args:
        uuid (UUID): The unique identifier for the integration.
        task_id (int): The unique identifier for the integration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatabaseErrorResponse | DatabaseServiceTaskDetailsResponse]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        task_id=task_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    task_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> DatabaseErrorResponse | DatabaseServiceTaskDetailsResponse | None:
    """Get task

     Returns task details of a Managed Database service by its {uuid} and the task {id} obtained from
    Create Managed Database task.

    Args:
        uuid (UUID): The unique identifier for the integration.
        task_id (int): The unique identifier for the integration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatabaseErrorResponse | DatabaseServiceTaskDetailsResponse
    """

    return sync_detailed(
        uuid=uuid,
        task_id=task_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    task_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DatabaseErrorResponse | DatabaseServiceTaskDetailsResponse]:
    """Get task

     Returns task details of a Managed Database service by its {uuid} and the task {id} obtained from
    Create Managed Database task.

    Args:
        uuid (UUID): The unique identifier for the integration.
        task_id (int): The unique identifier for the integration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatabaseErrorResponse | DatabaseServiceTaskDetailsResponse]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        task_id=task_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    task_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> DatabaseErrorResponse | DatabaseServiceTaskDetailsResponse | None:
    """Get task

     Returns task details of a Managed Database service by its {uuid} and the task {id} obtained from
    Create Managed Database task.

    Args:
        uuid (UUID): The unique identifier for the integration.
        task_id (int): The unique identifier for the integration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatabaseErrorResponse | DatabaseServiceTaskDetailsResponse
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            task_id=task_id,
            client=client,
        )
    ).parsed
