from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.database_error_response import DatabaseErrorResponse
from ...models.database_service_user_modify import DatabaseServiceUserModify
from ...models.database_user_response import DatabaseUserResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    username: str,
    *,
    body: DatabaseServiceUserModify | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/1.3/database/{uuid}/users/{username}".format(
            uuid=quote(str(uuid), safe=""),
            username=quote(str(username), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DatabaseErrorResponse | DatabaseUserResponse:
    if response.status_code == 200:
        response_200 = DatabaseUserResponse.from_dict(response.json())

        return response_200

    response_default = DatabaseErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DatabaseErrorResponse | DatabaseUserResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uuid: UUID,
    username: str,
    *,
    client: AuthenticatedClient | Client,
    body: DatabaseServiceUserModify | Unset = UNSET,
) -> Response[DatabaseErrorResponse | DatabaseUserResponse]:
    """Modify user

     Modifies the user {username} details for the Managed Database service {uuid}.

    Args:
        uuid (UUID): The unique identifier for the integration.
        username (str): The title of an entity.
        body (DatabaseServiceUserModify | Unset): Schema for modifying a service user

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatabaseErrorResponse | DatabaseUserResponse]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        username=username,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    username: str,
    *,
    client: AuthenticatedClient | Client,
    body: DatabaseServiceUserModify | Unset = UNSET,
) -> DatabaseErrorResponse | DatabaseUserResponse | None:
    """Modify user

     Modifies the user {username} details for the Managed Database service {uuid}.

    Args:
        uuid (UUID): The unique identifier for the integration.
        username (str): The title of an entity.
        body (DatabaseServiceUserModify | Unset): Schema for modifying a service user

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatabaseErrorResponse | DatabaseUserResponse
    """

    return sync_detailed(
        uuid=uuid,
        username=username,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    username: str,
    *,
    client: AuthenticatedClient | Client,
    body: DatabaseServiceUserModify | Unset = UNSET,
) -> Response[DatabaseErrorResponse | DatabaseUserResponse]:
    """Modify user

     Modifies the user {username} details for the Managed Database service {uuid}.

    Args:
        uuid (UUID): The unique identifier for the integration.
        username (str): The title of an entity.
        body (DatabaseServiceUserModify | Unset): Schema for modifying a service user

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatabaseErrorResponse | DatabaseUserResponse]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        username=username,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    username: str,
    *,
    client: AuthenticatedClient | Client,
    body: DatabaseServiceUserModify | Unset = UNSET,
) -> DatabaseErrorResponse | DatabaseUserResponse | None:
    """Modify user

     Modifies the user {username} details for the Managed Database service {uuid}.

    Args:
        uuid (UUID): The unique identifier for the integration.
        username (str): The title of an entity.
        body (DatabaseServiceUserModify | Unset): Schema for modifying a service user

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatabaseErrorResponse | DatabaseUserResponse
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            username=username,
            client=client,
            body=body,
        )
    ).parsed
