from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.database_error_response import DatabaseErrorResponse
from ...types import Response


def _get_kwargs(
    uuid: UUID,
    username: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/1.3/database/{uuid}/users/{username}".format(
            uuid=quote(str(uuid), safe=""),
            username=quote(str(username), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | DatabaseErrorResponse:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    response_default = DatabaseErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DatabaseErrorResponse]:
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
) -> Response[Any | DatabaseErrorResponse]:
    """Delete user

     Deletes the user {username} from the Managed Database service {uuid}.

    Args:
        uuid (UUID): The unique identifier for the integration.
        username (str): The title of an entity.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DatabaseErrorResponse]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        username=username,
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
) -> Any | DatabaseErrorResponse | None:
    """Delete user

     Deletes the user {username} from the Managed Database service {uuid}.

    Args:
        uuid (UUID): The unique identifier for the integration.
        username (str): The title of an entity.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DatabaseErrorResponse
    """

    return sync_detailed(
        uuid=uuid,
        username=username,
        client=client,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    username: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DatabaseErrorResponse]:
    """Delete user

     Deletes the user {username} from the Managed Database service {uuid}.

    Args:
        uuid (UUID): The unique identifier for the integration.
        username (str): The title of an entity.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DatabaseErrorResponse]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        username=username,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    username: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DatabaseErrorResponse | None:
    """Delete user

     Deletes the user {username} from the Managed Database service {uuid}.

    Args:
        uuid (UUID): The unique identifier for the integration.
        username (str): The title of an entity.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DatabaseErrorResponse
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            username=username,
            client=client,
        )
    ).parsed
